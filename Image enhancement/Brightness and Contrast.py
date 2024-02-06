import cv2
import numpy as np

img = cv2.imread("resources/cars.jpg")
cv2.imshow("Original",img)
image = cv2.addWeighted(img,2.3,np.zeros(img.shape,img.dtype),0,10)
cv2.imshow("output",image)
cv2.waitKey(0)

''' 
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
  
# Load the image 
image = cv2.imread('GFG.jpeg') 
  
#Plot the original image 
plt.subplot(1, 2, 1) 
plt.title("Original") 
plt.imshow(image) 
  
# Adjust the brightness and contrast  
# g(i,j)=α⋅f(i,j)+β 
# control Contrast by 1.5 
alpha = 1.5  
# control brightness by 50 
beta = 50  
image2 = cv2.convertScaleAbs(image, alpha=alpha, beta=beta) 
  
#Save the image 
cv2.imwrite('Brightness & contrast.jpg', image2) 
#Plot the contrast image 
plt.subplot(1, 2, 2) 
plt.title("Brightness & contrast") 
plt.imshow(image2) 
plt.show() '''