import numpy as np
import cv2 as cv
 
img = cv.imread('../../../images/dog.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
 
print(contours)
cv.drawContours(img, contours, -1, (0, 255, 0), 1)

cv.imshow("dog", cv.cvtColor(img, cv.COLOR_GRAY2BGR))
cv.waitKey(0)
cv.destroyAllWindows()