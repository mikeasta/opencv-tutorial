import cv2 as cv
import numpy as np 

img = cv.imread("../../../images/dog.jpg")

lower_1 = cv.pyrDown(img)
lower_2 = cv.pyrDown(lower_1)
lower_3 = cv.pyrDown(lower_2)
cv.imshow("Pyr 3", lower_3)
cv.waitKey(0)
cv.destroyAllWindows()
