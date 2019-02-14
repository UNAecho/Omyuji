import time
import random
import cv2 as opencv
import numpy as np
from tasks.tools.operation import mouse_click, mouse_dclick, mouse_move, key_input
from tasks.tools.screenshot import getScreenshot
from tasks.tools.fight import fight

def getExplore(floor):
    # 点击探索
    mouse_click(1000, 360)
    time.sleep(5)

    # 识别章节
    getScreenshot('chapter.bmp', 1310, 380, 218, 480)
    img = opencv.imread('chapter.bmp', 0)
    template = opencv.imread('tasks/tools/images/chapter%d.jpg' % floor, 0)

    res = opencv.matchTemplate(img, template, opencv.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.95)
    for pt in zip(*loc[::-1]):
        gps = pt
    
    loc_x = gps[0] + int(random.uniform(5, 20)) + 1310
    loc_y = gps[1] + int(random.uniform(5, 24)) + 380
    mouse_click(loc_x, loc_y)
    time.sleep(4)

    # 点击探索
    loc_x = int(random.uniform(40, 80)) + 1177
    loc_y = int(random.uniform(20, 40)) + 675
    mouse_click(loc_x, loc_y)
    time.sleep(4)

    threshold = 0.95
    # 开始刷怪
    while True:
        getScreenshot('screen.bmp', 392, 220, 1136, 640)
        screen = opencv.imread('screen.bmp', 0)
        boss = opencv.imread('tasks/tools/images/boss.jpg', 0)
        boss_res = opencv.matchTemplate(screen, boss, opencv.TM_CCOEFF_NORMED)
        loc = np.where(boss_res >= threshold)
        boss_gps = None
        for pt in zip(*loc[::-1]):
            boss_gps = pt
        if boss_gps:
            # 打Boss
            loc_x = boss_gps[0] + int(random.uniform(10, 46)) + 392
            loc_y = boss_gps[1] + int(random.uniform(10, 35)) + 220
            mouse_click(loc_x, loc_y)
            fight()
            break
        else:
            monster = opencv.imread('tasks/tools/images/monster.jpg', 0)
            monster_res = opencv.matchTemplate(screen, monster, opencv.TM_CCOEFF_NORMED)
            loc = np.where(monster_res >= threshold)
            gps = []
            for pt in zip(*loc[::-1]):
                gps.append(pt)
            if len(gps) > 0:
                loc_x = gps[0][0] + int(random.uniform(10, 46)) + 392
                loc_y = gps[0][1] + int(random.uniform(10, 35)) + 220
                mouse_click(loc_x, loc_y)
                time.sleep(2)
                fight()
            else:
                mouse_click(1452, 670)
            
            time.sleep(3.5)

    # 拾取奖励
    time.sleep(6)
    while True:
        getScreenshot('screen.bmp', 392, 220, 1136, 640)
        screen = opencv.imread('screen.bmp', 0)
        treasure = opencv.imread('tasks/tools/images/treasure.jpg', 0)
        treasure_res = opencv.matchTemplate(screen, treasure, opencv.TM_CCOEFF_NORMED)
        loc = np.where(treasure_res >= threshold)
        treasure_gps = None
        for pt in zip(*loc[::-1]):
            treasure_gps = pt
        if treasure_gps:
            loc_x = treasure_gps[0] + 392 + int(random.uniform(10, 30))
            loc_y = treasure_gps[1] + 220 + int(random.uniform(10, 24))
            mouse_click(loc_x, loc_y)
            time.sleep(2.5)
            loc_x = 970 + 392 + int(random.uniform(20, 130))
            loc_y = 230 + 220 + int(random.uniform(20, 130))
            mouse_click(loc_x, loc_y)
            time.sleep(1)
        else:
            time.sleep(3)
            break
    
    print('探索结束')
            

            
    