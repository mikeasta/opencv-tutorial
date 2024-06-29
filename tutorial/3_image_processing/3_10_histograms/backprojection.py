import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../../images/dog.jpg") 
roi = img[500:600, 250:300, :] 


hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)

hist_roi = cv.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv.normalize(hist_roi, hist_roi, 0, 255, cv.NORM_MINMAX)
dst = cv.calcBackProject([hsv_img], [0, 1], hist_roi, [0, 180, 0, 256], 1)

disc = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
cv.filter2D(dst,-1,disc,dst)

ret,thresh = cv.threshold(dst,50,255,0)
thresh = cv.merge((thresh,thresh,thresh))
res = cv.bitwise_and(img,thresh)

res = np.concatenate([img,thresh,res], axis=1)
cv.imshow('res.jpg',res)
cv.waitKey(0)