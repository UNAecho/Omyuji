import pytesseract
from PIL import Image
from tasks.tools import readContentOfScreen
from tasks.repository import GameCoordinateIndex
import time
import cv2
from tasks.tools import identifyImg

identifyImg.identify_find_template_or_not("boundary_available_flag.png",0.8)

