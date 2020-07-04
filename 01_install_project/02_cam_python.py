import numpy as np
import cv2

# pip install opencv-contrib-python

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

while(True):
    # capture frame by frame
    ret, frame = cap.read()

    # our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # display the resulting frame
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


