import cv2
import numpy as np
import matplotlib.pyplot as plt
  
path = "images/chessboard_02.jpg" 

file_name = path.split('/')

img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners_img = cv2.goodFeaturesToTrack(gray,50,0.01,10)

corners_img = np.int0(corners_img)

for corners in corners_img:
    x,y = corners.ravel()
    cv2.circle(img,(x,y),3,[0,255,0],-1)

cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()