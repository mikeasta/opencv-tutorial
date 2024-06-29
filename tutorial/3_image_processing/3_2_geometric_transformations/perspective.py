import cv2 as cv
import numpy as np

img = cv.imread("../../../images/dog.jpg")
rows, cols, ch = img.shape

pts1 = [[200, 50], [50, 200], [200, 400], [350, 200]]
pts2 = [[200, 50], [50, 150], [200, 500], [350, 150]]

pts1_float32 = np.float32(pts1)
pts2_float32 = np.float32(pts2)

M = cv.getPerspectiveTransform(pts1_float32, pts2_float32)
dst = cv.warpPerspective(img, M, (cols, rows))

for p in pts1:
    cv.circle(img, p, 5, (0, 255, 0), -1)

for p in pts2:
    cv.circle(dst, p, 5, (0, 255, 0), -1)

res = np.concatenate([img, dst], axis=1)
cv.imshow("persp", res)
cv.waitKey(0)
cv.destroyAllWindows()
