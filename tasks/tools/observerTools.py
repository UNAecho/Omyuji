import random
import time
import win32api
import win32con
import pytesseract
from PIL import Image

from tasks.repository.GameCoordinateIndex import Coordinate
from tasks.tools.operation import mouse_click, mouse_move,key_input
from tasks.tools import identifyImg
from tasks.tools import fight
from tasks import yuling
from tasks.tools import windowTools
from tasks.tools import readContentOfScreen
from tasks.repository import templateEntity


def remaining_of_personal_breakthrough_ticket():
    number = readContentOfScreen.read_number_of_screen(
                    'screenshot_temp\\breakthrough_ticket.png',
                    Coordinate.explore_number_of_breakthrough_ticker_x_left,
                    Coordinate.explore_number_of_breakthrough_ticker_y_top,
                    77, 31)
    return number


