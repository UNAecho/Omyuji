import random
import time
import win32api
import win32con
import win32gui

from tasks import yuling
from tasks.repository import templateEntity
from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools import fight
from tasks.tools import identifyImage
from tasks.tools import readContentOfScreen
from tasks.tools import windowTools
from tasks.tools.operation import mouse_click, mouse_move
from tasks import breakthrough
from tasks.tools import observerTools
from tasks.tools import invitationTask

# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()


def multi_player(omyuji_hwnd_info,config):
    # 点击探索
    # mouse_click(random.randint(Coordinate.explore_x_left,Coordinate.explore_x_left), random.randint(Coordinate.explore_y_top,Coordinate.explore_y_bottom))
    # time.sleep(3)

    battle_statistics_and_command(omyuji_hwnd_info, dict(config))


# 寻找指定章节，并点击进入
def choose_the_latest_chapter(chapter):
    # 鼠标选择指定章节，鼠标滚轮一直滚到看到指定章节的模板为止，并点击
    print("开始找最新章节，当前试图寻找 %d" % chapter + " 章")
    chapter_coordinate = identifyImage.identify_find_template_or_not("explore_choose_chapter.png", 0.85)
    if chapter_coordinate:
        mouse_move(chapter_coordinate['x'], chapter_coordinate['y'])
        time.sleep(1)
        while True:
            # 先找章节模板，找不到就滚动滚轮寻找
            aim_of_chapter_coordinate = identifyImage.identify_find_template_or_not("explore_chapter_%d.png" % chapter,
                                                                                    0.95)
            if aim_of_chapter_coordinate:
                # 点击指定章节
                mouse_click(aim_of_chapter_coordinate['x'], aim_of_chapter_coordinate['y'])
                # 等待屏幕移动出现选择难度及组队信息
                wait_for_explore_button = identifyImage.look_for_template_for_a_moment_return_boolean("common_button_explore.png", 3.5,
                                                                                                      0.85)
                # 看到屏幕出现等待信息后，判断是否点击了困难标志，否则无法组队
                if wait_for_explore_button:
                    hard_status_coordinate = identifyImage.identify_find_template_or_not("experience_hard.png",0.85)
                    # 如果看到了困难标志没有点上，点击
                    if hard_status_coordinate:
                        mouse_click(hard_status_coordinate['x'],hard_status_coordinate['y'])
                    # 点击组队，结束本方法
                    identifyImage.identify_template_click("common_button_creatteam.png",
                                                          template_cv2_entity["common_button_creatteam.png"], 0.85)
                    break
            # win32con.MOUSEEVENTF_WHEEL代表鼠标中轮，第四个参数正数代表往上轮滚，负数代表往下
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -128)
            time.sleep(0.3)
    return


def battle_statistics_and_command(omyuji_hwnd_info, config):
    # 解析要做的任务
    for key, value in config.items():
        # 要打的章节
        chapter = int(key)
        # 要刷的次数
        residue_number = value
    battle_count = 0
    win_count = 0

    # 寮突破是否可以继续打的Flag，True：可以打，False：不可以继续打了
    whether_breakthrough_is_available = True
    # 判断大号是否开始执行个人突破，突破票28张以上就开打
    windowTools.switch_window(list(omyuji_hwnd_info.keys())[0])
    # breakthrough.AOP_for_breakthrough(omyuji_hwnd_info)
    # 切回队长小号开始流程
    windowTools.switch_window(list(omyuji_hwnd_info.keys())[1])

    # 开始进入刷狗粮主流程，当前刷28章
    # 获取队长号窗口焦点
    win32gui.SetForegroundWindow(list(omyuji_hwnd_info.keys())[1])
    # 寻找指定章节，直至点击组队开始准备邀请收益号
    choose_the_latest_chapter(chapter)
    # 邀请收益号，直至进入刷狗粮界面，开始准备打怪主流程
    invitationTask.invite_main_account_experience(omyuji_hwnd_info, chapter)

    # 刷狗粮主流程
    while True:
        boss_flag = identifyImage.look_for_template_for_a_moment_return_boolean("boss_appear.png", 1, 0.65)
        if boss_flag:
            identifyImage.wait_for_a_moment_and_click_template("boss.png", 5, 0.85)
            fight.fight_for_experience(omyuji_hwnd_info)
