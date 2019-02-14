import win32api
import win32con
import time
from ctypes import *
from tasks.tools.keycode import keycode

# 鼠标点击操作
def mouse_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# 鼠标双击
def mouse_dclick(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

# 鼠标移动
def mouse_move(x,y):
    win32api.SetCursorPos((x, y))
    # windll.user32.SetCursorPos(x, y)
# 输入
def key_input(str):
    for c in str:
        win32api.keybd_event(keycode[c],0,0,0)
        time.sleep(0.01)
        win32api.keybd_event(keycode[c],0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(0.02)

# 鼠标拖拽
def mouse_drag(x, y, x2, y2):
    mouse_move(x, y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.2)
    mw = int(x2 * 65535 / 1920)
    mh = int(y2 * 65535 / 1080)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)    
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)