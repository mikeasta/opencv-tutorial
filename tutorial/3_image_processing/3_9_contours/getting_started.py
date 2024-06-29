import numpy as np
import cv2 as cv

im = cv.imread("../../../images/dog.jpg")
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(
    thresh, 
    cv.RETR_TREE, 
    cv.CHAIN_APPROX_NONE
)
contours_s, hierarchy_s = cv.findContours(
    thresh, 
    cv.RETR_TREE, 
    cv.CHAIN_APPROX_SIMPLE
)

cv.drawContours(im, contours, -1, (0, 255, 0), 1)
cv.drawContours(im, contours_s, -1, (255, 0, 0), 1)
cv.imshow("contour", im)
cv.waitKey(0)