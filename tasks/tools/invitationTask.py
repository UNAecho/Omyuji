import random
import time

from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools import windowTools
from tasks.repository import templateEntity
from tasks.tools import identifyImage
from tasks.tools.operation import mouse_click
from tasks import yuhun
from tasks import experience

# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()


def invite_main_account_for_yuhun(omyuji_hwnd_info):
    while True:
        invite_main_account()
        # 切大号接受
        accept_invite_from_captain(omyuji_hwnd_info)
        # 切换小号观察大号是否进来，如是，开始战斗。如不是，重新邀请
        print("切换小号观察大号是否进来，如是，开始战斗。如不是，重新邀请")
        windowTools.switch_window(list(omyuji_hwnd_info.keys())[1])
        headportrait_of_main_account_filename = "headportrait_of_main_account.png"
        headportrait_of_main_account_coordinate = \
            identifyImage.identify_find_template_or_not(headportrait_of_main_account_filename, 0.85)
        if headportrait_of_main_account_coordinate.__len__() > 0:
            # 发现大号头像，判断大号进来了，返回开始开始战斗按钮坐标
            start_battle_button_is_availeable_filename = "common_team_start_battle_button.png"
            start_battle_button_is_availeable_coordinate = \
                identifyImage.identify_find_template_or_not(start_battle_button_is_availeable_filename, 0.85)

            print("邀请成功，退出invite_main_account_for_yuhun()")
            break
        else:
            print("邀请失败，再来")
    time.sleep(0.3)
    return start_battle_button_is_availeable_coordinate


def invite_main_account():
    print("Start with invite_main_account()")
    # 如果邀请失败了，临时重新打开御魂邀请界面邀请
    checkk_explore_filename = "check_explore.png"
    checkk_explore = identifyImage.identify_find_template_or_not(checkk_explore_filename, 0.85)
    if checkk_explore.__len__() > 0:
        # 点击御魂
        mouse_click(random.randint(Coordinate.yuhun_x_left, Coordinate.yuhun_x_right),
                    random.randint(Coordinate.yuhun_y_top, Coordinate.yuhun_y_bottom))

        time.sleep(2)
        # 点击大蛇
        mouse_click(random.randint(Coordinate.choose_yuhun_not_yeyuanhuo_x_left, Coordinate.choose_yuhun_not_yeyuanhuo_x_right),
                    random.randint(Coordinate.choose_yuhun_not_yeyuanhuo_y_top, Coordinate.choose_yuhun_not_yeyuanhuo_y_bottom))
        yuhun.start_choose_floor_of_yuhun_to_attack()
    # 点击队友空位栏处的邀请图标邀请他人
    invite_ico_filename = "invite_ico.png"
    identifyImage.identify_template_click(invite_ico_filename, template_cv2_entity[invite_ico_filename], 0.85)
    time.sleep(2)
    # 开始寻找大号头像并点击邀请
    headportrait_of_main_account_filename = "headportrait_of_main_account.png"
    main_account_coordinate = identifyImage.identify_find_template_or_not(
        headportrait_of_main_account_filename, 0.8)
    if main_account_coordinate.__len__() > 0:
        # 找到头像后往右移动60像素点击，防止点击头像出现玩家信息操作界面
        mouse_click(main_account_coordinate['x'] + 60, main_account_coordinate['y'])
    time.sleep(0.5)
    # 点击邀请
    invite_button_filename = "invite_button.png"
    identifyImage.identify_template_click(invite_button_filename, template_cv2_entity[invite_button_filename], 0.8)


def invite_main_account_experience(omyuji_hwnd_info, chapter):
    # 首先等待看见大号名字
    main_account_appeare_flag = identifyImage.wait_for_a_moment_and_click_template("headportrait_of_main_account.png", 3, 0.85)
    if not main_account_appeare_flag:
        # 如果出现异常，直接点击X退出到探索主界面，重新选择章节再邀请一次。
        catch_invite_main_account_error(chapter)
    invite_click_is_done_flag = identifyImage.wait_for_a_moment_and_click_template("invite_click_is_done.png", 2, 0.85)
    if not invite_click_is_done_flag:
        # 如果出现异常，直接点击X退出到探索主界面，重新选择章节再邀请一次。
        catch_invite_main_account_error(chapter)
    # 疯狂邀请至大号进来为止
    while True:
        # 点击邀请
        identifyImage.wait_for_a_moment_and_click_template("invite_button.png", 1, 0.85)
        # 接受队长邀请
        accept_invite_from_captain(omyuji_hwnd_info)
        # 判断大号是否进入
        success_flag = identifyImage.look_for_template_for_a_moment_return_boolean("experience_move_left.png", 9, 0.85)
        if success_flag:
            return


# 接受队长的邀请，仅接受，并切回队长号，不判断是否成功进入
def accept_invite_from_captain(omyuji_hwnd_info):
    # 切换大号接受
    windowTools.switch_window(list(omyuji_hwnd_info.keys())[0])
    accept_xiaohao_invite = "accept_xiaohao_invite.png"
    for i in range(10):
        # 检测小号邀请信息，点击对号
        xiaohao_invite_coordinate = identifyImage. \
            identify_find_template_or_not(accept_xiaohao_invite, 0.85)
        if xiaohao_invite_coordinate:
            # 如果找到默认邀请了，仅点击对号接受邀请
            if identifyImage.look_for_template_for_a_moment_return_boolean("continuous_invited_flag.png", 3, 0.85):
                mouse_click(xiaohao_invite_coordinate['x'] - 170, xiaohao_invite_coordinate['y'] + 10)
                print("检测到小号发来的默认邀请，仅点击对号接受本次邀请")
                time.sleep(0.2)
                break
            # 如果没找到默认邀请的标志，那么就是普通邀请
            mouse_click(xiaohao_invite_coordinate['x'] - 95,
                        xiaohao_invite_coordinate['y'] + 10)
            time.sleep(0.2)
            print("检测到小号发来的普通邀请，点击对号接受本次邀请")
            break
    # 切换队长号继续流程
    windowTools.switch_window(list(omyuji_hwnd_info.keys())[1])

# 邀请出现失败时，重新尝试走一遍探索邀请流程
def catch_invite_main_account_error(chapter):
    # 点2次是因为第一次有邀请界面，点X会首先退出邀请界面
    identifyImage.look_for_template_to_click("breakthrough_union_close.png", 1, 0.75)
    identifyImage.look_for_template_to_click("breakthrough_union_close.png", 1, 0.75)
    experience.choose_the_latest_chapter(chapter)