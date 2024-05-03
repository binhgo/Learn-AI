from ultralytics import YOLO
import os
from tqdm import tqdm
import supervision as sv
import cv2

# Load a model
model = YOLO('yolov8n-seg.pt')  # load an official model
# model = YOLO('path/to/best.pt')  # load a custom model

HOME = os.getcwd()
VIDEO_PATH = f"{HOME}/vehicles.mp4"
RESULT_VIDEO = f"{HOME}/videos/segment-yolo-seg-result.mp4"

vid_info = sv.VideoInfo.from_video_path(VIDEO_PATH)
frame_gen = sv.get_video_frames_generator(VIDEO_PATH)

mask_annotator = sv.MaskAnnotator()
# label_annotator = sv.LabelAnnotator()

with sv.VideoSink(RESULT_VIDEO, vid_info) as sink:
    for frame in tqdm(frame_gen, total=vid_info.total_frames):
        results = model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)
        annotated_image = mask_annotator.annotate(scene=frame.copy(), detections=detections)
        sink.write_frame(annotated_image)
