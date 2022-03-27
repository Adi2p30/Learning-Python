import numpy as np
from skimage import io
import matplotlib.pyplot as plt

image = io.imread('Assets/WIN_20201115_17_51_56_Pro.jpg')
print(image.shape)
plt.imshow(image)
type(image)
np.ndarray


mask = image < 87.2
print(image)
image[mask] = 255
plt.imshow(image, cmap = 'gray')
plt.show()
print(np.shape(image))