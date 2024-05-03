import os
import cv2
import supervision as sv
from ultralytics import YOLO
from supervision.assets import download_assets, VideoAssets
import numpy as np

HOME = os.getcwd()
TARGET_VIDEO_PATH = f"{HOME}/videos/people-walking-result.mp4"

from supervision.assets import download_assets, VideoAssets

# Download a supervision video asset
VIDEO_PATH = download_assets(VideoAssets.PEOPLE_WALKING)

from inference.models.utils import get_roboflow_model

# Load a pre trained yolov8 nano model from Roboflow Inference.
model = get_roboflow_model('yolov8n-640')

vid_info = sv.VideoInfo.from_video_path(VIDEO_PATH)
labelAnnotator = sv.LabelAnnotator()

byteTracker = sv.ByteTrack(frame_rate=vid_info.fps)

frameGen = sv.get_video_frames_generator(source_path=VIDEO_PATH)

aFrame = next(frameGen)

result = model.infer(aFrame)[0]

detections = sv.Detections.from_inference(result)

tracked_detections = byteTracker.update_with_detections(detections=detections)

labels = [f"{tracker_id}" for tracker_id in tracked_detections.tracker_id]

annotated_frame = labelAnnotator.annotate(scene=aFrame.copy(), detections=tracked_detections, labels=labels)

sv.plot_image(image=annotated_frame)
