import random
import time
import win32api
import win32con
import sys
from tasks.tools import observerTools
from tasks import yuling
from tasks.repository import templateEntity
from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools import fight
from tasks.tools import bufferTools
from tasks.tools import identifyImg
from tasks.tools import readContentOfScreen
from tasks.tools import windowTools
from tasks.tools.operation import mouse_click, mouse_move
from tasks.tools import OsUtils

# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()


def start_to_breakthrough(breakthrough_type, mode):
    if breakthrough_type == "personal":
        breakthrough_personal(mode)
        return True
    else:
        return_flag = breakthrough_union(mode)
        return return_flag


# mode代表在哪项任务中穿插打突破，如：狗粮中打个突，魂十、御灵中打个突
def breakthrough_personal(mode):
    time.sleep(0.5)
    print("开始进行个人突破")
    mouse_click(random.randint(Coordinate.breakthrough_x_left, Coordinate.breakthrough_x_right),
                random.randint(Coordinate.breakthrough_y_top, Coordinate.breakthrough_y_bottom))
    time.sleep(1)
    # 标记当前玩家是否被攻破
    battle_status = False
    # 开始个突大循环，一直到票为0之后才break
    while True:
        print("个突开始，首先读取剩余票数")
        breakthrough_personal_ticket = readContentOfScreen.read_number_of_screen(
            'screenshot_temp\\breakthrough_ticket.png',
            Coordinate.breakthrough_personal_ticket_x_left,
            Coordinate.breakthrough_personal_ticket_y_top,
            72, 26)
        print("突破票还有：" + breakthrough_personal_ticket + "张")
        # 突破票大于0再打突破
        if int(breakthrough_personal_ticket) > 0:
            # 从1号玩家打到9号玩家
            for i in range(1, 10):
                # 重置判断玩家是否被攻破计数
                whether_battle_count = 0
                print("开始打第" + str(i) + "号玩家")
                while True:
                    # 判断如果被攻破，则去打下一个人，并将下一个人Flag标为False，防止一下全部跳过去
                    if battle_status:
                        battle_status = False
                        # print("将当前第" + str(i) + "号玩家被击破Flag设置为False")
                        break
                    if whether_battle_count < 2:
                        try:
                            print("开始读取剩余突破票数量,当前目标是第" + str(i) + "号玩家")
                            breakthrough_personal_ticket = readContentOfScreen.read_number_of_screen(
                                'screenshot_temp\\breakthrough_ticket.png',
                                Coordinate.breakthrough_personal_ticket_x_left,
                                Coordinate.breakthrough_personal_ticket_y_top,
                                72, 26)
                            print("突破票还有：" + breakthrough_personal_ticket + "张")
                        except Exception as e:
                            print("error! errormessage is : " + str(e))
                            breakthrough_personal_ticket = "0"
                        time.sleep(1)
                        if abs(int(breakthrough_personal_ticket)) > 0:
                            # 点完任务之后是否有战斗按钮弹出，如果有则正常打，如果超过2次没有弹出，则证明该人物已经被突破
                            battle_false_count = 0
                            while True:
                                if whether_battle_count > 2:
                                    print("点了2次没反应，应该是打完了，那么打下一个人")
                                    break
                                if battle_false_count < 2:
                                    breakthrough_personal_info = Coordinate.breakthrough_personal_info[i]
                                    mouse_click(breakthrough_personal_info['x'], breakthrough_personal_info['y'])
                                    time.sleep(1)
                                    attack_button_filename = "attack.png"
                                    whether_battle = identifyImg.identify_find_template_or_not(
                                        attack_button_filename, 0.85)
                                    if whether_battle.__len__() > 0:
                                        try:
                                            identifyImg.identify_template_click(
                                                attack_button_filename, template_cv2_entity[attack_button_filename], 0.85)
                                        except Exception:
                                            break
                                        battle_result = fight.fight("personal_breakthrough_flag.png")
                                        if battle_result and i % 3 == 0:
                                            time.sleep(0.5)
                                            for j in range(6):
                                                mouse_click(random.randint(Coordinate.breakthrough_personal_reward_x_left,
                                                                           Coordinate.breakthrough_personal_reward_x_right),
                                                            random.randint(Coordinate.breakthrough_personal_reward_y_top,
                                                                           Coordinate.breakthrough_personal_reward_y_bottom)
                                                            )
                                                time.sleep(random.uniform(0.3, 0.8))
                                            battle_status = True
                                            break
                                        elif battle_result:
                                            time.sleep(2)
                                            battle_status = True
                                            break
                                        else:
                                            battle_false_count += 1
                                            print("个突失败了！失败统计次数 + 1 ，当前失败次数 ： " + str(battle_false_count))
                                            battle_status = False
                                    else:
                                        whether_battle_count += 1
                                        print("靠？打完了？我现在点了 " + str(whether_battle_count) + "次，再点 "
                                              + str(3 - whether_battle_count) + "次 ，再不行，就不打了")
                                else:
                                    print("打了2次都没打过，放弃殴打，准备2秒后刷新下一批倒霉孩子")
                                    time.sleep(2)
                                    mouse_click(random.randint(Coordinate.breakthrough_personal_refresh_x_left,
                                                               Coordinate.breakthrough_personal_refresh_x_right),
                                                random.randint(Coordinate.breakthrough_personal_refresh_y_top,
                                                               Coordinate.breakthrough_personal_refresh_y_bottom)
                                                )
                                    time.sleep(1)
                                    mouse_click(random.randint(Coordinate.breakthrough_personal_refresh_confirm_x_left,
                                                               Coordinate.breakthrough_personal_refresh_confirm_x_right),
                                                random.randint(Coordinate.breakthrough_personal_refresh_confirm_y_top,
                                                               Coordinate.breakthrough_personal_refresh_confirm_y_bottom)
                                                )
                                    time.sleep(0.5)
                                    break
                        else:
                            return
                    else:
                        break
        else:
            #如果突破票小于0，退出个突最外层大循环
            break
    if mode == "yuhun":
        # 首先点击个人选项卡，重置当前页面，防止卡在某一个弹出界面上
        for i in range(3):
            mouse_click(random.randint(Coordinate.breakthrough_personal_x_left,
                                       Coordinate.breakthrough_personal_x_right),
                        random.randint(Coordinate.breakthrough_personal_y_top,
                                       Coordinate.breakthrough_personal_y_bottom))
            time.sleep(1.5)
        # 退出突破X键
        identifyImg.look_for_template_to_click("common_close_button.png", 0.5, 0, 0)
        return
    elif mode == "yuling":
        yuling.start_choose_yuling_to_attack()
    elif mode == "infinite_union":
        # 点击个人突破选项卡，为了在外层使用BackToIndex()方法退出任务
        for i in range(3):
            mouse_click(random.randint(Coordinate.breakthrough_personal_x_left,
                                       Coordinate.breakthrough_personal_x_right),
                        random.randint(Coordinate.breakthrough_personal_y_top,
                                       Coordinate.breakthrough_personal_y_bottom))
        # 退出突破X键
        identifyImg.look_for_template_to_click("common_close_button.png", 0.5, 0, 0)
        time.sleep(1)
    else:
        print("personal_breakthrough()方法的mode参数未定义，继续进行退出流程")
    time.sleep(0.5)
    print("本次breakthrough_personal()循环结束")
    return


