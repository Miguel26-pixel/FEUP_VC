import cv2
import numpy as np

path = "images/gohan.jpg"

file_name = path.split('/')

img0 = cv2.imread(path)
img = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

gb = cv2.GaussianBlur(img,(3,3),0)

gX = cv2.Sobel(gb, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=3)
gY = cv2.Sobel(gb, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=3)

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
    cv2.imshow("image2", result)


# create window
cv2.namedWindow("image2", cv2.WINDOW_NORMAL)

# create trackbar
cv2.createTrackbar("Value", "image2", thresholdValue, maxValue, onTrackbarValueChange)

# call method to initialize first time
onTrackbarValueChange(thresholdValue)

canny = cv2.Canny(img, 85, 255) 

def callback(x):
    print(x)

cv2.namedWindow('image')
cv2.createTrackbar('L', 'image', 0, 255, callback) #lower threshold trackbar for window 'image
cv2.createTrackbar('U', 'image', 0, 255, callback) #upper threshold trackbar for window 'image

while(1):
    numpy_horizontal_concat = np.concatenate((img, canny), axis=1) # to display image side by side
    cv2.imshow('image', numpy_horizontal_concat)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: #escape key
        break
    l = cv2.getTrackbarPos('L', 'image')
    u = cv2.getTrackbarPos('U', 'image')

    canny = cv2.Canny(img, l, u)


cv2.destroyAllWindows()

