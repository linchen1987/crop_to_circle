from PIL import Image, ImageDraw
import sys

def crop_to_circle(input_path, output_path):
    try:
        # 打开图片
        img = Image.open(input_path).convert("RGBA")
        
        # 确保图片是正方形
        width, height = img.size
        if width != height:
            size = min(width, height)
            left = (width - size) // 2
            top = (height - size) // 2
            img = img.crop((left, top, left + size, top + size))
        
        # 创建圆形遮罩
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
        
        # 应用遮罩
        result = Image.new("RGBA", img.size, (0, 0, 0, 0))
        result.paste(img, (0, 0), mask)
        
        # 保存结果
        result.save(output_path, "PNG")
        print(f"成功将图片裁剪为圆形并保存为: {output_path}")
        
    except Exception as e:
        print(f"处理图片时出错: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使用方法: python crop_to_circle.py 输入图片路径 输出图片路径")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    crop_to_circle(input_path, output_path) 