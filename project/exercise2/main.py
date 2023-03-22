import cv2
import numpy as np

coords = []
b = False

def click_event(event, x, y, flags, params):

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    0.5, (255, 0, 0), 2)
        cv2.imshow('image', img)
        if len(coords)==1:
            b = True
        coords.append((x,y))
        
    if len(coords) == 2 and b:
        result = distanceCalculate(coords[0], coords[1])
        print("distance: " + str(result))
        coords.pop()
        coords.pop()
        b = False

def distanceCalculate(p1, p2):
    dis = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
    return dis

def detect_plane(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.medianBlur(gray, 5)
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpen = cv2.filter2D(blur, -1, sharpen_kernel)

    # Threshold and morph close
    thresh = cv2.threshold(sharpen, 160, 255, cv2.THRESH_BINARY_INV)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find contours and filter using threshold area
    cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    min_area = 100
    max_area = 1500
    image_number = 0
    for c in cnts:
        area = cv2.contourArea(c)
        if area > min_area and area < max_area:
            x,y,w,h = cv2.boundingRect(c)
            ROI = img[y:y+h, x:x+w]
            cv2.imwrite('ROI_{}.png'.format(image_number), ROI)
            cv2.rectangle(img, (x, y), (x + w, y + h), (36,255,12), 2)
            image_number += 1

    cv2.imshow('sharpen', sharpen)
    cv2.imshow('close', close)
    cv2.imshow('thresh', thresh)
    cv2.imshow('image', img)


img = cv2.imread('images/gohan.jpg', 1)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", img)

cv2.setMouseCallback('image', click_event)

#detect_plane(img)

cv2.waitKey(0)

cv2.destroyAllWindows()