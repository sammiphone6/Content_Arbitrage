import time
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button
import pyautogui
import os
import shutil
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

def reload():
    my_keyboard.press(Key.cmd)
    my_keyboard.press("r")
    my_keyboard.release("r")
    my_keyboard.release(Key.cmd)

def select_all():
    my_keyboard.press(Key.cmd)
    my_keyboard.press("a")
    my_keyboard.release("a")
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

def click(file, confidence = 0.9):
    x, y = pyautogui.locateCenterOnScreen(file, confidence = 0.9)
    pyautogui.click(x/2, y/2)

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
def pause_for(file, tries = 20):
    for _ in range(tries):
        try:
            click(file)
            return True
        except:
            time.sleep(1)
    return False

def open_incognito_window(): #first be hovering over a normal GChrome window to the rightmost window of all your windows
    # with pyautogui.hold('shift'):
    my_keyboard.press(Key.shift)
    my_keyboard.press(Key.cmd)
    my_keyboard.press('n')
    my_keyboard.release('n')
    my_keyboard.release(Key.cmd)
    my_keyboard.release(Key.shift)
    pause_for('button_icons/incognito/incognito.png')

def catch_ig_cookie_popup():
    return pause_for('button_icons/IG Essential cookies.png', 3)

def catch_fb_cookie_popup():
    return pause_for('button_icons/FB Essential cookies.png', 3)

def fb_login(fb_cred):
    directory = 'button_icons/facebook'
    searchbar()
    time.sleep(1)

    type('https://www.facebook.com')
    time.sleep(1)

    enter()
    time.sleep(2)

    catch_fb_cookie_popup()
    pause_for(f'{directory}/facebook.png')

    time.sleep(2)

    tab()
    time.sleep(1)

    email, password = fb_cred
    type(email)
    time.sleep(1)

    tab()
    time.sleep(1)

    type(password)
    time.sleep(1)

    enter()
    time.sleep(2)

    pause_for(f'{directory}/Welcome.png')

def create_page():
    directory = 'button_icons/facebook'
    searchbar()
    time.sleep(1)

    type('https://www.facebook.com/pages/creation/?ref_type=launch_point')
    time.sleep(1)

    enter()
    pause_for(f'{directory}/Page name.png')

    type('goodpage')
    time.sleep(1)
    type(str(int(1000000 + random.random()*9000000)))
    time.sleep(1)

    pause_for(f'{directory}/Category.png')
    type('des')
    pause_for(f'{directory}/Design.png')

    pause_for(f'{directory}/Create page.png')
    my_mouse.position = (100,100)

    if pause_for(f'{directory}/Too many pages.png', 2) or pause_for(f'{directory}/Account restricted.png', 2):
        return False
    
    if not pause_for(f'{directory}/Next.png', 10): return False
    if not pause_for(f'{directory}/Next.png', 5): return False
    if not pause_for(f'{directory}/Skip.png', 5): return False
    if not pause_for(f'{directory}/Next.png', 5): return False
    if not pause_for(f'{directory}/Done.png', 5): return False
    if not pause_for(f'{directory}/Not now fb page.png', 5): return False
    return True

def link_account():
    directory = 'button_icons/facebook'

    searchbar()
    time.sleep(1)

    type('https://www.facebook.com/settings/?tab=linked_instagram')
    time.sleep(1)

    enter()

    if not pause_for(f'{directory}/Connect account.png', 10): link_account() 
    if not pause_for(f'{directory}/Connect.png'): link_account() 
    if not pause_for(f'{directory}/Confirm.png'): link_account() 

def fb_connect_ig_login(insta_cred):
    directory = 'button_icons/facebook'
    
    if not pause_for(f'{directory}/IG prompt.png', 4):
        catch_fb_cookie_popup()
        if not pause_for(f'{directory}/IG prompt.png'):
            reload()
            pause_for(f'{directory}/IG prompt.png')
    
    ## Challenge in the instagram link blocks the IP, regardless of which account you try
    email, password = insta_cred
    type(email)
    time.sleep(1)

    tab()
    time.sleep(1)

    type(password)
    time.sleep(1)

    enter()
    time.sleep(2)

    catch_ig_cookie_popup()

    pause_for(f'{directory}/Not now.png')
    connected = pause_for(f'{directory}/IG connected.png')
    pause_for(f'{directory}/Account connected done.png',4)

    review_needed = pause_for(f'{directory}/Review needed.png', 2)
    
    return connected and not review_needed

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
    time.sleep(2)

def regular_ig_login(insta_cred):
    directory = 'button_icons/instagram_account_info'
    searchbar()
    time.sleep(1)

    type('https://www.instagram.com/')
    time.sleep(1)

    enter()

    catch_ig_cookie_popup()
    pause_for(f'{directory}/Insta Log In.png')

    username, password = insta_cred
    type(username)
    time.sleep(1)

    tab()
    time.sleep(1)

    type(password)
    time.sleep(1)

    enter()
    time.sleep(2)

    if pause_for(f'{directory}/IG successful login.png', 5): ## Now you're logged into instagram
        return True
    elif pause_for(f"{directory}/Couldn't connect.png", 3):
        pass
    elif catch_ig_cookie_popup():
        pause_for(f'{directory}/IG successful login.png', 3)
    elif pause_for(f"{directory}/Account suspended.png", 3):
        return False
    
    regular_ig_login(insta_cred)

