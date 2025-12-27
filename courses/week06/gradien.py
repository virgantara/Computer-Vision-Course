import matplotlib.pyplot as plt
import numpy as np
import imageio
from scipy import ndimage
import os
import cv2

data_path = 'data'

img = cv2.imread(os.path.join(data_path, "grad1.png"))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

Ix = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
Iy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

step = 10
y, x = np.mgrid[0:gray.shape[0]:step, 0:gray.shape[1]:step]


plt.figure(figsize=(16,16))

plt.subplot(2,2,1)
plt.imshow(gray, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(np.abs(Ix), cmap='gray')
plt.title("Gradient Ix ")
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(np.abs(Iy), cmap='gray')
plt.title("Gradient Iy")
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(gray, cmap='gray')
plt.quiver(
    x, y,
    Ix[::step, ::step],
    Iy[::step, ::step],
    color='red'
)
plt.title("Vektor Gradien")
plt.axis('off')

plt.show()