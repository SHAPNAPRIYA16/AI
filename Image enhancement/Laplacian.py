import cv2

img = cv2.imread("resources/cars.jpg")
cv2.imshow("Original",img)
sharpened_img = cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow("Output",sharpened_img)
cv2.waitKey(0)