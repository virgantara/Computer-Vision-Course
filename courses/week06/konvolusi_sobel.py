import cv2
import numpy as np
from util import convolve
import matplotlib.pyplot as plt

def konvolusi():
	img = cv2.imread('../week05/data/kursi.jpg')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	(h, w) = img.shape[:2]
	sobel_x = np.array([
	    [-1, 0, 1],
	    [-2, 0, 2],
	    [-1, 0, 1]
	])

	sobel_y = np.array([
	    [-1, -2, -1],
	    [ 0,  0,  0],
	    [ 1,  2,  1]
	])

	gx = convolve(img, sobel_x)
	gy = convolve(img, sobel_y)

	gradient = np.sqrt(gx**2 + gy**2)

	plt.imshow(gradient, cmap='gray')
	plt.title("Sobel Edge Detection")
	plt.show()


if __name__ == '__main__':
	konvolusi()