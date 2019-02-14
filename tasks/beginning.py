import time
import random
from tasks.repository.GameCoordinateIndex import Coordinate
from tasks import breakthrough, experience
from tasks import yuhun
from tasks import yuling
from tasks.backToIndex import backToIndex
from tasks.tools.operation import mouse_click
from tasks.repository import templateEntity

# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()


def single_work(omyuji_hwnd_info, mission):
    # 选择任务模式,mission字典中的key代表任务名称，会在每一个任务方法中取出，分析本次任务执行方式
    for key in mission:
        # if key == "yuhun":
        #     print("准备开始打御魂，预计打"+str(mission[key])+"次")
        #     yuhun_singleplayer(omyuji_hwnd_array, mission[key])
        if key == "yuling":
            print("准备开始打御灵，预计打"+str(mission[key])+"次")
            yuling.single_player(omyuji_hwnd_info, mission[key])
        elif key == "infinite_breakthrough":
            # 点击探索
            mouse_click(random.randint(Coordinate.explore_x_left, Coordinate.explore_x_left),
                        random.randint(Coordinate.explore_y_top, Coordinate.explore_y_bottom))
            time.sleep(3)
            breakthrough.infinite_breakthrough_loop(mission[key])

    # 回到主界面
    backToIndex()


def multi_work(omyuji_hwnd_info, mission):
    # 选择任务模式,mission字典中的key代表任务名称，会在每一个任务方法中取出，分析本次任务执行方式
    for key in mission:
        if key == "yuhun":
            print("准备开始打御魂，预计打"+str(mission[key])+"次")
            yuhun.multi_player(omyuji_hwnd_info, mission[key])
        elif key == "infinite_breakthrough":
            # 点击探索
            mouse_click(random.randint(Coordinate.explore_x_left, Coordinate.explore_x_left),
                        random.randint(Coordinate.explore_y_top, Coordinate.explore_y_bottom))
            time.sleep(3)
            breakthrough.infinite_breakthrough_loop(mission[key])
        elif key == "experience":
            experience.multi_player(omyuji_hwnd_info, mission[key])
        # if key == "yuling":
        #     print("准备开始打御灵，预计打"+str(mission[key])+"次")
        #     yuling.yuling_multiplayer(omyuji_hwnd_array, mission[key])

    # 回到主界面
    backToIndex()


