import cv2 as cv
import numpy as np

def draw_logo():
    img = np.full((512, 512, 3), 255, np.uint8)

    cv.ellipse(img, (100, 175), (30, 30), 45, 90, 360, (0, 0, 255), 25)
    cv.ellipse(img, (50, 250), (30, 30), -90, 90, 360, (0, 255, 0), 25)
    cv.ellipse(img, (150, 250), (30, 30), 225, 90, 360, (255, 0, 0), 25)
    font = cv.FONT_HERSHEY_PLAIN
    cv.putText(img, "OpenCV", (200, 225), font, 4, (0, 0, 0), 3)

    cv.imshow("OpenCV Logo", img)
    if cv.waitKey(0) == ord("s"):
        cv.imwrite("../../images/logo.jpg", img)
        print("Picture saved")

if __name__ == "__main__":
    draw_logo()