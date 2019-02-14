import random
import time

from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools.operation import mouse_click


def choose_floor_and_start_battle():

    # 点击战斗
    mouse_click(random.randint(Coordinate.explore_start_battle_x_left, Coordinate.explore_start_battle_x_right),
                random.randint(Coordinate.explore_start_battle_y_top, Coordinate.explore_start_battle_y_top))
    time.sleep(1)
    return
