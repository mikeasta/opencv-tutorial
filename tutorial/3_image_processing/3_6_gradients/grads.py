import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../../images/dog.jpg", cv.IMREAD_GRAYSCALE)

laplacian = cv.Laplacian(img, cv.CV_64F)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=5)

images = [img, laplacian, sobelx, sobely]
titles = ["Original", "Laplacian", "Sobel using dx", "Sobel using dy"]

for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.title(titles[i])
    plt.imshow(images[i], cmap="gray")
    plt.xticks([])
    plt.yticks([])
               
plt.show()