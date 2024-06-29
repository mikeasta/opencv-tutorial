import cv2 as cv
import numpy as np

cap  = cv.VideoCapture(0)
logo = cv.imread("../../images/logo.jpg")[0:480, 0:480] 

# Mask
logo_gray = cv.bitwise_not(cv.cvtColor(logo, cv.COLOR_BGR2GRAY)) # bitw Not to convert white background
ret, mask = cv.threshold(logo_gray, 10, 256, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# Mask on logo
fg = cv.bitwise_and(logo, logo, mask=mask)

# Optimize
cv.setUseOptimized(True)
while cap.isOpened():
    ret, frame = cap.read()    
    blend = False
    
    if blend:
        # Blend
        blend = cv.addWeighted(
            frame[0:480, 0:480, :],
            0.7,
            logo,
            0.3,
            0
        )
        cv.imshow("image", blend)
    else:
        # Mask on roi
        roi = frame[0:480, 0:480]
        bg = cv.bitwise_and(roi, roi, mask=mask_inv)

        # Sum background and foreground
        res = cv.add(fg, bg)
        
        #res = np.concatenate([logo_gray, mask, mask_inv], axis=1)
        cv.imshow("img", res)

    if cv.waitKey(10) == ord("s"):
        break


cap.release()
cv.destroyAllWindows()