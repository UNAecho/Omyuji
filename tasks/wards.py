import time
import random
from tasks.tools.operation import mouse_click, mouse_dclick, mouse_move, key_input
from tasks.tools.screenshot import getScreenshot, getPrint
from tasks.tools.fight import fight


def breakWards():
    # 点击探索
    mouse_click(1000, 360)
    time.sleep(5)

    