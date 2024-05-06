import os

from tqdm import tqdm
from huggingface_hub import notebook_login
from transformers import pipeline
import supervision as sv
import cv2
from PIL import Image, ImageDraw
import numpy as np

HOME = os.getcwd()
VIDEO_PATH = f"{HOME}/vehicles.mp4"
RESULT_VIDEO = f"{HOME}/videos/hug-segmentation-result-1.mp4"

vid_info = sv.VideoInfo.from_video_path(VIDEO_PATH)
frame_gen = sv.get_video_frames_generator(VIDEO_PATH)

semantic_segmentation = pipeline("image-segmentation", "nvidia/segformer-b1-finetuned-cityscapes-1024-1024")

videodims = (vid_info.width, vid_info.height)
fourcc = cv2.VideoWriter_fourcc(*'avc1')
video = cv2.VideoWriter(RESULT_VIDEO, fourcc, 60, videodims)
img = Image.new('RGB', videodims, color='darkred')
# draw stuff that goes on every frame here
# for i in range(0, 60 * 60):
#     imtemp = img.copy()
#     # draw frame specific stuff here.
#     video.write(cv2.cvtColor(np.array(imtemp), cv2.COLOR_RGB2BGR))
# video.release()

count = 0

for frame in tqdm(frame_gen, total=vid_info.total_frames):
    if count == 300:
        break
    count = count + 1

    color_converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(color_converted).convert('RGBA')
    # sv.plot_image(pil_image, size=(8, 8))

    results = semantic_segmentation(pil_image)

    overlay = Image.new('RGBA', pil_image.size, (255, 255, 255, 0))
    drawing = ImageDraw.Draw(overlay)
    drawing.bitmap((0, 0), results[0]['mask'], fill=(255, 0, 0, 128))
    final = Image.alpha_composite(pil_image, overlay)
    # sv.plot_image(final, size=(8, 8))

    video.write(cv2.cvtColor(np.array(final), cv2.COLOR_RGB2BGR))
    # sink.write_frame(final)

video.release()
