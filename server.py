import os
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, send_from_directory
from PIL import Image

IMAGE_SIZE = 224
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# index.html is looked for in a "frontend" folder first, otherwise next to server.py
_frontend = os.path.join(BASE_DIR, "frontend")
FRONTEND_DIR = _frontend if os.path.isdir(_frontend) else BASE_DIR

# index.html has its own CSS and JavaScript inside, so no static files are served
app = Flask(__name__, static_folder=None)

model = tf.keras.models.load_model(os.path.join(BASE_DIR, "leafcare_mobilenetv2.keras"), compile=False)
with open(os.path.join(BASE_DIR, "class_names.txt")) as f:
    class_names = [line.strip() for line in f if line.strip()]

# Folder name (from class_names.txt) -> (crop, condition) exactly as written in index.html
LABEL_INFO = {
    "Potato___Early_blight": ("Potato", "Early Blight"),
    "Potato___Late_blight": ("Potato", "Late Blight"),
    "Potato___healthy": ("Potato", "Healthy"),
    "Tomato_healthy": ("Tomato", "Healthy"),
    "Tomato_Leaf_Mold": ("Tomato", "Leaf Mold"),
    "Tomato__Tomato_mosaic_virus": ("Tomato", "Mosaic Virus"),
    "Tomato__Target_Spot": ("Tomato", "Target Spot"),
}

def describe(name):
    if name in LABEL_INFO:
        return LABEL_INFO[name]
    parts = [p for p in name.replace("___", "_").replace("__", "_").split("_") if p]   # fallback guess
    return (parts[0].title() if parts else "Unknown"), (" ".join(parts[1:]).title() or "Unknown")

def estimate_severity(img):
    """Rough % of the leaf that is not healthy green (yellow / brown / dark patches).
    A simple colour-based estimate, not a trained model."""
    hsv = np.array(img.convert("HSV"), dtype="float32")
    hue = hsv[..., 0] * 360 / 255
    sat = hsv[..., 1] / 255
    val = hsv[..., 2] / 255
    leaf = (sat > 0.20) & (val > 0.10)            # ignores grey / white / black background
    green = leaf & (hue >= 70) & (hue <= 160)
    diseased = leaf & ~green
    total = int(leaf.sum())
    if total < 500:
        return 0.0
    return float(min(100.0, 100.0 * diseased.sum() / total))

@app.after_request
def allow_other_origins(resp):
    # lets the page work when opened from VS Code Live Server (port 5500)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/health")
def health():
    return jsonify({"status": "ok", "classes": class_names})

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    try:
        img = Image.open(request.files["image"].stream).convert("RGB")
    except Exception:
        return jsonify({"error": "Could not read that file as an image"}), 400

    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    arr = np.array(img, dtype="float32")[None, ...]

    probs = model.predict(arr, verbose=0)[0]
    idx = int(np.argmax(probs))
    crop, condition = describe(class_names[idx])
    severity = 0.0 if condition == "Healthy" else estimate_severity(img)

    return jsonify({
        "label": f"{crop} {condition}",       # shown on the page, e.g. "Potato Early Blight"
        "crop": crop,
        "condition": condition,
        "confidence": float(probs[idx]),      # 0 to 1
        "severity": round(severity, 1),       # 0 to 100 (rough colour-based estimate)
    })

if __name__ == "__main__":
    # local run. On Render, gunicorn starts the app instead (see the start command)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
