import cv2
import numpy as np

height=100
width=200
img = np.zeros((height,width,3), np.uint8)
img[:]=(0,124,255)

cv2.namedWindow('image')

start_point = (0, 0)

end_point = (200, 100)

color = (255, 0, 0)

thickness = 9

img = cv2.line(img, start_point, end_point, color, thickness)

start_point = (0, 100)

end_point = (200, 0)

color = (0, 0, 255)

thickness = 9

img = cv2.line(img, start_point, end_point, color, thickness)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()