"""
OpenCV 28天学习计划 — Day2：像素操作与ROI区域

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day2 学习目标：理解图像矩阵本质，掌握像素读写与 ROI 区域裁剪。

【重点算子】

1. cv2.imread(filename, flags)
   功能：从本地文件读取图像，解码为 numpy 数组
   参数：
     - filename (str)：图片路径
     - flags (int，可选)：读取模式，默认 cv2.IMREAD_COLOR（BGR 三通道）
   返回值：成功返回 ndarray；失败返回 None

2. img.shape
   功能：获取图像矩阵的尺寸信息
   参数：无（img 为 ndarray 图像对象）
   返回值：
     - 彩色图：(高度, 宽度, 通道数)，通道数通常为 3
     - 灰度图：(高度, 宽度)
   说明：高度对应行数（y 轴），宽度对应列数（x 轴）

3. img[y, x]
   功能：读取或修改单个像素值
   参数：
     - y (int)：行索引（高度方向），取值范围 0 ~ 高度-1
     - x (int)：列索引（宽度方向），取值范围 0 ~ 宽度-1
   返回值：像素值；彩色图为 [B, G, R] 三个 uint8 值，灰度图为单个 uint8 值

4. img[y1:y2, x1:x2]
   功能：通过 numpy 切片裁剪 ROI（Region of Interest）区域
   参数：
     - y1:y2 (int)：行范围（高度方向），取值范围 0 ~ 图像高度，y1 < y2
     - x1:x2 (int)：列范围（宽度方向），取值范围 0 ~ 图像宽度，x1 < x2
   返回值：ROI 区域的 ndarray 视图（修改 ROI 会同步影响原图）

5. roi[:] = (B, G, R)
   功能：批量修改 ROI 区域内所有像素的颜色
   参数：
     - (B, G, R) (tuple)：BGR 颜色值，每个分量取值范围 0 ~ 255
   返回值：无（直接修改原数组）

6. cv2.imshow(winname, mat)
   功能：在窗口中显示图像
   参数：
     - winname (str)：窗口名称
     - mat (ndarray)：图像数据
   返回值：无

7. cv2.waitKey(delay)
   功能：等待键盘输入并刷新窗口
   参数：
     - delay (int)：等待毫秒数，0 表示无限等待
   返回值：按键 ASCII 码；超时返回 -1

8. cv2.imwrite(filename, img)
   功能：将图像保存到本地文件
   参数：
     - filename (str)：保存路径
     - img (ndarray)：图像数据
   返回值：保存成功返回 True，失败返回 False

注意：OpenCV 默认使用 BGR 通道顺序，与 matplotlib/PIL 的 RGB 不同。
      图像矩阵先行后列，访问格式为 img[行, 列] 即 img[y, x]。
"""

import os

import cv2

# 当前脚本所在目录，用于拼接相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 输入图片路径
PATH_IMG = os.path.join(SCRIPT_DIR, "images", "cat1.jpg")
# 原始 ROI 裁剪图保存路径
PATH_ROI_OUT = os.path.join(SCRIPT_DIR, "output", "day2_roi.jpg")
# 修改像素后的完整图像保存路径
PATH_RESULT_OUT = os.path.join(SCRIPT_DIR, "output", "day2_pixel_modified.jpg")

# 读取本地图片
img = cv2.imread(PATH_IMG)

# 获取图像宽高与通道数（shape：高度, 宽度, 通道数）
height, width, channels = img.shape
print(f"图像尺寸：高={height}, 宽={width}, 通道数={channels}")

# 读取单个像素值（以图像中心点为例）
center_y, center_x = height // 2, width // 2
pixel_bgr = img[center_y, center_x]
print(f"中心点像素 BGR 值：{pixel_bgr}")

# 定义 ROI 区域坐标（行范围 y1~y2，列范围 x1~x2）
y1, y2 = height // 4, height // 2
x1, x2 = width // 4, width // 2

# 裁剪 ROI 区域
roi = img[y1:y2, x1:x2]

# 保存原始 ROI 裁剪结果
os.makedirs(os.path.join(SCRIPT_DIR, "output"), exist_ok=True)
cv2.imwrite(PATH_ROI_OUT, roi)

# 将 ROI 区域所有像素改为红色（BGR: 0, 0, 255）
roi[:] = (0, 0, 255)

# 显示修改后的完整图像，按任意键关闭
cv2.imshow("Day2 - Pixel Modified", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 保存修改后的完整图像
cv2.imwrite(PATH_RESULT_OUT, img)
print(f"ROI 区域已保存：{PATH_ROI_OUT}")
print(f"修改后图像已保存：{PATH_RESULT_OUT}")
