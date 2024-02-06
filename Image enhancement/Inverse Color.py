import cv2

img = cv2.imread("resources/cat.jpg")
inverse = 255-img
cv2.imshow("Original",img)
cv2.imshow("output",inverse)
cv2.waitKey(0)