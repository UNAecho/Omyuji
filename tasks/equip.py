import time
import random
from tasks.tools.operation import mouse_click, mouse_dclick, mouse_move, key_input
from tasks.tools.fight import fight
from tasks.tools.floor import selectFloor

def getEquip(config):
    # 点击探索
    mouse_click(1000, 360)
    time.sleep(5)

    # 选择御魂副本
    mouse_click(570, 810)
    time.sleep(2)

    # 选择八歧大蛇 600,400 - 900,600
    random_x = int(random.uniform(600, 900))
    random_y = int(random.uniform(400, 600))
    mouse_click(random_x, random_y)
    time.sleep(2)

    for floor in config.keys():
        for i in range(config[floor]):
            selectFloor(floor)

            # 点击挑战 1200，650 - 1275，680
            random_x = int(random.uniform(1200, 1275))
            random_y = int(random.uniform(650, 680))
            mouse_click(random_x, random_y)

            # 战斗
            fight()
            time.sleep(2)
        

    time.sleep(5)
    # 返回到探索
    mouse_click(1328, 328)
    time.sleep(5)

    # 返回到庭院
    key_input(['esc'])
    time.sleep(5)