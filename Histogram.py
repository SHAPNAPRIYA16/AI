import cv2
from matplotlib import pyplot as py

img = cv2.imread("resources/flower.jpg",0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
py.plot(hist)
py.show()

