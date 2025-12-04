import cv2
import numpy as np

def rotasi(derajat=0.0):
	img = cv2.imread('data/kursi.jpg')

	(h, w) = img.shape[:2]
	center = (w//2, h//2)

	scale = 1.0

	M = cv2.getRotationMatrix2D(center, derajat, scale)
	rotated = cv2.warpAffine(img, M, (w, h))

	cv2.imshow("Rotated", rotated)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	rotasi(-45)