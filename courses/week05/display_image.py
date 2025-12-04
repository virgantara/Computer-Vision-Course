import cv2
import numpy as np




img = cv2.imread('data/kursi.jpg')
cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
