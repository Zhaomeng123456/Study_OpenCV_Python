import cv2
import os

path_img = "E:\Python_CV\stady\Day8\images\shufa.jpg"
img = cv2.imread(path_img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_gray", img_gray)

#滑动条窗口名称
name_window = "Threshold"
#滑动条名称
name_trackbar = "Threshold"

#创建滑动条窗口
cv2.namedWindow(name_window)
cv2.createTrackbar(name_trackbar, name_window, 127, 255, lambda x: None)

#循坏读取滑动条并试试进行二值化
while True:
    #获取当前滑动条值
    thresh_val = cv2.getTrackbarPos(name_trackbar, name_window)
    #进行二值化
    _, img_binary = cv2.threshold(img_gray, thresh_val, 128, cv2.THRESH_BINARY)
    #_, img_binary = cv2.threshold(img_gray, thresh_val, 100, cv2.THRESH_BINARY_INV)
    #_, img_binary = cv2.threshold(img_gray, thresh_val, 255, cv2.THRESH_TRUNC)
    #_, img_binary = cv2.threshold(img_gray, thresh_val, 255, cv2.THRESH_TOZERO)
    #_, img_binary = cv2.threshold(img_gray, thresh_val, 255, cv2.THRESH_TOZERO_INV)
    #显示二值化结果
    cv2.imshow(name_window, img_binary)
    #按q键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

  


cv2.waitKey(0)
cv2.destroyAllWindows()