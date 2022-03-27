import numpy as np
from skimage import data
import matplotlib.pyplot as plt


image = data.camera()
type(image)
numpy.ndarray  # Image is a NumPy array:

mask = image < 87
image[mask] = 255
plt.imshow(image, cmap='gray')