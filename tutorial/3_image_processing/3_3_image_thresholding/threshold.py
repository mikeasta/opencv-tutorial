import cv2 as cv
import numpy as np

img = cv.imread("../../../images/dog.jpg", cv.IMREAD_GRAYSCALE)

ret, thresh1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img, 100, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img, 100, 255, cv.THRESH_TOZERO_INV)


cv.putText(img, "Initial", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, color=[0, 0, 0])
cv.putText(thresh1, "THRESH_BINARY", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, color=[0, 0, 0])
cv.putText(thresh2, "THRESH_BINARY_INV", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, color=[255, 255, 255])
cv.putText(thresh3, "THRESH_TRUNC", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, color=[0, 0, 0])
cv.putText(thresh4, "THRESH_TOZERO", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, color=[0, 0, 0])
cv.putText(thresh5, "THRESH_TOZERO_INV", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, color=[255, 255, 255])

res = np.concatenate([img, thresh1, thresh2, thresh3, thresh4, thresh5], axis=1)
cv.imshow("thresh", res)
cv.waitKey(0)
cv.imwrite("../../../images/threshold_examples.jpg", res)
cv.destroyAllWindows()