def switch_logged_in_instagram_to_business():
    directory = 'button_icons/instagram_business_account'
    searchbar()
    time.sleep(1)

    type('https://www.instagram.com/accounts/convert_to_professional_account/')
    time.sleep(1)

    enter()

    if pause_for(f'{directory}/Business.png', 3):
        pass
    elif pause_for(f'{directory}/Already professional.png', 3):
        return
    else:
        switch_logged_in_instagram_to_business() if not pause_for(f'{directory}/Business.png', 10) else None
    
    if not pause_for(f'{directory}/Next.png', 4): switch_logged_in_instagram_to_business() 
    if not pause_for(f'{directory}/Next.png', 4): switch_logged_in_instagram_to_business() 
    if not pause_for(f'{directory}/Art.png', 4): switch_logged_in_instagram_to_business() 
    if not pause_for(f'{directory}/Done.png', 4): switch_logged_in_instagram_to_business() 
    if not pause_for(f"{directory}/Don't use.png", 4): switch_logged_in_instagram_to_business() 
    if not pause_for(f'{directory}/Done.png', 4): switch_logged_in_instagram_to_business() 


### Get more good cheap instas https://accsmarket.com/en/catalog/instagram/pva 
### Also, fully automate by getting their name, pfp from tiktok, make some generic bio formula,
### And while creating a new account you can easily test available usernames from the ten we might want
### Bio formula should include not impersonating.
def update_account_info(insta_info): #For this to work, make sure that PFP is on 
    directory = 'button_icons/instagram_account_info'
    
    def update_pfp_on_account(username, prev_pfp = False, AC = False): #AC = accounts center setup
        pfp_directory = 'PFPs'
        new_file = None
        for file in os.listdir(pfp_directory):
            if file[:len(username)] == username and len (file) <= len(username)+5: #.jpeg is longest
                orig_file = f'{pfp_directory}/{file}'
                new_file = f'{pfp_directory}/temp_{pfp_directory}/{file}'
                shutil.copy(orig_file, new_file)

                if AC:
                    pause_for(f'{directory}/AC upload new photo.png', 4)
                    ## See what happens on an earlier account if updating pfp and account center (likley not needed for a while)
                else:
                    pause_for(f'{directory}/Change profile photo.png', 4)
                    pause_for(f'{directory}/Upload new photo.png', 2)
                time.sleep(5)

                down()
                time.sleep(2)

                enter()
                time.sleep(3) ## PFP should now be updated
                os.remove(new_file)## REMOVE PFP FROM FOLDER
                return
    
    username, name, bio, update_pfp = insta_info

    if pause_for(f'{directory}/X account center.png', 3): #Then AC
        #Do bio first
        pause_for(f'{directory}/Bio.png', 3)
        select_all()
        time.sleep(0.5)
        type(bio)
        time.sleep(0.5) 
        
        pause_for(f'{directory}/Accounts center.png', 8)
        pause_for(f'{directory}/IG account center.png')

        pause_for(f'{directory}/AC change name.png')
        pause_for(f'{directory}/AC name.png')
        select_all()
        time.sleep(0.5)
        type(name)
        time.sleep(0.5)
        pause_for(f'{directory}/AC done.png')

        pause_for(f'{directory}/AC change username.png')
        pause_for(f'{directory}/AC username.png')
        select_all()
        time.sleep(0.5)
        type(username)
        time.sleep(0.5)
        pause_for(f'{directory}/AC done.png')

        if update_pfp:
            pause_for(f'{directory}/AC change pfp.png')
            update_pfp_on_account(username, AC = True)
            pause_for(f'{directory}/AC save.png')

        time.sleep(1)

    else:
        if update_pfp:
            update_pfp_on_account(username, AC = False)

        pause_for(f'{directory}/Name.png', 3)
        select_all()
        time.sleep(0.5)
        type(name)
        time.sleep(0.5)

        pause_for(f'{directory}/Username.png', 3)
        select_all()
        time.sleep(0.5)
        type(username)
        time.sleep(0.5)

        pause_for(f'{directory}/Bio.png', 3)
        select_all()
        time.sleep(0.5)
        type(bio)
        time.sleep(0.5) 

        pause_for(f'{directory}/Submit.png', 3)
        pause_for(f'{directory}/Profile saved.png', 15)
        time.sleep(1)
    


## Complex Processes
#Incomplete
def update_instagram_settings(insta_cred, new_account_info):
    open_incognito_window()
    if not regular_ig_login(insta_cred):
        return False
    switch_logged_in_instagram_to_business() # Now we should be automatically redirected here https://www.instagram.com/accounts/edit/
    update_account_info(new_account_info)
    close_page()
    return True

    # Need to (1) figure out how to select pfp in our filesystem (or some other solution)
    # (2) verify usernames are available ahead of time

#Complete
def add_fb_page_and_link_instagram(fb_creds, insta_creds):
    open_incognito_window()
    fb_login(fb_creds)

    if not create_page():
        close_page()
        return False
    
    link_account()
    result = fb_connect_ig_login(insta_creds)
    close_page()
    return result

