# import the necessary packages
import numpy as np
import cv2
 
# Image Reading
image = cv2.imread("test.png")
 
# Find the red color game in the image
upper = np.array([65, 65, 255])
lower = np.array([0, 0, 200])
mask = cv2.inRange(image, lower, upper)
 
# Find contours in the masked image and keep the largest one
(cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
c = max(cnts, key=cv2.contourArea)
 
# Approximate the contour
peri = cv2.arcLength(c, True)
approx = cv2.approxPolyDP(c, 0.05 * peri, True)
 
# Draw a green bounding box surrounding the red game
cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
cv2.imshow("Image", image)
cv2.waitKey(0)