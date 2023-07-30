import sys
import pythoncom
import win32com.client
import ctypes

ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
def get_desktop_count():
    win32com.client.Dispatch("WbemScripting.SWbemLocator")
    win32com.client.Dispatch("WbemScripting.SWbemLocator").ConnectServer(".", "root\cimv2")
    try:
        pythoncom.CoInitialize()
        if pythoncom.CoInitialize() != 0:
            print("COM 初始化失败")
            return
        with win32com.client.Dispatch("wscript.shell") as wm:
            print(wm)
            count = wm.SendKeys('%{F4}')
    except:
        print("调用失败!")
        count = 0
    finally:
        pythoncom.CoUninitialize()
    
    return count

count = get_desktop_count()
print("桌面数量:", count)