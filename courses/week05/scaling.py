import cv2
import numpy as np

def scale(skala=1.5):
	img = cv2.imread('data/kursi.jpg')

	scaled = cv2.resize(img, None, fx=skala, fy=skala)
	cv2.imshow("Scaled", scaled)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	scale(skala=0.3)