import os
import numpy as np
from matplotlib import pyplot as plt
import cv2
from scipy import ndimage
import random


def add_noise(img):

	row , col, r = img.shape
	
	number_of_pixels = row*col // 20
	for i in range(number_of_pixels):
		
		y_coord=random.randint(0, row - 1)
		
		x_coord=random.randint(0, col - 1)
		
		img[y_coord][x_coord] = 255
		
	number_of_pixels = row*col // 20
	for i in range(number_of_pixels):
		
		y_coord=random.randint(0, row - 1)
		
		x_coord=random.randint(0, col - 1)
		
		img[y_coord][x_coord] = 0
		
	return img

path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)
img = add_noise(img)
black_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(black_image,(3,3),0)

kernel = (1/16)*np.array([[1,2,1],[2,4,2],[1,2,1]])
result = ndimage.convolve(gauss,kernel)


cv2.imshow("Original", img)
cv2.imshow("OpenCV GaussianBlur", gauss)
cv2.imshow("My 3x3 convolution w/Gaussian mask", result)
cv2.waitKey(0)
cv2.destroyAllWindows()