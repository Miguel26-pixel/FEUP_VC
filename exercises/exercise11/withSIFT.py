import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('images/match_scene01_2.png',cv2.IMREAD_GRAYSCALE)          
img2 = cv2.imread('images/match_scene01_3.png',cv2.IMREAD_GRAYSCALE) 

sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

good = []
for m,n in matches:
    if m.distance < 0.65*n.distance:
        good.append([m])

img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
cv2.imshow("result",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()