import cv2
#import numpy as np
import os

path_img = "E:\Python_CV\stady\Day2\images\cat1.jpg"
path_roi = "E:\Python_CV\stady\Day2\output\day2_roi.jpg"
path_result = "E:\Python_CV\stady\Day2\output\day2_pixel_modified.jpg"

img = cv2.imread(path_img)

H,W,C = img.shape

print(f"图像尺寸：高={H}, 宽={W}, 通道数={C}")

center_y, center_x = H // 2, W // 2
pixel_bgr = img[center_y, center_x]
print(f"中心点像素 BGR 值：{pixel_bgr}")


y1, y2 = H // 4, H // 2
x1, x2 = W // 4, W // 2

roi = img[y1:y2, x1:x2]

#计算roi区域灰度平均值
gray_mean = cv2.mean(roi)
print(f"ROI 区域灰度平均值：{gray_mean}")

#在原图上显示roi区域边框并显示在窗口中
cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
cv2.imshow("ROI区域", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#保存ROI区域
cv2.imwrite(path_roi, roi)