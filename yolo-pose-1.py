import cv2
from ultralytics import YOLO
import supervision as sv
import os

# Load a model
# model = YOLO('yolov8n-pose.yaml')  # build a new model from YAML
model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n-pose.yaml').load('yolov8n-pose.pt')  # build from YAML and transfer weights

# Train the model
# results = model.train(data='coco8-pose.yaml', epochs=100, imgsz=640)
HOME = os.getcwd()
IMAGE_PATH = f"{HOME}/bus.jpeg"

img = cv2.imread(filename=IMAGE_PATH)

results = model(img)[0]
results[2].show()
# sv.plot_image(results, size=(8, 8))

keypoints = sv.KeyPoints.from_ultralytics(results)
print(keypoints)

# annotator = sv.PolygonAnnotator()

# annotated_image = annotator.annotate(scene=img.copy(), detections=keypoints)
# annotated_image = mask_annotator.annotate(annotated_image, detections)
# sv.plot_image(image=annotated_image, size=(8, 8))
