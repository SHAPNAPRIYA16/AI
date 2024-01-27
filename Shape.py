import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
'''img[:] = 255, 0, 0     # img[0:100,100:200]
cv2.imshow("image", img)'''

cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.rectangle(img, (0,0), (100,200), (0,0,255), 2)  # instead of thickness give cv2.FILLED
cv2.circle(img,(450,450),30,(255,255,0),5)
cv2.putText(img,"OPENCV",(300,300),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

cv2.imshow("line", img)




cv2.waitKey(0)