from huggingface_hub import notebook_login
from transformers import pipeline
from PIL import Image
import requests
import supervision as sv
import cv2

import sys
from PIL import Image, ImageDraw

import os

HOME = os.getcwd()
IMAGE_PATH = f"{HOME}/images/segmentation_input.jpeg"
RESULT_PATH = f"{HOME}/images/segmentation_input_result.PNG"

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/segmentation_input.jpg"
image = Image.open(requests.get(url, stream=True).raw)

semantic_segmentation = pipeline("image-segmentation", "nvidia/segformer-b1-finetuned-cityscapes-1024-1024")
results = semantic_segmentation(image)
# sv.plot_image(image=image, size=(8, 8))
# sv.plot_image(image=results, size=(8, 8))
print('\n')
print(len(results))
print('\n')
# print(results)

# img = cv2.imread(filename=IMAGE_PATH)

input_img = (Image.open(IMAGE_PATH)).convert('RGBA')
# input_img.putalpha(128)

overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
drawing = ImageDraw.Draw(overlay)
drawing.bitmap((0, 0), results[9]['mask'], fill=(255, 255, 255, 128))
# overlay.save(RESULT_PATH, "PNG")

final = Image.alpha_composite(input_img, overlay)
final.save(RESULT_PATH, "PNG")

# sv.plot_image(image=x['mask'], size=(8, 8))
# with (Image.open(IMAGE_PATH)).convert('RGBA') as im:
#     draw = ImageDraw.Draw(im)
#     # for x in results:
#     draw.bitmap([0, 0], results[9]['mask'], fill=(0, 0, 0, 0))
#     im.save(RESULT_PATH, "PNG")

# cv2.imwrite(filename="abc.jpg", img=x['mask'])
# results[-1]["mask"]
# sv.plot_image(image=results[-1]["mask"], size=(612, 415))
# sv.plot_image(image=results[0]["mask"], size=(612, 415))
# sv.plot_image(image=results[1]["mask"], size=(612, 415))
