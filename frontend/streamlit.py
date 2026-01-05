import streamlit as st
import requests
from PIL import Image
import io

# Backend API URL
API_URL = "http://localhost:8000/predict"  # Change to your actual API endpoint

st.title("Skin Disease Classification")
st.write("Upload an image of a skin condition to get its diagnosis (e.g., eczema, scabies).")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    # Show the uploaded image
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Button to send image to backend
    if st.button("Classify"):
        # Send image to FastAPI backend
        files = {"file": uploaded_file.getvalue()}
        try:
            response = requests.post(API_URL, files=files)
            response.raise_for_status()
            result = response.json()
            label = result

            st.success(f"Predicted Label: **{label}**")
        except requests.exceptions.RequestException as e:
            st.error(f"API request failed: {e}")
