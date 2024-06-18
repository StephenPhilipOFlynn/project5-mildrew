import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.data_management import load_pkl_file

# add further details once model rerun

def resize_input_image(img, version):
    """ 
    Reshape image
    """ 
    image_shape = load_pkl_file(file_path=f"outputs/{version}/image_shape.pk1")
    img_resized = img.resize((image_shape[1], image_shape[0]), Image.ANTIALIAS)
    my_image = np.expland_dims(img_resized, axis=0) / 255

    return my_image

def load_model_and_predict(my_image, version):
    """ 
    Load and Perform ML prediction on new image
    """
    model = load_model(f"outputs/{version}/mildew_detector_model100.h5")

    ### finish this function