# mode代表在哪项任务中穿插打寮突，如：狗粮中打寮突，魂十、御灵中打寮突
def breakthrough_union(mode):
    # 定义寮突破是否还可以继续打的Flag，这是一个返回值。True为可以（未攻破），False为不可以再打（已攻破）
    whether_breakthrough_is_available = True
    print("开始进行寮突破")
    time.sleep(1.5)
    mouse_click(random.randint(Coordinate.breakthrough_x_left, Coordinate.breakthrough_x_right),
                random.randint(Coordinate.breakthrough_y_top, Coordinate.breakthrough_y_bottom))
    time.sleep(1.5)
    mouse_click(random.randint(Coordinate.breakthrough_union_x_left, Coordinate.breakthrough_union_x_right),
                random.randint(Coordinate.breakthrough_union_y_top, Coordinate.breakthrough_union_y_bottom))
    time.sleep(1.5)
    whether_start = check_whether_start()

    # 点完勋章之后是否有战斗按钮弹出，如果有则正常打，如果超过2次没有弹出，则证明该人物已经被突破
    whether_battle_count = 0
    if whether_start:
        print("寮突开了，开始寮突循环")
        # 战斗失败次数统计
        battle_false_count = 0
        while True:
            if whether_battle_count > 2:
                print("点了2次发现没弹出战斗按钮，推测该人物已被攻破，开始判断是否整个寮突都打完了")
                # 判断寮突破是否被100%攻破了，如是，返回False（表示不可以再打了）
                check_breakthrough_availabe_filename = "check_breakthrough_availabe.png"
                check_breakthrough_availabe_corrdinate = identifyImg.identify_find_template_or_not(
                    check_breakthrough_availabe_filename, 0.85
                )
                if check_breakthrough_availabe_corrdinate.__len__() > 0:
                    whether_breakthrough_is_available = False
                break
            read_attack_remaining = readContentOfScreen.read_number_of_screen('screenshot_temp\\union.bmp',
                                                                              Coordinate.breakthrough_union_attack_remaining_x_left,
                                                                              Coordinate.breakthrough_union_attack_remaining_y_top, 56, 56)
            if read_attack_remaining.isdigit() is False:
                break
            print("剩余可攻击次数 ：" + read_attack_remaining + " 当前失败次数统计 ： " + str(battle_false_count))
            attack_count = int(read_attack_remaining)
            if attack_count > 0:
                if battle_false_count < 2:
                    # 开始点击勋章，或者空寻找槽位。优先打空勋章槽位，因为好打。
                    try:
                        if identifyImg.identify_find_template_or_not("medal-none.png",0.8):
                            identifyImg.identify_template_click("medal-none.png",template_cv2_entity["medal-none.png"],0.8)
                        else:
                            identifyImg.look_for_template_to_click("medal.png", template_cv2_entity["medal.png"], 0.75)
                    except Exception as e:
                        print("error! errormessage is : " + str(e))
                        break
                    time.sleep(1)
                    # 点击勋章之后如果没有弹出进攻，说明已攻破。
                    # 计算失败次数，如果超过3次，那么猜测可能为突破完毕，终止本次突破
                    whether_battle = identifyImg.identify_find_template_or_not("attack.png", 0.8)
                    if whether_battle.__len__() > 0:
                        try:
                            identifyImg.identify_template_click(
                                "attack.png", template_cv2_entity["attack.png"], 0.75)
                        except Exception:
                            break
                        battle_result = fight.fight("union_breakthrough_flag.png")
                        if battle_result:
                            battle_false_count = 0
                        else:
                            battle_false_count += 1
                            print("寮突失败了！失败统计次数 + 1 ，当前失败次数 ： " + str(battle_false_count))
                    else:
                        whether_battle_count += 1
                        print("靠？打完了？我现在点了 " + str(whether_battle_count) + "次，再点 "
                              + str(3 - whether_battle_count) + "次 ，再不行，就不打了")
                else:
                    # 勋章ico，打人失败两次后，将鼠标移动到任意一个勋章位置，为了使接下来的滚轮操作生效。
                    # 不然如果鼠标处于界面外，滚轮动作将无法完成
                    medal_filename = "medal.png"
                    medal_file_coordinateindex = identifyImg.identify_find_template_or_not(
                        medal_filename, 0.75)
                    if medal_file_coordinateindex.__len__() > 0:
                        mouse_move(medal_file_coordinateindex['x'],
                                   medal_file_coordinateindex['y'])
                    # 如果失败了2次还没打过，那么鼠标滚轮往下滚一点，打别人。
                    # win32con.MOUSEEVENTF_WHEEL代表鼠标中轮，第四个参数正数代表往上轮滚，负数代表往下
                    for i in range(4):
                        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -128)
                        time.sleep(0.3)
                    battle_false_count = 0
            else:
                break
    else:
        print("会长副会真懒，都 "+str(time.localtime().tm_hour)+" 点了还没开寮突")
    # 开始退出寮突破
    # 首先点击个人选项卡，重置当前页面，防止卡在某一个弹出界面上
    mouse_click(Coordinate.breakthrough_personal_x_left, Coordinate.breakthrough_personal_y_top)
    time.sleep(0.3)
    # 退出突破X键
    mouse_click(Coordinate.breakthrough_logout_x_left, Coordinate.breakthrough_logout_y_top)
    # 开始执行返回进入寮突破流程之前的界面
    if mode == "yuhun":
        # TODO
        return whether_breakthrough_is_available
    elif mode == "yuling":
        yuling.start_choose_yuling_to_attack()
    else:
        print("本次无限breakthrough_union()循环结束")
    time.sleep(0.5)
    return whether_breakthrough_is_available


