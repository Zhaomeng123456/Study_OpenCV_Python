"""
OpenCV 28天学习计划 — Day3：色彩空间转换

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day3 学习目标：掌握 BGR / GRAY / HSV 色彩空间转换，理解通道分离与合并。

【重点算子】

1. cv2.cvtColor(src, code)
   功能：在不同色彩空间之间转换图像
   参数：
     - src (ndarray)：输入图像
     - code (int)：色彩空间转换码，常用取值：
         cv2.COLOR_BGR2GRAY — BGR 彩色图转单通道灰度图
         cv2.COLOR_BGR2HSV  — BGR 转 HSV（H:0~179, S:0~255, V:0~255）
         cv2.COLOR_HSV2BGR  — HSV 转回 BGR
         cv2.COLOR_BGR2RGB  — BGR 转 RGB（对接 matplotlib/PIL 时使用）
   返回值：转换后的 ndarray；灰度图形状 (高, 宽)，HSV/BGR 为 (高, 宽, 3)

2. cv2.split(m)
   功能：将多通道图像拆分为单通道数组列表
   参数：
     - m (ndarray)：多通道输入图像，通常为 BGR 三通道图
   返回值：通道元组，BGR 图返回 (b, g, r)，每个元素为 (高, 宽) 的二维数组

3. cv2.merge(mv)
   功能：将多个单通道数组合并为多通道图像
   参数：
     - mv (list/tuple)：单通道数组列表，BGR 合并需传入 [b, g, r]
   返回值：合并后的多通道 ndarray，形状 (高, 宽, 通道数)

注意：OpenCV 默认使用 BGR 通道顺序，与 matplotlib/PIL 的 RGB 不同。
      HSV 中 H（色调）范围在 OpenCV 中为 0~179，而非常见的 0~360。
      灰度图常用于简化计算；HSV 便于按颜色分割（后续颜色追踪会用到）。
"""

import os

import cv2

# 当前脚本所在目录，用于拼接相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 输入图片路径
PATH_IMG = os.path.join(SCRIPT_DIR, "images", "dog.jpg")
# 灰度图保存路径
PATH_GRAY_OUT = os.path.join(SCRIPT_DIR, "output", "day3_gray.jpg")
# HSV 图保存路径
PATH_HSV_OUT = os.path.join(SCRIPT_DIR, "output", "day3_hsv.jpg")
# 通道拆分图保存路径
PATH_B_OUT = os.path.join(SCRIPT_DIR, "output", "day3_channel_b.jpg")
PATH_G_OUT = os.path.join(SCRIPT_DIR, "output", "day3_channel_g.jpg")
PATH_R_OUT = os.path.join(SCRIPT_DIR, "output", "day3_channel_r.jpg")
# 通道合并还原图保存路径
PATH_MERGE_OUT = os.path.join(SCRIPT_DIR, "output", "day3_merged.jpg")

# 读取本地图片（cv2.imread）
img = cv2.imread(PATH_IMG)

# BGR 转灰度图（cv2.cvtColor + COLOR_BGR2GRAY）
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f"灰度图 shape：{img_gray.shape}")

# BGR 转 HSV 色彩空间（cv2.cvtColor + COLOR_BGR2HSV）
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(f"HSV 图 shape：{img_hsv.shape}")

# 拆分 BGR 三个通道（cv2.split）
channel_b, channel_g, channel_r = cv2.split(img)
print(f"蓝色通道 shape：{channel_b.shape}")

# 合并三个通道还原为 BGR 图像（cv2.merge）
img_merged = cv2.merge([channel_b, channel_g, channel_r])

# 确保 output 目录存在
os.makedirs(os.path.join(SCRIPT_DIR, "output"), exist_ok=True)

# 保存转换结果与通道图（cv2.imwrite）
cv2.imwrite(PATH_GRAY_OUT, img_gray)
cv2.imwrite(PATH_HSV_OUT, img_hsv)
cv2.imwrite(PATH_B_OUT, channel_b)
cv2.imwrite(PATH_G_OUT, channel_g)
cv2.imwrite(PATH_R_OUT, channel_r)
cv2.imwrite(PATH_MERGE_OUT, img_merged)

# 分别显示灰度图、HSV 图及 B/G/R 三个通道，按任意键关闭
cv2.imshow("Gray", img_gray)
cv2.imshow("HSV", img_hsv)
cv2.imshow("Channel B", channel_b)
cv2.imshow("Channel G", channel_g)
cv2.imshow("Channel R", channel_r)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"灰度图已保存：{PATH_GRAY_OUT}")
print(f"HSV 图已保存：{PATH_HSV_OUT}")
print(f"通道图已保存：{PATH_B_OUT}, {PATH_G_OUT}, {PATH_R_OUT}")
print(f"合并还原图已保存：{PATH_MERGE_OUT}")
