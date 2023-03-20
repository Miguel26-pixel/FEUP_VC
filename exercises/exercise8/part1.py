import cv2
import numpy as np
import math

path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)
img_ = img
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_ = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray,100,200,apertureSize = 3)
#cv2.imshow('edges',edges)

minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength=minLineLength,maxLineGap=maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('houghlinesp',img)

canny = cv2.Canny(gray_, 100, 150,apertureSize = 3)
lines = cv2.HoughLines(canny, 1, np.pi/180, 200)
  
if lines is not None:
    for elem in lines:
        rho = elem[0][0]
        theta = elem[0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv2.line(img_, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow('houghlines', img_)
cv2.waitKey(0)
cv2.destroyAllWindows()