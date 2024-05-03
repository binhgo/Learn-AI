import os
import cv2
import supervision as sv
from ultralytics import YOLO
from supervision.assets import download_assets, VideoAssets
import numpy as np

HOME = os.getcwd()
VIDEO_PATH = f"{HOME}/vehicles.mp4"
TARGET_VIDEO_PATH = f"{HOME}/videos/count-objects-crossing-the-line-result.mp4"


# download_assets(VideoAssets.VEHICLES)

def processFrame(frame: np.ndarray, index: int) -> np.ndarray:
    result = model(frame, verbose=False)[0]
    detections = sv.Detections.from_ultralytics(result)
    detections = byteTracker.update_with_detections(detections)

    annotated_frame = frame.copy()

    labels = [
        f"#{tracker_id} {model.model.names[class_id]} {confidence:0.2f}"
        for confidence, class_id, tracker_id
        in zip(detections.confidence, detections.class_id, detections.tracker_id)
    ]

    annotated_frame = trace_annotator.annotate(
        scene=annotated_frame,
        detections=detections)

    annotated_frame = bounding_box_annotator.annotate(
        scene=annotated_frame,
        detections=detections)

    annotated_frame = label_annotator.annotate(
        scene=annotated_frame,
        detections=detections,
        labels=labels)

    lineZone.trigger(detections)

    return lineZoneAnnotator.annotate(annotated_frame, line_counter=lineZone)


if __name__ == '__main__':
    model = YOLO("yolov8s.pt")
    # info = sv.VideoInfo.from_video_path(video_path=VIDEO_PATH)
    # frame_generator = sv.get_video_frames_generator(source_path=VIDEO_PATH)
    # frame = next(iter(frame_generator))
    #
    # annotatedFrame = frame.copy()
    # result = model(frame)[0]
    # print(result)
    # detections = sv.Detections.from_ultralytics(result)
    #
    # annotator = sv.BoundingBoxAnnotator(thickness=4)
    # annotatedFrame = annotator.annotate(annotatedFrame, detections)
    # # sv.plot_image(image=annotatedFrame, size=(8, 8))

    # draw line
    start = sv.Point(0, 1500)
    end = sv.Point(3840, 1500)
    lineZone = sv.LineZone(start, end)
    lineZoneAnnotator = sv.LineZoneAnnotator(thickness=4, text_thickness=4, text_scale=2)
    # annotatedFrame = lineZoneAnnotator.annotate(annotatedFrame, line_counter=lineZone)
    # sv.plot_image(image=annotatedFrame, size=(8, 8))

    byteTracker = sv.ByteTrack()

    bounding_box_annotator = sv.BoundingBoxAnnotator(thickness=4)
    label_annotator = sv.LabelAnnotator(text_thickness=4, text_scale=2)
    trace_annotator = sv.TraceAnnotator(thickness=4)

    sv.process_video(VIDEO_PATH, TARGET_VIDEO_PATH, processFrame)
    print("abc")
