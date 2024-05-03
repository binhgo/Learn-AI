from ultralytics import YOLO
from ultralytics import YOLOWorld
import os
import supervision as sv

HOME = os.getcwd()
IMAGE_PATH = f"{HOME}/images/camry.png"

# Load your custom model
model = YOLOWorld('custom-yolov8s-worldv2-for-car-part.pt')

# Run inference to detect your custom classes
results = model.predict(IMAGE_PATH, max_det=100, iou=0.01, conf=0.04)
# results = model.predict(IMG_PATH, max_det=100, iou=0.01, conf=0.05)

detections = sv.Detections.from_ultralytics(results)[0]

# Show results
results[0].show()
