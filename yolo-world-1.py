# Import YOLOWorld class from ultralytics module
import os
from ultralytics import YOLOWorld
import torch

HOME = os.getcwd()
IMG_PATH = f"{HOME}/images/camry.png"
RESULT_PATH = f"{HOME}/images/camry-result.JPEG"

# Initialize the model with pre-trained weights
model = YOLOWorld('yolov8s-world')

# Set the classes you'd like to find in your image
model.set_classes(["car", "wheel", "car door", "car mirror", "license plate", ""])

# Run object detection for your custom classes on your image
results = model.predict(IMG_PATH, max_det=100, iou=0.01, conf=0.05)

# Save the results
results[0].save(filename=RESULT_PATH)
