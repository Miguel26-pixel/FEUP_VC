import cv2
import numpy as np
import math

path1 = "images/streetLines_01.jpg"
path2 = "images/chessboard_02.jpg"
path = path1

file_name = path.split('/')

img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray, 200, 200,apertureSize = 5)
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
        cv2.line(img, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)

cv2.imshow(file_name[1], img)
cv2.waitKey(0)
cv2.destroyAllWindows()