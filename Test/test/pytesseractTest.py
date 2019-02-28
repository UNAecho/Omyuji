import pytesseract
from PIL import Image
import time

time.sleep(1)
read_screen_text = pytesseract.image_to_string(Image.open("../../omyuji_ico/微信截图_20190227113259.png"))
print(read_screen_text)