def check_whether_start():
    return not identifyImg.look_for_template_for_a_moment_return_boolean("check_breakthrough_start.png", 2, 0.85)

def read_breakthrough_ticker_remaining(mode):
    print("读取个人突破票数，如果大于25，那么就开干")

    time.sleep(1)
    breakthrough_ticket_remaining = readContentOfScreen.read_number_of_screen(
                  'screenshot_temp\\breakthrough_ticket.png',
                  Coordinate.explore_number_of_breakthrough_ticker_x_left,
                  Coordinate.explore_number_of_breakthrough_ticker_y_top, 107, 24)
    if breakthrough_ticket_remaining > 25:
        breakthrough_personal(mode)
    return


def infinite_breakthrough_loop(type):
    if type =="personal":
        # 无限寮突模式，适用于周一和周三御魂比较差的时候。
        print("开始无限打个人突破")
        time.sleep(1)
        windowTools.move_window_to_0_0()
        fail_count = 0
        loop_number = 0
        while fail_count < 10 or loop_number < 10:
            try:
                start_to_breakthrough("personal", "")
                loop_number += 1
            except Exception as e:
                print("******* somewhere cause an error！********，errormessage ：" + str(e))
                fail_count += 1
                continue
            time.sleep(2)
    else:
        # 无限寮突模式，适用于周一和周三御魂比较差的时候。
        print("开始执行无限寮突模式")
        time.sleep(1)
        windowTools.move_window_to_0_0()
        # 无限寮突等待时间
        wait_time = 30
        while True:
            if identifyImg.identify_find_template_or_not("multi_login.png", 0.8):
                print("重复登陆，终止程序")
                break
            try:
                return_flag = start_to_breakthrough("union", "")
                print("本次无限寮突结束，尝试进行个突来最大化收益")
                # 在无限寮突之中插入一次个突，最大收益利用时间。
                start_to_breakthrough("personal", "infinite_union")
                print("本次个突结束，根据寮突是否被100%攻破来决定下一步做什么")
                # 如果发现寮被100%突破了就不要循环了
                if not return_flag:
                    print("寮突100%被攻破，结束无限循环")
                    break
            except Exception:
                continue
            print("寮突还未完全攻破，等待 %s 秒后继续" % wait_time)
            time.sleep(wait_time)
        OsUtils.shutdown_computer("sleep")


def AOP_for_breakthrough(omyuji_hwnd_info):
    # 首先判断大号结界突破票是否大于28，如是，则进入突破状态
    time.sleep(1)
    personal_breakthrough_ticket = observerTools.remaining_of_personal_breakthrough_ticket()
    print("当前突破票剩余：" + personal_breakthrough_ticket)
    if int(personal_breakthrough_ticket) > 28:
        # Sensitive operation!!!
        # 关buffer
        bufferTools.switch_off_all_of_buffer()

        print("突破票大于28张，开工了，个人突破")
        breakthrough_personal("yuhun")

        # Sensitive operation!!!
        # 开buffer
        bufferTools.switch_on_buffer("yuhun")
