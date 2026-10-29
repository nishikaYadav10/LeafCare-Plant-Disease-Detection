import numpy as np
import tensorflow as tf
import streamlit as st
from PIL import Image
IMAGE_SIZE = 224
TREATMENT = {
    "Potato___Early_blight": "Remove affected leaves, apply a copper-based fungicide every 7-10 days, avoid overhead watering.",
    "Potato___Late_blight": "Spreads fast. Remove infected plants, apply a systemic fungicide, improve drainage and airflow.",
    "Potato___healthy": "No treatment needed. Keep monitoring.",
    "Tomato_healthy": "No treatment needed. Keep monitoring.",
    "Tomato_Leaf_Mold": "Improve ventilation, reduce humidity, apply a leaf-mold fungicide, remove badly affected leaves.",
    "Tomato__Tomato_mosaic_virus": "No cure. Remove infected plants, disinfect tools, control aphids.",
    "Tomato__Target_Spot": "Prune for airflow, remove infected leaves, apply a recommended fungicide early.",
}
@st.cache_resource
def load_everything():
    model = tf.keras.models.load_model("leafcare_mobilenetv2.keras")
    with open("class_names.txt") as f:
        class_names = f.read().splitlines()
    return model, class_names
model, class_names = load_everything()
st.title("LeafCare")
st.write("Upload a photo of a potato or tomato leaf to check for disease.")
uploaded = st.file_uploader("Leaf photo", type=["jpg", "jpeg", "png"])
if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, use_container_width=True)
    arr = np.array(img.resize((IMAGE_SIZE, IMAGE_SIZE)), dtype="float32")[None, ...]
    probs = model.predict(arr, verbose=0)[0]
    idx = int(np.argmax(probs))
    name = class_names[idx]
    confidence = float(probs[idx]) * 100
    st.subheader(name.replace("___", " - ").replace("__", " - ").replace("_", " "))
    st.progress(int(confidence), text=f"Confidence: {confidence:.1f}%")
    if confidence < 60:
        st.warning("The model is not very sure about this photo. Try a clearer, closer picture of a single leaf.")
    st.info(TREATMENT.get(name, "No treatment note added for this class."))
