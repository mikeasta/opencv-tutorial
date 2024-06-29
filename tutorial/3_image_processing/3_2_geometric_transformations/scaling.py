import cv2 as cv
import numpy as np

# SCALING
img = cv.imread("../../../images/dog.jpg")
assert img is not None, "Cant read image"

res = cv.resize(img, None, fx=0.1, fy=0.1, interpolation=cv.INTER_LINEAR)

cv.imshow("scaling", res)
if cv.waitKey(0) == ord("s"):
    cv.destroyAllWindows()


