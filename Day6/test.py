import os
import cv2
import numpy as np

#from Day6.day6_affine_perspective import matrix_perspective

path_img = "E:\Python_CV\stady\Day6\images\\test.jpg"
img = cv2.imread(path_img)
cv2.imshow("img", img)

#源图像中的点
points_src = np.float32([[30, 30], [450, 20], [20, 460], [490, 490]])

#目标图像中的点-仿射变换
point_src_affine = np.float32([[30, 30], [450, 20], [20, 460]])
points_dst_affine = np.float32([[30, 30], [650, 20], [20, 460]])

#计算仿射变换矩阵
matrix_affine = cv2.getAffineTransform(point_src_affine, points_dst_affine)

#应用仿射变换矩阵
img_affine = cv2.warpAffine(img, matrix_affine, (700, 500))
cv2.imshow("img_affine", img_affine)
cv2.imwrite("E:\Python_CV\stady\Day6\output\\testimg_affine.jpg", img_affine)

#目标图像中的点-透视变换
point_src_perspective = np.float32([[30, 30], [450, 20], [20, 460], [490, 490]])
points_dst_perspective = np.float32([[20, 20], [680, 20], [20, 480], [680, 480]])

#计算透视变换矩阵
matrix_perspective = cv2.getPerspectiveTransform(point_src_perspective, points_dst_perspective)
#应用透视变换矩阵
img_perspective = cv2.warpPerspective(img, matrix_perspective, (700, 500))

cv2.imshow("img_perspective", img_perspective)

cv2.imwrite("E:\Python_CV\stady\Day6\output\\testimg_perspective.jpg", img_perspective)
cv2.waitKey(0)
cv2.destroyAllWindows()

