# OpenCV 28 天系统学习计划

基于《OpenCV_28天学习计划表_跟随AI编程.xlsx》整理的实战学习项目，每日固定学习 2 小时，从图像基础到工业视觉综合应用。

## 项目简介

本项目按 28 天（4 周）循序渐进学习 OpenCV，面向工业视觉入门场景。每周有明确的学习主题与验收标准，每日代码按 `Day1/` ~ `Day28/` 目录组织。

**开发准则**：新增每日练习代码前，请先阅读 [`开发准则.md`](开发准则.md)。

**当前进度**：Day1 ~ Day5 已实现（图像 IO、像素与 ROI、色彩空间转换、几何变换、平移与旋转）。

## 环境准备

```bash
pip install -r requirements.txt
```

推荐使用 VS Code 作为开发工具。安装完成后，可先运行 Day1 脚本验证环境是否正常。

## 每日时长分配

| 环节 | 时长 |
|------|------|
| 知识点 + 函数讲解 | 40 分钟 |
| 代码编写 + 参数调试 | 70 分钟 |
| 问题记录 + 当日复盘 | 10 分钟 |

## 四阶段学习路线

### 第一周（Day1 ~ Day7）：图像基础 & 几何变换

**核心内容**：图像基础、色彩空间、几何变换（地基）

| 天数 | 学习主题 | 核心知识点 | 当日目标 |
|------|----------|------------|----------|
| Day1 | 图像 IO 与窗口基础 | imread / imshow / imwrite；VideoCapture；BGR 通道特性 | 熟练完成图片、视频流基础读写 |
| Day2 | 像素操作 & ROI 区域 | 图像宽/高/通道属性；像素读取与修改；局部 ROI 裁剪 | 掌握任意区域截取，理解图像矩阵逻辑 |
| Day3 | 色彩空间转换 | BGR ↔ GRAY、BGR ↔ HSV；通道分离/合并 | 分清各类色彩空间用途，掌握 HSV 基础 |
| Day4 | 基础几何变换 | resize 缩放、flip 翻转 | 灵活调整图像尺寸与画面方向 |
| Day5 | 平移 & 旋转 | warpAffine 平移、图像旋转 | 掌握简单旋转画面的矫正方法 |
| Day6 | 仿射 & 透视变换入门 | 仿射变换四点映射、透视变换基础 | 理解变换矩阵作用，实现基础图像矫正 |
| Day7 | 第一周综合复盘 + 小项目 | 整合本周全部基础 API | 独立完成小型工具，梳理本周疑难问题 |

**第一周验收标准**：可独立完成图片读写、裁剪、旋转、基础矫正，熟练使用色彩空间转换。

### 第二周（Day8 ~ Day14）：图像预处理

**核心内容**：阈值、滤波、形态学操作（工业预处理核心）

| 天数 | 学习主题 | 核心知识点 |
|------|----------|------------|
| Day8 | 全局二值化 | threshold 全局阈值、各类二值化模式 |
| Day9 | 自适应二值化 | adaptiveThreshold 自适应阈值 |
| Day10 | 基础滤波 | 均值滤波、高斯滤波 |
| Day11 | 进阶滤波 | 中值滤波、双边滤波 |
| Day12 | 形态学基础 | 腐蚀 erode、膨胀 dilate、结构元素核 |
| Day13 | 形态学组合运算 | 开运算、闭运算、形态学梯度 |
| Day14 | 综合项目：颜色追踪 | HSV 阈值分割 + 滤波 + 形态学组合 |

**第二周验收标准**：可根据图像噪声、光照条件，自主搭配「滤波 + 二值化 + 形态学」预处理流程。

### 第三周（Day15 ~ Day21）：边缘、轮廓与目标分析

**核心内容**：边缘检测、轮廓分析、绘图标注（传统视觉核心）

| 天数 | 学习主题 | 核心知识点 |
|------|----------|------------|
| Day15 | 梯度边缘 | Sobel 算子、Laplacian 拉普拉斯算子 |
| Day16 | Canny 边缘检测 | Canny 双阈值、边缘降噪逻辑 |
| Day17 | 绘图与标注 | 画线、矩形、圆形、文字绘制 |
| Day18 | 轮廓基础 | findContours、drawContours、轮廓层级 |
| Day19 | 轮廓特征计算 | 轮廓面积、周长、外接矩形、最小包围矩形 |
| Day20 | 综合项目：物体计数 | 二值化 + 形态学 + 轮廓统计 |
| Day21 | 综合项目：运动目标检测 | 帧差法 + 轮廓检测 |

**第三周验收标准**：熟练实现边缘提取、轮廓分析、物体计数、动态目标检测。

### 第四周（Day22 ~ Day28）：工业综合项目 + 进阶算子

**核心内容**：工业视觉场景落地项目，衔接相机、图像拼接业务

| 天数 | 学习主题 | 核心知识点 |
|------|----------|------------|
| Day22 | 像素尺寸测量 | 像素-物理尺寸标定、轮廓矩形换算 |
| Day23 | 外观缺陷检测 | 阈值分割 + 轮廓筛选 + 特征判断 |
| Day24 | 模板匹配 | matchTemplate 模板匹配、匹配度筛选 |
| Day25 | 图像直方图 | 直方图计算、图像亮度/对比度调整 |
| Day26 | 角点检测 | Harris、Shi-Tomasi 角点检测 |
| Day27 | 图像拼接与矫正 | 特征点匹配 + 透视变换 |
| Day28 | 全周期复盘 + 项目优化 | 梳理全量算子、算法流程、常见问题 |

