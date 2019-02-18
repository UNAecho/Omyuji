import time

from tasks import beginning
from tasks.tools import hwndInfo
from tasks.tools import windowTools

# 阴阳师位置
yys_exe = 'C:\\game\\Onmyoji\\Launch.exe'

omyuji_hwnd_info = hwndInfo.getHwndInfo()


# 设定想要执行的任务模式
# mission = {"yuling": 90, "infinite_breakthrough": "union"}
# mission = {"infinite_breakthrough": "personal"}
# mission = {"infinite_breakthrough": "union"}
mission = {"yuhun": 500 - 29}
# mission = {"experience": {"28": 500-30}}
# 移动窗口
windowTools.move_window_to_0_0()
time.sleep(1)
# 判断是否为多开模式
if omyuji_hwnd_info.keys().__len__() == 1:
    print("您目前处于单开模式")
    beginning.single_work(omyuji_hwnd_info, mission)
else:
    print("您目前处于多开模式")
    beginning.multi_work(omyuji_hwnd_info, mission)

