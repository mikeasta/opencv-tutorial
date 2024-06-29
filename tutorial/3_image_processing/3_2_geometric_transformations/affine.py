import cv2 as cv
import numpy as np

img = cv.imread("../../../images/dog.jpg")
assert img is not None, "Cant read image"
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 50], [200, 70], [100, 200]])

M = cv.getAffineTransform(pts1, pts2)
dst = cv.warpAffine(img, M, (cols, rows))

print(list(list(pts1)[0]))
for p in list(pts1):
    cv.circle(img, list(map(int, list(p))), 10, (0, 255, 0), -1)

for p in list(pts2):
    cv.circle(dst, list(map(int, list(p))), 10, (0, 255, 0), -1)

cv.imshow("affine", np.concatenate([img, dst], axis=1))
cv.waitKey(0)
cv.destroyAllWindows()