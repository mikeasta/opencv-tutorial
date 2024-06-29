import cv2 as cv
import numpy as np

# Translation
img = cv.imread("../../../images/dog.jpg", cv.IMREAD_GRAYSCALE)
assert img is not None, "Cant read image"
rows, cols = img.shape

offset_x, offset_y = 100, 50

M = np.float32([[1, 0, offset_x], [0, 1, offset_y]])
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow("trans", dst)
cv.waitKey(0)
cv.destroyAllWindows()