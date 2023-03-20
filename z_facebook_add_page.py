import time
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button
import pyautogui
import os
import random


start = time.time()
my_keyboard = keyboard.Controller()
my_mouse = mouse.Controller()

## Simple functions
def tab():
    pyautogui.press(['tab'])

def shift_tab():
    my_keyboard.press(Key.shift)
    my_keyboard.press(Key.tab)
    my_keyboard.release(Key.tab)
    my_keyboard.release(Key.shift)

def paste():
    my_keyboard.press(Key.cmd)
    my_keyboard.press("v")
    my_keyboard.release("v")
    my_keyboard.release(Key.cmd)

def space():
    my_keyboard.press(Key.space)
    my_keyboard.release(Key.space)

def down():
    pyautogui.press(['down'])

def up():
    pyautogui.press(['up'])

def click():
    my_mouse.click(Button.left)

def enter(): #if enter doesn't work, press space, usually has same effect
    # my_keyboard.press(Key.enter)
    pyautogui.press(['enter'])

def type(text):
    my_keyboard.type(text)

def searchbar():
    my_keyboard.press(Key.cmd)
    my_keyboard.press('l')
    my_keyboard.release('l')
    my_keyboard.release(Key.cmd)


# Maybe change all your pauses to have 5% variance via a pause function
## Sequences
def open_incognito_window(): #first be hovering over a normal GChrome window to the rightmost window of all your windows
    # with pyautogui.hold('shift'):
    my_keyboard.press(Key.shift)
    my_keyboard.press(Key.cmd)
    my_keyboard.press('n')
    my_keyboard.release('n')
    my_keyboard.release(Key.cmd)
    my_keyboard.release(Key.shift)
    time.sleep(5)

def fb_login(fb_cred):
    searchbar()
    time.sleep(1)

    type('https://www.facebook.com')
    time.sleep(1)

    enter()
    time.sleep(10)

    email, password = fb_cred
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
    time.sleep(5)

    down()
    time.sleep(1)

    enter()
    time.sleep(1)

    tab() #should be in the extra comments section
    time.sleep(1) #should be in the extra comments section

    tab()
    time.sleep(1)  #should be hovering over create page

    enter()
    time.sleep(15) #should enter on create page
    ## Be careful above not to create a page before you want to

    for _ in range(2):
        tab()
        time.sleep(1)

    for _ in range(4):
        enter()
        time.sleep(1)

    tab()
    time.sleep(1)

    enter()
    time.sleep(10)

    enter()
    time.sleep(1)

    enter()
    time.sleep(1)

def link_account():
    searchbar()
    time.sleep(1)

    type('https://www.facebook.com/settings/?tab=linked_instagram')
    time.sleep(1)

    enter()
    time.sleep(10)

    shift_tab()
    time.sleep(1)

    enter() ## This presses "Connect account"
    time.sleep(3) 

    shift_tab()
    time.sleep(1)

    enter()
    time.sleep(3)

    shift_tab()
    time.sleep(1)

    enter()
    time.sleep(10)

    ##Continue with instagram sign in, etc.

def fb_connect_ig_login(insta_cred):
    email, password = insta_cred
    type(email)
    time.sleep(1)

    tab()
    time.sleep(1)

    type(password)
    time.sleep(1)

    enter()
    time.sleep(10)

    for _ in range(12):
        tab()
        time.sleep(1)

    enter()
    time.sleep(25)

    enter()
    time.sleep(2)

def get_instagram_id():
    searchbar()
    time.sleep(1)

    type('https://business.facebook.com/latest/settings/business_assets')
    time.sleep(1)

    enter()
    time.sleep(10)

def close_page():
    my_keyboard.press(Key.cmd)
    my_keyboard.press('w')
    my_keyboard.release('w')
    my_keyboard.release(Key.cmd)
    time.sleep(2)

    enter()
    time.sleep(5)

def regular_ig_login(insta_cred):
    searchbar()
    time.sleep(1)

    type('https://www.instagram.com/')
    time.sleep(1)

    enter()
    time.sleep(10)

    for _ in range(2):
        tab()
        time.sleep(1)

    username, password = insta_cred
    type(username)
    time.sleep(1)

    tab()
    time.sleep(1)

    type(password)
    time.sleep(1)

    enter()
    time.sleep(20) ## Now you're logged into instagram

def switch_logged_in_instagram_to_business():
    searchbar()
    time.sleep(1)

    type('https://www.instagram.com/accounts/convert_to_professional_account/')
    time.sleep(1)

    enter()
    time.sleep(10)

    for _ in range(2):
        tab()
        time.sleep(1)

    shift_tab()
    time.sleep(1)

    space()
    time.sleep(1)

    tab()
    time.sleep(1)

    enter()
    time.sleep(1)

    for _ in range(2):
        tab()
        time.sleep(1)

    enter()
    time.sleep(1)

    for _ in range(3):
        tab()
        time.sleep(1)

    space()
    time.sleep(1)

    for _ in range(2):
        tab()
        time.sleep(1)

    enter()
    time.sleep(10)

    for _ in range(8):
        tab()
        time.sleep(1)

    enter()
    time.sleep(10)

    tab()
    time.sleep(1)

    enter()
    time.sleep(10)


## Complex Processes
def update_instagram_settings(insta_cred):
    open_incognito_window()
    regular_ig_login(insta_cred)
    switch_logged_in_instagram_to_business()
    # Now we should be automatically redirected here https://www.instagram.com/accounts/edit/
    # 28 tabs to get to 'change profile photo' on accounts/edit
    # Need to (1) figure out how to select pfp in our filesystem (or some other solution)
    # (2) verify usernames are available ahead of time

#Complete
def add_fb_page_and_link_instagram(fb_creds, insta_creds):
    open_incognito_window()
    fb_login(fb_creds)
    create_page()
    link_account()
    fb_connect_ig_login(insta_creds)
    close_page()

def get_fb_paired_instagram_account_id():
    pass
    ##todo
    # open_incognito_window()
    # fb_login(cred)
    # get_instagram_id()
    # https://www.instagram.com/accounts/convert_to_professional_account/
    




## Main script

print("Starting Script...")
initial_wait = 6
time.sleep(initial_wait)



creds = [
    # ('picakunyssenq@hotmail.com', 'zHCDominguezDCassie644'),
    # ('offjot216@digdig.org', 'xpranto@#25'),
    ('gutgap@prin.be', 'xpranto@#26')
]
insta = ('lewismargaretfqj8h4', 'IeDIa0gSCT')

# for cred in creds: #change back to just numtiktoks
#     add_fb_page_and_link_instagram(creds, insta)

update_instagram_settings(insta)

end = time.time()
print("All ", len(creds), " facebook accounts complete!\n")
print("It took ", (int)(end-start), " seconds to run (", (int)((end-start)/len(creds)), " seconds per account on average).")

