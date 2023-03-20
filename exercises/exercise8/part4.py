import cv2
import numpy as np

path1 = "images/coins_01.jpg"
path2 = "images/coins_02.jpg"
path = path2
file_name = path2.split('/')

img = cv2.imread(path2)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 130)


circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow(file_name[1], img)

file_name = path1.split('/')

img_ = cv2.imread(path1)

gray_ = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)

circles_ = cv2.HoughCircles(gray_, cv2.HOUGH_GRADIENT, 1.4, 120)


circles_ = np.uint16(np.around(circles_))
for i in circles_[0,:]:
    cv2.circle(img_,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img_,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow(file_name[1], img_)
cv2.waitKey(0)
cv2.destroyAllWindows()