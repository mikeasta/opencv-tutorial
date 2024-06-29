import cv2 as cv
import pathlib
import time

def capture_video(video_path: str | pathlib.Path) -> None:
    cap = cv.VideoCapture(video_path)

    if not cap.isOpened():
        print("Cant get video capture")
        exit()

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Cant get image from video")
            break

        cv.imshow(video_path, frame)

        if cv.waitKey(30) == ord("s"):
            print("Video stopped")
            break
    
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    capture_video("../../videos/meeting.mp4")