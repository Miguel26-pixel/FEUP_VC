import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


path = "images/gohan.jpg"

file_name = path.split('/')

img = cv.imread(path, 0)

equ = cv.equalizeHist(img)
res = np.hstack((img,equ))
cv.imshow('image',res)

hist = cv.calcHist([equ],[0],None,[256],[0,256])

plt.plot(hist, color='b')
plt.title('Image Histogram For Blue Channel GFG')
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()