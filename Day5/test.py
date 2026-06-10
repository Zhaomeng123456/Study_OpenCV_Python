import cv2
import os
import numpy as np

path_img = "E:\Python_CV\stady\Day5\images\cat1.jpg"
img = cv2.imread(path_img)

#平移
matrix_translate = np.float32([[1, 0, 50], [0, 1, 30]])
img_translate = cv2.warpAffine(img, matrix_translate, (img.shape[1], img.shape[0]))
cv2.imshow("img_translate", img_translate)


#旋转
h,w,c = img.shape
matrix_rotate = cv2.getRotationMatrix2D((w/2, h/2), 90, 1)
img_rotate = cv2.warpAffine(img, matrix_rotate, (w, h))
cv2.imshow("img_rotate", img_rotate)

img_rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("img_rotate", img_rotate)

#缩放
matrix_scale = cv2.getRotationMatrix2D((h/2, w/2), 0, 0.5)
img_scale = cv2.warpAffine(img, matrix_scale, (w, h))
img_resize = cv2.resize(img, (w//2, h//2))
cv2.imshow("img_scale", img_scale)
cv2.imshow("img_resize", img_resize)

#cv2.imwrite("Day5\output\img_resize.jpg", img_resize)
#cv2.imwrite("Day5\output\img_scale.jpg", img_scale)

cv2.waitKey(0)
cv2.destroyAllWindows()