import cv2
import numpy as np


scene = cv2.imread("./images/full.png")
marker1 = cv2.imread("./images/marker1.png", cv2.IMREAD_GRAYSCALE)
marker2 = cv2.imread("./images/marker2.png", cv2.IMREAD_GRAYSCALE)

""" cv2.imshow("Scene", scene)
cv2.imshow("Marker 1", marker1)
cv2.imshow("Marker 2", marker2)
"""

# Define the corners of the template markers
marker1_corners = [
    (0, 0),
    (marker1.shape[1], 0),
    (marker1.shape[1], marker1.shape[0]),
    (0, marker1.shape[0]),
]

marker2_corners = [
    (0, 0),
    (marker2.shape[1], 0),
    (marker2.shape[1], marker2.shape[0]),
    (0, marker2.shape[0]),
]

i = 0


# Find the corners in the scene
# This is being done manually for now, as corner detectors were not having good results
# Change to detectors or improve images quality
def mouse_callback(event, x, y, flags, param):
    global i

    if i >= 8:
        return

    if event == cv2.EVENT_LBUTTONDOWN:
        if i < 4:
            pts1[i] = [x, y]
            cv2.circle(scene_copy, (x, y), 5, (0, 255, 0), -1)
        else:
            pts2[i - 4] = [x, y]
            cv2.rectangle(scene_copy, (x - 5, y - 5), (x + 5, y + 5), (0, 0, 255), -1)
        i += 1
        cv2.imshow("image", scene_copy)


pts1 = np.zeros((4, 2), dtype=np.float32)
pts2 = np.zeros((4, 2), dtype=np.float32)
scene_copy = scene.copy()

print("Select the 4 corners of each marker and press 'q' to continue")

cv2.imshow("image", scene_copy)
cv2.setMouseCallback("image", mouse_callback)

# Wait for 'q' to quit all windows
KEY = -1
while KEY != ord("q") and i < 8:
    KEY = cv2.waitKey(0)

# Find the homography transformation between the template markers and the scene markers
H1, _ = cv2.findHomography(np.float32(marker1_corners), pts1)
H2, _ = cv2.findHomography(np.float32(marker2_corners), pts2)

# Print the homography matrices
print("Homography Matrix 1:\n", H1)
print("Homography Matrix 2:\n", H2)

marker_frontal1 = cv2.warpPerspective(marker1, H1, (scene.shape[1], scene.shape[0]))
cv2.imshow("frontal marker 1", marker_frontal1)

marker_frontal2 = cv2.warpPerspective(marker2, H2, (scene.shape[1], scene.shape[0]))
cv2.imshow("frontal marker 2", marker_frontal2)

cv2.waitKey(0)

cv2.destroyAllWindows()
