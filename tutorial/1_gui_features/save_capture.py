import cv2 as cv

def save_capture():
    cap = cv.VideoCapture(0)

    w = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv.VideoWriter.fourcc(*"mp4v")
    out = cv.VideoWriter("../../videos/capture.mp4", fourcc, 20.0, (w, h))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Cant get image from capture")
            break

        frame = cv.flip(frame, 0)

        out.write(frame) # Сохранить кадр в реальном времени
        cv.imshow("capture", frame) # Показать кадр в реальном времени

        if cv.waitKey(1) == ord("s"):
            print("Capture stopped")
            break
        
    cap.release()
    out.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    save_capture()