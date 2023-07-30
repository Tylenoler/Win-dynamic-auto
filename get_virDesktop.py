import win32com.client


def get_desktop_count():
    # 初始化COM库
    win32com.client.Dispatch("WbemScripting.SWbemLocator")
    win32com.client.Dispatch("WbemScripting.SWbemLocator").ConnectServer(".", "root\cimv2")

    # 获取Virtual Desktop Manager的接口
    virtual_desktop_manager = win32com.client.Dispatch("VirtualDesktopManagerInternal")

    # 获取桌面数量
    desktop_count = virtual_desktop_manager.GetDesktopCount()

    return desktop_count


# 调用函数获取桌面数量
count = get_desktop_count()
print("桌面数量:", count)
