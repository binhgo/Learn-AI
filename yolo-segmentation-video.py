import os

from tqdm import tqdm
import cv2
import supervision as sv
from ultralytics import YOLO
from supervision.assets import download_assets, VideoAssets
from inference.models.utils import get_roboflow_model

HOME = os.getcwd()
VIDEO_PATH = f"{HOME}/vehicles.mp4"
RESULT_VIDEO = f"{HOME}/videos/segmentation-result.mp4"

vid_info = sv.VideoInfo.from_video_path(VIDEO_PATH)
frame_gen = sv.get_video_frames_generator(VIDEO_PATH)

mask_annotator = sv.MaskAnnotator(color_lookup=sv.ColorLookup.INDEX, opacity=.5)
label_annotator = sv.LabelAnnotator()

model = YOLO("yolov8n-seg.pt")

with sv.VideoSink(RESULT_VIDEO, vid_info) as sink:
    for frame in tqdm(frame_gen, total=vid_info.total_frames):
        results = model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)
        annotated_image = label_annotator.annotate(scene=frame.copy(), detections=detections)
        annotated_image = mask_annotator.annotate(annotated_image, detections)
        sink.write_frame(annotated_image)
