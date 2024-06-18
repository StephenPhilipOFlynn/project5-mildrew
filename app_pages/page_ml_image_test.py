import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file
from src.machine_learning.predictive_analysis import resize_input_image
from src.machine_learning.predictive_analysis import load_model_and_predict

def ml_image_test_body():
    st.title("Healthy Leaf Detector")
    
    st.write("Upload an image of a leaf to determine if it is healthy or unhealthy.")
    
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Leaf Image', use_column_width=True)

    # preprocess
    version = "v1"
    processed_image = resize_input_image(image, version)

    #prediction
    pred_proba, pred_class = load_model_and_predict(processed_image, version)

    #display
    st.write(f"The predictive analysis indicates the leaf is {pred_class}.")
    st.write(f"Prediction confidence: {pred_proba * 100:.2f}%")

