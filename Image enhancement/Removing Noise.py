import cv2

img = cv2.imread("resources/cat.jpg")
remove_img = cv2.medianBlur(img,11)
cv2.imshow("Output",remove_img)
cv2.imshow("Original",img)
cv2.waitKey(0)