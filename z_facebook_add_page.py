import time
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button
import pyautogui
import os
import random

def add_fb_page(creds):
    start = time.time()

    def tab():
        pyautogui.press(['tab'])

    def paste():
        my_keyboard.press(Key.cmd)
        my_keyboard.press("v")
        my_keyboard.release("v")
        my_keyboard.release(Key.cmd)

    def down():
        pyautogui.press(['down'])

    def up():
        pyautogui.press(['up'])

    def click():
        my_mouse.click(Button.left)

    def enter():
        my_keyboard.press(Key.enter)

    def type(text):
        my_keyboard.type(text)

    def searchbar():
        my_keyboard.press(Key.cmd)
        my_keyboard.press('l')
        my_keyboard.release('l')
        my_keyboard.release(Key.cmd)

    def process(cred): #hover mouse over browser searchbar
        def open_incognito_window(): #first be hovering over a normal GChrome window to the rightmost window of all your windows
            # with pyautogui.hold('shift'):
            my_keyboard.press(Key.shift)
            my_keyboard.press(Key.cmd)
            my_keyboard.press('n')
            my_keyboard.release('n')
            my_keyboard.release(Key.cmd)
            my_keyboard.release(Key.shift)
            time.sleep(5)
        
        def login(cred):
            searchbar()
            time.sleep(1)

            type('https://www.facebook.com')
            time.sleep(1)

            enter()
            time.sleep(10)

            email, password = cred
            type(email)
            time.sleep(1)

            tab()
            time.sleep(1)

            type(password)
            time.sleep(1)

            enter()
            time.sleep(20)

        def create_page():
            searchbar()
            time.sleep(1)

            type('https://www.facebook.com/pages/creation/?ref_type=launch_point')
            time.sleep(1)

            enter()
            time.sleep(15)

            type('goodpage')
            time.sleep(1)
            type(str(int(1000000 + random.random()*9000000)))
            time.sleep(1)

            tab()
            time.sleep(0.5)

            tab()
            time.sleep(0.5)

            type('des')
            time.sleep(1)

            down()
            time.sleep(1)

            enter()
            time.sleep(1)

            tab() #should be in the extra comments section
            time.sleep(1) #should be in the extra comments section

            # tab()
            time.sleep(10)  #should be hovering over create page

            #### enter()
            #### time.sleep(15) #should enter on create page
            ## Be careful above not to create a page before you want to

        def close_page():
            my_keyboard.press(Key.cmd)
            my_keyboard.press('w')
            my_keyboard.release('w')
            my_keyboard.release(Key.cmd)
            time.sleep(2)

            enter()
            time.sleep(5)


        open_incognito_window()
        login(cred)
        create_page()
        close_page()






    ## ------------------------
    ## Variables

    initial_wait = 6
    ## Variables
    ## ------------------------

    print("Starting Script...")
    time.sleep(initial_wait)
    my_keyboard = keyboard.Controller()
    my_mouse = mouse.Controller()

    for cred in creds*2: #change back to just numtiktoks
        process(cred)
        

    end = time.time()
    print("All ", len(creds), " facebook accounts complete!\n")
    print("It took ", (int)(end-start), " seconds to run (", (int)((end-start)/len(creds)), " seconds per account on average).")

creds = [('picakunyssenq@hotmail.com', 'zHCDominguezDCassie644')]
add_fb_page(creds)
