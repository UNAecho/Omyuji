import time
import random
from tasks.tools.operation import mouse_click, mouse_dclick, mouse_move, key_input
from tasks.tools.screenshot import getScreenshot, getPrint


def login(type, username, password):
    time.sleep(10)

    while True:
        getScreenshot('login.bmp', 892, 310, 30, 30)
        key = getPrint('login.bmp')
        if key == 258:
            break
        else:
            time.sleep(1.5)
    time.sleep(0.5)

    # 登陆
    if type == 'phone':
        pass
    else:
        # 选择邮箱登陆
        mouse_click(880, 440)
        time.sleep(1)

        # 选中用户名
        mouse_click(930, 512)
        time.sleep(1)

        # 输入用户名
        key_input(username)
        time.sleep(1)

        # 选中163邮箱
        mouse_click(955, 548)
        time.sleep(1)

    # 选中密码栏
    mouse_click(930, 574)
    time.sleep(1)

    # 输入密码
    key_input(password)
    time.sleep(0.5)
    key_input(['enter'])
    time.sleep(4)

    # 选择安卓平台
    mouse_click(1053, 562)
    time.sleep(5)

    # 关闭游戏公告
    mouse_click(1420, 290)
    time.sleep(5)

    # 点击进入游戏
    mouse_click(936, 800)
    time.sleep(5)

    # 点击任意区域 1100-1300, 500-700
    random_x = int(random.uniform(1100, 1300))
    random_y = int(random.uniform(500, 700))
    mouse_click(random_x, random_y)
    time.sleep(6)