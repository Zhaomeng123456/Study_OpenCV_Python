"""
OpenCV 28天学习计划 — Day5：平移与旋转

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day5 学习目标：掌握 warpAffine 仿射变换，实现图像平移与旋转矫正。

【重点算子】

1. cv2.getRotationMatrix2D(center, angle, scale)
   功能：生成 2×3 旋转矩阵，供 warpAffine 使用
   参数：
     - center (tuple)：旋转中心点 (x, y)，通常取图像中心 (宽/2, 高/2)
     - angle (float)：旋转角度（度），正值逆时针，负值顺时针
     - scale (float)：缩放比例，1.0 表示不缩放
   返回值：2×3 的 ndarray 变换矩阵

2. cv2.warpAffine(src, M, dsize, flags, borderMode, borderValue)
   功能：对图像施加仿射变换（平移、旋转、缩放等）
   参数：
     - src (ndarray)：输入图像
     - M (ndarray)：2×3 仿射变换矩阵
     - dsize (tuple)：输出图像尺寸 (宽, 高)，通常与原图相同
     - flags (int，可选)：插值方式，默认 cv2.INTER_LINEAR
     - borderMode (int，可选)：边界填充方式，常用：
         cv2.BORDER_CONSTANT — 用常数填充（默认黑色）
         cv2.BORDER_REPLICATE — 复制边缘像素
     - borderValue：边界填充颜色，BORDER_CONSTANT 时有效
   返回值：变换后的 ndarray

   平移矩阵构造（2×3）：
     M = [[1, 0, tx],
          [0, 1, ty]]   tx、ty 为水平/垂直平移像素数

注意：旋转后图像四角可能出现黑色填充区域，属正常现象。
      转正时需根据实际倾斜角度调整 angle 参数（与倾斜角度相反）。
"""

import os

import cv2
import numpy as np

# 当前脚本所在目录，用于拼接相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 输入图片路径
PATH_IMG = os.path.join(SCRIPT_DIR, "images", "cat1.jpg")
# 平移结果保存路径
PATH_TRANSLATE_OUT = os.path.join(SCRIPT_DIR, "output", "day5_translated.jpg")
# 模拟倾斜图保存路径
PATH_TILTED_OUT = os.path.join(SCRIPT_DIR, "output", "day5_tilted.jpg")
# 旋转矫正结果保存路径
PATH_CORRECTED_OUT = os.path.join(SCRIPT_DIR, "output", "day5_corrected.jpg")

# 平移像素数（向右 50px，向下 30px）
TRANSLATE_X = 50
TRANSLATE_Y = 30
# 模拟倾斜角度（度），转正时取相反数
TILT_ANGLE = 20

# 读取本地图片（cv2.imread）
img = cv2.imread(PATH_IMG)
height, width = img.shape[:2]
# 旋转中心（图像中心）
center = (width // 2, height // 2)

# 构造平移矩阵并执行仿射变换（cv2.warpAffine）
matrix_translate = np.float32([[1, 0, TRANSLATE_X], [0, 1, TRANSLATE_Y]])
img_translated = cv2.warpAffine(img, matrix_translate, (width, height))

# 模拟倾斜：旋转 TILT_ANGLE 度（getRotationMatrix2D + warpAffine）
matrix_tilt = cv2.getRotationMatrix2D(center, TILT_ANGLE, 1.0)
img_tilted = cv2.warpAffine(img, matrix_tilt, (width+100, height+100))

# 转正：反向旋转 -TILT_ANGLE 度
matrix_correct = cv2.getRotationMatrix2D(center, -TILT_ANGLE, 1.0)
img_corrected = cv2.warpAffine(img_tilted, matrix_correct, (width, height))

# 确保 output 目录存在并保存结果（cv2.imwrite）
os.makedirs(os.path.join(SCRIPT_DIR, "output"), exist_ok=True)
cv2.imwrite(PATH_TRANSLATE_OUT, img_translated)
cv2.imwrite(PATH_TILTED_OUT, img_tilted)
cv2.imwrite(PATH_CORRECTED_OUT, img_corrected)

# 显示原图、平移、倾斜与矫正结果，按任意键关闭
cv2.imshow("Original", img)
cv2.imshow("Translated", img_translated)
cv2.imshow("Tilted", img_tilted)
cv2.imshow("Corrected", img_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"平移图已保存：{PATH_TRANSLATE_OUT}")
print(f"倾斜图已保存：{PATH_TILTED_OUT}")
print(f"矫正图已保存：{PATH_CORRECTED_OUT}")
