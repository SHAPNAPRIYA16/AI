import cv2
print("Package imported")
img1 = cv2.imread("resources/cat.jpg")
cv2.imshow("Cat1", img1)
cv2.waitKey(0)