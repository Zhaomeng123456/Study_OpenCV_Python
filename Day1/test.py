#跟着AI学习
import cv2
import os

path_img = "E:\Python_CV\stady\Day1\images\cat1.jpg"
img = cv2.imread(path_img)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("E:\Python_CV\stady\Day1\output\cat1.jpg", img)
