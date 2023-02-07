"""
Starts the user's camera, allows the user to take a still picture,
then reders a grey-scale image in the web page
"""
import streamlit as st
from PIL import Image

GREY = "L"  # Image.convert argument for grey_scale

with st.expander("Start Camera"):
    pic = st.camera_input("Camera")  # Start the camera

if pic:
    img = Image.open(pic)  # Create a Pillow image instance
    grey = img.convert(GREY)  # Convert to greyscale
    st.image(grey)  # render the image in the web page
