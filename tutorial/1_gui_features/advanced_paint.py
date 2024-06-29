import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# Создадим окно
WINDOW_NAME = "Advanced Paint"
cv.namedWindow(WINDOW_NAME)

# Зададим ползунки
nothing = lambda x: print(x)
cv.createTrackbar("R", WINDOW_NAME, 255, 255, nothing)
cv.createTrackbar("G", WINDOW_NAME, 255, 255, nothing)
cv.createTrackbar("B", WINDOW_NAME, 255, 255, nothing)

switch = "0 : Circle\n1 : Rectangle"
cv.createTrackbar(switch, WINDOW_NAME, 1, 1, nothing)

# Настраиваем рисование
color = (255, 255, 255)
drawing = False
mode = True
ix, iy = -1, -1

def draw(event, x, y, flags, params):
    global img, color, drawing, ix, iy

    if event == cv.EVENT_LBUTTONDOWN:
        # ЛКМ нажата
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        # Курсор передвигается
        if drawing:
            if mode:
                cv.rectangle(img, (ix, iy), (x, y), color, -1)
            else:
                cv.circle(img, (x, y), 3, color, -1)
            
            ix, iy = x, y

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False

cv.setMouseCallback(WINDOW_NAME, draw)

while True:
    # Отрисовываем картинку
    cv.imshow(WINDOW_NAME, img)

    # Ожидаем остановки программы
    key = cv.waitKey(1) & 0xFF
    if key == ord("s"):
        cv.imwrite("../../images/advance_paint_drawing.jpg", img)
        print("Paint stopped")
        break

    # Изменяем параметры кисти согласно ползункам
    r = cv.getTrackbarPos("R", WINDOW_NAME)
    g = cv.getTrackbarPos("G", WINDOW_NAME)
    b = cv.getTrackbarPos("B", WINDOW_NAME)
    s = cv.getTrackbarPos(switch, WINDOW_NAME)

    color = (b, g, r)
    mode = s

    
cv.destroyAllWindows()  