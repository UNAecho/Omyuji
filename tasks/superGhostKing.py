import random
import time
from datetime import datetime

from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools.fight import fight
from tasks.tools.pressBattleButton import choose_floor_and_start_battle
from tasks.tools.operation import mouse_click, key_input
from tasks.tools import identifyImage
from tasks.tools import screenshot
import pytesseract
from PIL import Image
from tasks.tools import windowTools


def read_number_of_physical_power_remaining():
    screenshot.getScreenshot('D:\\win32Screenshot\\physical_power.bmp', Coordinate.physical_power_value_x_left,
                  Coordinate.physical_power_value_y_top, 86, 21)
    read_screen_text = pytesseract.image_to_string(Image.open('D:\\win32Screenshot\\physical_power.bmp'))
    if read_screen_text is None:
        print("没读出来，什么破玩意")
    number_of_physical_power = str(read_screen_text).strip(" ").split("/")[0]
    return number_of_physical_power


while True:
    time.sleep(1)
    windowTools.move_window_to_0_0()
    mouse_click(random.randint(570,578),random.randint(311, 318))
    time.sleep(1)

    try_find_tuizhi_button_count = 0
    whether_tiaozhan_buttion = {}
    while try_find_tuizhi_button_count < 3:
        if try_find_tuizhi_button_count == 0:
            try_find_tuizhi_button_count += 1
            mouse_click(random.randint(367, 400), random.randint(296, 331))
            whether_tiaozhan_buttion = identifyImage.identify_find_template_or_not(
                "D:\\omyuji_ico\\tuizhi_superGhost_King.png", 0.5)
            if whether_tiaozhan_buttion.__len__() > 0:
                break
        elif try_find_tuizhi_button_count == 1:
            try_find_tuizhi_button_count += 1
            mouse_click(random.randint(367, 400), random.randint(400, 420))
            whether_tiaozhan_buttion = identifyImage.identify_find_template_or_not(
                "D:\\omyuji_ico\\tuizhi_superGhost_King.png", 0.5)
            if whether_tiaozhan_buttion.__len__() > 0:
                break
        else:
            try_find_tuizhi_button_count += 1
            mouse_click(random.randint(367, 400), random.randint(562, 570))
            whether_tiaozhan_buttion = identifyImage.identify_find_template_or_not(
                "D:\\omyuji_ico\\tuizhi_superGhost_King.png", 0.5)
            if whether_tiaozhan_buttion.__len__() > 0:
                break

    if whether_tiaozhan_buttion.__len__() > 0:
        physical_power = int(read_number_of_physical_power_remaining())
        if 0 <= physical_power <= 90:
            identifyImage.identify_template_click("D:\\omyuji_ico\\tuizhi_superGhost_King.png", 0.8)
            fight()
        else:
            time.sleep(300)
    else:
        identifyImage.identify_template_click("D:\\omyuji_ico\\back_button_blue.png", 0.7)
    time.sleep(5)
