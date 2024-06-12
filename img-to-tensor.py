import torch
import torchvision.transforms as transforms
from PIL import Image
import os

HOME = os.getcwd()
VIDEO_PATH = f"{HOME}/images/dog.jpeg"
# Load an image (assuming it is in RGB format)
image = Image.open(VIDEO_PATH)

# Transform to tensor (shape will be [3, 512, 512] if the image is 512x512 pixels)
transform = transforms.Compose([
    transforms.ToTensor()  # Convert the image to a tensor
])

image_tensor = transform(image)  # Image tensor will have shape (3, 512, 512)
print(image_tensor.shape)
print(image_tensor)
