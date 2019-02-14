import time
import random
from tasks.tools.operation import mouse_click, mouse_dclick, mouse_move, key_input
from tasks.tools.fight import fight

def getAwake(times):

    # 点击探索
    mouse_click(1000, 360)
    time.sleep(5)

    for i in range(len(times)):

        # 选择御魂副本
        mouse_click(485, 810)
        time.sleep(2)


        # 选择觉醒副本类型
        click_y = 540
        if i == 0:
            click_x = 600
        elif i == 1:
            click_x = 850
        elif i == 2:
            click_x = 1100
        else:
            click_x = 1350
        
        mouse_click(click_x, click_y)
        time.sleep(2)


        for i in range(times[i]):
            # 点击挑战 1200，650 - 1275，680
            random_x = int(random.uniform(1200, 1275))
            random_y = int(random.uniform(650, 680))
            mouse_click(random_x, random_y)

            # 战斗
            fight()
            time.sleep(2)

        time.sleep(3)
        # 返回到探索
        mouse_click(1328, 328)
        time.sleep(3)

    
    # 返回到庭院
    key_input(['esc'])
    time.sleep(5)