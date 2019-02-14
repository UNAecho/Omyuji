import time
import win32api

import win32con


# win32con.MOUSEEVENTF_WHEEL代表鼠标中轮，第四个参数正数代表往上轮滚，负数代表往下

def scroll_down_to_the_bottom():
    for i in range(10):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -128)
        time.sleep(0.2)
