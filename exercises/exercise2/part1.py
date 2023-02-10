import cv2
import numpy as np

height=100
width=200
img = np.zeros((height,width,3), np.uint8)
img[:]=(0,0,0)

cv2.namedWindow('image')

start_point = (0, 0)

end_point = (200, 100)

color = (100, 100, 100)

thickness = 9

# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
img = cv2.line(img, start_point, end_point, color, thickness)

start_point = (0, 100)

end_point = (200, 0)

color = (255, 255, 255)

thickness = 9

# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
img = cv2.line(img, start_point, end_point, color, thickness)

# Displaying the image
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()