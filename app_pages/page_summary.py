import streamlit as st
import os
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
import numpy as np
import seaborn as sns
import itertools
import random
## from src.machine_learning.evaluate_clf import load_test_evaluation

def page_summary_body():
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
    "2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew fungus.")

def page_summary_hypothesis():
    st.write("### Project Hypothesis and Validation")
    
    st.success(
        """We hypothesise that mildew-infected leaves exhibit distinct visual characteristics, 
        that can be distinguished from healthy plants using image classification machine learning techniques.""")
        ### add further details on validation here 

