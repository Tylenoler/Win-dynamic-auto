import ctypes

user32 = ctypes.WinDLL('user32')

SM_CMONITORS = 80

desktop_count = user32.GetSystemMetrics(SM_CMONITORS)

print(desktop_count)
