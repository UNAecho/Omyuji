import win32gui, win32ui, win32con
import numpy as np
from PIL import Image
# import pytesseract

def getScreenshot(filename, x, y, width, height):
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(0)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()

    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (x, y), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)

def getPrint(filename):
    arr = np.array(Image.open(filename))
    result = 0
    total = 0
    for row in arr:
        total += len(row)
        for pixel in row:
            result += int(pixel[0]) + int(pixel[1]) + int(pixel[2])
    result = int(result/total)
    return result