import os

import cv2
import supervision as sv
from ultralytics import YOLO

HOME = os.getcwd()
IMAGE_PATH = f"{HOME}/images/dog.jpeg"

img = cv2.imread(filename=IMAGE_PATH)

model = YOLO("yolov8n-seg.pt")
results = model(img)[0]
detections = sv.Detections.from_ultralytics(results)

mask_annotator = sv.MaskAnnotator(color_lookup=sv.ColorLookup.INDEX, opacity=.5)
label_annotator = sv.LabelAnnotator()

annotated_image = label_annotator.annotate(scene=img.copy(), detections=detections)
annotated_image = mask_annotator.annotate(annotated_image, detections)

sv.plot_image(image=annotated_image, size=(8, 8))
