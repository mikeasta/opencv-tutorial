import numpy as np
import cv2 as cv

img = cv.imread("../../images/dog.jpg")
assert img is not None, "Cant read image, check path"

# = Accessing and Modifying pixel values
x, y = 100, 100
px = img[y, x] # Getting pixel with coords (100, 100) (i suppose "y" first since [row_index, col_index])
print(f"Pixel {x}, {y}: {px}") # BGR output

# getting blue value of pixel
blue = img[y, x, 0]
print(f"Blue value of {x}, {y}: {blue}")

# modifying pixel values (bad approach)
img[y, x] = [255, 255, 255]
print(f"Modified pixel {x}, {y} value: {img[y, x]}")

# modifying pixel values (good approach)
print(img.item(10, 10, 2)) # Getting red value
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2)) # Getting updated red value

# = Accessing image properties
print(f"Shape: {img.shape}")
print(f"Size: {img.size}")
print(f"Type: {img.dtype}")

# = Image "Region of Interest"
# Copy and paste part of image to the other side
eye = img[270:310, 240:290] # y_top:y_bottom, x_left:x_right
img[10:50, 10:60] = eye # Same distances inside dimensions
cv.imwrite("../../images/dog_patched.jpg", img)

# = Splitting and merging image channels
b, g, r = cv.split(img)
img = cv.merge((b, g, r))

b = img[:, :, 0] # Get all blue values manually
img[:, :, 2] = 0 # Set all red values to zero
cv.imwrite("../../images/dog_no_red.jpg", img)

img[:, :, 1] = 0 # Set all green values to zero
cv.imwrite("../../images/dog_only_blue.jpg", img)