import cv2 as opencv
import numpy as np
import time
import random
from tasks.tools.screenshot import getScreenshot
from tasks.tools.operation import mouse_click

def selectFloor(n):
    getScreenshot('screen.bmp', 612, 335, 275, 255)
    img = opencv.imread('screen.bmp', 0)
    template = opencv.imread('tasks/tools/images/floor%d.jpg' % n, 0)

    res = opencv.matchTemplate(img, template, opencv.TM_CCOEFF_NORMED)
    threshold = 0.98
    gps = None
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        gps = pt
    
    if gps:
        loc_x = gps[0] + 612 + int(random.uniform(2, 20))
        loc_y = gps[1] + 335 + int(random.uniform(3, 20))
        mouse_click(loc_x, loc_y)
    else:
        # todo 滚动选择
        pass
    
    time.sleep(0.5)