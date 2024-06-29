import cv2 as cv
import sys
import pathlib


def load_image(image_path: str | pathlib.Path):
    image = cv.imread(image_path)
    if image is None:
        sys.exit("Could not read image.")

    cv.imshow("dog", image)
    key = cv.waitKey(0)

    if key == ord("s"):
        cv.imwrite(image_path, image)


if __name__ == "__main__":
    load_image("../../images/dog.jpg")
    