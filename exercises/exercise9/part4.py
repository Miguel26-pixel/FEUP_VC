import numpy as np
import cv2
from matplotlib import pyplot as plt

path = "images/chessboard_02.jpg" 

file_name = path.split('/')

img = cv2.imread(path)
img.resize(1000,1000)

fast = cv2.FastFeatureDetector_create()

kp = fast.detect(img,None)
img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))

cv2.imshow('w/out', img2)

fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)

img3 = cv2.drawKeypoints(img, kp, None, color=(255,0,0))

cv2.imshow('with', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()