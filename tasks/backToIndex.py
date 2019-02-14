import time
import random
from tasks.tools.operation import mouse_click, mouse_dclick, mouse_move, key_input


def backToIndex():
    # 退出
    key_input(['esc'])
    time.sleep(random.randint(3, 4))
