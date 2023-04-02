import cv2
import numpy as np

scene = cv2.imread("./images/full.png")
marker1 = cv2.imread("./images/marker1.png")
marker2 = cv2.imread("./images/marker2.png")

marker1_gray = cv2.cvtColor(marker1, cv2.COLOR_BGR2GRAY)
marker2_gray = cv2.cvtColor(marker2, cv2.COLOR_BGR2GRAY)


# find corners in markers
corners1 = cv2.goodFeaturesToTrack(
    marker1_gray, maxCorners=200, qualityLevel=0.15, minDistance=20
)
corners2 = cv2.goodFeaturesToTrack(
    marker2_gray, maxCorners=200, qualityLevel=0.15, minDistance=10
)
corners1 = np.int0(corners1)
corners2 = np.int0(corners2)

for i in corners1:
    x, y = i.ravel()
    cv2.circle(marker1, (x, y), 3, (0, 0, 255), -1)

for i in corners2:
    x, y = i.ravel()
    cv2.circle(marker2, (x, y), 3, (0, 0, 255), -1)


# find corners in the scene
scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(
    scene_gray, maxCorners=100, qualityLevel=0.15, minDistance=5
)
corners = np.int0(corners)
print(len(corners))

for i in corners:
    x, y = i.ravel()
    cv2.circle(scene, (x, y), 3, (0, 0, 255), -1)

# match corners between the markers and the scene
THRESHOLD = 30

matched_corners1 = []
for corner in corners:
    min_distance = float("inf")
    for template_corner in corners1:
        distance = np.linalg.norm(corner - template_corner)
        if distance < min_distance:
            min_distance = distance
            closest_corner = template_corner
    if min_distance < THRESHOLD:
        matched_corners1.append((corner, closest_corner))

matched_corners2 = []
for corner in corners:
    min_distance = float("inf")
    for template_corner in corners2:
        distance = np.linalg.norm(corner - template_corner)
        if distance < min_distance:
            min_distance = distance
            closest_corner = template_corner
    if min_distance < THRESHOLD:
        matched_corners2.append((corner, closest_corner))

# Define colors for matched corners
color1 = (0, 0, 255)  # red
color2 = (0, 255, 0)  # green

# Draw matched corners on scene image
for corner_pair in matched_corners1:
    cv2.circle(scene, tuple(corner_pair[0][0]), 5, color1, -1)
for corner_pair in matched_corners2:
    cv2.circle(scene, tuple(corner_pair[0][0]), 5, color2, -1)

# Show the result
cv2.imshow("Matched Corners", scene)
print(matched_corners1)
print(matched_corners2)

# Compute homography for template 1
marker1_homography, _ = cv2.findHomography(
    np.array([pair[1] for pair in matched_corners1]),
    np.array([pair[0] for pair in matched_corners1]),
)

# Compute homography for template 2
marker2_homography, _ = cv2.findHomography(
    np.array([pair[1] for pair in matched_corners2]),
    np.array([pair[0] for pair in matched_corners2]),
)

print("Homography 1", marker1_homography)
print("Homography 2", marker2_homography)


marker_frontal1 = cv2.warpPerspective(
    marker1, marker1_homography, (scene.shape[1], scene.shape[0])
)
cv2.imshow("frontal marker 1", marker_frontal1)

marker_frontal2 = cv2.warpPerspective(
    marker2, marker2_homography, (scene.shape[1], scene.shape[0])
)
cv2.imshow("frontal marker 2", marker_frontal2)


cv2.imshow("image", scene)
cv2.imshow("marker1", marker1)
cv2.imshow("marker2", marker2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Code below would ask the user to select the corners
""" # Find the corners in the scene
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
    KEY = cv2.waitKey(0) """

""" pts1 = []
pts2 = []

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
 """

cv2.waitKey(0)

cv2.destroyAllWindows()
