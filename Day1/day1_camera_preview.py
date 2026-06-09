"""
OpenCV 28天学习计划 — Day1：摄像头实时预览

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day1 学习目标：掌握摄像头/视频流的读取与实时显示。

【重点算子】

1. cv2.VideoCapture(index_or_path, apiPreference)
   功能：打开摄像头设备或视频文件，创建视频捕获对象
   参数：
     - index_or_path：设备索引或文件路径
         int 0, 1, 2 ... — 摄像头编号，0 为系统默认摄像头
         str 路径        — 视频文件路径，如 "test.mp4"
     - apiPreference (int，可选)：后端 API，常用取值：
         cv2.CAP_ANY   (值为 0，默认)：自动选择后端
         cv2.CAP_DSHOW (值为 700)：Windows DirectShow 后端
         cv2.CAP_MSMF  (值为 1400)：Windows Media Foundation 后端
   返回值：VideoCapture 对象；可用 cap.isOpened() 判断是否打开成功

2. cap.read()
   功能：从摄像头或视频中读取一帧画面
   参数：无
   返回值：(ret, frame) 元组
     - ret (bool)：True 表示读取成功，False 表示读取失败或视频结束
     - frame (ndarray)：当前帧图像，BGR 三通道，形状 (高, 宽, 3)

3. cv2.namedWindow(winname, flags)
   功能：创建一个指定名称的显示窗口，需在 imshow 之前调用
   参数：
     - winname (str)：窗口名称，需与 imshow / resizeWindow 保持一致
     - flags (int，可选)：窗口属性，常用取值：
         cv2.WINDOW_AUTOSIZE (值为 1，默认)：窗口大小自动匹配图像尺寸
         cv2.WINDOW_NORMAL   (值为 0)：窗口可拖拽缩放，resizeWindow 才能生效
   返回值：无

4. cv2.resizeWindow(winname, width, height)
   功能：设置窗口的显示宽高
   参数：
     - winname (str)：窗口名称
     - width  (int)：窗口宽度（像素），建议 > 0
     - height (int)：窗口高度（像素），建议 > 0
   返回值：无
   注意：需配合 WINDOW_NORMAL 使用

5. cv2.imshow(winname, mat)
   功能：将当前帧显示到指定窗口
   参数：
     - winname (str)：窗口名称
     - mat (ndarray)：当前帧图像数据
   返回值：无

6. cv2.waitKey(delay)
   功能：等待键盘按键并刷新窗口，视频流中必须调用否则画面卡顿
   参数：
     - delay (int)：等待时间（毫秒）
         0  — 无限等待（静态图常用）
         1  — 等待 1 毫秒（摄像头/视频流常用）
         >0 — 等待指定毫秒数
   返回值：按键 ASCII 码；超时返回 -1；常与 & 0xFF 配合取低 8 位

7. cap.release()
   功能：释放摄像头/视频文件资源，程序结束前必须调用
   参数：无
   返回值：无

8. cv2.destroyAllWindows()
   功能：关闭并销毁所有 OpenCV 窗口
   参数：无
   返回值：无
"""

import cv2

# 窗口名称（namedWindow / resizeWindow / imshow 需使用同一名称）
WINDOW_NAME = "camera"

# 打开默认摄像头（index=0）
cap = cv2.VideoCapture(0)

# 创建可调整大小的预览窗口
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW_NAME, 800, 600)

# 循环读取并显示每一帧，按 q 键退出
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow(WINDOW_NAME, frame)

    # waitKey(1) 适合视频流；按 q 退出循环
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 释放摄像头并关闭窗口
cap.release()
cv2.destroyAllWindows()
