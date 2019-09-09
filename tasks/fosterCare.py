import time
import datetime
from tasks.tools import identifyImg
from tasks.tools.operation import mouse_click
from tasks.tools import shikigamiTools
import win32api
import win32con


# task_type:当前调用寄养的方法，人物所处的任务环境。比如打魂十的时候调用寄养时，task_type = "yuhun"
def check_time_and_foster(task_type):
    # 进入方法时间，目前方法不够精确，所以是否寄养成功，都返回寄养时间，防止寄养失败后，每一次循环都启用一次寄养。
    foster_time = datetime.datetime.now()
    # 首先检查人物所处位置，如果在探索菜单就先返回主界面
    # 先找下有没有后退的蓝色按钮，不断地按直到没有找到
    if identifyImg.look_for_template_for_a_moment_return_boolean("back_button_blue.png", 2, 0.8):
        while identifyImg.look_for_template_for_a_moment_return_boolean("back_button_blue.png", 5, 0.8):
            identifyImg.look_for_template_to_click("back_button_blue.png", 0.8)
            if identifyImg.look_for_template_for_a_moment_return_boolean("main_menu_yinyangliao.png", 0.5, 0.8):
                print("检测到退回主界面了，开始点击阴阳寮")
                break
    # 点击主界面阴阳寮按钮
    identifyImg.look_for_template_to_click("main_menu_yinyangliao.png", 0.8)
    # 点击结界，进入结界界面
    identifyImg.wait_for_a_moment_and_click_template("boundary_button.png", 5, 0.8)
    # 点击式神育成
    identifyImg.wait_for_a_moment_and_click_template("boundary_index.png", 8, 0.7)
    time.sleep(1)
    # 观察一下寄养按钮是否可用
    foster_coordinate = identifyImg.identify_find_template_or_not("boundary_foster_button.png", 0.8)
    # 如果寄养还没结束，则终止寄养流程，开始准备返回上一级调用
    if not foster_coordinate:
        # 返回正在进行的任务，比如御魂
        back_to_mission(task_type)
        return foster_time
    mouse_click(foster_coordinate['x'], foster_coordinate['y'])
    # 最多等待5秒寄养主界面弹出，方法是检测模板中的【结界卡】字样
    identifyImg.look_for_template_for_a_moment_return_boolean("boundary_foster_main_menu_flag.png", 5, 0.8)

    # 开始挑卡寄养，尽量选择收益高的
    foster_time = check_friend_to_foster()

    # 挂完卡之后，开始返回进行中任务
    back_to_mission(task_type)
    return foster_time


def check_friend_to_foster():
    while True:
        # 检查当前画面是否有好友挂了卡并开放寄养，目前是鉴定鸟居图标是否出现
        friend_boundary_available_coordinate = identifyImg.multi_template_coordinate("boundary_available_flag.png", 0.9)
        # 如果没有人挂卡，终止循环
        if friend_boundary_available_coordinate.__len__() == 0:
            print("无卡可挂，推测是没有收益的坑可蹲，记录当前时间，返回当前执行的任务。比如御魂")
            foster_time = datetime.datetime.now()
            break
        # 开始逐个点击可挂卡的好友
        for coordinate in friend_boundary_available_coordinate:
            # 点击鸟居flag，代表该好友挂了卡
            mouse_click(coordinate[0], coordinate[1])
            identifyImg.wait_loading()
            time.sleep(1)
            if identifyImg.identify_find_template_or_not("taiko_level_6.png", 0.8):
                print("六星太鼓赶紧寄养，赚飞了")
                foster_time = foster_execute()
                break
            elif identifyImg.identify_find_template_or_not("taiko_level_6.png", 0.8):
                print("六星斗鱼太赚了，体力就是一切")
                foster_time = foster_execute()
                break
            elif identifyImg.identify_find_template_or_not("taiko_level_4_and_5.png", 0.8):
                print("四五星太鼓，直接寄养")
                foster_time = foster_execute()
                break
            elif identifyImg.identify_find_template_or_not("fish_level_4_and_5.png", 0.8):
                print("四星斗鱼，也行")
                foster_time = foster_execute()
                break
        # 这一轮没找到的话，就往下滚轮
        for i in range(4):
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -128)
            time.sleep(0.3)
    return foster_time


def foster_execute():
    # 点击进入结界
    identifyImg.look_for_template_to_click("boundary_entry_other_boundary.png", 0.8)
    # 寻找【友】字的坑位
    if identifyImg.look_for_template_for_a_moment_return_boolean("boundary_foster_available_flag.png", 8, 0.8):
        # 寻找目标式神，并返回等级的坐标位置
        shikigami_level_coordinate = shikigamiTools.select_shikigami()
        # 如果没找到滑块，直接return
        if shikigami_level_coordinate.__len__() == 0:
            return
        # N卡被吃光，直接切回全部，随便选第一个寄养
        elif shikigami_level_coordinate.__len__() > 0 and shikigami_level_coordinate['x'] == 0:
            identifyImg.wait_for_a_moment_and_click_template("common_rare_N.png", 3, 0.8)
            identifyImg.wait_for_a_moment_and_click_template("common_rare_button.png", 3, 0.8)
            temp_coordinate = identifyImg.identify_find_template_or_not("common_rare_button.png", 0.8)
            mouse_click(temp_coordinate['x'], temp_coordinate['y'])
            identifyImg.wait_for_a_moment_and_click_template("common_confirm_button.png", 3, 0.8)
            return
        else:
            # 如果正常返回坐标，开始寄养
            mouse_click(shikigami_level_coordinate['x'], shikigami_level_coordinate['y'])
            identifyImg.wait_for_a_moment_and_click_template("common_confirm_button.png", 3, 0.8)
    return datetime.datetime.now()


def back_to_mission(task_type):
    # 挂完卡之后，开始退出界面，方法是不断地点击蓝色退后按钮，直至出现阴阳寮主界面
    while True:
        identifyImg.wait_for_a_moment_and_click_template("back_button_blue.png", 5, 0.8)
        if identifyImg.identify_find_template_or_not("boundary_button.png", 0.8):
            identifyImg.look_for_template_to_click("common_close_button.png", 0.8)
            break
    if task_type == "yuhun":
        identifyImg.look_for_template_to_click("explore_main_button.png", 0.7)
    elif task_type == "infinite_breakthrough":
        identifyImg.look_for_template_to_click("explore_main_button.png", 0.7)
