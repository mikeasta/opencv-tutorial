import cv2 as cv
import numpy as np

# Apply adaptive thresholding + gaussian blue
def apply_threshold(image: np.array, kernel_size: int = 11):
    # Split to several channels
    b, g, r = cv.split(image)
    kernel = (kernel_size, kernel_size)

    b_blur = cv.GaussianBlur(b,kernel,0)
    g_blur = cv.GaussianBlur(g,kernel,0)
    r_blur = cv.GaussianBlur(r,kernel,0)
    
    b_ret, b_th = cv.threshold(b_blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    g_ret, g_th = cv.threshold(g_blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
    r_ret, r_th = cv.threshold(r_blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

    return cv.merge((b_th, g_th, r_th))



cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    ret, frame = cap.read()

    # # Adaptive thresh
    # res_frame = apply_threshold(frame)

    # # Contours
    # res_frame = frame.copy()
    # imgray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # ret, thresh = cv.threshold(imgray, 127, 255, 0)
    # contours, hierarchy = cv.findContours(thresh, 1, 2)
    # cv.drawContours(res_frame, contours, -1, (255,0,0), 1)

    # # Canny edge detection
    # res_frame = cv.Canny(frame,100,200)

    # # Laplassian gradient
    # res_frame = cv.Laplacian(frame, cv.CV_64F)

    # # Sobel
    # sobelx = cv.Sobel(frame.copy(),cv.CV_64F,1,0,ksize=5)
    # sobely = cv.Sobel(frame.copy(),cv.CV_64F,0,1,ksize=5)
    # res_frame = np.concatenate([frame, sobelx, sobely], axis=1)

    # # Erode and Dilate
    # kernel = np.ones((5,5),np.uint8)
    # erosion = cv.erode(frame,kernel,iterations = 1)
    # dilation = cv.dilate(frame,kernel,iterations = 1)
    # res_frame = np.concatenate([frame, erosion, dilation], axis=1)

    # # Hats
    # kernel = np.ones((5,5),np.uint8)
    # tophat = cv.morphologyEx(frame, cv.MORPH_TOPHAT, kernel)
    # blackhat = cv.morphologyEx(frame, cv.MORPH_BLACKHAT, kernel)
    # res_frame = np.concatenate([frame, tophat, blackhat], axis=1)
    
    # # Open and Close
    # kernel = np.ones((5,5),np.uint8)
    # opening = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
    # closing = cv.morphologyEx(frame, cv.MORPH_CLOSE, kernel)
    # res_frame = np.concatenate([frame, opening, closing], axis=1)

    # # Bilateral filtering 
    # blur = cv.bilateralFilter(frame,9,75,75)
    # res_frame = np.concatenate([frame, blur], axis=1)

    # # Median blur
    # median = cv.medianBlur(frame,7)
    # res_frame = np.concatenate([frame, median], axis=1)

    cv.imshow("Thresholded", res_frame)
    if cv.waitKey(20) == ord("s"):
        break

cap.release()
cv.destroyAllWindows()