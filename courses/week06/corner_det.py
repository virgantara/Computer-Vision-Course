import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("data/buku.jpg", cv2.IMREAD_GRAYSCALE).astype(np.float32)

Ix = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
Iy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

Ixx = cv2.GaussianBlur(Ix * Ix, (3, 3), 0.5)
Iyy = cv2.GaussianBlur(Iy * Iy, (3, 3), 0.5)
Ixy = cv2.GaussianBlur(Ix * Iy, (3, 3), 0.5)

k = 0.04
R = (Ixx * Iyy - Ixy**2) - k * (Ixx + Iyy)**2

# DEBUG: lihat response
# plt.figure(figsize=(6,5))
# plt.imshow(R, cmap="jet")
# plt.colorbar()
# plt.title("Harris Response")
# plt.axis("off")
# plt.show()

# Threshold lebih longgar
threshold = 0.001 * R.max()
corners = R > threshold

img_color = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_GRAY2BGR)
img_color[corners] = [0, 0, 255]

plt.figure(figsize=(8,6))
plt.imshow(img_color[..., ::-1])
plt.title("Detected Harris Corners")
plt.axis("off")
plt.show()
