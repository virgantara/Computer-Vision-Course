import cv2
import numpy as np

def translasi():
	img = cv2.imread('data/kursi.jpg')

	tx, ty = 50, 100
	T = np.float32([[1, 0, tx],
	                [0, 1, ty]])

	translated = cv2.warpAffine(img, T, (img.shape[1], img.shape[0]))
	cv2.imshow("Translated", translated)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	translasi()