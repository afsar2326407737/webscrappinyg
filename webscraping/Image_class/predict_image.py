import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the trained model
model = tf.keras.models.load_model('best_image_classification_model.h5')

# Define a function to process and predict an image
def predict_image(image_path):
    # Load and preprocess the image
    image = load_img(image_path, target_size=(32, 32))  # Resize to model input size
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    image = image / 255.0  # Normalize

    # Make a prediction
    predictions = model.predict(image)
    class_index = np.argmax(predictions[0])  # Get the class with the highest score
    confidence = predictions[0][class_index]

    # Return the class index and confidence
    return class_index, confidence
