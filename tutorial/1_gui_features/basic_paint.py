import cv2 as cv
import numpy as np

drawing = False # Зажата ли кнопка мыши для рисования
mode    = True  # Режим рисования прямоугольников, иначе - кругов
ix, iy = -1, -1 # Используется в качестве буфера. Например, при нажатии и пере-
                # -носе курсора, для сохранения стартовых координат.

img = np.full((512, 512, 3), 255, np.uint8)

def draw(event, x, y, flags, params):
    global img, drawing, mode, ix, iy

    if event == cv.EVENT_LBUTTONDOWN:
        # Клавиша нажата, сохраняем координаты
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_LBUTTONUP:
        # Клавижа разжата
        drawing = False

    elif event == cv.EVENT_MOUSEMOVE:
        # Курсор передвигается
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), -1)
            else:
                cv.circle(img, (x, y), 3, (0, 255, 0), -1)
            ix, iy = x, y

WINDOW_NAME = "Paint"

cv.namedWindow(WINDOW_NAME)
cv.setMouseCallback(WINDOW_NAME, draw)

while True:
    cv.imshow(WINDOW_NAME, img)
    key = cv.waitKey(1) & 0xFF
    if key == ord("m"):
        mode = not mode
    elif key == ord("s"):
        cv.imwrite("../../images/painting.jpg", img)
        break

cv.destroyAllWindows()
        