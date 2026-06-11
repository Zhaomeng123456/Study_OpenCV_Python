"""
OpenCV 28天学习计划 — Day8：全局二值化

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day8 学习目标：掌握全局阈值二值化，理解阈值参数对分割效果的影响。

【重点算子】

1. cv2.threshold(src, thresh, maxval, type)
   功能：对灰度图进行全局阈值二值化
   参数：
     - src (ndarray)：输入灰度图，单通道 uint8
     - thresh (float)：阈值，取值范围 0~255
     - maxval (float)：超过阈值时赋的值，二值化通常为 255
     - type (int)：二值化模式，常用取值：
         cv2.THRESH_BINARY     — 大于阈值取 maxval，否则取 0
         cv2.THRESH_BINARY_INV — 大于阈值取 0，否则取 maxval
         cv2.THRESH_TRUNC      — 大于阈值取 thresh，否则不变
         cv2.THRESH_TOZERO     — 大于阈值保留原值，否则取 0
         cv2.THRESH_TOZERO_INV — 大于阈值取 0，否则保留原值
   返回值：(retval, dst) 元组
     - retval：实际使用的阈值（配合 OTSU 时自动计算）
     - dst：二值化结果图像

2. cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
   功能：在指定窗口创建滑动条，动态调节参数
   参数：
     - trackbarName (str)：滑动条名称
     - windowName (str)：窗口名称，需先用 namedWindow 创建
     - value (int)：滑动条初始值
     - count (int)：滑动条最大值
     - onChange (function)：回调函数，参数为当前值；可传空函数
   返回值：无

3. cv2.getTrackbarPos(trackbarname, winname)
   功能：获取滑动条当前位置（即当前阈值）
   参数：
     - trackbarname (str)：滑动条名称
     - winname (str)：窗口名称
   返回值：int，当前滑动条值

注意：全局二值化对整张图使用同一阈值，光照不均时效果可能变差（Day9 自适应二值化可解决）。
      二值化前需先将彩色图转为灰度图。
"""

import os

import cv2

# 当前脚本所在目录，用于拼接相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 输入图片路径
PATH_IMG = os.path.join(SCRIPT_DIR, "images", "shufa.jpg")
# 二值化结果保存路径
PATH_OUT = os.path.join(SCRIPT_DIR, "output", "day8_binary.jpg")

# 滑动条窗口名称
WINDOW_NAME = "Day8 - Threshold"
# 滑动条名称
TRACKBAR_NAME = "Threshold"

# 读取本地图片（cv2.imread）
img = cv2.imread(PATH_IMG)

# 转为灰度图（cv2.cvtColor，Day3 已学）
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 创建窗口与滑动条（namedWindow / createTrackbar）
cv2.namedWindow(WINDOW_NAME)
cv2.createTrackbar(TRACKBAR_NAME, WINDOW_NAME, 127, 255, lambda x: None)

print("拖动滑动条调节阈值，按 q 键退出并保存")

# 循环读取滑动条值并实时二值化
while True:
    # 获取当前阈值（getTrackbarPos）
    thresh_val = cv2.getTrackbarPos(TRACKBAR_NAME, WINDOW_NAME)

    # 全局二值化（cv2.threshold，THRESH_BINARY 模式）
    _, img_binary = cv2.threshold(img_gray, thresh_val, 255, cv2.THRESH_BINARY)

    '''
         cv2.THRESH_BINARY     — 大于阈值取 maxval，否则取 0
         cv2.THRESH_BINARY_INV — 大于阈值取 0，否则取 maxval
         cv2.THRESH_TRUNC      — 大于阈值取 thresh，否则不变
         cv2.THRESH_TOZERO     — 大于阈值保留原值，否则取 0
         cv2.THRESH_TOZERO_INV — 大于阈值取 0，否则保留原值
    '''

    # 显示原图与二值化结果（imshow）
    cv2.imshow("Original", img)
    cv2.imshow(WINDOW_NAME, img_binary)

    # 按 q 退出（waitKey）
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

# 保存当前阈值下的二值化结果（cv2.imwrite）
os.makedirs(os.path.join(SCRIPT_DIR, "output"), exist_ok=True)
cv2.imwrite(PATH_OUT, img_binary)
cv2.destroyAllWindows()

print(f"阈值={thresh_val}，二值图已保存：{PATH_OUT}")
