import cv2
import numpy as np

# Load the image
img = cv2.imread('lane_image.png')

# Define the region of interest
roi_vertices = [(0, img.shape[0]), (img.shape[1] / 2, img.shape[0] / 2), (img.shape[1], img.shape[0])]
mask = np.zeros_like(img)
cv2.fillPoly(mask, np.int32([roi_vertices]), (255, 255, 255))
masked_img = cv2.bitwise_and(img, mask)

# Convert the image to grayscale
gray_img = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
canny_img = cv2.Canny(gray_img, 100, 200)

# Define the Hough transform parameters
rho = 2
theta = np.pi / 180
threshold = 50
min_line_len = 100
max_line_gap = 50

# Run Hough on edge detected image
lines = cv2.HoughLinesP(canny_img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)

# Create a black image for drawing the lane lines
lane_lines = np.zeros_like(img)

# Check if any lines were detected
if lines is not None:
    # Reshape lines into the expected format for cv2.polylines()
    lines = np.array(lines).reshape((1, -1, 4))

    # Draw the lane lines on the black image
    cv2.polylines(lane_lines, lines, isClosed=False, color=(0, 0, 255), thickness=10)

# Display the output
cv2.imshow('Original Image', img)
cv2.imshow('Masked Image', masked_img)
cv2.imshow('Canny Image', canny_img)
cv2.imshow('Lane Lines', lane_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()
