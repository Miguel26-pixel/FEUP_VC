# Python program to explain cv2.imread() method

# importing cv2 
import cv2

# path
path = "images/gohan.jpg"

file_name = path.split('/')

# Using cv2.imread() method
img = cv2.imread(path)

# Displaying the image
cv2.imshow(file_name[-1], img)

print("Height:", img.shape[0])
print("Width:", img.shape[1])

cv2.waitKey()