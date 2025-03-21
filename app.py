import streamlit as st
import cv2
import numpy as np
import face_recognition

st.title("Facial Recognition Web App")

# Upload video
uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    st.video(uploaded_video)

    # Process the video frame by frame
    cap = cv2.VideoCapture(uploaded_video.name)

    stframe = st.empty()  # Placeholder for displaying video

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_frame)

        for top, right, bottom, left in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Display the frame
        stframe.image(frame, channels="BGR")

    cap.release()
