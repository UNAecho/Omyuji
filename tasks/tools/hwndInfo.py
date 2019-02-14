import time
import win32gui

from tasks.windowsInfo.windowsInfo import WindowsCoordinateIndex


def getHwndInfo():

    print("getHwndInfo()获取窗口信息")
    # 定义返回类型：dict
    return_result = dict()

    # 定义所有窗口句柄信息类型：字典
    hwnd_title = dict()
    # 获取所有窗口信息

    def get_all_hwnd(hwnd,mouse):
        if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            hwnd_title.update({hwnd:win32gui.GetWindowText(hwnd)})
    win32gui.EnumWindows(get_all_hwnd, 0)

    # 保存阴阳师窗口句柄信息数组
    omyuji_hwnd_array = []

    for handles_key, handles_value in hwnd_title.items():
        if handles_value == "阴阳师-网易游戏":
            omyuji_hwnd_array.append(handles_key)
    time.sleep(1)

    # # 获取窗口焦点
    # win32gui.SetForegroundWindow(omyuji_hwnd_array[0])

    time.sleep(0.3)

    for i in range(omyuji_hwnd_array.__len__()):
        window_x_left, window_y_top, window_x_right, window_y_bottom = win32gui.GetWindowRect(omyuji_hwnd_array[i])
        # 当前句柄所对应的坐标，在本辅助程序中经常使用
        window_info_dict = {"window_x_left": window_x_left,
                            "window_y_top": window_y_top,
                            "window_x_right": window_x_right,
                            "window_y_bottom": window_y_bottom
                            }
        # 返回当前窗口的坐标信息
        return_result[omyuji_hwnd_array[i]] = window_info_dict

    return return_result
