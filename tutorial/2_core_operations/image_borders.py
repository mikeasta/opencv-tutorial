import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

BLUE = [0, 0, 255]

img = cv.imread("../../images/logo.jpg")
assert img is not None, "Cant find image, check path"

replicate = cv.copyMakeBorder(img,100, 100, 100, 100, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img,100, 100, 100, 100, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img,100, 100, 100, 100, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img,100, 100, 100, 100, cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img,100, 100, 100, 100, cv.BORDER_CONSTANT,value=BLUE)
 
plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
 
plt.show()