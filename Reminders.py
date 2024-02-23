import ctypes
import random
import time
from PIL import Image

# 定义壁纸路径
wallpapers = [
    "wallpaper1.jpg",
    "wallpaper2.jpg",
    "wallpaper3.jpg",
]

# 定义提示文本
message = "您已经工作 120 分钟了，请休息一下"

# 获取桌面句柄
hwnd = ctypes.windll.user32.GetDesktopWindow()

# 定义函数，用于设置桌面壁纸
def set_wallpaper(path):
    image = Image.open(path)
    width, height = image.size
    ctypes.windll.user32.SystemParametersInfoW(20, 0, width, height, 1)
    ctypes.windll.user32.SetWallpaper(path, 0)

# 定义函数，用于显示提示
def show_message():
    x = 0
    while x < 1000:
        ctypes.windll.user32.SetWindowPos(
            0, hwnd, x, 0, 0, 0, 0x0001 | 0x0002
        )
        ctypes.windll.user32.DrawText(
            hwnd,
            message,
            len(message),
            (x, 0),
            0x00000004 | 0x00000020 | 0x00000080,
        )
        x += 1
        time.sleep(0.01)

# 开始循环
while True:
    # 随机选择一张壁纸
    wallpaper = random.choice(wallpapers)
    # 设置桌面壁纸
    set_wallpaper(wallpaper)
    # 显示提示
    show_message()
    # 等待 60 分钟
    time.sleep(60 * 60)
