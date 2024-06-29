import cv2 as cv
import numpy as np

WINDOW_NAME = "Paint"

def event_listener(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 20, (0, 0, 255), -1)

img = np.full((512, 512, 3), 255, np.uint8)
cv.namedWindow(WINDOW_NAME)
cv.setMouseCallback(WINDOW_NAME, event_listener)

while True:
    cv.imshow(WINDOW_NAME, img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()