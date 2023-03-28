import cv2
import numpy as np

coords = []
def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN and len(coords) < 2:
        print(x, ' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img2, str(x) + ',' +
                    str(y), (x, y), font,
                    0.5, (255, 0, 0), 2)
        cv2.imshow('image', img2)
        coords.append((x,y))

    if len(coords) == 2:
        #result = distanceCalculate(coords[0], coords[1])
        return coords

def distanceCalculate(p1, p2):
    dis = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return dis


MIN_MATCH_COUNT = 10

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
img1 = cv2.imread('images/match_box01a_1.png')          
img2 = cv2.imread('images/match_box01a_2.png') 
cv2.imshow('image', img2)

cv2.setMouseCallback('image', click_event)

cv2.waitKey()

print(coords)
if len(coords) == 2:
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)   # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params,search_params)

    matches = flann.knnMatch(des1,des2,k=2)
    matchesMask = [[0,0] for i in range(len(matches))]
    cv2.destroyWindow('image')
    good = []
    for mat in matches:
        m,n = mat
        img1_idx = m.queryIdx
        coord = kp1[img1_idx].pt
        array_int = (round(coord[0]), round(coord[1]))
        print("coords : " + str(coords))
        print("coord : " + str(array_int))
        if (array_int[0] == coords[0][0] or array_int[0] == coords[1][0]):
            good.append(m)

    print("good : " + str(good))

    if len(good)>0:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()
        h,w = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)
        img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)


        draw_params = dict(matchColor = (150,255,255),
                        singlePointColor = None,
                        matchesMask = matchesMask,
                        flags = 2)
        img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

        cv2.imshow("result",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()