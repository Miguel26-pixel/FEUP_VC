import cv2

# path
path = "images/gohan.jpg"

file_name = path.split('/')

# Using cv2.imread() method
img = cv2.imread(path)

def mouse_callback(event, x, y, flags, params):
    if event == 2:
        print(f"coords {x, y}, colors Blue- {img[y, x, 0]} , Green- {img[y, x, 1]}, Red- {img[y, x, 2]} ")

    if event == cv2.EVENT_LBUTTONDOWN:
        img[y,x] = (0,0,0)
        cv2.imshow(file_name[-1], img)

cv2.namedWindow(file_name[-1])

cv2.setMouseCallback(file_name[-1], mouse_callback)

# Displaying the image
cv2.imshow(file_name[-1], img)

cv2.waitKey(0)
cv2.destroyAllWindows()