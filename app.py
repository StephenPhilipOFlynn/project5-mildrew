import streamlit as st
from app_pages.multipage import MultiPage

#set page configuration.
st.set_page_config(page_title="Mildew Detector", layout="centered")

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_summary import page_summary_hypothesis
from app_pages.page_ml_performance import page_ml_performance_metrics
from app_pages.page_visualiser import page_visualiser_body
from app_pages.page_ml_image_test import ml_image_test_body



app = MultiPage(app_name= "Mildew Detector") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_summary_body)
app.add_page("Project Hypothesis", page_summary_hypothesis)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)
app.add_page("Visualiser", page_visualiser_body)
app.add_page("Test Image", ml_image_test_body)

#app.add_page("Visualiser", page_visualiser_body)
#app.add_page("Mildew Detection", page_mildew_detector_body)

app.run() # Run the  app
