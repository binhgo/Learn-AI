import os
import cv2
import supervision as sv
from ultralytics import YOLO
from supervision.assets import download_assets, VideoAssets
import numpy as np

HOME = os.getcwd()
print(HOME)

# download_assets(VideoAssets.VEHICLES)

if __name__ == '__main__':
    IMAGE_PATH = f"{HOME}/dog.jpeg"
    image = cv2.imread(IMAGE_PATH)
    print(sv.__version__)

    model = YOLO("yolov8s.pt")

    VIDEO_PATH = f"{HOME}/vehicles.mp4"
    print(VIDEO_PATH)

    info = sv.VideoInfo.from_video_path(video_path=VIDEO_PATH)
    print(info)

    frame_generator = sv.get_video_frames_generator(source_path=VIDEO_PATH)
    frame = next(iter(frame_generator))
    sv.plot_image(image=frame, size=(8, 8))

    RESULT_VIDEO_PATH = f"{HOME}/videos/vehicle-counting-result.mp4"

    with sv.VideoSink(target_path=RESULT_VIDEO_PATH, video_info=info) as sink:
        for frame in sv.get_video_frames_generator(source_path=VIDEO_PATH, stride=2):
            sink.write_frame(frame=frame)

    # result = model(image, verbose=False)[0]
    # detections = sv.Detections.from_ultralytics(result)

    # mask_annotator = sv.MaskAnnotator(color_lookup=sv.ColorLookup.INDEX)
    # annotated_image = mask_annotator.annotate(image.copy(), detections=detections)
    # sv.plot_image(image=annotated_image, size=(8, 8))
    #
    # box_annotator = sv.BoxAnnotator()
    # labels = [
    #     f"{model.model.names[class_id]} {confidence:.2f}"
    #     for class_id, confidence in zip(detections.class_id, detections.confidence)
    # ]
    # annotated_image = box_annotator.annotate(image.copy(), detections=detections, labels=labels)
    # sv.plot_image(image=annotated_image, size=(8, 8))

    # detections_index = detections[0]
    # print(detections_index)
