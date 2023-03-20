import cv2
import numpy as np

path = "images/gohan.jpg"

file_name = path.split('/')

img0 = cv2.imread(path)
img = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

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

