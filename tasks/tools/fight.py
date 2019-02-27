import random
import time
import win32gui

from tasks.repository import templateEntity
from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools import identifyImg
from tasks.tools.operation import mouse_click

# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()

# 无影响点击处，用于快速弹出奖励，和点击画面结束战斗
random_x = int(random.randint(Coordinate.explore_getoutofbattle_x_left, Coordinate.explore_getoutofbattle_x_right))
random_y = int(random.randint(Coordinate.explore_getoutofbattle_y_top, Coordinate.explore_getoutofbattle_y_bottom))


# template_filename ：用于检测战斗退出时的模板，主要用于判定战斗是否完全退出了。
def fight(template_filename=None):
    # 本次战斗结果返回值，True为胜利，否则失败
    result = False
    print("fight()已启动，首先判断上一次操作是否真的进入了战斗，目前的方法是检测左下角自动图标有没有出现")
    # 判断战斗是否真正进入的循环次数，暂时先判断25次，每次1秒
    whether_start_battle_try_count = 0
    # 判定战斗的模板名称
    word_auto_filename = "word_auto.png"
    while True:
        if whether_start_battle_try_count < 25:
            whether_still_fight = identifyImg.identify_find_template_or_not(
                word_auto_filename, 0.85)
            if whether_still_fight:
                # 看到自动图标出现，代表进入了战斗，跳出当前循环开始执行战斗流程
                break
            else:
                whether_start_battle_try_count += 1
                time.sleep(1)
        else:
            print("可能上一次操作没有真正进入流程，暂时先走战斗失败流程")
            return result
    # ready_button_filename = "ready_button.png"
    # whether_ready_button = identifyImage.identify_find_template_or_not(
    #     ready_button_filename, template_cv2_entity[ready_button_filename], 0.85)
    # if whether_ready_button.__len__() > 0:
    #     print("检测到战斗按钮，点击准备开始战斗")
    #     identifyImage.identify_template_click(
    #         ready_button_filename, template_cv2_entity[ready_button_filename], 0.8)
    # else:
    #     print("没检测到准备按钮，推测阵容锁定，直接进入战斗")
    print("开始进入战斗")
    while True:
        whether_still_fight = identifyImg.identify_find_template_or_not(
            word_auto_filename, 0.85)

        if whether_still_fight:
            # 检测为持续战斗就继续等待结束
            time.sleep(2)
        else:
            print("没有检测到战斗状态，开始判断战斗结果")
            result = check_battle_result()
            break
    # 点击屏幕退出战斗画面
    if template_filename is not None:
        # 尝试点击退出次数，如果超数一定数额，判定是不是要求默认邀请，或者御魂超数量6000了
        try_count = 0
        while True:
            out_of_fight_flag_coordinate = identifyImg.identify_find_template_or_not(
                template_filename, 0.75)
            print("等待模板"+ template_filename + "的出现")
            if out_of_fight_flag_coordinate.__len__() > 0:
                print("已识别出进入战斗前模板：" + template_filename + " fight()方法结束")
                break
            # 超过一定尝试次数，开始特殊状态判断
            if try_count >= 5:
                # 判断是否有默认组队
                checkbox_need_to_click_filename = "checkbox_need_to_click.png"
                checkbox_need_to_click_coordinate = identifyImg. \
                    identify_find_template_or_not(
                    checkbox_need_to_click_filename, 0.85)
                if checkbox_need_to_click_coordinate.__len__() > 0:
                    print("点击默认邀请队友")
                    mouse_click(checkbox_need_to_click_coordinate['x'],
                                checkbox_need_to_click_coordinate['y'])
                    # 点击确定
                    common_confirm_button_filename = "common_confirm_button.png"
                    identifyImg.identify_template_click(common_confirm_button_filename,
                                                        template_cv2_entity[common_confirm_button_filename], 0.85)
                    break
                # 判断御魂数量大于6000
                yuhun_number_exceeded_filename = "yuhun_number_exceeded.png"
                yuhun_number_exceeded_coordinate = identifyImg.identify_find_template_or_not(
                    yuhun_number_exceeded_filename, 0.85)
                if yuhun_number_exceeded_coordinate.__len__() > 0:
                    mouse_click(yuhun_number_exceeded_coordinate['x'],
                                yuhun_number_exceeded_coordinate['y'])
                    # 点击完超6000提醒后还要点击一下无影响位置，用于退出战斗
                    time.sleep(0.3)
                    mouse_click(random_x, random_y)
                    break
                # 判断掉线了
                connecting_filename = "connecting.png"
                connecting_coordinate = identifyImg.identify_find_template_or_not(
                    connecting_filename, 0.85)
                if connecting_coordinate.__len__() > 0:
                    while True:
                        print("掉线了！3秒后继续判断连接状态")
                        time.sleep(3)
                        still_connecting_coordinate = identifyImg.identify_find_template_or_not(
                            connecting_filename, 0.85)
                        if still_connecting_coordinate.__len__() > 0:
                            print("还没连接上，等待中")
                            continue
                        else:
                            print("重连回来了，继续流程，判断战斗是否退出")
                            break
            try_count += 1
            print("没发现出去的迹象，继续点击，尝试次数：" + str(try_count))
            mouse_click(random_x, random_y)
            time.sleep(0.3)
    return result


