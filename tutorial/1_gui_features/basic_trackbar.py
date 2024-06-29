import cv2 as cv
import numpy as np

img = np.full((300, 512, 3), 255, np.uint8)

# Определяем окно
WINDOW_NAME = "Trackbar"
cv.namedWindow(WINDOW_NAME)

# Создаем функцию, которая будет логировать изменение ползунка
def on_change(new_value: int):
    print(f"Новое значение = {new_value}")

# Смена цветового канала
cv.createTrackbar("R", WINDOW_NAME, 0, 255, on_change)
cv.createTrackbar("G", WINDOW_NAME, 0, 255, on_change)
cv.createTrackbar("B", WINDOW_NAME, 0, 255, on_change)

# Переключатель
switch = "0 : OFF\n1 : ON"
cv.createTrackbar(switch, WINDOW_NAME, 0, 1, on_change)

# Отрисовка
while True:
    cv.imshow(WINDOW_NAME, img)
    key = cv.waitKey(1) & 0xFF
    if key == ord("s"):
        break

    # Получить текущие значения ползунков
    r = cv.getTrackbarPos("R", WINDOW_NAME)
    g = cv.getTrackbarPos("G", WINDOW_NAME)
    b = cv.getTrackbarPos("B", WINDOW_NAME)
    s = cv.getTrackbarPos(switch, WINDOW_NAME)

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()




