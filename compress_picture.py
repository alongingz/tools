from PIL import Image, ImageFilter, ImageOps
import os, math
import tkinter as tk
from tkinter import messagebox, filedialog


def dodge(a, b, alpha):
    return min(int(a * 255 / (256 - b * alpha)), 255)


def draw(img, blur=25, alpha=1.0):
    img = Image.open(img)
    img1 = img.convert('L')  # 图片转换成灰色
    img2 = img1.copy()
    img2 = ImageOps.invert(img2)
    for i in range(blur):  # 模糊度
        img2 = img2.filter(ImageFilter.BLUR)
    width, height = img1.size
    for x in range(width):
        for y in range(height):
            a = img1.getpixel((x, y))
            b = img2.getpixel((x, y))
            img1.putpixel((x, y), dodge(a, b, alpha))
    img1.show()
    # img1.save('E:\\picture\\10.png')
def change_img_suffix(in_img, suffix):
    """
    图片后缀格式转换
    :param in_img: 图片文件地址
    :param suffix: 要转换的后缀名
    :return: 图片保存地址
    """
    try:
        img = Image.open(in_img)
        imgpath_name = os.path.splitext(in_img)[0]
        if "." in suffix:
            out_name = imgpath_name + suffix
            img.save(out_name)
        else:
            out_name = imgpath_name + "." + suffix
            img.save(out_name)
        return out_name
    except Exception as e:
        return e




def change_img_width_heignt(in_img, out_width_height):
    """
    修改图片尺寸
    :param in_img: 图片地址
    :param out_width_height: 元组类型，宽高
    :return: 图片保存地址
    """
    try:
        img_path, suffix = os.path.splitext(in_img)
        img = Image.open(in_img)
        out_img = img.resize(out_width_height, Image.ANTIALIAS)
        out_image_name = img_path + "_" + str(out_width_height[0]) + "_" + str(out_width_height[1]) + suffix
        out_img.save(out_image_name)
        return out_image_name
    except Exception as e:
        return e


def change_img_size(in_img, out_size, step=3, quality=90):
    """
    修改图片大小
    :param in_img: 图片地址
    :param out_size: 想要的图片大小 单位：kb
    :param step: 每次压缩步值
    :param quality: 初始压缩比率
    :return: 图片保存地址
    """
    try:
        img_path, suffix = os.path.splitext(in_img)
        in_img_size = math.ceil(os.path.getsize(in_img) / 1024)
        out_img = img_path + "_" + str(out_size) + suffix
        nums = 1
        while True:
            if in_img_size > out_size:
                img = Image.open(in_img)
                img.save(out_img, quality=quality)
                img.close()
                quality -= step
                in_img_size = math.ceil(os.path.getsize(out_img) / 1024)
                nums += 1
            else:
                return out_img
    except Exception as e:
        return e


def compress_img_width_height():
    """
    tkinter 使用 压缩尺寸
    :return:
    """
    file = filedialog.askopenfilename()  # 调用文件管理器打开文件并返回文件名
    file_target_size = (int(size_width.get()), int(size_hight.get()))
    img_out_name = change_img_width_heignt(file, file_target_size)
    messagebox.showinfo(title="转换成功", message="图片保存地址：{}".format(img_out_name))
    return img_out_name


def compress_img_size():
    """
    tkinter使用，压缩大小
    :return:
    """
    file = filedialog.askopenfilename()  # 调用文件管理器打开文件并返回文件名
    out_size = int(img_out_size.get())
    img_out_name = change_img_size(file, out_size)
    messagebox.showinfo(title="转换成功", message="图片保存地址：{}".format(img_out_name))
    return img_out_name


top = tk.Tk()
top.title("图片处理")
top.geometry("500x200")
frame1 = tk.Frame(top)
frame2 = tk.Frame(top)

# 图片尺寸处理
tk.Label(frame1, text="图片尺寸处理", width=15).pack(side="left")
tk.Label(frame1, text="图片宽度：", width=10).pack(side="left")
size_width = tk.Entry(frame1, width=10)
size_width.pack(side="left")
tk.Label(frame1, text="图片高度：", width=10).pack(side="left")
size_hight = tk.Entry(frame1, width=10)
size_hight.pack(side="left")
tk.Button(frame1, text="选择图片", width=8, command=compress_img_width_height).pack(side="left")
# 图片大小处理
tk.Label(frame2, text="图片大小处理", width=15).pack(side="left")
tk.Label(frame2, text="目标图片大小(单位：kb)：", width=20).pack(side="left")
img_out_size = tk.Entry(frame2, width=10)
img_out_size.pack(side="left")
tk.Label(frame2, text=" ", width=10).pack(side="left")  # 补缺  美观
tk.Button(frame2, text="选择图片", width=8, command=compress_img_size).pack(side="left")

frame1.pack(padx=1, pady=1)
frame2.pack(padx=1, pady=1)
top.mainloop()

# draw("./2.jpg")
# print(os.path.dirname("./1.jpg"))
# print(os.path.abspath("./1.jpg"))
# print(os.path.realpath("./1.jpg"))
# print(os.path.basename("./1.jpg"))
# print(os.path.getsize("./1.jpg"))  # 单位 b
# print(os.path.split("./1.jpg"))
# print(os.path.splitext("./1.jpg"))
# changeImgWH("./timg.jpg", (360, 180))
# change_img_size("./2.jpg", 500)
# print(round(1.6))
# change_img_width_heignt(r"./2.jpg", (3000, 4000))
# change_img_suffix("./1.jpg", "ico")
