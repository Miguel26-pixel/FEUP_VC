import random
import cv2
from matplotlib import pyplot as plt

path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)

black_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([black_image],[0],None,[256],[0,256])

plt.plot(hist, color='b')
plt.title('Image Histogram For Blue Channel GFG')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
