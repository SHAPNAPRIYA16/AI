import cv2

img = cv2.imread("resources/cat.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
imgThres1 = cv2.threshold(imgGray, 100, 255, cv2.THRESH_BINARY)[1]
# Inverse of above.
imgThres2 = cv2.threshold(imgGray,100,255,cv2.THRESH_BINARY_INV)[1]

''' If pixel intensity value is greater than threshold, it is truncated to the threshold. 
# The pixel values are set to be the same as the threshold. All other values remain the same.'''
imgThres3 = cv2.threshold(imgGray,10,255,cv2.THRESH_TRUNC)[1]

# Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
imgThres4 = cv2.threshold(imgGray,100,255,cv2.THRESH_TOZERO)[1]
# Inverse of above.
imgThres5 = cv2.threshold(imgGray,100,255,cv2.THRESH_TOZERO_INV)[1]

cv2.imshow("Gray",imgGray)
cv2.imshow("Thres1", imgThres1)
cv2.imshow("Thres2", imgThres2)
cv2.imshow("Thres3", imgThres3)
cv2.imshow("Thres4", imgThres4)
cv2.imshow("Thres5", imgThres5)
cv2.waitKey(0)