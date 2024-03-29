import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret,thresh = cv.threshold(gray,128,255,0)

    cv.imshow('color frame', frame)
    cv.imshow('gray frame', thresh)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()