# return : True:战斗胜利，False:战斗失败
def check_battle_result():
    battle_win_continue_filename = "battle_win_continue.png"
    battle_failed_filename = "battle_failed.png"
    # 计数，防止程序点出了战斗界面，但是循环还在一直判断战斗是成功了还是失败了。
    # 如果超过10秒还在判断，证明程序已经误点出去，默认战斗成功
    count = 0
    while True:
        fail_result = identifyImg.identify_find_template_or_not(
            battle_failed_filename, 0.85)
        if fail_result.__len__() > 0:
            print("战斗失败")
            mouse_click(random_x, random_y)
            return False
        win_result = identifyImg.identify_find_template_or_not(
            battle_win_continue_filename, 0.85)
        if win_result.__len__() > 0:
            print("战斗胜利")
            mouse_click(random_x, random_y)
            return True
        if count < 10:
            count += 1
            mouse_click(random_x, random_y)
            time.sleep(0.3)
        else:
            print("点了10次发现还是没有发现判断战斗结果的图标，证明程序误点出去了，默认战斗胜利")
            return True


def fight_for_experience(omyuji_hwnd_info,template_filename=None):
    battle_result = False
    whether_battle_start = identifyImg.look_for_template_for_a_moment_return_boolean("common_exit_battle.png", 15, 0.85)
    if not whether_battle_start:
        print("fight_for_experience()判断未进入战斗，返回战斗失败退出方法")
        return battle_result
    # 开始更换两个号的狗粮
    check_level_of_hellspawn(omyuji_hwnd_info)


def check_level_of_hellspawn(omyuji_hwnd_info):
    # 定义各个式神满级状态
    level_max_flag_of_main_1 = False
    level_max_flag_of_main_2 = False
    level_max_flag_of_main_3 = False
    # 首先更换收益号狗粮
    win32gui.SetForegroundWindow(list(omyuji_hwnd_info.keys())[0])
    # 开始逐个判断3个位置的式神满级情况
    custom_1_coordinate = (
                            Coordinate.experience_1_member_x_left,
                            Coordinate.experience_1_member_y_top,
                            Coordinate.experience_1_member_x_right,
                            Coordinate.experience_1_member_y_bottom,
                         )
    level_max_flag = identifyImg.identify_find_template_or_not("full_level.png", 0.85, custom_1_coordinate)
    if level_max_flag:
        level_max_flag_of_main_1 = True
    custom_2_coordinate = (
                            Coordinate.experience_2_member_x_left,
                            Coordinate.experience_2_member_y_top,
                            Coordinate.experience_2_member_x_right,
                            Coordinate.experience_2_member_y_bottom,
                         )
    level_max_flag = identifyImg.identify_find_template_or_not("full_level.png", 0.85, custom_2_coordinate)
    if level_max_flag:
        level_max_flag_of_main_2 = True
    custom_3_coordinate = (
                            Coordinate.experience_3_member_x_left,
                            Coordinate.experience_3_member_y_top,
                            Coordinate.experience_3_member_x_right,
                            Coordinate.experience_3_member_y_bottom,
                         )
    level_max_flag = identifyImg.identify_find_template_or_not("full_level.png", 0.85, custom_3_coordinate)
    if level_max_flag:
        level_max_flag_of_main_3 = True
    # 如果有式神满级，点击至更换式神界面
    if level_max_flag_of_main_1 or level_max_flag_of_main_2 or level_max_flag_of_main_3:
        # 开始把满级式神更换至1级式神
        change_the_level_max_hellspawn()


def change_the_level_max_hellspawn():
    mouse_click(random_x, random_y)
    identifyImg.wait_for_a_moment_and_click_template("common_rare_button.png", 5, 0.85)
    identifyImg.wait_for_a_moment_and_click_template("common_rare_N.png", 5, 0.85)
