import numpy as np
import cv2 as cv

path = "images/chessboard_02.jpg" 

file_name = path.split('/')

img = cv.imread(path)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.02)

dst = cv.dilate(dst,None)

img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)

cv.waitKey(0)
cv.destroyAllWindows()
