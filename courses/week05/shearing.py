import cv2
import numpy as np

def shear(shear_factor=0.0):
	img = cv2.imread('data/kursi.jpg')
	(h, w) = img.shape[:2]
	M = np.float32([[1, shear_factor, 0],
	                [0, 1, 0]])

	sheared = cv2.warpAffine(img, M, (int(w + shear_factor*h), h))
	cv2.imshow("Sheared", sheared)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	shear(shear_factor=0.5)