import random
import time
import win32api
import win32con
import win32gui
from datetime import datetime
from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools.operation import mouse_click
from tasks.tools.operation import mouse_move
from tasks.tools import identifyImage
from tasks.repository import templateEntity
from tasks.tools import mouseevent_wheel
from tasks.tools import invitationTask
from tasks.tools import fight
from tasks.tools import observerTools
from tasks import breakthrough
from tasks.tools import windowTools
from tasks.tools import bufferTools

# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()


def single_player(omyuji_hwnd_info,mission):
    coordinate = Coordinate()
    # 点击探索
    mouse_click(random.randint(coordinate.explore_x_left,coordinate.explore_x_left), random.randint(coordinate.explore_y_top,coordinate.explore_y_bottom))
    time.sleep(3)


def multi_player(omyuji_hwnd_info,config):
    # 点击探索
    # mouse_click(random.randint(Coordinate.explore_x_left,Coordinate.explore_x_left), random.randint(Coordinate.explore_y_top,Coordinate.explore_y_bottom))
    # time.sleep(3)

    battle_statistics_and_command(omyuji_hwnd_info,config)


def start_yuhun_to_attack_for_multi_player(omyuji_hwnd_info, config):
    time.sleep(1)

    # 获取窗口焦点
    win32gui.SetForegroundWindow(list(omyuji_hwnd_info.keys())[1])
    # 点击御魂
    mouse_click(random.randint(Coordinate.yuhun_x_left, Coordinate.yuhun_x_right),
                random.randint(Coordinate.yuhun_y_top, Coordinate.yuhun_y_bottom))

    time.sleep(2)

    # 点击大蛇打开御魂组队界面
    mouse_click(random.randint(Coordinate.choose_yuhun_not_yeyuanhuo_x_left, Coordinate.choose_yuhun_not_yeyuanhuo_x_right),
                random.randint(Coordinate.choose_yuhun_not_yeyuanhuo_y_top, Coordinate.choose_yuhun_not_yeyuanhuo_y_bottom))

    time.sleep(1)

    start_choose_floor_of_yuhun_to_attack(omyuji_hwnd_info)


def start_choose_floor_of_yuhun_to_attack(omyuji_hwnd_info=None):
    # 选择组队
    common_button_creatteam_file = "common_button_creatteam.png"
    identifyImage.identify_template_click(common_button_creatteam_file, template_cv2_entity[common_button_creatteam_file], 0.95)
    time.sleep(1.5)
    # # 开始选择层数
    # team_choose_yuhun_floor_filename = "team_choose_yuhun_floor.png"
    # choose_floor_button_coordinate = identifyImage.identify_find_template_or_not(team_choose_yuhun_floor_filename,template_cv2_entity[team_choose_yuhun_floor_filename], 0.95)
    # if choose_floor_button_coordinate.__len__() > 0:
    #     mouse_move(choose_floor_button_coordinate['x'], choose_floor_button_coordinate['x'])
    #     mouseevent_wheel.scroll_down_to_the_bottom()
    # # 点击十层
    # floor_10_filename = "floor_10.png"
    # identifyImage.identify_template_click(floor_10_filename, template_cv2_entity[floor_10_filename], 0.95)
    # time.sleep(1)
    # 点击创建队伍
    create_team_filename = "create_team.png"
    identifyImage.identify_template_click(create_team_filename, template_cv2_entity[create_team_filename], 0.95)
    time.sleep(1)
    # 开始配置魂十-不公开队伍
    choose_10_floor_of_yuhun_private_team()


def choose_10_floor_of_yuhun_private_team():
    # 为了效率，默认跳过
    # # 副本类型选择魂十
    # mouse_move(Coordinate.create_team_choose_type_of_battle_x_left, Coordinate.create_team_choose_type_of_battle_y_top)
    # time.sleep(0.5)
    # mouseevent_wheel.scroll_down_to_the_bottom()
    # time.sleep(0.5)
    # 选择十层
    mouse_move(Coordinate.create_team_choose_floor_of_battle_x_left, Coordinate.create_team_choose_floor_of_battle_y_top)
    mouseevent_wheel.scroll_down_to_the_bottom()
    time.sleep(0.5)
    # 限制60级进入
    mouse_move(Coordinate.create_team_minimum_lv_x_left, Coordinate.create_team_minimum_lv_y_top)
    mouseevent_wheel.scroll_down_to_the_bottom()
    time.sleep(0.5)
    mouse_move(Coordinate.create_team_max_lv_x_left, Coordinate.create_team_max_lv_y_top)
    mouseevent_wheel.scroll_down_to_the_bottom()
    time.sleep(0.5)
    # 点击创建
    create_button_filename = "create_button.png"
    identifyImage.identify_template_click(create_button_filename, template_cv2_entity[create_button_filename], 0.95)
    time.sleep(1)


