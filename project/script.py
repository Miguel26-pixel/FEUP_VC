import cv2
import numpy as np
import matplotlib.pyplot as plt

scene = cv2.imread("./images/full.png")  # query image
marker1 = cv2.imread("./images/marker1.png", cv2.IMREAD_GRAYSCALE)  # train image #1
marker2 = cv2.imread("./images/marker2.png", cv2.IMREAD_GRAYSCALE)  # train image #2

scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT_create(nfeatures=100000, contrastThreshold=0.01, edgeThreshold=20, nOctaveLayers=5)
kp_scene, des_scene = sift.detectAndCompute(scene_gray, None)

kp1, des1 = sift.detectAndCompute(marker1, None)
kp2, des2 = sift.detectAndCompute(marker2, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=100)
search_params = dict(checks=10000)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches_marker1 = flann.knnMatch(des1, des_scene, k=2)
print(len(matches_marker1))

good_matches1 = []
for m, n in matches_marker1:
    if m.distance < 0.80 * n.distance:
        good_matches1.append(m)

MIN_MATCH_COUNT = 4

if len(good_matches1) > MIN_MATCH_COUNT:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches1]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp_scene[m.trainIdx].pt for m in good_matches1]).reshape(
        -1, 1, 2
    )
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()
    h, w = marker1.shape
    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, M)
    img2 = cv2.polylines(scene_gray, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
else:
    print(
        "Not enough matches are found - {}/{}".format(
            len(good_matches1), MIN_MATCH_COUNT
        )
    )
    matchesMask = None

draw_params = dict(
    matchColor=(0, 255, 0),  # draw matches in green color
    singlePointColor=None,
    matchesMask=matchesMask,  # draw only inliers
    flags=2,
)
img3 = cv2.drawMatches(
    marker1, kp1, scene, kp_scene, good_matches1, None, **draw_params
)

cv2.imshow("Result", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
