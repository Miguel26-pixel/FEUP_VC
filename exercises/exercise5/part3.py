import numpy as np
import cv2
from matplotlib import pyplot as plt


path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path,1)

img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])

image = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)

hist = cv2.calcHist([image],[0],None,[256],[0,256])

# plt.plot(hist, color='b')
# plt.title('Image Histogram For Blue Channel GFG')
# plt.show()

clahe_model = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
colorimage_b = clahe_model.apply(img[:,:,0])
colorimage_g = clahe_model.apply(img[:,:,1])
colorimage_r = clahe_model.apply(img[:,:,2])
color_result = np.stack((colorimage_b,colorimage_g,colorimage_r), axis=2)

hist2 = cv2.calcHist([color_result],[0],None,[256],[0,256])

# plt.plot(hist, color='b')
# plt.title('Image Histogram For Blue Channel GFG')
# plt.show()

res = np.hstack((img,image,color_result))
cv2.imshow('image',res)

cv2.waitKey(0)
cv2.destroyAllWindows()