def battle_statistics_and_command(omyuji_hwnd_info, mission):
    residue_number = mission
    battle_count = 0
    win_count = 0
    # 寮突破是否可以继续打的Flag，True：可以打，False：不可以继续打了
    whether_breakthrough_is_available = True
    # 判断收益号是否开始执行个人突破，突破票28张以上就开打
    windowTools.switch_window(list(omyuji_hwnd_info.keys())[0])
    breakthrough.AOP_for_breakthrough(omyuji_hwnd_info)

    # 切回队长小号开始流程
    windowTools.switch_window(list(omyuji_hwnd_info.keys())[1])
    # 开始进入刷御魂主流程
    start_yuhun_to_attack_for_multi_player(omyuji_hwnd_info, mission)
    # 邀请大号，返回开始战斗图标坐标
    start_battle_button_is_availeable_coordinate = invitationTask.invite_main_account_for_yuhun(omyuji_hwnd_info)
    # 点击开始战斗
    mouse_click(start_battle_button_is_availeable_coordinate['x'],
                start_battle_button_is_availeable_coordinate['y'])
    # 获取当前时间点，用时间差计算何时进入寮突：
    the_last_breakthrough_union_time = datetime.now()
    while win_count < residue_number:
        # 进入大小号无限刷的循环
        print("当前已打："+str(battle_count)+"次，胜利："+str(win_count)+"次，还需再打"+str(residue_number - win_count)+"次")
        # 进入战斗，注意当前是小号视角，退出战斗可以找开始战斗按钮是否出现
        battle_result = fight.fight("common_team_start_battle_button.png")
        battle_count += 1
        if battle_result:
            win_count += 1
        # 设置默认邀请队友界面是否会弹出的Flag
        default_invite = False
        # 第一次组队，一定会弹出默认邀请
        first_default_invite = True

        # 检测弹出【是否默认邀请队友界面】
        if not default_invite and first_default_invite:
            # 开始执行点击默认邀请流程，首先要把首次进入战斗Flag设为False
            first_default_invite = False
            checkbox_need_to_click_filename = "checkbox_need_to_click.png"
            checkbox_need_to_click_coordinate = identifyImage.\
                identify_find_template_or_not(
                checkbox_need_to_click_filename,0.85)
            if checkbox_need_to_click_coordinate.__len__() > 0:
                print("点击默认邀请队友")
                mouse_click(checkbox_need_to_click_coordinate['x'],
                            checkbox_need_to_click_coordinate['y'])
                # 点击确定
                common_confirm_button_filename = "common_confirm_button.png"
                identifyImage.identify_template_click(common_confirm_button_filename,
                                                       template_cv2_entity[common_confirm_button_filename], 0.95)
                # 点了默认邀请之后，默认邀请Flag设置为True
                default_invite = False
        windowTools.switch_window(list(omyuji_hwnd_info.keys())[0])
        check_explore_filename = "check_explore.png"
        # 切出去等待大号点出战斗，判断方式为左下角出现御魂图标
        while True:
            time.sleep(0.6)
            print("点击屏幕退出战斗画面")
            # 为了防止弹出御魂6000超量警告，这里加一个判断点击
            # 判断御魂数量大于6000
            yuhun_number_exceeded_filename = "yuhun_number_exceeded.png"
            yuhun_number_exceeded_coordinate = identifyImage.identify_find_template_or_not(
                yuhun_number_exceeded_filename, 0.85)
            if yuhun_number_exceeded_coordinate.__len__() > 0:
                mouse_click(yuhun_number_exceeded_coordinate['x'],
                            yuhun_number_exceeded_coordinate['y'])
                print("大号御魂超数了，赶紧去清了")
            # 如果没见到超量，就正常点击小号邀请
            check_explore = identifyImage.identify_find_template_or_not(check_explore_filename, 0.75)
            if check_explore.__len__() > 0:
                break
            # 如果意外地弹出去直接进了队，那么离开点击
            leave_the_team_button_filename = "leave_the_team_button.png"
            leave_the_team_button_coordinate = identifyImage.identify_find_template_or_not(leave_the_team_button_filename, 0.85)
            if leave_the_team_button_coordinate.__len__() > 0:
                break
            mouse_click(Coordinate.explore_getoutofbattle_x_left, Coordinate.explore_getoutofbattle_y_top)
        # 在接受前，判断大号突破票是否大于28张，如是，则先进行突破
        personal_breakthrough_ticket = observerTools.remaining_of_personal_breakthrough_ticket()
        print("当前突破票剩余：" + personal_breakthrough_ticket)
        if int(personal_breakthrough_ticket) > 28:

            # Sensitive operation!!!
            # 关buffer
            # bufferTools.switch_off_all_of_buffer()

            # 开始突破
            breakthrough.breakthrough_personal("yuhun")

            # Sensitive operation!!!
            # 开buffer
            # bufferTools.switch_on_buffer("yuhun")

        # 接下来判断经过时间，用于进入寮突破
        breakthrough_loop_time = datetime.now()
        time_lapse = (breakthrough_loop_time - the_last_breakthrough_union_time).seconds
        print("与上次突破时间相比，当前经过了：" + str(time_lapse) + "秒")
        if time_lapse > 300 or time_lapse < 5:
            # 加入定时寮突破
            print("又该打寮突了，当前时间 ：" + str(datetime.now()))
            if whether_breakthrough_is_available:
                # Sensitive operation!!!
                # 关buffer
                # buffer_tools.switch_off_all_of_buffer()

                # 开始寮突破
                whether_breakthrough_is_available = breakthrough.start_to_breakthrough("union", "yuhun")

                # Sensitive operation!!!
                # 开buffer
                # buffer_tools.switch_on_buffer("yuhun")

                # 记录打完突破的时间点，用于下一次计算时长
                the_last_breakthrough_union_time = datetime.now()
            else:
                print("记得上一次看到100%被攻破了，那今天先不打寮突了")
        # 判断完个突（如果票够）和寮突（如果时间点对）后，点击对号接受组队
        # mouse_click(Coordinate.accept_invite_x_left, Coordinate.accept_invite_y_top)
        accept_xiaohao_invite = "accept_xiaohao_invite.png"
        for i in range(10):
            # 检测小号邀请信息，点击对号
            xiaohao_invite_coordinate = identifyImage. \
                identify_find_template_or_not(accept_xiaohao_invite, 0.85)
            if xiaohao_invite_coordinate:
                # 如果找到默认邀请了，仅点击对号接受邀请
                if identifyImage.look_for_template_for_a_moment_return_boolean("continuous_invited_flag.png", 3, 0.85):
                    mouse_click(xiaohao_invite_coordinate['x'] - 170,
                                xiaohao_invite_coordinate['y'] + 10)
                    print("检测到小号发来的默认邀请，仅点击对号接受本次邀请")
                    time.sleep(0.2)
                    break
                # 如果没找到默认邀请的标志，那么就是普通邀请
                mouse_click(xiaohao_invite_coordinate['x'] - 95,
                            xiaohao_invite_coordinate['y'] + 10)
                print("检测到小号发来的普通邀请，点击对号接受本次邀请")
                time.sleep(0.2)
                break
        time.sleep(0.1)
        # 打完突破（如果打了）之后，切换小号观察大号是否进来，如是，开始战斗。如不是，重新邀请
        windowTools.switch_window(list(omyuji_hwnd_info.keys())[1])
        time.sleep(0.3)
        headportrait_of_main_account_filename = "headportrait_of_main_account.png"
        headportrait_of_main_account_coordinate = \
            identifyImage.identify_find_template_or_not(headportrait_of_main_account_filename, 0.85)
        if headportrait_of_main_account_coordinate.__len__() > 0:
            # 看开始战斗按钮是否可用，如有，则进行下一轮循环，直到打满输入次数
            common_team_start_battle_button_filename = "common_team_start_battle_button.png"
            start_battle_button_is_availeable_coordinate = \
                identifyImage.identify_find_template_or_not(common_team_start_battle_button_filename, 0.95)
            if start_battle_button_is_availeable_coordinate.__len__() > 0:
                print("邀请成功，退出invite_main_account_for_yuhun()")
                # 点击开始战斗
                mouse_click(start_battle_button_is_availeable_coordinate['x'],
                            start_battle_button_is_availeable_coordinate['y'])
        else:
            # 邀请大号，返回开始战斗图标坐标
            start_battle_button_is_availeable_coordinate = invitationTask.invite_main_account_for_yuhun(omyuji_hwnd_info)
            # 点击开始战斗
            mouse_click(start_battle_button_is_availeable_coordinate['x'],
                        start_battle_button_is_availeable_coordinate['y'])
