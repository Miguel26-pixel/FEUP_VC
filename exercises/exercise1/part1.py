import cv2

path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)

cv2.imshow(file_name[-1], img)

print("Height:", img.shape[0])
print("Width:", img.shape[1])

cv2.waitKey()