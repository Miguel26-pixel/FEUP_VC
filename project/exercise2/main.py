import cv2
import numpy as np

coords = []
def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN and len(coords) < 2:

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

def multiply_matrix(A,B):
    global C
    if  len(A[0]) == len(B):
        C = np.zeros((len(B),len(A[0])),dtype = int)
        for row in range(len(B)):
            for col in range(len(A[0])):
                for elt in range(len(B[0])):
                    C[row, col] += A[row][col] * B[col][elt]
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
    for mat in matches:
        m,n = mat
        if m.distance < 0.9*n.distance:
            point = kp1[m.queryIdx].pt
            good.append(m)
            if distanceCalculate(point, coords[0]) < 30:
                print("1")
                print(distanceCalculate(point, coords[0]))
            if distanceCalculate(point, coords[1]) < 30:
                print("2")
                print(distanceCalculate(point, coords[1]))
            if distanceCalculate(point, coords[0]) < minimum1:
                minimum1 = distanceCalculate(point, coords[0])
                match1 = (True, m)
            if distanceCalculate(point, coords[1]) < minimum2:
                minimum2 = distanceCalculate(point, coords[1])
                match2 = (True, m)

    if (match1 == None or match2 == None):
        print("No matches found")

    if len(good)>0 and not (match1 == None or match2 == None):
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()

        h,w,r = img1.shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)
        img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

        result1 = kp2[match1[1].trainIdx].pt
        result2 = kp2[match2[1].trainIdx].pt

        print(result1)
        print(result2)

        mul1 = multiply_matrix(M, [[result1[0]],[result1[1]],[1]])
        mul2 = multiply_matrix(M, [[result2[0]],[result2[1]],[1]])

        print(mul1)
        print(mul2)

        result = ((round(mul1[0][0]), round(mul1[1][1])), (round(mul2[0][0]), round(mul2[1][1])))


        distance = distanceCalculate(result[0], result[1])
        print(distance)

        draw_params = dict(matchColor = (150,255,255),
                        singlePointColor = None,
                        matchesMask = matchesMask,
                        flags = 2)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
    
        img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

        cv2.putText(img3, str(result[0][0]) + ',' +
                    str(result[0][1]), (result[0][0], result[0][1]), font,
                    0.5, (255, 0, 0), 2)
        
        cv2.putText(img3, str(result[1][0]) + ',' +
                    str(result[1][1]), (result[1][0], result[1][1]), font,
                    0.5, (255, 0, 0), 2)

        cv2.imshow("result",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()