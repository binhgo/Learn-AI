import numpy as np
import matplotlib.pyplot as plt

# Create a blank image (e.g., 256x256 pixels)
height, width = 256, 256
blank_image = np.zeros((height, width), dtype=np.float32)

# Add Gaussian noise
mean = 0
std_dev = 1
gaussian_noise = np.random.normal(mean, std_dev, (height, width))

# Display the noisy image
plt.imshow(gaussian_noise, cmap='gray')
plt.title('Gaussian Noise')
plt.axis('off')
plt.show()
