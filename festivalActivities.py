import time
from tasks.tools import identifyImg
from tasks.tools import hwndInfo
from tasks.tools import windowTools
from tasks.tools import readContentOfScreen
from tasks.tools import operation
from tasks.tools import fight

def start_to_battle_every_30_min(template_path):
    omyuji_hwnd_info = hwndInfo.getHwndInfo()
    omyuji_hwnd_array = list(omyuji_hwnd_info.keys())
    windowTools.switch_window(omyuji_hwnd_array[0])
    while True:
        time.sleep(1)
        # 读取体力
        phycial_power = readContentOfScreen.read_number_of_screen(r"D:\PyCharm 2018.3.4\workspace\Omyuji\screenshot_temp\breakthrough_ticket.png",1020,46,81,22)
        if int(phycial_power) <= 100:
            # 关闭居酒屋
            identifyImg.wait_for_a_moment_and_click_template(r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\common_close_button.png",5,0.7)
            time.sleep(1)
            # 打开澡堂
            identifyImg.wait_for_a_moment_and_click_template(r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\festival_bashroom.png",5,0.8)
            time.sleep(1)
            # 泡澡
            identifyImg.wait_for_a_moment_and_click_template(r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\festival_bash.png",5,0.8)
            time.sleep(1)
            # 关闭澡堂
            identifyImg.wait_for_a_moment_and_click_template(r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\common_close_button.png",5,0.8)
            time.sleep(1)
            # 打开居酒屋
            identifyImg.wait_for_a_moment_and_click_template(r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\fastive_bar.png",5,0.8)
            time.sleep(1)
        # 继续打居酒屋
        identifyImg.wait_for_a_moment_and_click_template(r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\fastive_battle_button.png", 5, 0.8)
        fight.fight(r"D:\PyCharm 2018.3.4\workspace\Omyuji\omyuji_ico\fastive_battle_button.png")
        time.sleep(3)


start_to_battle_every_30_min("quanyecha_team_button.png")
