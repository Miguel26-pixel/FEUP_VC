import cv2

path = "images/gohan.jpg"

file_name = path.split('/')

img = cv2.imread(path)

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

(H, S, V) = cv2.split(hsv_img)

S = S + 10

cv2.imshow("H", H)
cv2.imshow("S", S)
cv2.imshow("V", V)

merged = cv2.merge([H, S, V])
cv2.imshow("Merged", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()