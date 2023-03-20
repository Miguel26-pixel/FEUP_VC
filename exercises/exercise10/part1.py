import numpy as np
import cv2


path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create()
kp = sift.detect(gray,None)
img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow(file_name[1],img)
cv2.waitKey(0)
cv2.destroyAllWindows()