from ultralytics import YOLO
import os

HOME = os.getcwd()
IMG_PATH = f"{HOME}/images/offi.jpeg"
RESULT_PATH = f"{HOME}/images/offi-result.JPEG"

# Initialize a YOLO-World model
model = YOLO('yolov8s-world.pt')  # or choose yolov8m/l-world.pt

# Define custom classes
model.set_classes(["person", "bus", ""])

# Execute prediction for specified categories on an image
results = model.predict(IMG_PATH)

# Show results
results[0].show()
