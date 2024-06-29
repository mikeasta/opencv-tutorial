import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../../../images/dog.jpg", cv.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)

erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
gradient_ellipse = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

# Plotting
images = [
    img, 
    erosion,
    dilation,
    opening,
    closing,
    gradient,
    tophat,
    blackhat,
    gradient_ellipse
]
titles = [
    "Original",
    "Erosion",
    "Dilation",
    "Opening",
    "Closing",
    "Gradient",
    "Tophat",
    "Blackhat",
    "Gradient with Ellipse kernel"
]


for i in range(len(images)):
    plt.subplot(3, 3, i+1)
    plt.title(titles[i])
    plt.imshow(images[i], "gray")
    plt.xticks([])
    plt.yticks([])
               
plt.show()