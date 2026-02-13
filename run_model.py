import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tkinter import Tk, filedialog
import os

# Define the class labels (sorted alphabetically as per flow_from_directory)
CLASS_LABELS = [
    'Aloevera', 'Amla', 'Amruta_Balli', 'Arali', 'Ashoka', 'Ashwagandha', 'Avacado', 
    'Bamboo', 'Basale', 'Betel', 'Betel_Nut', 'Brahmi', 'Castor', 'Curry_Leaf', 
    'Doddapatre', 'Ekka', 'Ganike', 'Gauva', 'Geranium', 'Henna', 'Hibiscus', 
    'Honge', 'Insulin', 'Jasmine', 'labels', 'Lemon', 'Lemon_grass', 'Mango', 'Mint', 
    'Nagadali', 'Neem', 'Nithyapushpa', 'Nooni', 'Pappaya', 'Pepper', 'Pomegranate', 
    'Raktachandini', 'Rose', 'Sapota', 'Tulasi', 'Wood_sorel'
]

# Load your trained model
print("Loading model...")
model = tf.keras.models.load_model("medicinal_plant_classifier.h5")
print("Model loaded.")

# Open file picker dialog
print("Please select an image file...")
root = Tk()
root.withdraw()  # Hide the main Tk window
img_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
)
root.destroy() # Destroy the root window after selection

if not img_path:
    print("No image selected.")
    exit()

print(f"Selected image: {img_path}")

# Preprocess the image
img = image.load_img(img_path, target_size=(224, 224))  # Resize to training size
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0  # Normalize

# Predict
predictions = model.predict(img_array)
predicted_class_index = np.argmax(predictions, axis=1)[0]
confidence = np.max(predictions)

print("Raw model output:", predictions)
print(f"Predicted class index: {predicted_class_index}")

if 0 <= predicted_class_index < len(CLASS_LABELS):
    print(f"Predicted Class: {CLASS_LABELS[predicted_class_index]}")
    print(f"Confidence: {confidence:.2f}")
else:
    print("Unknown class index")
