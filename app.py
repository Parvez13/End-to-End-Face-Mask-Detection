import sys,os
from maskDetection.pipeline.training_pipeline import TrainPipeline
from maskDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
from maskDetection.constant.application import APP_HOST, APP_PORT
import streamlit as st

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

clApp = ClientApp()

@st.cache
def train_model():
    obj = TrainPipeline()
    obj.run_pipeline()

def main():
    st.title("Object Detection Web App")

    menu = ["Home", "Train", "Predict", "Live"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to the Object Detection Web App!")

    elif choice == "Train":
        st.subheader("Train")
        train_model()
        st.write("Training Successful!")

    elif choice == "Predict":
        st.subheader("Predict")
        image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if image is not None:
            decodeImage(image, clApp.filename)

            os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source ../data/inputImage.jpg")

            opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
            result = {"image": opencodedbase64.decode('utf-8')}
            os.system("rm -rf yolov5/runs")
            st.image(image, caption="Input Image")
            st.image(result["image"], caption="Output Image")

    elif choice == "Live":
        st.subheader("Live")
        os.system("cd yolov5/ && python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
        os.system("rm -rf yolov5/runs")
        st.write("Camera starting!!")

if __name__ == "__main__":
    main()

