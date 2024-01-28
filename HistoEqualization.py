import cv2

img = cv2.imread("resources/flower.jpg",0)
imgHist = cv2.equalizeHist(img)
cv2.imshow("Original",img)
cv2.imshow("HistEqu", imgHist)
cv2.waitKey(0)
