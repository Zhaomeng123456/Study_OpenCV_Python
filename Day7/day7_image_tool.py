"""
OpenCV 28天学习计划 — Day7：第一周综合复盘（简易图片工具）

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day7 学习目标：整合第一周已学 API，独立完成简易图片处理流程。

本脚本串联第一周核心操作，对单张图片依次完成：
  读取 → ROI 裁剪 → 缩放 → 翻转 → 保存

【重点算子】

本周无新增算子。本工具整合 Day1~Day6 已学操作：

1. ROI 裁剪（Day2）
   img[y1:y2, x1:x2] — 按行列范围截取局部区域

2. cv2.resize（Day4）
   按比例或指定尺寸缩放图像，缩小时常用 cv2.INTER_AREA

3. cv2.flip（Day4）
   flipCode=1 左右镜像，flipCode=0 上下镜像

处理流程中 imread / imshow / imwrite 等常用算子见代码行内注释。
"""

import os

import cv2

# 当前脚本所在目录，用于拼接相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 输入图片路径
PATH_IMG = os.path.join(SCRIPT_DIR, "images", "cat1.jpg")
# 工具处理结果保存路径
PATH_OUT = os.path.join(SCRIPT_DIR, "output", "day7_result.jpg")

# 缩放比例（宽、高均缩小为原来的 50%）
RESIZE_SCALE = 0.5

# 读取本地图片（cv2.imread）
img = cv2.imread(PATH_IMG)
height, width = img.shape[:2]
print(f"原图尺寸：高={height}, 宽={width}")

# 步骤1：ROI 裁剪（取图像中心区域）
y1, y2 = height // 4, height * 3 // 4
x1, x2 = width // 4, width * 3 // 4
img = img[y1:y2, x1:x2]
print(f"裁剪后：高={img.shape[0]}, 宽={img.shape[1]}")

# 步骤2：按比例缩放（cv2.resize）
img = cv2.resize(img, None, fx=RESIZE_SCALE, fy=RESIZE_SCALE,
                 interpolation=cv2.INTER_AREA)
print(f"缩放后：高={img.shape[0]}, 宽={img.shape[1]}")

# 步骤3：左右翻转（cv2.flip，flipCode=1）
img = cv2.flip(img, 1)

# 确保 output 目录存在并保存结果（cv2.imwrite）
os.makedirs(os.path.join(SCRIPT_DIR, "output"), exist_ok=True)
cv2.imwrite(PATH_OUT, img)

# 显示处理结果，按任意键关闭（imshow / waitKey / destroyAllWindows）
cv2.imshow("Day7 - Image Tool Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"处理完成，已保存：{PATH_OUT}")
