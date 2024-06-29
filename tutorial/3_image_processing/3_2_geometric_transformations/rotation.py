import cv2 as cv
import numpy as np

# Rotation
img = cv.imread("../../../images/dog.jpg", cv.IMREAD_GRAYSCALE)
assert img is not None, "Cant read image"
rows, cols = img.shape

M = cv.getRotationMatrix2D(((cols - 1) / 2, (rows - 1) / 2), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow("trans", dst)
cv.waitKey(0)
cv.destroyAllWindows()