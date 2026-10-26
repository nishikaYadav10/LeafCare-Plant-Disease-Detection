import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, send_from_directory
from PIL import Image

IMAGE_SIZE = 224

# Serves your frontend folder (index.html, style.css, script.js) from the same address as the API
app = Flask(__name__, static_folder=".", static_url_path="")

model = tf.keras.models.load_model("leafcare_mobilenetv2.keras")
with open("class_names.txt") as f:
    class_names = f.read().splitlines()

# Folder name (from class_names.txt)  ->  key used in the frontend's script.js (KB)
LABEL_MAP = {
    "Potato___Early_blight": "potato_early_blight",
    "Potato___Late_blight": "potato_late_blight",
    "Potato___healthy": "potato_healthy",
    "Tomato_healthy": "tomato_healthy",
    "Tomato_Leaf_Mold": "tomato_leaf_mold",
    "Tomato__Tomato_mosaic_virus": "tomato_mosaic",
    "Tomato__Target_Spot": "tomato_target_spot",
}

def to_key(name):
    # falls back to a guess if a folder name is not in LABEL_MAP
    return LABEL_MAP.get(name, name.lower().replace("___", "_").replace("__", "_"))

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

@app.route("/")
def home():
    return send_from_directory(".", "index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    img = Image.open(request.files["image"].stream).convert("RGB")
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    arr = np.array(img, dtype="float32")[None, ...]

    probs = model.predict(arr, verbose=0)[0]
    idx = int(np.argmax(probs))
    key = to_key(class_names[idx])
    severity = 0.0 if "healthy" in key else estimate_severity(img)

    return jsonify({
        "label": key,
        "confidence": float(probs[idx]),      # 0 to 1, as script.js expects
        "severity": round(severity, 1),       # 0 to 100
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)