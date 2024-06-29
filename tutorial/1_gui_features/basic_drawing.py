import cv2 as cv
import numpy as np

def draw():
    # Создание RGB холста
    img = np.zeros((512, 512, 3), np.uint8)

    # Линия
    cv.line(img, (1, 1), (255, 50), (255, 0, 0), 5)

    # Прямоугольник
    cv.rectangle(img, (256, 256), (0, 511), (0, 0, 255), 1)

    # Круг
    cv.circle(img, (400, 256), 50, (0, 255, 0), -1)

    # Эллипс
    cv.ellipse(img, (400, 400), (100, 50), 0, 0, 360, 255, 2)

    # Полигон
    pts = np.array([[10, 5], [100, 50], [50, 100], [20, 50]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], True, (0, 255, 0), 2)

    # Текст
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, "OpenCV", (100, 200), font, 2, (255, 255, 255), 2)

    cv.imshow("Picture", img)
    if cv.waitKey(0) == ord("s"):
        cv.imwrite("../../images/drawing.jpg", img)
        print("Picture saved")

if __name__ == "__main__":
    draw()