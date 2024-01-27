import cv2
import numpy as np

img = cv2.imread("resources/cat.jpg")
kernel = np.ones((5,5), np.uint8)  #uint8 for 8 bit 0-255
#cv2.imshow("kernel",kernel)

# Gray image
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("graycat", imgGray)

# Blur image
imgBlur = cv2.GaussianBlur(img, (7,7),0)
cv2.imshow("blurcat", imgBlur)

# edge detector
imgEdge = cv2.Canny(img, 200, 200)
cv2.imshow("canny", imgEdge)

# dilation
imgDilation = cv2.dilate(imgEdge, kernel, iterations=1)
cv2.imshow("dilated", imgDilation)

# Erosion
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
cv2.imshow("eroded", imgEroded)

cv2.waitKey(0)
