import cv2
import io

path_img = "E:\Python_CV\stady\Day4\images\dog.jpg"

img = cv2.imread(path_img)
cv2.imshow("img", img)

img_resize = cv2.resize(img, (300, 300))
cv2.imshow("img_resize", img_resize)

img_filp_horizontal = cv2.flip(img, 1)
cv2.imshow("img_filp_horizontal", img_filp_horizontal)

img_filp_vertical = cv2.flip(img, 0)
cv2.imshow("img_filp_vertical", img_filp_vertical)

img_filp_both = cv2.flip(img, -1)
cv2.imshow("img_filp_both", img_filp_both)

cv2.waitKey(0)
cv2.destroyAllWindows()
