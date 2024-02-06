import cv2
#import imutils

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

img = cv2.imread("resources/pedestrian.jpg")

#img = imutils.resize(img,width = min(400,img.shape[1]))
(places,success) = hog.detectMultiScale(img,winStride=(5,5),padding=(5,5),scale=1.05)
for (x,y,w,h) in places:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Output",img)
cv2.waitKey(0)


