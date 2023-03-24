from PIL import Image
import time
import os
import pytesseract
import pyautogui

def contains(text):
    filename = 'temp_screenshot.png'
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'{filename}')
    img = Image.open(f'{filename}')

    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(img)
    os.remove(f'{filename}')
    return result

time.sleep(3)
print(contains('Welcome to Facebook,'))

# file = ''
# x, y = pyautogui.locateCenterOnScreen(file, confidence = 0.9)
# pyautogui.click(x/2, y/2)