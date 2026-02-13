import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os
import sys
import random

# Define the class labels (sorted alphabetically)
CLASS_LABELS = [
    'Aloevera', 'Amla', 'Amruta_Balli', 'Arali', 'Ashoka', 'Ashwagandha', 'Avacado', 
    'Bamboo', 'Basale', 'Betel', 'Betel_Nut', 'Brahmi', 'Castor', 'Curry_Leaf', 
    'Doddapatre', 'Ekka', 'Ganike', 'Gauva', 'Geranium', 'Henna', 'Hibiscus', 
    'Honge', 'Insulin', 'Jasmine', 'labels', 'Lemon', 'Lemon_grass', 'Mango', 'Mint', 
    'Nagadali', 'Neem', 'Nithyapushpa', 'Nooni', 'Pappaya', 'Pepper', 'Pomegranate', 
    'Raktachandini', 'Rose', 'Sapota', 'Tulasi', 'Wood_sorel'
]

def test_image(img_path):
    if not os.path.exists(img_path):
        print(f"Error: File not found at {img_path}")
        return

    print(f"Testing image: {img_path}")
    
    # Load model
    try:
        model = tf.keras.models.load_model("medicinal_plant_classifier.h5")
    except Exception as e:
        print(f"Error loading model: {e}")
        return

    # Preprocess
    try:
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0
    except Exception as e:
        print(f"Error processing image: {e}")
        return

    # Predict
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)

    print("-" * 30)
    print(f"Predicted Class Index: {predicted_class_index}")
    if 0 <= predicted_class_index < len(CLASS_LABELS):
        print(f"Predicted Class: {CLASS_LABELS[predicted_class_index]}")
        print(f"Confidence: {confidence:.2f}")
    else:
        print("Unknown class index")
    print("-" * 30)

def main():
    if len(sys.argv) > 1:
        img_path = sys.argv[1]
        test_image(img_path)
    else:
        print("No image path provided. Looking for a random sample image...")
        # Try to find an image in the images directory
        images_dir = "images"
        if os.path.exists(images_dir):
            categories = [d for d in os.listdir(images_dir) if os.path.isdir(os.path.join(images_dir, d))]
            if categories:
                random_category = random.choice(categories)
                category_path = os.path.join(images_dir, random_category)
                files = [f for f in os.listdir(category_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
                if files:
                    random_image = random.choice(files)
                    img_path = os.path.join(category_path, random_image)
                    print(f"Selected random image from dataset: {img_path} (True Label: {random_category})")
                    test_image(img_path)
                else:
                    print(f"No images found in {random_category}")
            else:
                print("No categories found in images directory.")
        else:
            print("Images directory not found.")
            print("Usage: python test_project.py <path_to_image>")

if __name__ == "__main__":
    main()
