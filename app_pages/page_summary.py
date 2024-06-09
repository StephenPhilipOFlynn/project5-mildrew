import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread


st.title('Mildew in Cherry leaves')

st.write("## Project Summary")

st.info(
    "General Information\n\n"
    "**Project Dataset is taken from Kaggle. The data set is taken under licence from Code Institute.\n\n"
    "https://www.kaggle.com/datasets/codeinstitute/cherry-leaves")

st.write(
    "For additional information, please visit and **read** the "
    "[Project README file](https://github.com/StephenPhilipOFlynn/project5-mildrew).")

st.success(
    "The project has 2 business requirements:\n\n"
    "1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.\n\n"
    "2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew fungus."
)

st.write("### Project Hypothesis and Validation")

st.success(
        "We hypothesise that mildew-infected leaves exhibit distinct visual characteristics, that can be distinguished from healthy plants using image classification machine learning techniques.")
