import numpy as np
import cv2
from matplotlib import pyplot as plt


path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)

orb = cv2.ORB_create()

kp = orb.detect(img,None)

kp, des = orb.compute(img, kp)

img2 = cv2.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)

cv2.imshow(file_name[1],img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
