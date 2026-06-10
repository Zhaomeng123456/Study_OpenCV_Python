import cv2
import io

path_img = "E:\Python_CV\stady\Day3\images\dog.jpg"

img = cv2.imread(path_img)
cv2.imshow("img", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_gray", img_gray)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("img_hsv", img_hsv)

img_b,img_g,img_r = cv2.split(img)
cv2.imshow("img_b", img_b)
cv2.imshow("img_g", img_g)
cv2.imshow("img_r", img_r)

img_merged = cv2.merge([img_b,img_g,img_r])
cv2.imshow("img_merged", img_merged)

cv2.waitKey(0)
cv2.destroyAllWindows()