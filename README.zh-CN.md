# 圆形图片裁剪工具

这是一个简单的 Python 脚本，用于将正方形图片裁剪成圆形。该工具使用 PIL (Python Imaging Library) 来处理图像。

## 功能特点

- 将正方形图片裁剪为完美的圆形
- 保持原始图片的质量
- 支持透明背景（输出为 PNG 格式）

## 使用要求

- Python 3.x
- Pillow 库

## 安装依赖

克隆项目后，在项目根目录执行以下命令安装所需依赖：

```bash
pip install -r requirements.txt
```

## 使用方法

在项目根目录执行以下命令：

```bash
python crop_to_circle.py 输入图片路径 输出图片路径
``` 