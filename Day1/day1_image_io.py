"""
OpenCV 28天学习计划 — Day1：图像IO与窗口基础

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day1 学习目标：掌握图片的读取、显示、保存，理解 OpenCV 图像基础操作。

【重点算子】

1. cv2.imread(filename, flags)
   功能：从本地文件读取图像，解码为 numpy 数组（图像矩阵）
   参数：
     - filename (str)：图片路径，支持 .jpg / .png / .bmp 等常见格式
     - flags (int，可选)：读取模式，常用取值：
         cv2.IMREAD_COLOR     (默认，值为 1)：读取彩色图，3 通道 BGR
         cv2.IMREAD_GRAYSCALE (值为 0)：读取为单通道灰度图
         cv2.IMREAD_UNCHANGED (值为 -1)：保留原图通道（含透明通道 Alpha）
   返回值：成功返回 ndarray，形状 (高, 宽, 通道数)；失败返回 None

2. cv2.namedWindow(winname, flags)
   功能：创建一个指定名称的显示窗口，需在 imshow 之前调用
   参数：
     - winname (str)：窗口名称，需与 imshow / resizeWindow 保持一致
     - flags (int，可选)：窗口属性，常用取值：
         cv2.WINDOW_AUTOSIZE (值为 1，默认)：窗口大小自动匹配图像尺寸，不可拖拽
         cv2.WINDOW_NORMAL   (值为 0)：窗口可手动拖拽缩放，resizeWindow 才能生效
   返回值：无

3. cv2.resizeWindow(winname, width, height)
   功能：设置窗口的显示宽高（不改变图像本身像素，只改变显示区域大小）
   参数：
     - winname (str)：窗口名称，必须与 namedWindow 创建时一致
     - width  (int)：窗口宽度（像素），建议 > 0，如 640、800、1920
     - height (int)：窗口高度（像素），建议 > 0，如 480、600、1080
   返回值：无
   注意：仅当 namedWindow 使用 WINDOW_NORMAL 时本函数才有效

4. cv2.imshow(winname, mat)
   功能：将图像显示到指定名称的窗口中
   参数：
     - winname (str)：窗口名称，若窗口不存在则自动创建
     - mat (ndarray)：要显示的图像数据，需为 uint8 类型矩阵
   返回值：无

5. cv2.waitKey(delay)
   功能：等待键盘按键，同时刷新窗口显示（不调用则窗口可能无响应）
   参数：
     - delay (int)：等待时间（毫秒）
         0  — 无限等待，直到按下任意键（静态图片常用）
         1  — 等待 1 毫秒（视频流/摄像头常用）
         >0 — 等待指定毫秒数，超时返回 -1
   返回值：按键的 ASCII 码；超时未按键返回 -1

6. cv2.destroyAllWindows()
   功能：关闭并销毁所有由 OpenCV 创建的窗口，释放显示资源
   参数：无
   返回值：无

7. cv2.imwrite(filename, img, params)
   功能：将图像矩阵编码并保存到本地文件
   参数：
     - filename (str)：保存路径，扩展名决定格式（.jpg→JPEG，.png→PNG）
     - img (ndarray)：要保存的图像数据
     - params (list，可选)：编码参数，例如：
         [cv2.IMWRITE_JPEG_QUALITY, 95]   — JPEG 质量，范围 0~100，默认 95
         [cv2.IMWRITE_PNG_COMPRESSION, 3] — PNG 压缩等级，范围 0~9，默认 3
   返回值：保存成功返回 True，失败返回 False

注意：OpenCV 默认使用 BGR 通道顺序，与 matplotlib/PIL 的 RGB 不同。
"""

import os

import cv2

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_IMG = os.path.join(SCRIPT_DIR, "images", "cat1.jpg")
PATH_OUT = os.path.join(SCRIPT_DIR, "output", "cat1.jpg")

# 窗口名称（namedWindow / resizeWindow / imshow 需使用同一名称）
WINDOW_NAME = "img"

# 读取本地图片
img = cv2.imread(PATH_IMG)

# 创建可调整大小的窗口（WINDOW_NORMAL 允许手动拖拽和 resizeWindow 生效）
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)

# 设置窗口初始显示尺寸（宽 800，高 600）
cv2.resizeWindow(WINDOW_NAME, 800, 600)

# 在窗口中显示图片，按任意键关闭
cv2.imshow(WINDOW_NAME, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 将图片保存到 output 目录
os.makedirs(os.path.join(SCRIPT_DIR, "output"), exist_ok=True)
cv2.imwrite(PATH_OUT, img)
