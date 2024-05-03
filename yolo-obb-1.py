from ultralytics import YOLO
import os
import cv2

HOME = os.getcwd()
IMAGE_PATH = f"{HOME}/images/cars.jpeg"

img = cv2.imread(filename=IMAGE_PATH)

# Load a model
model = YOLO('yolov8n-obb.pt')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model

# Predict with the model
results = model.predict(img)  # predict on an image
# print(results[0])

results[0].show()
