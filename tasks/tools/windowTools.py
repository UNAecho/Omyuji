import time
import win32gui
import win32com.client
from tasks.tools import hwndInfo

# 所有操作


def switch_window(hwnd):
    time.sleep(0.5)
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.5)


def move_window_to_0_0():

    # 获取窗口信息
    omyuji_hwnd_info = hwndInfo.getHwndInfo()
    omyuji_hwnd_array = list(omyuji_hwnd_info.keys())
    if omyuji_hwnd_array.__len__() == 1:
        window_info_dict = omyuji_hwnd_info[omyuji_hwnd_array[0]]

        # 获取窗口焦点
        win32gui.SetForegroundWindow(omyuji_hwnd_array[0])
        # 移动窗口
        win32gui.MoveWindow(omyuji_hwnd_array[0], 0, 0, window_info_dict['window_x_right'] - window_info_dict['window_x_left'], window_info_dict['window_y_bottom'] - window_info_dict['window_y_top'], False)

    else:
        for i in range(omyuji_hwnd_array.__len__()):
            time.sleep(1)
            window_info_dict = omyuji_hwnd_info[omyuji_hwnd_array[i]]
            switch_window(omyuji_hwnd_array[i])
            # 移到i，0为了临时区分大小号
            win32gui.MoveWindow(omyuji_hwnd_array[i], i, 0,
                                window_info_dict['window_x_right'] - window_info_dict['window_x_left'],
                                window_info_dict['window_y_bottom'] - window_info_dict['window_y_top'], False)
            time.sleep(1)
            print("第"+str(i)+"号处理完毕")

