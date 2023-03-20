import cv2
import numpy as np
import math

path = "images/gohan.jpg"
path1 = "images/streetLines_01.jpg"
path2 = "images/chessboard_02.jpg"
file_name1 = path1.split('/')
file_name2 = path2.split('/')

img = cv2.imread(path1)
img_ = cv2.imread(path2)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_ = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)


edges = cv2.Canny(gray,100,200,apertureSize = 3)
edges_ = cv2.Canny(gray_,100,200,apertureSize = 3)
#cv2.imshow('edges',edges)

minLineLength = 30
maxLineGap = 10
lines = cv2.HoughLinesP(edges,1,np.pi/180,15,minLineLength=minLineLength,maxLineGap=maxLineGap)
lines_ = cv2.HoughLinesP(edges_,1,np.pi/180,15,minLineLength=minLineLength,maxLineGap=maxLineGap)
for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

for x in range(0, len(lines_)):
    for x1,y1,x2,y2 in lines_[x]:
        cv2.line(img_,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('houghlinespR',img)
cv2.imshow('houghlinespC',img_)
cv2.waitKey(0)
cv2.destroyAllWindows()