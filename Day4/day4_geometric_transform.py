"""
OpenCV 28天学习计划 — Day4：基础几何变换

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day4 学习目标：掌握图像缩放与翻转，灵活调整图像尺寸与画面方向。

【重点算子】

1. cv2.resize(src, dsize, fx, fy, interpolation)
   功能：调整图像尺寸（放大或缩小）
   参数：
     - src (ndarray)：输入图像
     - dsize (tuple，可选)：目标尺寸 (宽, 高)；设为 None 时配合 fx/fy 使用
     - fx (float，可选)：水平缩放比例，>1 放大，0~1 缩小
     - fy (float，可选)：垂直缩放比例
     - interpolation (int，可选)：插值方式，常用取值：
         cv2.INTER_LINEAR  — 双线性插值（默认，速度较快）
         cv2.INTER_AREA    — 区域插值（缩小图像时效果较好）
         cv2.INTER_CUBIC   — 双三次插值（放大时较平滑，速度较慢）
         cv2.INTER_NEAREST — 最近邻插值（速度最快，易有锯齿）
   返回值：缩放后的 ndarray

2. cv2.flip(src, flipCode)
   功能：沿水平或垂直方向翻转图像（镜像）
   参数：
     - src (ndarray)：输入图像
     - flipCode (int)：翻转方式，取值：
         0  — 沿 x 轴翻转（上下镜像）
         1  — 沿 y 轴翻转（左右镜像）
         -1 — 同时水平和垂直翻转（等价旋转 180°）
   返回值：翻转后的 ndarray
"""

import os

import cv2

# 当前脚本所在目录，用于拼接相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 输入图片路径
PATH_IMG = os.path.join(SCRIPT_DIR, "images", "cat1.jpg")
# 缩放结果保存路径
PATH_RESIZE_OUT = os.path.join(SCRIPT_DIR, "output", "day4_resized.jpg")
# 左右镜像保存路径
PATH_FLIP_H_OUT = os.path.join(SCRIPT_DIR, "output", "day4_flip_horizontal.jpg")
# 上下镜像保存路径
PATH_FLIP_V_OUT = os.path.join(SCRIPT_DIR, "output", "day4_flip_vertical.jpg")

# 缩放比例（宽、高均缩小为原来的 50%）
RESIZE_SCALE = 0.5

# 读取本地图片（cv2.imread）
img = cv2.imread(PATH_IMG)

# 按比例缩放，缩小图像使用 INTER_AREA 插值（cv2.resize）
img_resized = cv2.resize(img, None, fx=RESIZE_SCALE, fy=RESIZE_SCALE,
                         interpolation=cv2.INTER_AREA)
print(f"缩放：{img.shape[:2]} -> {img_resized.shape[:2]}")

# 左右镜像（cv2.flip，flipCode=1）
img_flip_h = cv2.flip(img, 1)

# 上下镜像（cv2.flip，flipCode=0）
img_flip_v = cv2.flip(img, 0)

# 确保 output 目录存在并保存结果（cv2.imwrite）
os.makedirs(os.path.join(SCRIPT_DIR, "output"), exist_ok=True)
cv2.imwrite(PATH_RESIZE_OUT, img_resized)
cv2.imwrite(PATH_FLIP_H_OUT, img_flip_h)
cv2.imwrite(PATH_FLIP_V_OUT, img_flip_v)

# 显示原图、缩放图与翻转结果，按任意键关闭（imshow / waitKey / destroyAllWindows）
cv2.imshow("Original", img)
cv2.imshow("Resized", img_resized)
cv2.imshow("Flip Horizontal", img_flip_h)
cv2.imshow("Flip Vertical", img_flip_v)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"缩放图已保存：{PATH_RESIZE_OUT}")
print(f"左右镜像已保存：{PATH_FLIP_H_OUT}")
print(f"上下镜像已保存：{PATH_FLIP_V_OUT}")
