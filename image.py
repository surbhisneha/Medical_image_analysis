
import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Set directories (adjust the paths if needed based on your dataset structure)
train_dir = r'C:\Users\nitik\Downloads\archive\Training'
test_dir = r'C:\Users\nitik\Downloads\archive\Testing'

# ImageDataGenerator for normalization (no augmentation for test set)
test_datagen = ImageDataGenerator(rescale=1./255)

# Test data generator
test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

# Load the trained models
def load_models():
    models = {}
    models['ResNet50'] = tf.keras.models.load_model(r'C:\Users\nitik\.vscode\python\resnet_model.h5')
    models['DenseNet121'] = tf.keras.models.load_model(r'C:\Users\nitik\.vscode\python\densenet_model.h5')
    models['VGG16'] = tf.keras.models.load_model(r'C:\Users\nitik\.vscode\python\vgg_model.h5')
    return models

# Preprocess the image
def preprocess_image(image):
    if image.mode != 'RGB':
        image = image.convert('RGB')  # Convert to RGB if the image is not in RGB mode
    image = image.resize((224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Rescale the image
    return image

# Ensemble prediction
def ensemble_predict(models, image):
    preds = [model.predict(image) for model in models.values()]
    avg_preds = np.mean(preds, axis=0)
    return avg_preds

# Load models
models = load_models()

# Streamlit app
def run():
    st.title("Brain Tumor Classification")

    st.write("Please upload an image file to classify the type of brain tumor")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Image uploaded successfully!")
        
        # Preprocess the image
        preprocessed_image = preprocess_image(image)

        # Get the prediction
        predictions = ensemble_predict(models, preprocessed_image)
        pred_class = np.argmax(predictions, axis=1)[0]
        
        # Map the prediction to the class label
        class_labels = {v: k for k, v in test_generator.class_indices.items()}
        result = class_labels[pred_class]

        st.write(f"Predicted Class: {result}")
