import cv2 as cv 
import numpy as np 

img = cv.imread("../../../images/dog.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img, contours, -1, (0, 255, 0), 3)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()

