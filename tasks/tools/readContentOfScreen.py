import pytesseract
from PIL import Image
import shutil
from datetime import datetime

from tasks.tools.screenshot import getScreenshot

# 读取截图中的数字，多数用于各种挑战的数量剩余
# params:
# file_path:识别图片的路径
# screenshot_x:被截图左上角那一点的x轴坐标
# screenshot_y:被截图左上角那一点的y轴坐标
# screenshot_wight_x:图片x轴长度
# screenshot_high_y:图片y轴长度


def read_number_of_screen(file_path, screenshot_x, screenshot_y, screenshot_wight_x, screenshot_high_y):
    try:
        getScreenshot(file_path, screenshot_x,
                      screenshot_y, screenshot_wight_x, screenshot_high_y)
        read_screen_text = pytesseract.image_to_string(Image.open(file_path))
        if read_screen_text is None or "":
            print("带数字的图片路径：" + file_path + " 没读出来，这程序写的什么破玩意")
        number_of_remaining = str(read_screen_text).replace(" ", "").split("/")[0]
        if int(number_of_remaining) <= 0:
            return number_of_remaining.replace("-", "")
        else:
            return number_of_remaining
    except Exception as e:
        print("读取数字出错！错误信息：" + str(e))
        # 输出读取错误的图片，方便人工debug原因
        # 请定期清理文件，不然文件夹体积会越来越大
        # error_image_filepath = 'D:\\errorImage\\' + datetime.now().strftime('%Y%m%d%H%M%S') + '.png'
        # shutil.copyfile(file_path, error_image_filepath)
        # print("读取出错的图片路径为：" + error_image_filepath+"，请定期清理，防止文件夹越来越大")
        return "0"


def read_chi_of_screen(file_path, screenshot_x, screenshot_y, screenshot_wight_x, screenshot_high_y):
    getScreenshot(file_path, screenshot_x,
                  screenshot_y, screenshot_wight_x, screenshot_high_y)
    read_screen_text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')
    return read_screen_text
