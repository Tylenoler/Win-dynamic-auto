import ctypes
import os
import time

def change_wallpaper(image_path):
    # 使用ctypes库加载user32.dll
    user32 = ctypes.windll.user32

    # 设置壁纸的常量
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    # 调用SystemParametersInfo函数来设置壁纸
    user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

def get_wallpaper_path():
    # 使用ctypes库加载user32.dll
    user32 = ctypes.windll.user32

    # 获取壁纸路径的常量
    SPI_GETDESKWALLPAPER = 0x0073
    MAX_PATH = 260

    # 创建一个缓冲区来存储壁纸路径
    wallpaper_path = ctypes.create_unicode_buffer(MAX_PATH)

    # 调用SystemParametersInfo函数来获取壁纸路径
    user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, MAX_PATH, wallpaper_path, 0)

    # 返回壁纸路径
    return wallpaper_path.value

def main():
    # 获取当前时间
    current_time = time.localtime()

    # 根据当前时间选择要设置的壁纸
    if current_time.tm_hour < 12:
        image_path = "F:\GITHUBCODELIBRARY\Win-dynamic-auto\APPLEWALL/1Early.jpg"
    elif current_time.tm_hour < 18:
        image_path = "F:\GITHUBCODELIBRARY\Win-dynamic-auto\APPLEWALL/1Early.jpg"
    else:
        image_path = "F:\GITHUBCODELIBRARY\Win-dynamic-auto\APPLEWALL/1Early.jpg"

    # 获取当前壁纸路径
    current_wallpaper = get_wallpaper_path()

    # 检查当前壁纸是否与要设置的壁纸相同
    if os.path.abspath(image_path) != current_wallpaper:
        # 更改壁纸
        change_wallpaper(image_path)
        print("壁纸已更改！")
    else:
        print("壁纸已是所需的壁纸，无需更改。")

    # 获取所有桌面的数量
    desktop_count = ctypes.windll.user32.GetSystemMetrics(80)

    # 遍历所有桌面并设置壁纸
    for i in range(desktop_count):
        # 设置当前桌面
        ctypes.windll.user32.SetThreadDesktop(ctypes.windll.user32.OpenDesktopW(str(i), 0, False, 0x0100))

        # 更改壁纸
        change_wallpaper(image_path)

    # 切换回默认桌面
    ctypes.windll.user32.SetThreadDesktop(ctypes.windll.user32.OpenDesktopW("Default", 0, False, 0x0100))

if __name__ == "__main__":
    main()
