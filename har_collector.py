from account_adding.fsm_functions import instagram, type, save_har
import pyautogui
import string
import time
import random


account = ('karensmithnrnpdhbvpa', '0gEnruTrFt')

instagram(account, har=True)

names = ['ullivan', 'atenlina']
for name in names:
    type(name, type='type')
    for letter in string.ascii_lowercase:
        type(letter)
        time.sleep(1.2 + random.random()*2.4)
        pyautogui.press('backspace')
        time.sleep(0.12)
    
    pyautogui.hotkey('command', 'backspace', interval=0.2)
    time.sleep(0.06)

save_har()
