import streamlit as st
import matplotlib.pyplot as plt

def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"Add")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - Add "
        f".\n"
        f"* 2 - . "
        )
