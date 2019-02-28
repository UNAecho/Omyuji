import time
import datetime
from tasks.tools import identifyImg
from tasks.tools.operation import mouse_click


# task_type:当前调用寄养的方法，人物所处的任务环境。比如打魂十的时候调用寄养时，task_type = "yuhun"
def check_time_and_foster(task_type):
    # 首先检查人物所处位置，如果在探索菜单就先返回主界面
    # 先找下有没有后退的蓝色按钮，不断地按直到没有找到
    if identifyImg.look_for_template_for_a_moment_return_boolean("back_button_blue.png", 2, 0.8):
        while identifyImg.look_for_template_to_click("back_button_blue.png", 0.8):
            identifyImg.look_for_template_to_click("back_button_blue.png", 0.8)
    # 点击主界面阴阳寮按钮
    identifyImg.look_for_template_to_click("main_menu_yinyangliao.png", 0.8)
    # 点击结界，进入结界界面
    identifyImg.wait_for_a_moment_and_click_template("boundary_button.png", 5, 0.8)
    # 点击式神育成
    identifyImg.wait_for_a_moment_and_click_template("boundary_index.png", 5, 0.75)
    time.sleep(1)
    # 观察一下寄养按钮是否可用
    foster_coordinate = identifyImg.identify_find_template_or_not("boundary_foster_button.png", 0.8)
    # 如果寄养还没结束，则终止寄养流程，开始准备返回上一级调用
    if not foster_coordinate:
        # 返回正在进行的任务，比如御魂
        back_to_mission(task_type)
        return
    mouse_click(foster_coordinate['x'], foster_coordinate['y'])
    # 最多等待5秒寄养主界面弹出，方法是检测模板中的【结界卡】字样
    identifyImg.look_for_template_for_a_moment_return_boolean("boundary_foster_main_menu_flag.png", 5, 0.8)
    while True:
        # 检查当前画面是否有好友挂了卡并开放寄养，目前是鉴定鸟居图标是否出现
        friend_boundary_available_coordinate = identifyImg.multi_template_coordinate("boundary_available_flag.png", 0.9)
        # 如果没有人挂卡，终止循环
        if friend_boundary_available_coordinate.__len__() == 0:
            break
        # 开始挑卡寄养，尽量选择收益高的
        check_friend_to_foster(friend_boundary_available_coordinate)

    # 挂完卡之后，开始返回进行中任务
    back_to_mission(task_type)


def back_to_mission(task_type):
    pass


def check_friend_to_foster(friend_boundary_available_coordinate):
    # 开始逐个点击可挂卡的好友
    for coordinate in friend_boundary_available_coordinate:
        # 点击鸟居flag，代表该好友挂了卡
        mouse_click(coordinate[0], coordinate[1])
        identifyImg.wait_loading()
        if identifyImg.identify_find_template_or_not("taiko_level_6.png", 0.8):
            print("六星太鼓赶紧寄养，赚飞了")
            break
        elif identifyImg.identify_find_template_or_not("taiko_level_6.png", 0.8):
            print("六星斗鱼太赚了，体力就是一切")
            break
        elif identifyImg.identify_find_template_or_not("taiko_level_4_and_5.png", 0.8):
            print("四五星太鼓，直接寄养")
            break
        elif identifyImg.identify_find_template_or_not("fish_level_4_and_5.png", 0.8):
            print("四星斗鱼，也行")
            break
    # 点击进入结界
    identifyImg.look_for_template_to_click("boundary_entry_other_boundary.png", 0.8)
    # 寻找【友】字的坑位
    if identifyImg.look_for_template_for_a_moment_return_boolean("boundary_entry_other_boundary.png", 8, 0.8):
        # 如果有坑位，点击【全部】按钮，挑选寄养式神的稀有度
        identifyImg.look_for_template_to_click("common_rare_button.png", 0.8)
        # 选择N卡狗粮寄养
        identifyImg.wait_for_a_moment_and_click_template("common_rare_N.png", 3, 0.8)


