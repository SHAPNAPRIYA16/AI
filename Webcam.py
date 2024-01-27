import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640)  #width
cap.set(4,280) #height
cap.set(10,100) #brightness

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
