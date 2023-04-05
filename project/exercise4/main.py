import cv2
import numpy as np

img = cv2.imread('lane.png')

#manual segmentation
roi_vertices = [(0, img.shape[0]), (img.shape[1] / 2, img.shape[0] / 2), (img.shape[1], img.shape[0])]
mask = np.zeros_like(img)
cv2.fillPoly(mask, np.int32([roi_vertices]), (255, 255, 255))
masked_img = cv2.bitwise_and(img, mask)

# Convert the image to grayscale
gray_img = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the image to remove noise
blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Apply Canny edge detection
canny_img = cv2.Canny(blur_img, 100, 200)

# Apply color thresholding to segment the lane lines
lower_white = np.array([200, 200, 200])
upper_white = np.array([255, 255, 255])
white_mask = cv2.inRange(masked_img, lower_white, upper_white)

combined_mask = cv2.bitwise_or(canny_img, white_mask)

# Define the Hough transform parameters
rho = 2
theta = np.pi / 180
threshold = 100
min_line_len = 100
max_line_gap = 75

# Run Hough on combined mask
lines = cv2.HoughLinesP(white_mask, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)

for x in range(0, len(lines)):
    for x1,y1,x2,y2 in lines[x]:
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

# Display the output
cv2.imshow('Original Image', img)
# cv2.imshow('Masked Image', masked_img)
# cv2.imshow('Canny Image', canny_img)
cv2.imshow('White Mask', white_mask) # best results
# cv2.imshow('Combined Mask', combined_mask)
#cv2.imshow('lines', lines)
cv2.waitKey(0)
cv2.destroyAllWindows()
