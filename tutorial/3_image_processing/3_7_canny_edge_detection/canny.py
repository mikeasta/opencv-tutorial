import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../../images/dog.jpg", cv.IMREAD_GRAYSCALE)

canny_edges = cv.Canny(img, 100, 200)
accurate_canny_edges = cv.Canny(img, 100, 200, L2gradient=True)

images = [img, canny_edges, accurate_canny_edges]
titles = ["Original", "Canny", "More Accurate Canny Formula"]


for i in range(len(images)):
    plt.subplot(1, 3, i+1)
    plt.title(titles[i])
    plt.imshow(images[i], cmap="gray")
    plt.xticks([])
    plt.yticks([])
               
plt.show()