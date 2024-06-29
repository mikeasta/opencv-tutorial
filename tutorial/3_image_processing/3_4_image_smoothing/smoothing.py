import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.bitwise_not(cv.imread("../../../images/logo.jpg"))
rows, cols, ch = img.shape

# Adding noise
gauss_noise = np.zeros((rows, cols), dtype=np.uint8)
cv.randn(gauss_noise, 70, 30)
b, g, r = cv.split(img)
b = cv.add(b, gauss_noise)
g = cv.add(g, gauss_noise)
r = cv.add(r, gauss_noise)
noised = cv.merge((b, g, r))

# Blurring images
averaging = cv.blur(noised, (5, 5))
gaussian_blurring = cv.GaussianBlur(noised, (5, 5), 0)
median_blurring = cv.medianBlur(noised, 5)
bilateral_filtering = cv.bilateralFilter(noised, 9, 75, 75)

# Plotting
images = [
    img, 
    noised,
    averaging, 
    gaussian_blurring,
    median_blurring,
    bilateral_filtering
]

titles = [
    "Original", 
    "Added Noise",
    "Averaging Blur", 
    "Gaussian Blur",
    "Median Blur",
    "Bilateral Filtering"
]

for i in range(len(images)):
    plt.subplot(3, 2, i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
    plt.xticks([])
    plt.yticks([])
               
plt.show()