# Import YOLOWorld class from ultralytics module
import os
from ultralytics import YOLOWorld
import torch

# HOME = os.getcwd()
# IMG_PATH = f"{HOME}/images/camry.png"
# RESULT_PATH = f"{HOME}/images/camry-result.JPEG"

# Initialize the model with pre-trained weights
model = YOLOWorld('yolov8s-world')

# Set the classes you'd like to find in your image
model.set_classes(["car", "wheel", "car door", "car mirror", "license plate", ""])

# save custom model
model.save("custom-yolov8s-worldv2-for-car-part.pt")
