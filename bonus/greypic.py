"""
Starts the user's camera, allows the user to take a still picture,
then renders a grey-scale image in the web page.
Added an option to allow the user to pick a picture file and render that in grey-scale
"""
import streamlit as st
from PIL import Image

GREY = "L"  # Image.convert argument for grey_scale


def do_pic(pic):
    img = Image.open(pic)  # Create a Pillow image instance
    grey = img.convert(GREY)  # Convert to greyscale
    st.info("\nHere is your picture in grey-scale:")
    st.image(grey)  # render the image in the web page


uploaded_pic = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    camera_pic = st.camera_input("Camera")  # Start the camera

if uploaded_pic:
    do_pic(uploaded_pic)
if camera_pic:
    do_pic(camera_pic)
