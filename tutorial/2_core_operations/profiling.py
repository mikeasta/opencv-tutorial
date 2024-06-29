import cv2 as cv
import numpy as np
import time

img1 = cv.imread("../../images/dog.jpg")
img2 = np.copy(img1)

def median(img: np.array):
    for i in range(5, 49, 2):
        img = cv.medianBlur(img, i)


# Time lib approach
start = time.time()
median(img1)
finish = time.time()
print(f"Time approach: {finish - start} seconds")

# CV lib approach
start = cv.getTickCount()
median(img2)
finish = cv.getTickCount()
print(f"CV2 approach: {(finish - start) / cv.getTickFrequency()} seconds")

# Difference about 0.3%