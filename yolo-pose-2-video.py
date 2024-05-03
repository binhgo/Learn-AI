from ultralytics import YOLO
import supervision as sv
import os
from tqdm import tqdm

# Load a model
# model = YOLO('yolov8n-pose.yaml')  # build a new model from YAML
model = YOLO('yolov8n-pose.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n-pose.yaml').load('yolov8n-pose.pt')  # build from YAML and transfer weights

# Train the model
# results = model.train(data='coco8-pose.yaml', epochs=100, imgsz=640)

HOME = os.getcwd()
VIDEO_PATH = f"{HOME}/people-walking.mp4"
RESULT_VIDEO = f"{HOME}/videos/pose-result-2.mp4"

vid_info = sv.VideoInfo.from_video_path(VIDEO_PATH)
frame_gen = sv.get_video_frames_generator(VIDEO_PATH)

mask_annotator = sv.PolygonAnnotator()

with sv.VideoSink(RESULT_VIDEO, vid_info) as sink:
    for frame in tqdm(frame_gen, total=vid_info.total_frames):
        results = model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)
        annotated_image = mask_annotator.annotate(scene=frame.copy(), detections=detections)
        sink.write_frame(annotated_image)
