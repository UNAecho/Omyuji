from time import sleep
from tasks.tools import identifyImg
from tasks.tools import hwndInfo
from tasks.tools import windowTools
from tasks.tools import readContentOfScreen
from tasks.tools.operation import mouse_click
from tasks.tools import fight


def start_to_battle_every_30_min(template_path):
    omyuji_hwnd_info = hwndInfo.getHwndInfo()
    omyuji_hwnd_array = list(omyuji_hwnd_info.keys())
    windowTools.switch_window(omyuji_hwnd_array[0])
    while True:
        sleep(1)
        # 读取体力
        phycial_power = readContentOfScreen.read_number_of_screen(
            r"D:\PyCharm 2018.3.4\workspace\Omyuji\screenshot_temp\breakthrough_ticket.png", 1020, 46, 81, 22)
        if int(phycial_power) <= 100:
            # 关闭居酒屋
            identifyImg.wait_for_a_moment_and_click_template(
                r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\common_close_button.png", 5, 0.7)
            sleep(1)
            # 打开澡堂
            identifyImg.wait_for_a_moment_and_click_template(
                r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\festival_bashroom.png", 5, 0.8)
            sleep(1)
            # 泡澡
            identifyImg.wait_for_a_moment_and_click_template(
                r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\festival_bash.png", 5, 0.8)
            sleep(1)
            # 关闭澡堂
            identifyImg.wait_for_a_moment_and_click_template(
                r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\common_close_button.png", 5, 0.8)
            sleep(1)
            # 打开居酒屋
            identifyImg.wait_for_a_moment_and_click_template(
                r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\fastive_bar.png", 5, 0.8)
            sleep(1)
        # 继续打居酒屋
        identifyImg.wait_for_a_moment_and_click_template(
            r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\fastive_battle_button.png", 5, 0.8)
        fight.fight(r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\fastive_battle_button.png")
        sleep(3)


# start_to_battle_every_30_min("quanyecha_team_button.png")


def city_of_sun():
    # 点日轮之城活动主界面
    identifyImg.look_for_template_to_click("sun_index.png", 0.85)
    # 10秒内等轮回秘境
    identifyImg.wait_for_a_moment_and_click_template("lun_hui_mi_jing.png", 10, 0.85)
    # 等待出现轮回重置按钮出现，代表页面读取完毕
    if identifyImg.look_for_template_for_a_moment_return_boolean("reset_lunhui.png", 10, 0.85):
        # 开始打秘境大循环
        while True:
            print("开始外层大循环,缓冲几秒")
            sleep(1)
            print("开始读取每一格坐标")
            battle_list = identifyImg.multi_template_coordinate("cityofsun.png", 0.9)
            # 开始读取每个板块坐标
            # 逻辑：优先看资源格子、下一层，如果什么都没发现就开始正常翻格子遍历
            # 下面的遍历是以每个板块坐标为单位
            for i in battle_list:
                sleep(0.5)
                # 如果有资源选取意愿，先点击御魂资源
                resources_button = identifyImg.identify_find_template_or_not("lunhuimijing_yuhun_ziyuan.png", 0.85)
                if resources_button:
                    mouse_click(resources_button['x'],resources_button['y'])
                    identifyImg.wait_for_a_moment_and_click_template("common_confirm.png",3,0.85)
                # 先看有没有宝箱
                box = identifyImg.multi_template_coordinate("lunhuimijing_box.png", 0.85)
                if box:
                    count =box.__len__()
                    print("有宝箱，拾取%d个宝箱" %count)
                    for j in box:
                        mouse_click(j[0], j[1])
                        # 等待箱子开完，点击屏幕取消掉奖励
                        identifyImg.wait_for_a_moment_and_click_template("battle_win_continue.png", 5, 0.85)
                        # 判断是否取消掉屏幕，如果没有，直接点到看不到达摩弹出的金币奖励图标为止
                        while identifyImg.identify_find_template_or_not("money_ico.png",0.9):
                            print("持续点击到没有金币为止")
                            identifyImg.look_for_template_to_click("battle_win_continue.png",0.85)
                # 再看有没有时曲碎片
                shiqusuipian = identifyImg.multi_template_coordinate("lunhuimijing_shiqusuipian.png", 0.9)
                if shiqusuipian:
                    count = shiqusuipian.__len__()
                    print("有碎片，拾取%d个碎片"%count)
                    for k in shiqusuipian:
                        mouse_click(k[0], k[1])
                        sleep(1)
                # 再看有没有下一层
                sleep(0.5)
                next_floor = identifyImg.identify_find_template_or_not("lunhuimijing_next_floor.png", 0.85)
                if next_floor:
                    print("发现下一层了，直接进入下一层")
                    mouse_click(next_floor['x'], next_floor['y'])
                    # 点击下一层的时候有2种情况
                    # 第一种是第一次点击，出现BOSS战斗界面
                    sleep(1)
                    boss_battle_button = identifyImg.identify_find_template_or_not("lunhuimijing_start_battle.png", 0.85)
                    if boss_battle_button:
                        mouse_click(boss_battle_button['x'], boss_battle_button['y'])
                        fight.fight("reset_lunhui.png")
                        print("打完下一层BOSS了，等待2秒缓冲去下一层")
                        sleep(2)
                    # 第二种是打完boss了，弹出是否进入下一层，会现common的确定按钮，直接点击进入下一层
                    common_confirm_button = identifyImg.identify_find_template_or_not("common_confirm_button.png", 0.85)
                    if common_confirm_button:
                        mouse_click(common_confirm_button['x'], common_confirm_button['y'])
                        continue

                # 如果特殊资源格子都没发现，那么就开始正常点击每个板块翻
                mouse_click(i[0], i[1])
                sleep(0.3)
                # 找单人挑战的按钮
                start_battle_button_cd = identifyImg.identify_find_template_or_not("lunhuimijing_start_battle.png",
                                                                                   0.85)
                if start_battle_button_cd:
                    mouse_click(start_battle_button_cd['x'], start_battle_button_cd['y'])
                    fight.fight("reset_lunhui.png")
                else:
                    continue

city_of_sun()