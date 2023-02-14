import cv2
import numpy as np
from matplotlib import pyplot as plt


path = "images/gohan.jpg"

file_name = path.split('/')

img0 = cv2.imread(path)

gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

img = cv2.GaussianBlur(gray,(3,3),0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv2.imshow('image',combined)

cv2.waitKey(0)
cv2.destroyAllWindows()

