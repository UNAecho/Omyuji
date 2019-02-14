import random
import time
import win32api
import win32con

from tasks import yuling
from tasks.repository import templateEntity
from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools import fight
from tasks.tools import identifyImage
from tasks.tools import readContentOfScreen
from tasks.tools import windowTools
from tasks.tools.operation import mouse_click, mouse_move

# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()


def switch_on_buffer(type):
    while True:
        print("switch_on_buffer()尝试寻找加成灯笼图标")
        # 如果看到有寮突的关闭按键，点击关闭后再找灯笼
        identifyImage.look_for_template_to_click("breakthrough__union_close.png", 0.5, 0, 0)
        # 点击加成按钮
        buffer_button_explore_filename = "buffer_button_explore.png"
        buffer_button_coordinate = identifyImage.identify_find_template_or_not(buffer_button_explore_filename, 0.85)
        if buffer_button_coordinate.__len__() > 0:
            # 如果找到加成灯笼的坐标，点击之后检查觉醒图标是否出现
            mouse_click(buffer_button_coordinate['x'], buffer_button_coordinate['y'])
            whether_page_of_buffer_is_available = check_whether_page_of_buffer_is_available()
            if whether_page_of_buffer_is_available:
                break
        time.sleep(0.5)
    # 选择要点击的buffer
    if type == "yuhun":
        yuhun_buffer_filename = "yuhun_buffer.png"
        yuhun_buffer_button_coordinate = identifyImage.identify_find_template_or_not(yuhun_buffer_filename, 0.85)
        time.sleep(0.8)
        if yuhun_buffer_button_coordinate.__len__() > 0:
            # 在坐标后面加上数字修正是为了点击buffer按钮，模板返回的坐标为模板左上角那一点
            mouse_click(yuhun_buffer_button_coordinate['x'] + 105, yuhun_buffer_button_coordinate['y'] + 3)
            time.sleep(1)
    elif type == "experience":
        experience_buffer_filename = "experience_buffer.png"
        experience_buffer_button_coordinate = identifyImage.identify_find_template_or_not(experience_buffer_filename, 0.85)
        time.sleep(0.8)
        if experience_buffer_button_coordinate.__len__() > 0:
            # +100和+5是为了点击buffer按钮，模板返回的坐标为模板左上角那一点
            mouse_click(experience_buffer_button_coordinate['x'] + 105, experience_buffer_button_coordinate['y'] + 3)
            time.sleep(1)
    # 点击加成按钮关闭buffer页面
    mouse_click(buffer_button_coordinate['x'], buffer_button_coordinate['y'])
    time.sleep(0.8)


# 关闭全部开启的buffer
# 当前无法识别关掉是哪个buffer，只能看到哪个开启就关闭哪个
def switch_off_all_of_buffer():
    print("进入switch_off_all_of_buffer()方法")
    while True:
        print("尝试寻找加成灯笼图标")
        # 点击加成按钮
        buffer_button_explore_filename = "buffer_button_explore.png"
        buffer_button_coordinate = identifyImage.identify_find_template_or_not(buffer_button_explore_filename, 0.85)
        if buffer_button_coordinate.__len__() > 0:
            # 如果找到加成灯笼的坐标，点击之后检查觉醒图标是否出现
            mouse_click(buffer_button_coordinate['x'], buffer_button_coordinate['y'])
            whether_page_of_buffer_is_available = check_whether_page_of_buffer_is_available()
            if whether_page_of_buffer_is_available:
                break
        time.sleep(0.5)
    buffer_on_filename = "buffer_on_little.png"
    # 截图判别模板次数
    try_to_identify_count = 0
    # 关掉的buffer数量计数
    count = 0
    # 执行try_to_identify_count数量的高频循环检查
    while try_to_identify_count < 50:
        # 检测回数+1
        try_to_identify_count += 1
        buffer_on_coordinate = identifyImage.identify_find_template_or_not(buffer_on_filename, 0.95)
        time.sleep(0.2)
        if buffer_on_coordinate.__len__() > 0:
            # 在坐标后面加上数字修正是为了点击buffer按钮，模板返回的坐标为模板左上角那一点
            mouse_click(buffer_on_coordinate['x'],
                        buffer_on_coordinate['y'])
            # 关掉1个buffer之后，重置检测回数，可以将误开启的buffer再次关闭
            try_to_identify_count = 0
            count += 1
            print("关完 "+str(count)+" 个")
    print("已关完全部buffer，退出switch_off_buffer()")
    # 点击加成按钮关闭buffer页面
    mouse_click(buffer_button_coordinate['x'], buffer_button_coordinate['y'])
    time.sleep(0.8)

def check_whether_page_of_buffer_is_available():
    time.sleep(0.5)
    # 点击加成灯笼之后，判断觉醒buffer图标是否出现，来判断是否点开了加成页面。如果不出现，则重复点击加成灯笼直至出现
    awakening_buffer_filename = "awakening_buffer.png"
    buffer_button_coordinate = identifyImage.identify_find_template_or_not(awakening_buffer_filename, 0.85)
    if buffer_button_coordinate.__len__() > 0:
        print("检测到觉醒图标，证明加成页面已弹出，返回True")
        return True
    else:
        print("没找到觉醒图标，页面没有弹出，返回False")
        return False