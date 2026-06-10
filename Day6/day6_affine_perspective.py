"""
OpenCV 28天学习计划 — Day6：仿射与透视变换入门

【项目介绍】
本项目是 OpenCV 28 天系统学习计划，按天练习工业视觉常用技能。
Day6 学习目标：理解变换矩阵作用，掌握仿射（3 点）与透视（4 点）矫正。

【重点算子】

1. cv2.getPerspectiveTransform(src, dst)
   功能：根据 4 对源/目标点计算 3×3 透视变换矩阵
   参数：
     - src (ndarray)：源图像中 4 个角点坐标，形状 (4, 2)，float32
     - dst (ndarray)：目标图像中 4 个对应点坐标，形状 (4, 2)，float32
   返回值：3×3 透视变换矩阵（ndarray，float64）

2. cv2.warpPerspective(src, M, dsize, flags, borderMode, borderValue)
   功能：对图像施加透视变换
   参数：
     - src (ndarray)：输入图像
     - M (ndarray)：3×3 透视变换矩阵
     - dsize (tuple)：输出图像尺寸 (宽, 高)
     - flags (int，可选)：插值方式，默认 cv2.INTER_LINEAR
     - borderMode (int，可选)：边界填充方式
         cv2.BORDER_CONSTANT — 用常数填充
         cv2.BORDER_REPLICATE — 复制边缘像素
     - borderValue：填充颜色（BORDER_CONSTANT 时有效）
   返回值：变换后的 ndarray

   仿射与透视的区别：
     - 仿射（3 点）：保持平行线不变（矩形→平行四边形）
     - 透视（4 点）：可改变平行关系（矩形→任意四边形）

注意：变换后图像四角可能出现黑色填充区域。
"""

import os

import cv2
import numpy as np

# 当前脚本所在目录，用于拼接相对路径
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# 输入图片路径（card.jpg 含网格，便于观察变换）
PATH_CARD = os.path.join(SCRIPT_DIR, "images", "card.jpg")
# 仿射矫正保存路径
PATH_AFFINE_OUT = os.path.join(SCRIPT_DIR, "output", "day6_affine.jpg")
# 透视矫正保存路径
PATH_PERSPECTIVE_OUT = os.path.join(SCRIPT_DIR, "output", "day6_perspective.jpg")

# 读取演示图片（cv2.imread）
img = cv2.imread(PATH_CARD)
height, width = img.shape[:2]

# 源图像中 4 个角点（左上、右上、左下、右下）
# card.jpg 有红色圆点标记，便于确定角点位置
src_points = np.float32([[20, 20], [680, 20], [20, 480], [680, 480]])

# 目标：输出图像的 4 个对应位置
output_w, output_h = 500, 500

# ========== 仿射变换（保留平行关系，3 点即可） ==========
# 取源点中 3 个（左上、右上、左下），映射到标准矩形
src_affine = np.float32([src_points[0], src_points[1], src_points[2]])
dst_affine = np.float32([[0, 0], [output_w, 0], [0, output_h]])

# 计算仿射变换矩阵（cv2.warpAffine 可用 getAffineTransform 或之前学的 getRotationMatrix2D）
matrix_affine = cv2.getAffineTransform(src_affine, dst_affine)
img_affine = cv2.warpAffine(img, matrix_affine, (output_w, output_h))
print(f"仿射纠正：{img.shape[:2]} -> ({output_w}, {output_h})")

# ========== 透视变换（支持非平行关系，需 4 点） ==========
# 模拟"拍摄角度歪斜"的目标位置，右下方偏移制造透视感
dst_perspective = np.float32([
    [30, 30],                # 左上（微调）
    [output_w - 50, 20],     # 右上（偏上）
    [20, output_h - 40],     # 左下（微调）
    [output_w - 10, output_h - 10]  # 右下（偏右下，视角倾斜）
])

# 计算透视变换矩阵（cv2.getPerspectiveTransform）
matrix_perspective = cv2.getPerspectiveTransform(src_points, dst_perspective)
# 应用透视变换（cv2.warpPerspective）
img_perspective = cv2.warpPerspective(img, matrix_perspective, (output_w, output_h))
print(f"透视变换：{img.shape[:2]} -> ({output_w}, {output_h})")

# 确保 output 目录存在并保存结果（cv2.imwrite）
os.makedirs(os.path.join(SCRIPT_DIR, "output"), exist_ok=True)
cv2.imwrite(PATH_AFFINE_OUT, img_affine)
cv2.imwrite(PATH_PERSPECTIVE_OUT, img_perspective)

# 显示原图、仿射与透视结果，按任意键关闭（imshow / waitKey / destroyAllWindows）
cv2.imshow("Original Card", img)
cv2.imshow("Affine Corrected", img_affine)
cv2.imshow("Perspective Transformed", img_perspective)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"仿射结果已保存：{PATH_AFFINE_OUT}")
print(f"透视结果已保存：{PATH_PERSPECTIVE_OUT}")
