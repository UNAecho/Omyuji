import random
import time
from datetime import datetime

from tasks import breakthrough
from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools.fight import fight
from tasks.tools.pressBattleButton import choose_floor_and_start_battle
from tasks.tools.operation import mouse_click


def single_player(hwnd_array,config):

    # 点击探索
    mouse_click(random.randint(Coordinate.explore_x_left,Coordinate.explore_x_left), random.randint(Coordinate.explore_y_top,Coordinate.explore_y_bottom))
    time.sleep(3)

    start_choose_yuling_to_attack()

    battle_statistics_and_command(config)

    return


def start_choose_yuling_to_attack():
    time.sleep(1)
    # 点击御灵
    mouse_click(random.randint(Coordinate.yuling_x_left, Coordinate.yuling_x_right),
                random.randint(Coordinate.yuling_y_top, Coordinate.yuling_y_bottom))

    time.sleep(3)

    today = time.localtime().tm_wday

    if today == 0:
        print("周一没御灵你挂啥?")
        return
    elif today == 1:
        print("今天周二，打神龙")
        # 点击神龙
        mouse_click(random.randint(Coordinate.dragon_x_left, Coordinate.dragon_x_right),
                    random.randint(Coordinate.dragon_y_top, Coordinate.dragon_y_bottom))
        time.sleep(1)
        # 选择三层
        mouse_click(random.randint(Coordinate.yuling_floor_x_left, Coordinate.yuling_floor_x_right),
                    random.randint(Coordinate.yuling_floor_y_top, Coordinate.yuling_floor_y_bottom))
        time.sleep(1)
    elif today == 2:
        print("今天周三，打白藏主")
        # 点击白藏主
        mouse_click(random.randint(Coordinate.baizangzhu_x_left, Coordinate.baizangzhu_x_right),
                    random.randint(Coordinate.baizangzhu_y_top, Coordinate.baizangzhu_y_bottom))
        time.sleep(1)
        # 选择三层
        mouse_click(random.randint(Coordinate.yuling_floor_x_left, Coordinate.yuling_floor_x_right),
                    random.randint(Coordinate.yuling_floor_y_top, Coordinate.yuling_floor_y_bottom))
        time.sleep(1)
    elif today == 3:
        print("今天周四，打黑豹")
        # 点击黑豹
        mouse_click(random.randint(Coordinate.panther_x_left, Coordinate.panther_x_right),
                    random.randint(Coordinate.panther_y_top, Coordinate.panther_y_bottom))
        time.sleep(1)
        # 选择三层
        mouse_click(random.randint(Coordinate.yuling_floor_x_left, Coordinate.yuling_floor_x_right),
                    random.randint(Coordinate.yuling_floor_y_top, Coordinate.yuling_floor_y_bottom))
        time.sleep(1)
    elif today == 4:
        print("今天周五，打孔雀")
        # 点击孔雀
        mouse_click(random.randint(Coordinate.peacock_x_left, Coordinate.peacock_x_right),
                    random.randint(Coordinate.peacock_y_top, Coordinate.peacock_y_bottom))
        time.sleep(1)
        # 选择三层
        mouse_click(random.randint(Coordinate.yuling_floor_x_left, Coordinate.yuling_floor_x_right),
                    random.randint(Coordinate.yuling_floor_y_top, Coordinate.yuling_floor_y_bottom))
        time.sleep(1)
    else:
        print("今天周末，打最弱的白藏主")
        # 选择最弱白藏主
        mouse_click(random.randint(Coordinate.baizangzhu_x_left, Coordinate.baizangzhu_x_right),
                    random.randint(Coordinate.baizangzhu_y_top, Coordinate.baizangzhu_y_bottom))
        time.sleep(1)
        # 选择三层
        mouse_click(random.randint(Coordinate.yuling_floor_x_left, Coordinate.yuling_floor_x_right),
                    random.randint(Coordinate.yuling_floor_y_top, Coordinate.yuling_floor_y_bottom))
        time.sleep(1)
    return


def battle_statistics_and_command(config):

    residue_number = config
    battle_count = 0
    win_count = 0
    # 寮突破是否可以继续打的Flag，True：可以打，False：不可以继续打了
    whether_breakthrough_is_available = True
    # 获取当前时间点，用时间差计算何时进入寮突：
    start_breakthrough_time = datetime.now()
    nowhour = time.localtime().tm_hour
    while True:
        breakthrough_loop_time = datetime.now()
        time_lapse = (breakthrough_loop_time - start_breakthrough_time).seconds
        print("与上次突破时间相比，当前经过了：" + str(time_lapse) + "秒")
        if time_lapse > 300 or time_lapse < 1:
            # 加入定时寮突破
            print("又该打寮突了，当前时间 ：" + str(datetime.now()))
            # 关闭御灵主界面 TODO
            mouse_click(931, 139)
            if whether_breakthrough_is_available:
                whether_breakthrough_is_available = breakthrough.start_to_breakthrough("union", "yuling")
                start_breakthrough_time = datetime.now()
            else:
                print("记得上一次看到100%被攻破了，那今天先不打寮突了")
        # 点击挑战
        choose_floor_and_start_battle()
        # 进入战斗
        battle_result = fight("challenge.png")
        battle_count = battle_count + 1
        if battle_result:
            # 计数
            win_count = win_count + 1
            residue_number = residue_number - 1
        print("当前已打" + str(battle_count + 1) + "次,胜利" + str(win_count) + "次,"+"还需胜利"+str(residue_number)+"次")
        if win_count == config:
            break
