import cv2
img1 = cv2.imread("resources/image1.png")
img2 = cv2.imread("resources/image2.png")

imgAnd = cv2.bitwise_and(img1,img2,mask=None)
imgOr = cv2.bitwise_or(img1,img2,mask=None)
imgXor = cv2.bitwise_xor(img1,img2,mask=None)
imgNot = cv2.bitwise_not(img1,mask=None)

cv2.imshow("AND",imgAnd)
cv2.imshow("OR",imgOr)
cv2.imshow("XOR",imgXor)
cv2.imshow("NOT",imgNot)
cv2.waitKey(0)
cv2.destroyAllWindows()


