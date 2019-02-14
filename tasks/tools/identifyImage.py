import random
import time

import cv2 as opencv
import numpy as np
from PIL import ImageGrab
from tasks.tools import hwndInfo
from tasks.tools.operation import mouse_click
from tasks.repository import templateEntity

# 获取窗口信息
omyuji_hwnd_info = hwndInfo.getHwndInfo()
omyuji_hwnd_array = list(omyuji_hwnd_info.keys())
# 目前多开窗口暂时叠加，等到窗口不叠加时使用
# if omyuji_hwnd_array.__len__() == 1:
#     window_info_dict = omyuji_hwnd_info[omyuji_hwnd_array[0]]
#     # 仅供PIL的ImageGrab.grab()所使用，为了截屏到内存，该参数仅支持元祖形式
#     window_info_tuple = tuple(window_info_dict.values())
window_info_dict = omyuji_hwnd_info[omyuji_hwnd_array[0]]
window_info_tuple = tuple(window_info_dict.values())


# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()


# threshold:阈值，越接近1，匹配度要求越高。
def identify_template_click(template_file_name, template_imread,threshold):
    identify_result = False
    false_count = 0
    while not identify_result:
        identify_coordinates = identify_find_template_or_not(template_file_name, threshold)
        if identify_coordinates.__len__() > 0:
            identify_result = True
            # print("点击坐标：x ：" + str(identify_coordinates['x']) +" y ：" +
            # str(identify_coordinates['y']))
            mouse_click(identify_coordinates['x'], identify_coordinates['y'])
        else:
            false_count += 1
            time.sleep(1)
        if false_count > 7:
            print("点击识别出现6次失败，放弃点击")
            print("想要点的模板名称为 ：" + template_file_name)
            return
    return


# threshold:阈值，越接近1，匹配度要求越高。
def identify_find_template_or_not(template_file_name, threshold, custom_coordinate=None):

    # 返回找到的坐标值，调用方需要根据返回值点击
    result_coordinates = {}
    # 读取cv2所使用的BGR模板
    template_imread = template_cv2_entity[template_file_name]
    if custom_coordinate is None:
        screen = np.array(ImageGrab.grab(window_info_tuple))
    else:
        custom_locale = (window_info_tuple[0]+custom_coordinate[0],
                         window_info_tuple[1]+custom_coordinate[1],
                         window_info_tuple[2]+custom_coordinate[2],
                         window_info_tuple[3]+custom_coordinate[3]
                         )
        screen = np.array(ImageGrab.grab(custom_locale))
    img_bgr = opencv.cvtColor(screen, opencv.COLOR_RGB2BGR)
    gray_img_for_cv2 = opencv.cvtColor(img_bgr, opencv.COLOR_BGR2GRAY)

    match_res = opencv.matchTemplate(gray_img_for_cv2, template_imread, opencv.TM_CCOEFF_NORMED)

    try:
        loc = np.where(match_res >= threshold)
        for pt in zip(*loc[::-1]):
            gps = pt
        # loc中为匹配处左上角位置，正常会加一点点偏移量以保证点到图片中间
            result_coordinates['x'] = gps[0] + random.randint(5, 20) + window_info_dict['window_x_left']
            result_coordinates['y'] = gps[1] + random.randint(5, 20) + window_info_dict['window_y_top']
    except UnboundLocalError:
        print("寻找模板出错了，推测为没找到，想要找的模板为： " + template_file_name)
        result_coordinates = {}

    return result_coordinates


# threshold:阈值，越接近1，匹配度要求越高。
# x/y：偏移量，用于修正点击位置
def look_for_template_to_click(template_file_name, threshold, x=None, y=None):
    try_count = 0
    while try_count < 10:
        time.sleep(0.5)
        identify_template_coordinate = identify_find_template_or_not(template_file_name, threshold)
        if identify_template_coordinate.__len__() > 0:
            print("找到模板了，x："+str(identify_template_coordinate['x']) +
                  "，y："+str(identify_template_coordinate['y']))
            mouse_click(identify_template_coordinate['x']+x,
                        identify_template_coordinate['y']+y)
            break
        else:
            try_count += 1
            print("没找到模板：" + template_file_name +
                  "当前点击：" + str(try_count) + " 次，再点" + str(10-try_count) + " 次，就不点了")
    time.sleep(0.3)
    return


# 等待断线重连
def wait_for_connecting():
    while True:
        coordinate = identify_find_template_or_not("connecting.png", 0.85)
        if coordinate:
            print("断线了，等待2秒重连")
            time.sleep(2)
        else:
            break


# 观察一阵子模板是否出现
# waitting_time:等待时间，单位为秒
def look_for_template_for_a_moment_return_boolean(template_file_name, waitting_time, threshold):
    return_result = False
    time_sum = 0
    while time_sum < waitting_time:
        coordinate = identify_find_template_or_not(template_file_name, threshold)
        if coordinate:
            print("观察到模板"+template_file_name+"了，返回True")
            return_result = True
            break
        else:
            time.sleep(0.5)
            time_sum += 0.5
    # print("观察 "+str(waitting_time) + "秒后，是否找到模板" + template_file_name+"：" + str(return_result))
    return return_result


# 观察一阵子模板是否出现，并点击
# waitting_time:等待时间，单位为秒
def wait_for_a_moment_and_click_template(template_file_name, waitting_time, threshold):
    return_result = False
    time_sum = 0
    while time_sum < waitting_time:
        coordinate = identify_find_template_or_not(template_file_name, threshold)
        if coordinate:
            print("观察到模板"+template_file_name+"了，开始点击")
            mouse_click(coordinate['x'], coordinate['y'])
            return_result = True
            break
        else:
            time.sleep(0.5)
            time_sum += 0.5
    return return_result
