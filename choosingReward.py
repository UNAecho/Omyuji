import time
import datetime
import schedule
import sys

from tasks.repository import templateEntity
from tasks.tools import identifyImg
from tasks.tools.operation import mouse_click

# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()


def choose_reward_by_time():
    # 先找悬赏封印的【封印】二字，返回坐标
    reward_invite_filename = "reward_invite.png"
    reward_invite_coordinate = identifyImg.identify_find_template_or_not(reward_invite_filename, 0.7)
    if reward_invite_coordinate.__len__() > 0:

        reward_refuse_filename = "reward_refuse.png"
        reward_refuse_coordinate = identifyImg.identify_find_template_or_not(reward_refuse_filename, 0.85)
        if reward_refuse_coordinate.__len__() > 0:
            # 如果过了18点，或者当天是周末，就接受悬赏，由于接受按钮在拒绝按钮上面，为了优化性能，将拒绝按钮y轴坐标减去86代表接受按钮坐标
            if time.localtime().tm_hour > 17 or datetime.datetime.now().weekday() > 4:
                mouse_click(reward_refuse_coordinate['x'], reward_refuse_coordinate['y'] - 86)
                print("晚上6点以后开始接客啦！")
            else:
                # 拒绝是点击关闭按钮，而非点X拒绝，这样邀请人无感知，不然秒拒绝会被当作是外挂
                mouse_click(reward_refuse_coordinate['x'] - 58, reward_refuse_coordinate['y'] - 327)
                print("有人邀请，立即点关闭并无视邀请，没有犹豫")
    if identifyImg.identify_find_template_or_not("multi_login.png", 0.8):
        print("重复登陆，终止程序")
        sys.exit()
    elif identifyImg.identify_find_template_or_not("shutdown_menu.png", 0.8):
        print("要休眠了，停止程序")
        sys.exit()


schedule.every(1).seconds.do(choose_reward_by_time)

while True:
    schedule.run_pending()
