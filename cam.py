import streamlit as st
import requests

# Display the file uploader to upload the image
uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

# Capture photo using the camera_input method
camera_image = st.camera_input("Capture Photo")

if camera_image is not None:
    st.image(camera_image, caption='Uploaded Image', use_column_width=True)
    if st.button('Check'):
            # Convert it to the  bytes format 
        file_bytes = camera_image.read()

            # Prepare the data to send to Flask
        files = {"file": ("image2.jpg", file_bytes, "image/jpeg")}

           
        response = requests.post("http://127.0.0.1:5000/camera-image", files=files)
        if response.status_code == 200:
            st.write("Response from Flask:", response.text)
        else:
            st.write("Couln't send the Image")

if uploaded_file is not None:
    st.image(uploaded_file, use_column_width=True)
    if st.button('Check'):
            # Convert the uploaded file to bytes
        file_bytes = uploaded_file.read()

            # Prepare the data to send to Flask
        files = {"file": ("image1.jpg", file_bytes, "image/jpeg")}

            # Make a POST request to Flask app
        response = requests.post("http://127.0.0.1:5000/upload-image", files=files)
        st.write("Status code :", response.status_code)
        st.write("Response from Flask:", response.text)
        if response.status_code == 200:
            st.write("Check your output.."
                f'''
                    <a style="" target="_self" href="/output">
                        <button style="border:0px solid black;color:#00ff44;border-radius:10px;padding: 0px 10px; background-color: #0b001b">
                            <p style="font-size:17px;color:$00ff44;"><u>click here</u></p>
                        </button>
                    </a>
                ''',unsafe_allow_html=True
        )