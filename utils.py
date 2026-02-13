import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import streamlit as st
from plant_info import PLANT_INFO

# Define class labels
CLASS_LABELS = sorted(list(PLANT_INFO.keys()))

import os

@st.cache_resource
def load_model(model_path="medicinal_plant_classifier.h5"):
    """Load and cache the model"""
    if not os.path.exists(model_path):
        st.error(f"Model file not found at {model_path}. Please ensure the model file is in the project directory.")
        return None
    try:
        model = tf.keras.models.load_model(model_path)
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def preprocess_image(img):
    """Preprocess the image for the model"""
    # Resize image to match model input
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    return img_array

def predict_plant(model, img_pil):
    """Run prediction on an image"""
    processed_img = preprocess_image(img_pil)
    predictions = model.predict(processed_img)
    
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)
    
    if 0 <= predicted_class_index < len(CLASS_LABELS):
        predicted_label = CLASS_LABELS[predicted_class_index]
        return predicted_label, confidence
    return None, 0.0
