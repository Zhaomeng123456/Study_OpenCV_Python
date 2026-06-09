"""
OpenCV 28天学习计划 — Day2：NumPy 在 OpenCV 图像处理中的用法

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day2 补充学习目标：理解 cv2.imread 读入的图像本质是 NumPy 数组，
掌握用 NumPy 索引、切片、通道访问和数组运算操作图像像素。

【重点算子 / 方法】

1. ndarray.shape
   功能：返回数组各维度长度
   参数：无
   返回值：tuple，彩色 OpenCV 图像通常为 (高度, 宽度, 通道数)
   说明：高度是行数（y），宽度是列数（x）

2. ndarray.dtype
   功能：返回数组元素的数据类型
   参数：无
   返回值：dtype 对象，OpenCV 图像像素通常为 uint8

3. ndarray.ndim
   功能：返回数组维度数量
   参数：无
   返回值：int，彩色图为 3，灰度图为 2

4. ndarray.size
   功能：返回数组元素总个数
   参数：无
   返回值：int，等于各维度长度的乘积

5. arr[row, col] / arr[row, col, channel]
   功能：访问或修改单个像素
   参数：
     - row (int)：行索引，范围 0 ~ 高度-1
     - col (int)：列索引，范围 0 ~ 宽度-1
     - channel (int，可选)：通道索引，BGR 图范围 0~2（0=B, 1=G, 2=R）
   返回值：对应位置的像素值

6. arr[y1:y2, x1:x2]
   功能：二维切片，裁剪 ROI 区域
   参数：
     - y1:y2 (int)：行范围，左闭右开，y1 < y2
     - x1:x2 (int)：列范围，左闭右开，x1 < x2
   返回值：原数组的视图（view），修改会同步影响原图

7. arr[:, :, c]
   功能：提取单个颜色通道的所有像素
   参数：
     - c (int)：通道索引，BGR 图中 0=蓝、1=绿、2=红
   返回值：二维 ndarray，形状 (高度, 宽度)

8. arr[:] = value
   功能：对整个数组或切片批量赋值（广播）
   参数：
     - value：标量或与通道数匹配的元组，如 (B, G, R)，分量范围 0~255
   返回值：无（原地修改）

9. arr.copy()
   功能：创建数组的深拷贝，与原数组内存独立
   参数：无
   返回值：新的 ndarray，修改拷贝不影响原图

10. np.mean(a, axis=None)
    功能：计算数组元素均值
    参数：
      - a (ndarray)：输入数组，如 ROI 区域或单通道数据
      - axis (int/tuple，可选)：沿指定轴求均值；None 表示对所有元素求均值
    返回值：float64 标量或降维后的数组

注意：OpenCV 图像矩阵先行后列，索引格式为 img[行, 列] 即 img[y, x]。
      切片得到的是视图；需要独立副本时请使用 .copy()。
"""

import os

import cv2
import numpy as np

# 当前脚本所在目录，用于拼接相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 输入图片路径
PATH_IMG = os.path.join(SCRIPT_DIR, "images", "cat1.jpg")
# NumPy 独立拷贝 ROI 保存路径
PATH_ROI_COPY_OUT = os.path.join(SCRIPT_DIR, "output", "day2_numpy_roi_copy.jpg")
# NumPy 修改通道后图像保存路径
PATH_CHANNEL_OUT = os.path.join(SCRIPT_DIR, "output", "day2_numpy_channel.jpg")

# 用 OpenCV 读取图片，得到 NumPy 数组
img = cv2.imread(PATH_IMG)

# 查看 ndarray 基本属性
print(f"shape  : {img.shape}")    # (高, 宽, 通道)
print(f"dtype  : {img.dtype}")    # 通常为 uint8
print(f"ndim   : {img.ndim}")     # 彩色图为 3
print(f"size   : {img.size}")     # 元素总个数

height, width, channels = img.shape

# 用 NumPy 索引读取中心点像素
center_y, center_x = height // 2, width // 2
pixel_bgr = img[center_y, center_x]
blue_value = img[center_y, center_x, 0]
print(f"中心点 BGR：{pixel_bgr}，蓝色通道值：{blue_value}")

# 用 NumPy 切片裁剪 ROI（视图，与原图共享内存）
y1, y2 = height // 4, height // 2
x1, x2 = width // 4, width // 2
roi_view = img[y1:y2, x1:x2]

# 计算 ROI 区域像素均值
roi_mean = np.mean(roi_view)
print(f"ROI 区域整体均值：{roi_mean:.2f}")

# 提取蓝色通道，计算该通道均值
blue_channel = img[:, :, 0]
blue_mean = np.mean(blue_channel)
print(f"蓝色通道均值：{blue_mean:.2f}")

# 用 .copy() 创建独立副本，修改拷贝不影响原图
roi_copy = roi_view.copy()
roi_copy[:] = (255, 0, 0)

# 在原图上用切片批量修改 ROI 为绿色（BGR: 0, 255, 0）
img[y1:y2, x1:x2] = (0, 255, 0)

# 显示 NumPy 拷贝的 ROI 与原图修改效果
cv2.imshow("NumPy ROI Copy (Blue)", roi_copy)
cv2.imshow("NumPy Modified Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存结果
os.makedirs(os.path.join(SCRIPT_DIR, "output"), exist_ok=True)
cv2.imwrite(PATH_ROI_COPY_OUT, roi_copy)
cv2.imwrite(PATH_CHANNEL_OUT, img)
print(f"独立 ROI 拷贝已保存：{PATH_ROI_COPY_OUT}")
print(f"通道修改后图像已保存：{PATH_CHANNEL_OUT}")
