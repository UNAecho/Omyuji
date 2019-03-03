from tasks.tools import identifyImg
from tasks.tools.operation import mouse_drag_to_target
import time

# 选择式神，返回式神的等级坐标
def select_shikigami():
    # 点击【全部】按钮，挑选式神的稀有度
    if identifyImg.look_for_template_to_click("common_rare_button.png", 0.75):
        print("找到全部按钮，开始点击选择目标稀有度")
        time.sleep(1.5)
        # 选择N卡狗粮
        identifyImg.wait_for_a_moment_and_click_template("common_rare_N.png", 3, 0.8)
        print("选择N卡狗粮")
    # 开始拖拽滑块，直至出现目标
    while True:
        # 首先寻找滑块位置
        slider_coordinae = identifyImg.identify_find_template_or_not("slider.png", 0.8)
        # 如果没找到滑块，程序应该是出错了，那么退出寄养
        if slider_coordinae.__len__() == 0:
            print("没找到滑块，程序可能出错了")
            break
        # 滑块坐标
        x = slider_coordinae['x']
        y = slider_coordinae['y']
        # 每次小幅度平移64个单位
        mouse_drag_to_target(x, y, x + 32, y)
        # 直至出现目标才停下
        shikigami_level_coordinate = identifyImg.identify_find_template_or_not("level_1.png", 0.9)
        if shikigami_level_coordinate:
            return shikigami_level_coordinate
        levle_max = identifyImg.identify_find_template_or_not("level_max.png", 0.8)
        if levle_max:
            print("已经没有要寄养的目标了，推测为N卡被吃光了")
            # 用x轴坐标为0代表N卡被吃光
            return {'x': 0}
