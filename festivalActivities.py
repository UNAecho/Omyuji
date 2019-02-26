import time
from tasks.tools import identifyImage
from tasks.tools import hwndInfo
from tasks.tools import windowTools
from tasks.tools import operation
import win32api


def start_to_battle_every_30_min(template_path):
    omyuji_hwnd_info = hwndInfo.getHwndInfo()
    omyuji_hwnd_array = list(omyuji_hwnd_info.keys())
    while True:
        for i in omyuji_hwnd_array:
            windowTools.switch_window(i)
            if identifyImage.identify_find_template_or_not("money_ico.png", 0.8):
                identifyImage.m_c_eye(131, 451)
                # 检查是否回了庭院
                main_menu_boolean = identifyImage.look_for_template_for_a_moment_return_boolean("main_menu_team_button.png", 10, 0.8)
                while not main_menu_boolean:
                    identifyImage.m_c_eye(131, 451)
            identifyImage.wait_for_a_moment_and_click_template("main_menu_team_button.png", 1, 0.8)
            identifyImage.wait_for_a_moment_and_click_template(template_path, 2, 0.8)
            time.sleep(1)
            coordinate = identifyImage.identify_find_template_or_not("automatic_matching.png", 0.8)
            if coordinate:
                identifyImage.m_c_eye(coordinate['x'], coordinate['y'])
        time.sleep(60)


start_to_battle_every_30_min("quanyecha_team_button.png")
