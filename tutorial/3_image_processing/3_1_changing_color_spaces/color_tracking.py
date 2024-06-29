import cv2 as cv
import numpy as np

# Активируем камеру и ее параметры
cap = cv.VideoCapture(0)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Задаем кодек для записи экрана
fourcc = cv.VideoWriter.fourcc(*"mp4v")
out = cv.VideoWriter("../../../videos/color_tracking.mp4", fourcc, 20.0, (width, height))

# Задаем таскбары
WINDOW_NAME = "frame"
cv.namedWindow(WINDOW_NAME)

nothing = lambda x: print(x)
cv.createTrackbar("Lower_R", WINDOW_NAME, 0, 255, nothing)
cv.createTrackbar("Lower_G", WINDOW_NAME, 0, 255, nothing)
cv.createTrackbar("Lower_B", WINDOW_NAME, 0, 255, nothing)
cv.createTrackbar("Upper_R", WINDOW_NAME, 255, 255, nothing)
cv.createTrackbar("Upper_G", WINDOW_NAME, 255, 255, nothing)
cv.createTrackbar("Upper_B", WINDOW_NAME, 255, 255, nothing)

# Рендеринг
while cap.isOpened():
    ret, frame = cap.read()
    assert ret, "Cant get image from capture"

    # Конвертируем изображение в Hue-Saturation-Vibrance формат
    # (ибо так якобы проще выделять цвет)
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Определяем границы заданного цвета
    lower_r = cv.getTrackbarPos("Lower_R", WINDOW_NAME)
    lower_g = cv.getTrackbarPos("Lower_G", WINDOW_NAME)
    lower_b = cv.getTrackbarPos("Lower_B", WINDOW_NAME)
    upper_r = cv.getTrackbarPos("Upper_R", WINDOW_NAME)
    upper_g = cv.getTrackbarPos("Upper_G", WINDOW_NAME)
    upper_b = cv.getTrackbarPos("Upper_B", WINDOW_NAME)

    lower_color = np.uint8([[[lower_b, lower_g, lower_r]]])
    upper_color = np.uint8([[[upper_b, upper_g, upper_r]]])

    lower_color_thresh = cv.cvtColor(lower_color, cv.COLOR_BGR2HSV)
    upper_color_thresh = cv.cvtColor(upper_color, cv.COLOR_BGR2HSV)

    # Маска
    mask = cv.inRange(hsv, lower_color_thresh[0][0], upper_color_thresh[0][0])

    # Применение маски
    masked_frame = cv.bitwise_and(frame, frame, mask=mask)

    # Объединение всего в одно изображение
    result = np.concatenate((
        frame, 
        cv.cvtColor(mask, cv.COLOR_GRAY2BGR), 
        masked_frame), axis=1)

    out.write(result)
    cv.imshow(WINDOW_NAME, result)

    if cv.waitKey(1) == ord("s"):
        print("Camera Stopped")
        break

cap.release()
out.release()
cv.destroyAllWindows()