from PIL import Image
import requests
import torch
from transformers import pipeline
from torch.nn.functional import cosine_similarity

img_urls = ["https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats.png",
            "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats.jpeg"]
image_real = Image.open(requests.get(img_urls[0], stream=True).raw).convert("RGB")
image_gen = Image.open(requests.get(img_urls[1], stream=True).raw).convert("RGB")

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
pipe = pipeline(task="image-feature-extraction",
                model_name="google/vit-base-patch16-384",
                device=DEVICE,
                pool=True)

outputs = pipe([image_real, image_gen])

print(len(outputs[0][0]))
# print(outputs)

similarity_score = cosine_similarity(torch.Tensor(outputs[0]),
                                     torch.Tensor(outputs[1]),
                                     dim=1)

print(similarity_score)
# tensor([0.6043])
