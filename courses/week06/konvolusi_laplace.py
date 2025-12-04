import cv2
import numpy as np
from util import convolve
import matplotlib.pyplot as plt

def konvolusi():
	img = cv2.imread('../week05/data/kursi.jpg')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	(h, w) = img.shape[:2]
	
	laplacian = np.array([
	    [0, -1, 0],
	    [-1, 4, -1],
	    [0, -1, 0]
	])

	lap = convolve(img, laplacian)
	
	plt.imshow(lap, cmap='gray')
	plt.title("Laplacian")
	plt.show()


if __name__ == '__main__':
	konvolusi()