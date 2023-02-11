# Python program to explain cv2.imread() method

# importing cv2 
import cv2

path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)

cv2.imshow(file_name[-1], img)

target_file = "images/target.bmp"

cv2.imwrite(target_file, img)

cv2.waitKey()