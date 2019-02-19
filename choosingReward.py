import time
import datetime
import schedule

from tasks.repository import templateEntity
from tasks.tools import identifyImage
from tasks.tools.operation import mouse_click

# 模板路径，key为模板文件名，value为图片对应的cv2使用的BGR转化为GRAY数组，注意转换前是BGR不是RGB。type为ndarray。
# 使用时，直接以字典取值方式即可
template_cv2_entity = templateEntity.generate_all_template_gray_ndarray_of_cv2()


def choose_reward_by_time():

    # 先找悬赏封印的【封印】二字，返回坐标
    reward_invite_filename = "reward_invite.png"
    reward_invite_coordinate = identifyImage.identify_find_template_or_not(reward_invite_filename, 0.8)
    if reward_invite_coordinate.__len__() > 0:

        reward_refuse_filename = "reward_refuse.png"
        reward_refuse_coordinate = identifyImage.identify_find_template_or_not(reward_refuse_filename, 0.85)
        if reward_refuse_coordinate.__len__() > 0:
            # 如果过了18点，开始接受悬赏，由于接受按钮在拒绝按钮上面，为了优化性能，将拒绝按钮y轴坐标减去86代表接受按钮坐标
            if time.localtime().tm_hour > 17:
                mouse_click(reward_refuse_coordinate['x'], reward_refuse_coordinate['y'] - 86)
                print("晚上6点以后开始接客啦！")
            else:
                mouse_click(reward_refuse_coordinate['x'], reward_refuse_coordinate['y'])
                print("有人邀请，立即拒绝，没有犹豫")


schedule.every(1).seconds.do(choose_reward_by_time)

while True:
    schedule.run_pending()
