import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../../images/logo.jpg")

kernel = np.ones((5, 5), np.float32) / 25
fil = cv.filter2D(img, -1, kernel)

res = np.concatenate([img, fil], axis=1)
cv.imshow("img", res)
cv.waitKey(0)
cv.destroyAllWindows()