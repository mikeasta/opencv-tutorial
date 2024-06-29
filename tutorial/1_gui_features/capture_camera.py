import cv2 as cv

def capture_camera():
    # Достаем камеру
    cap = cv.VideoCapture(0)

    # Получаем текущее разрешение
    w = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv.CAP_PROP_FRAME_HEIGHT)

    # Изменяем размер
    cap.set(cv.CAP_PROP_FRAME_WIDTH, w * 1.2)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, h * 1.2)

    # Отрисовываем кадры
    while True:
        if not cap.isOpened():
            # Если камера не заработала
            print(f"Cant open camera {0}")
            exit()

        else:
            # Если камера заработала, достаем из нее кадры. 
            # Если кадр не удается достать, ret будет равна False.
            ret, frame = cap.read()

            if not ret:
                print("Cant recieve frame (stream end?)")
                break
            
            # Применяем серый фильтр к кадру
            gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
            cv.imshow("camera", gray)

            # Работа программы продолжится, пока окно OpenCV не получит на вход
            # определенную клавишу
            if cv.waitKey(1) == ord("s"):
                print("Camera stoped")
                break

    # Камера отключается
    cap.release()

    # Все открытые окна закрываются
    cv.destroyAllWindows()

if __name__ == "__main__":
    capture_camera()
