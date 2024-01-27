import cv2
cap = cv2.VideoCapture("resources/video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("video1", img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
