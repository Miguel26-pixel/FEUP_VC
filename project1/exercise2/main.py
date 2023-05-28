import cv2
import numpy as np
from math import sqrt
import math

coords = []
coords_to_homography = []
def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN and len(coords) < 2:

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img2, str(x) + ',' +
                    str(y), (x, y), font,
                    0.5, (255, 0, 0), 2)
        cv2.imshow('image', img2)
        coords.append((x,y))

    elif event == cv2.EVENT_LBUTTONDOWN and len(coords_to_homography) < 4 and len(coords)==2:

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img2, str(x) + ',' +
                    str(y), (x, y), font,
                    0.5, (0, 255, 0), 2)
        cv2.imshow('image', img2)
        coords_to_homography.append((x,y))

    if len(coords) == 2 and len(coords_to_homography) == 4:
        return coords, coords_to_homography
    
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier
    
def nearPoint(matches, k, good):
    minimum = 50
    c = None
    for mat in matches:
        m,n = mat
        if m.distance < 0.9*n.distance:
            point = kp2[m.trainIdx].pt
            if (len(good) < 4):
                if distanceCalculate(point, coords_to_homography[k]) < minimum:
                    c = m
                    minimum = distanceCalculate(point, coords_to_homography[k])
    return c
    
def distanceCalculate(p1, p2):

    dis = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5

    return dis

def distanceCalculateMM(A, B, height, width):

    diffx = (B[1] - A[0])
    diffy = (B[0] - A[1])

    dft_size = cv2.getOptimalDFTSize(max(height, width))

    pixel_density = width / dft_size

    return sqrt(pow(diffx, 2) + pow(diffy,2))/pixel_density

def multiply_matrix(A,B):
    global C
    if  len(A[0]) == len(B):
        C = []
        for row in range(len(B)):
            for elt in range(len(B[0])):
                if row == 0:
                    C.append([A[row][elt] * B[row][elt] + A[row][elt+1] * B[row+1][elt] + A[row][elt+2] * B[row+2][elt]])
                elif row == 1:
                    C.append([A[row][elt] * B[row-1][elt] + A[row][elt+1] * B[row][elt] + A[row][elt+2] * B[row+1][elt]])
                elif row == 2:
                    C.append([A[row][elt] * B[row-2][elt] + A[row][elt+1] * B[row-2][elt] + A[row][elt+2] * B[row][elt]])
        return C
    else:
        return "Sorry, cannot multiply A and B."

MIN_MATCH_COUNT = 10

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
img1 = cv2.imread('images/match_box01a_1.png')          
img2 = cv2.imread('images/match_box01a_2.png') 
cv2.imshow('image', img2)

cv2.setMouseCallback('image', click_event)

cv2.waitKey()

if len(coords) == 2:
    sift = cv2.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 100)
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1,des2,k=2)

    cv2.destroyWindow('image')
    good = []
    good2 = []
    match1 = None
    match2 = None
    minimum1 = 30
    minimum2 = 30
    k = []
    for i in range(4):
        good.append(nearPoint(matches, i, good))

    for mat in matches:
        m,n = mat
        if m.distance < 0.9*n.distance:
            point = kp2[m.trainIdx].pt
            good2.append(m)

            if distanceCalculate(point, coords[0]) < minimum1:
                minimum1 = distanceCalculate(point, coords[0])
                match1 = (True, m)
            if distanceCalculate(point, coords[1]) < minimum2:
                minimum2 = distanceCalculate(point, coords[1])
                match2 = (True, m)
            

    if (match1 == None or match2 == None or len(good) != 4 or None in good):
        print("No matches found")

    if len(good)==4 and not (match1 == None or match2 == None) and None not in good:

        good.append(match1[1])
        good.append(match2[1])

        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        src_pts2 = np.float32([ kp1[m.queryIdx].pt for m in good2 ]).reshape(-1,1,2)
        dst_pts2 = np.float32([ kp2[m.trainIdx].pt for m in good2 ]).reshape(-1,1,2)

        M2, mask = cv2.findHomography(src_pts2, dst_pts2, cv2.RANSAC, 5.0)

        h,w,r = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M2)
        img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

        matchesMask = mask.ravel().tolist()

        result1 = kp1[match1[1].queryIdx].pt
        result2 = kp1[match2[1].queryIdx].pt

        result = ((result1[0], result1[1]), (result2[0], result2[1]))

        distance = distanceCalculateMM(result[0], result[1], h, w)

        draw_params = dict(matchColor = (150,255,255),
                        singlePointColor = None,
                        matchesMask = matchesMask,
                        flags = 2)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
    
        img3 = cv2.drawMatches(img1,kp1,img2,kp2,good2,None,**draw_params)

        cv2.putText(img3, str(round(result[0][0])) + ',' +
                    str(round(result[0][1])), (round(result[0][0]), round(result[0][1])), font,
                    0.5, (255, 0, 0), 2)
        
        cv2.putText(img3, str(round(result[1][0])) + ',' +
                    str(round(result[1][1])), (round(result[1][0]), round(result[1][1])), font,
                    0.5, (255, 0, 0), 2)
        
        cv2.putText(img3,"distance:" + str(round_half_up(distance,2)),(50,300),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),2,cv2.LINE_AA)

        cv2.imshow("result",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()