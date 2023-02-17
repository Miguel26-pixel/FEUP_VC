import cv2
import numpy as np

path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)

gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)

combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)

cv2.imshow('image1',combined)

thresholdValue = 128
maxValue = 255


# callback method for trackbar value change
def onTrackbarValueChange(*args):
    global thresholdValue
    thresholdValue = args[0]
    th, result = cv2.threshold(combined, thresholdValue, maxValue, cv2.THRESH_BINARY)
    cv2.imshow("image", result)


# create window
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# create trackbar
cv2.createTrackbar("Value", "image", thresholdValue, maxValue, onTrackbarValueChange)

# call method to initialize first time
onTrackbarValueChange(thresholdValue)

cv2.waitKey(0)
cv2.destroyAllWindows()

