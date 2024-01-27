import cv2
import numpy as np

img = cv2.imread("resources/cat.jpg")
imgHor = np.hstack((img,img))
cv2.imshow("Horizontal",imgHor)

imgVer = np.vstack((img,img))
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)