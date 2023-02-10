import cv2

# path
path = "images/gohan.jpg"

file_name = path.split('/')

# Using cv2.imread() method
img = cv2.imread(path)

cv2.namedWindow(file_name[-1])

img = cv2.resize(img, (200,100))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
cv2.imshow(file_name[-1], img)

cv2.waitKey(0)
cv2.destroyAllWindows()