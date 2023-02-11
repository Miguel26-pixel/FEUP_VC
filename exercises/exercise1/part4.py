import cv2

path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)

op_points = []

def mouse_callback(event, x, y, flags, params):
    if event == 2:
        print(f"coords {x, y}, colors Blue- {img[y, x, 0]} , Green- {img[y, x, 1]}, Red- {img[y, x, 2]} ")

    if event == cv2.EVENT_LBUTTONDOWN:
        op_points.append((y,x))
        if (len(op_points) == 2):
            img_cropped = img[op_points[0][0]:op_points[1][0], op_points[0][1]:op_points[1][1]]

            target_file = "images/target2.bmp"

            cv2.imwrite(target_file, img_cropped)

            cv2.imshow("image crop", img_cropped)

cv2.namedWindow(file_name[-1])

cv2.setMouseCallback(file_name[-1], mouse_callback)

cv2.imshow(file_name[-1], img)

cv2.waitKey(0)
cv2.destroyAllWindows()