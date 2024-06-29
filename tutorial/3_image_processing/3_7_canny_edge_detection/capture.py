import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
WINDOW_NAME = "Canny Demonstration"
cv.namedWindow(WINDOW_NAME)
cv.createTrackbar("MinVal", WINDOW_NAME, 0, 255, lambda x: None)
cv.createTrackbar("MaxVal", WINDOW_NAME, 255, 255, lambda x: None)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    minval = cv.getTrackbarPos("MinVal", WINDOW_NAME)
    maxval = cv.getTrackbarPos("MaxVal", WINDOW_NAME)

    canny = cv.Canny(frame, minval, maxval)
    res = np.concatenate([frame, canny], axis=1)
    cv.imshow(WINDOW_NAME, res)
    cv.waitKey(10)

cap.release()
cv.destroyAllWindows()