**第四周验收标准**：能够独立开发尺寸测量、缺陷检测、模板定位三类主流工业视觉程序。

## 通用执行规则 & 避坑提醒

1. **重参数调试，拒绝单纯抄代码**：工业视觉核心是参数调试，阈值、Canny、形态学核大小等参数需要反复修改观察效果，积累实战经验。
2. **注意图像通道差异**：OpenCV 默认读取图像为 **BGR** 通道，与 Matplotlib、PIL 的 **RGB** 通道不通用，混合使用时必须做通道转换。
3. **代码规范化**：练习过程中逐步将重复逻辑封装为函数，贴合工业项目代码规范。
4. **练习素材选型**：优先使用工业工件、零件、流水线画面练习，贴合实际工作场景。

## 目录结构

```text
stady/
├── README.md
├── requirements.txt
├── OpenCV_28天学习计划表_跟随AI编程.xlsx
├── Day1/
│   ├── images/                  # 放置测试图片
│   ├── output/                  # 脚本输出目录
│   ├── day1_image_io.py         # 图片读写练习
│   └── day1_camera_preview.py   # 摄像头实时预览
├── Day2/
│   ├── images/                  # 放置测试图片
│   ├── output/                  # 脚本输出目录
│   ├── day2_roi_pixel.py        # ROI 裁剪与像素修改（OpenCV 算子）
│   └── day2_numpy_in_cv.py      # NumPy 在 OpenCV 中的用法
├── Day3/
│   ├── images/                  # 放置测试图片
│   ├── output/                  # 脚本输出目录
│   └── day3_color_space.py      # 色彩空间转换与通道分离/合并
├── Day4/
│   ├── images/                  # 放置测试图片
│   ├── output/                  # 脚本输出目录
│   └── day4_geometric_transform.py  # 图像缩放与翻转
├── Day5/
│   ├── images/                  # 放置测试图片
│   ├── output/                  # 脚本输出目录
│   └── day5_translate_rotate.py # 平移与旋转矫正
├── Day6/ ~ Day28/               # 后续每日练习（待实现）
```

## Day1 快速开始

### 1. 准备测试图片

将一张测试图片（如 `test.jpg`）放入 `Day1/images/` 目录。

### 2. 运行图片读写脚本

```bash
python Day1/day1_image_io.py
```

脚本会读取图片、显示窗口、打印图像属性，并将结果保存到 `Day1/output/`。

### 3. 运行摄像头预览脚本

```bash
python Day1/day1_camera_preview.py
```

打开默认摄像头实时预览，按 **q** 键退出。

## Day2 快速开始

### 1. 准备测试图片

将测试图片（如 `cat1.jpg`）放入 `Day2/images/` 目录。

### 2. 运行 ROI 与像素操作脚本（OpenCV 算子）

```bash
python Day2/day2_roi_pixel.py
```

脚本会打印图像尺寸与像素值，裁剪 ROI 区域并修改指定区域颜色，输出保存至 `Day2/output/`：

- `day2_roi.jpg` — 原始 ROI 裁剪图
- `day2_pixel_modified.jpg` — 修改像素后的完整图像

### 3. 运行 NumPy 图像操作脚本

```bash
python Day2/day2_numpy_in_cv.py
```

脚本演示 OpenCV 图像作为 NumPy 数组的索引、切片、通道访问、`.copy()` 与 `np.mean()`，输出：

- `day2_numpy_roi_copy.jpg` — 独立拷贝后修改的 ROI
- `day2_numpy_channel.jpg` — 用 NumPy 切片修改 ROI 后的完整图像

## Day3 快速开始

### 1. 准备测试图片

将测试图片（如 `cat1.jpg`）放入 `Day3/images/` 目录。

### 2. 运行色彩空间转换脚本

```bash
python Day3/day3_color_space.py
```

脚本完成 BGR→灰度、BGR→HSV 转换，拆分 B/G/R 三通道并合并还原，输出保存至 `Day3/output/`：

- `day3_gray.jpg` — 灰度图
- `day3_hsv.jpg` — HSV 图
- `day3_channel_b.jpg` / `day3_channel_g.jpg` / `day3_channel_r.jpg` — 三通道单图
- `day3_merged.jpg` — 通道合并还原图

## Day4 快速开始

### 1. 准备测试图片

将测试图片（如 `cat1.jpg`）放入 `Day4/images/` 目录。

### 2. 运行基础几何变换脚本

```bash
python Day4/day4_geometric_transform.py
```

脚本对单张图片进行缩放与左右/上下镜像，输出保存至 `Day4/output/`：

- `day4_resized.jpg` — 缩放结果（默认缩小为 50%）
- `day4_flip_horizontal.jpg` — 左右镜像
- `day4_flip_vertical.jpg` — 上下镜像

## Day5 快速开始

### 1. 准备测试图片

将测试图片（如 `cat1.jpg`）放入 `Day5/images/` 目录。

### 2. 运行平移与旋转脚本

```bash
python Day5/day5_translate_rotate.py
```

脚本演示图像平移、模拟倾斜与旋转矫正，输出保存至 `Day5/output/`：

- `day5_translated.jpg` — 平移结果
- `day5_tilted.jpg` — 模拟倾斜（旋转 20°）
- `day5_corrected.jpg` — 旋转矫正（反向 -20°）
