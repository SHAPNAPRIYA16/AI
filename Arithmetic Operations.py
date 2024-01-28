import cv2

img1 = cv2.imread("resources/flower.jpg")
img2 = cv2.imread("resources/flower.jpg")
imgRes = cv2.add(img1,img2)
imgSub = cv2.subtract(img1,img2)
cv2.imshow("Output",imgRes)
cv2.imshow("Output2",imgSub)
cv2.waitKey(0)