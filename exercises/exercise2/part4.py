import random
import cv2

def add_noise(img):

	row , col = img.shape
	
	number_of_pixels = row*col // 20
	for i in range(number_of_pixels):
		
		# Pick a random y coordinate
		y_coord=random.randint(0, row - 1)
		
		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to white
		img[y_coord][x_coord] = 255
		
	# Randomly pick some pixels in
	# the image for coloring them black
	# Pick a random number between 300 and 10000
	number_of_pixels = row*col // 20
	for i in range(number_of_pixels):
		
		# Pick a random y coordinate
		y_coord=random.randint(0, row - 1)
		
		# Pick a random x coordinate
		x_coord=random.randint(0, col - 1)
		
		# Color that pixel to black
		img[y_coord][x_coord] = 0
		
	return img

# path
path = "images/gohan.jpg"

file_name = path.split('/')

# Using cv2.imread() method
img = cv2.imread(path)

black_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

noise_img = add_noise(black_image)

cv2.imshow('image', noise_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
