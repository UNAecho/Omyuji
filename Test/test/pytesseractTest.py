import pytesseract
from PIL import Image
from tasks.tools import readContentOfScreen
from tasks.repository.GameCoordinateIndex import Coordinate
import time

while True:
    time.sleep(1)
    read_screen_text = readContentOfScreen.read_chi_of_screen("D:\阴阳师像素截图\\Untitled-1.png",
                                                              Coordinate.explore_click_to_continue_x_left,
                                                              Coordinate.explore_click_to_continue_y_top,
                                                              173,34)
    print(read_screen_text)
