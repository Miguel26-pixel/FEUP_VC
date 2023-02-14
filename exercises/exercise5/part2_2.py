import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


path = "images/gohan.jpg"

file_name = path.split('/')

img = cv.imread(path, 0)

clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

hist = cv.calcHist([cl1],[0],None,[256],[0,256])

plt.plot(hist, color='b')
plt.title('Image Histogram For Blue Channel GFG')
plt.show()

res = np.hstack((img,cl1))
cv.imshow('image',res)

cv.waitKey(0)
cv.destroyAllWindows()