import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file

# add further details once model rerun

def resize_input_image(img, version):
    """ 
    Reshape image
    """ 
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pkl")
    target_size = (100, 100)
    img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
    my_image = np.expand_dims(img_resized, axis=0) / 255

    return my_image

def load_model_and_predict(my_image, version):
    """ 
    Load and Perform ML prediction on new image
    """
    model = load_model(f"outputs/{version}/mildew_detector_model100.h5", compile=False)

    # Perform the prediction and map
    prediction = model.predict(my_image)
    target_map = {'Healthy': 0, 'Unhealthy': 1}

    # Determining class and probability
    pred_proba = prediction[0][0]
    pred_class = 'Unhealthy' if pred_proba > 0.5 else 'Healthy'
    if pred_class == 'Healthy':
        pred_proba = 1 - pred_proba
    
    return pred_proba, pred_class

