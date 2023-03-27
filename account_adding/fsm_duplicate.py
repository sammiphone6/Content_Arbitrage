import time
import datetime
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button
import pyautogui
import os
import shutil
import random
from PIL import Image
import pytesseract
import fuzzysearch
import pyautogui
from pandas.io.clipboard import clipboard_get
import cv2


start = time.time()
my_keyboard = keyboard.Controller()
my_mouse = mouse.Controller()
debug = True


## VPN (by clicking NordVPN App)
def change_vpn():
    countries = [
        'France', 
        'Greece',
        'Iceland', 
        'Ireland',
        'Israel',
        'Italy',
        'Japan',
        'Luxembourg',
        'Mexico',
        'New Zealand',
        'Norway',
        'Portugal',
        'Romania',
        'Singapore',
        'Slovenia',
        'South Korea',
        'Spain',
        'Sweden',
        'Switzerland',
        'United States',
    ]
    country = random.choice(countries)
    for _ in range(3):
        pause_for(f'button_icons/Nord/{country}.png', tries = 5)
        time.sleep(2)
    
    for _ in range(2):
        pause_for(f'button_icons/Nord/Safari.png', tries = 5)
    
    waits = 0
    connected = False
    while not connected:
        if waits > 3:
            return change_vpn()
        time.sleep(1)
        if not (contains('ERROR') or contains('Connecting to')):
            connected = True
        waits += 1
    return country

## Facebook Functions
def facebook(fb_creds): #Big Boy
    directory = 'button_icons/facebook'

    ## Checks incognito is open
    open_incognito_window()
    if not pause_for('button_icons/incognito/incognito.png', tries = 5): return close_page(False), 0
    if debug: print('Incognito window opened')

    ## Checks facebook is loaded
    load_facebook()
    if not catch_fb_cookie_popup(f'{directory}/facebook.png', tries = 15): 
        close_page()
        time.sleep(4)
        change_vpn()
        return facebook(fb_creds)
    time.sleep(3) #This makes sure you don't recognize the facebook logo, and have a cookie popup come as
    catch_fb_cookie_popup(f'{directory}/facebook.png', tries = 5) # you're typing since that changes languag of cookie, etc.
    if debug: print('Facebook opened')

    ## Sign into facebook
    enter_facebook_credentials(fb_creds)
    if debug: print('Facebook credentials entered')
    if not catch_fb_cookie_popup('Welcome to Facebook,', type = 'contains', tries = 15): return close_page(False), 0
    if debug: print('Facebook log in successful')

    ## Start to create page
    go_to_create_page()
    if not catch_fb_cookie_popup(f'{directory}/Page name.png'): return close_page(False), 0
    if debug: print('Creating facebook page')

    ## Submit page
    page_name = add_and_submit_page_details()
    pyautogui.moveTo(200, 100)
    if not catch_fb_cookie_popup(f'{directory}/Next.png', tries = 12): return close_page(False), 0
    if debug: print('Page creation successful')

    ## Finish page setup
    continue_page_setup()
    if not catch_fb_cookie_popup('Manage Page', type = 'contains', tries = 15): return close_page(False), 0
    if debug: print('Page setup complete')

    ## Go to link instagram:
    visit_link_instagram()
    if not catch_fb_cookie_popup(['Connect', 'ccount', 'stagram'], type = 'contains', tries = 15, similarity = 'flexible1'): return close_page(False), 0
    if debug: print('Now on connect instagram account page')

    ## Connect account steps:
    connect_account_steps()
    if not catch_ig_cookie_popup(f'{directory}/IG prompt.png', 20): return close_page(False), 0 ##Might need 2? check this
    if debug: print('Opened instagram redirect for connection')

    ## Enter instagram login
    instas['last_connected']+=1
    print("instas['last_connected']:", instas['last_connected'])
    enter_instagram_credentials(instas['accounts'][instas['last_connected']])
    if debug: print('Instagram credentials entered')
    if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 10, ignore_refresh = True):
        if debug: print('Couldnt login, will press enter again')

        enter()
        if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 14, ignore_refresh = False): return close_page(False, 2), 0
    if debug: print('Instagram login successful')

    ## Select not now and confirm success
    if not (catch_ig_cookie_popup(f'{directory}/Not now.png', tries = 6) or 
            catch_ig_cookie_popup(f'{directory}/Not now2.png', tries = 6)): return close_page(False, 2), 0
    if debug: print('Pressed not now after successful IG login')

    ## Confirm it says success
    connected = pause_for(f'{directory}/IG connected.png', 10)
    pause_for(f'{directory}/Account connected done.png',4)
    if debug: print('Account successfully connected')

    review_needed = pause_for(f'{directory}/Review needed.png', 2)
    if debug: print('Review needed...' if review_needed else 'Review not needed :)')

    return close_page(connected and not review_needed), page_name

def load_facebook():
    searchbar()
    time.sleep(1)

    type('https://www.facebook.com/?sk=welcome')
    time.sleep(1)

    enter()
    time.sleep(2)

def enter_facebook_credentials(fb_cred):
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

def go_to_create_page():
    searchbar()
    time.sleep(1)

    type('https://www.facebook.com/pages/creation/?ref_type=launch_point')
    time.sleep(1)

    enter()
    time.sleep(1)

def add_and_submit_page_details():
    directory = 'button_icons/facebook'

    page_name = 'goodpage' + str(int(1000000 + random.random()*9000000))
    type(page_name)
    time.sleep(1)

    pause_for(f'{directory}/Category.png', 6)
    type('des')
    pause_for(f'{directory}/Design.png', 15)

    pause_for(f'{directory}/Create page.png', 5)
    my_mouse.position = (100,100)

    return page_name

def continue_page_setup():
    directory = 'button_icons/facebook'
    pause_for(f'{directory}/Next.png', 5)
    pause_for(f'{directory}/Skip.png', 5)
    pause_for(f'{directory}/Next.png', 5)
    pause_for(f'{directory}/Done.png', 5)
    pause_for(f'{directory}/Not now fb page.png', 15)

def visit_link_instagram():
    searchbar()
    time.sleep(1)

    type('https://www.facebook.com/settings/?tab=linked_instagram')
    time.sleep(1)

    enter()
    time.sleep(1)

def connect_account_steps():
    directory = 'button_icons/facebook'
    pause_for(f'{directory}/Connect account.png', 10)
    pause_for(f'{directory}/Connect.png', 10)
    pause_for(f'{directory}/Confirm.png', 10)
    time.sleep(2)

## Instagram Functions
def instagram(insta_creds, new_account_info): #Big Boy

    ## Checks incognito is open
    open_incognito_window()
    if not catch_ig_cookie_popup("You’ve gone Incognito", type = 'contains', tries = 5, similarity='flexible'): #pause_for('button_icons/incognito/incognito.png', tries = 5):
        close_page(False)
        change_vpn()
        if debug: print("Couldn't load incognito")
        return instagram(insta_creds, new_account_info)

    directory = 'button_icons/instagram_account_info'

    ## Checks instagram is loaded
    if debug: print("Loading instagram")
    load_instagram()
    if not catch_ig_cookie_popup(f'{directory}/Insta Log In.png', tries = 10): 
        close_page(False)
        change_vpn()
        if debug: print("Couldn't find insta log in")
        return instagram(insta_creds, new_account_info)

    ## Sign into instagram
    if debug: print("Entering insta creds")
    enter_instagram_credentials(insta_creds)
    
    if catch_ig_cookie_popup(f'{directory}/challenge thrown.png', tries = 1, ignore_refresh = True): 
        if debug: print("Challenge thrown")
        return close_page(False)
    if debug: print("No challenge thrown")

    if catch_ig_cookie_popup("suspended", type = 'contains', tries = 1, ignore_refresh = True, similarity='flexible'): 
        if debug: print("Account Suspended")
        return close_page(False)
    if debug: print("Account not suspended")
    
    if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 5, ignore_refresh = True, similarity='flexible1'):
        if catch_ig_cookie_popup(f'{directory}/accounts onetap.png', tries = 1, ignore_refresh = True):
            if debug: print("Needed to reload page")
            reload()
        else:
            if debug: print("Needed to press enter again")
            enter()
        if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 5, ignore_refresh = True, similarity='flexible1'): return close_page(False)
    if debug: print("Login confirmed")

    ## Start to switch to business account
    go_to_switch_business()
    if not catch_ig_cookie_popup('Business', type = 'contains', tries = 15): return close_page(False)
    if debug: print("Switched to business page")

    ## Finish switching to business account
    finish_switching()
    if debug: print("Finished steps to switch to business account")
    if not catch_ig_cookie_popup('Switch to personal account', type = 'contains', tries = 22, similarity='flexible'):
        go_to_switch_business()
        if not catch_ig_cookie_popup('Business', type = 'contains', tries = 15): return close_page(False)
        if debug: print("Switched to business page")

        ## Finish switching to business account
        finish_switching()
        if debug: print("Finished steps to switch to business account")
        if not catch_ig_cookie_popup('Switch to personal account', type = 'contains', tries = 22, similarity='flexible'): return close_page(False)


    if debug: print("Successfully switched to business account")

    ## Finish updating account info
    time.sleep(4)
    return close_page(update_account_info(new_account_info))

def load_instagram():
    searchbar()
    time.sleep(1)

    type('https://www.instagram.com/')
    time.sleep(1)

    enter()
    time.sleep(2)   

def enter_instagram_credentials(insta_cred):
    time.sleep(3)

    username, password = insta_cred
    type(username)
    time.sleep(1)

    tab()
    time.sleep(1)

    type(password)
    time.sleep(1)

    enter()
    time.sleep(2)

def go_to_switch_business():
    searchbar()
    time.sleep(1)

    type('https://www.instagram.com/accounts/convert_to_professional_account/')
    time.sleep(1)

    enter()
    time.sleep(1)

def finish_switching(tries = 0):
    if debug: print("finish_switching tries: ", tries)
    if tries == 2:
        return
    
    directory = 'button_icons/instagram_business_account'
    if not catch_ig_cookie_popup(file = f'{directory}/Business.png', tries = 10, ignore_refresh=True, business=True): return finish_switching(tries = tries+1)
    if debug: print("Clicked Business")
    if not catch_ig_cookie_popup(file = f'{directory}/Next.png', tries = 10, ignore_refresh=True, business=True): return finish_switching(tries = tries+1)
    if debug: print("Clicked Next 1")
    if not catch_ig_cookie_popup(file = f'{directory}/Next.png', tries = 10, ignore_refresh=True, business=True): return finish_switching(tries = tries+1)
    if debug: print("Clicked Next 2")
    if not catch_ig_cookie_popup(file = f'{directory}/Art.png', tries = 20, ignore_refresh=True, business=True): return finish_switching(tries = tries+1)
    if debug: print("Clicked Art")
    if not catch_ig_cookie_popup(file = f'{directory}/Done.png', tries = 10, ignore_refresh=True, business=True): return finish_switching(tries = tries+1)
    if debug: print("Clicked Done")
    if not catch_ig_cookie_popup(file = f"{directory}/Don't use.png", tries = 10, ignore_refresh=True, business=True): return finish_switching(tries = tries+1)
    if debug: print("Clicked Don't use")
    if not catch_ig_cookie_popup(file = f'{directory}/Done.png', tries = 10, ignore_refresh=True, business=True): return finish_switching(tries = tries+1)
    if debug: print("Clicked Done")

def update_account_info(insta_info, tries = 0): #For this to work, make sure that PFP is on 
    if tries == 2:
        return False
    
    directory = 'button_icons/instagram_account_info'
    
    def update_pfp_on_account(username, prev_pfp = False, AC = False): #AC = accounts center setup
        pfp_directory = 'PFPs'
        new_file = None
        for file in os.listdir(pfp_directory):
            if file[:len(username)+1] == f'{username}.' and len (file) <= len(username)+5: #.jpeg is longest
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

    ##################
    ## Next time, maybe try deleting the account from accounts center and going back to instagram.com then continuing
    catch_ig_cookie_popup(f'{directory}/X account center.png', tries = 2, ignore_refresh = True)
    if catch_ig_cookie_popup('Manage your connected', type = 'contains', tries = 3, ignore_refresh = True, similarity = 'flexible'): #Then AC
        #Do pfp and bio first
        if debug: print("Accounts center")
        if update_pfp:
            # pause_for(f'{directory}/AC change pfp.png')
            update_pfp_on_account(username, AC = False)
            if debug: print("Pfp updated")
            # update_pfp_on_account(username, AC = True)
            # pause_for(f'{directory}/AC save.png')

        pause_for(f'{directory}/Bio.png', 3)
        select_all()
        time.sleep(0.5)
        type(bio)
        time.sleep(0.5)
        if debug: print("Bio added")
        pause_for(f'{directory}/Submit.png', 3)
        pause_for(f'{directory}/Profile saved.png', 15)
        if debug: print("Profile saved")
        
        pause_for(f'{directory}/Accounts center.png', 8)
        if debug: print("Clicked on 'See more in accounts center'")
        if not catch_ig_cookie_popup(f'{directory}/IG account center 1.png'): 
            if debug: print("IG account center 1 not clicked")
            if not catch_ig_cookie_popup(f'{directory}/IG account center 2.png'): 
                if debug: print("IG account center 2 not clicked")
                if not catch_ig_cookie_popup(f'{directory}/IG account center 3.png'): return False
        if debug: print("Clicked on 'Instagram' label beneath icon")

        if not pause_for(f'{directory}/AC change name.png'): return False
        if not pause_for(f'{directory}/AC name.png'): return False
        select_all()
        time.sleep(0.5)
        type(name)
        time.sleep(0.5)
        if not pause_for(f'{directory}/AC done.png'): return False
        if debug: print("Name changed")

        if not pause_for(f'{directory}/AC change username.png'): return False
        if not pause_for(f'{directory}/AC username.png'): return False
        select_all()
        time.sleep(0.5)
        type(username)
        time.sleep(0.5)
        if not pause_for(f'{directory}/Username available.png', tries = 8): return False
        if debug: print("Username available")
        if not pause_for(f'{directory}/AC done.png'): return False
        if debug: print("Username changed")

        time.sleep(1)
        return True

    else:
        if debug: print("Normal settings layout (not accounts center)")
        if update_pfp:
            update_pfp_on_account(username, AC = False)
            if debug: print("Pfp updated")

        pause_for(f'{directory}/Name.png', 3)
        select_all()
        time.sleep(0.5)
        type(name)
        time.sleep(0.5)
        if debug: print("Name added")

        pause_for(f'{directory}/Username.png', 3)
        select_all()
        time.sleep(0.5)
        type(username)
        time.sleep(0.5)
        if debug: print("Username added")

        pause_for(f'{directory}/Bio.png', 3)
        select_all()
        time.sleep(0.5)
        type(bio)
        time.sleep(0.5)
        if debug: print("Bio added")

        pause_for(f'{directory}/Submit.png', 3)
        if not pause_for(f'{directory}/Profile saved.png', 15): return update_account_info(insta_info, tries = tries + 1)
        if debug: print("Profile successfully saved")
        
        return catch_ig_cookie_popup(insta_info[:3], type = 'contains', tries = 5, similarity = 'flexible')
    
## FB Developer App Functions
def developer(fb_creds):
    directory = 'button_icons/facebook'

    ## Checks incognito is open
    open_incognito_window()
    if not pause_for('button_icons/incognito/incognito.png', tries = 5): return close_page(False), 0

    ## Checks facebook is loaded
    load_facebook()
    if not catch_fb_cookie_popup(f'{directory}/facebook.png', tries = 15): 
        close_page()
        time.sleep(4)
        change_vpn()
        return developer(fb_creds)
    
    directory = 'button_icons/developer'

    load_developer_site()

def load_developer_site():
    searchbar()
    time.sleep(1)

    type('https://developer.facebook.com/')
    time.sleep(1)

    enter()
    time.sleep(2)

def enter_card_info():
    type('5268760045909178')
    time.sleep(1)

    tab()
    time.sleep(1)

    type('0327')
    time.sleep(1)

    tab()
    time.sleep(1)

    type('236')
    time.sleep(1)

    # tab()
    # time.sleep(1)

    # type('02139')
    # time.sleep(1)


# text = clipboard_get()                                                     
# print(text)



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
    pause_for(f'button_icons/Reload.png', 2)
    time.sleep(5)

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

def click(file, confidence = 0.85):
    # resize_factor = 90/100
    # img = cv2.imread(file)
    # new_file = cv2.resize(img, (img.shape[1]*resize_factor, img.shape[0](resize_factor)))
    # print(img.shape)
    # print(new_file.shape)
    # x, y = pyautogui.locateCenterOnScreen(image = new_file, confidence = confidence)
    # pyautogui.click(x/2, y/2)
    x, y = pyautogui.locateCenterOnScreen(image = file, confidence = confidence)
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


## Comparator functions         # Maybe change all your time.sleep()'s to have 5% variance via a pause function
def pause_for(file, tries = 20):
    for _ in range(tries):
        try:
            click(file)
            return True
        except:
            time.sleep(1)
    return False

def contains(text, similarity = 1):
    filename = 'temp_screenshot.png'
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'{filename}')
    img = Image.open(f'{filename}')

    # converts the image to result and saves it into result variable
    result = pytesseract.image_to_string(img)
    os.remove(f'{filename}')

    if isinstance(text, str):
        return match(text, result, similarity)
    if isinstance(text, list) or isinstance(text, tuple):
        return len([t for t in text if match(t, result, similarity)]) >= max(1, len(text)-1)

def match(text, result, similarity):
    if similarity == 1:
        return text in result
    
    if similarity == 'flexible':
        return len(fuzzysearch.find_near_matches(text, result, max_l_dist=2)) > 0
    if similarity == 'flexible1':
        return len(fuzzysearch.find_near_matches(text, result, max_l_dist=1)) > 0

## This alternates between checking for cookie and checking for result we want.
def catch_ig_cookie_popup(file, tries=10, type = 'pause', similarity = 1, ignore_refresh = False, business = False):
    for _ in range(tries):
        try:
            if type == 'pause':
                click(file)
            elif type == 'contains':
                if not contains(file, similarity): raise Exception 
            return True
        except:
            pass
        try:
            if business:
                click('button_icons/instagram_business_account/Continue.png') 
            else:
                if _%3 == 0: click('button_icons/IG Essential cookies.png') 
                elif _%3 == 1: click('button_icons/IG Essential cookies2.png')
                else: click('button_icons/instagram_account_info/No notifications.png')
        except:
            pass
        time.sleep(1)
        if _ == tries//2 and not ignore_refresh:
            reload()
    return False

def catch_fb_cookie_popup(file, tries=10, type = 'pause', similarity = 1, ignore_refresh = False):
    for _ in range(tries):
        try:
            if type == 'pause':
                click(file)
            elif type == 'contains':
                if not contains(file, similarity): raise Exception 
            return True
        except:
            pass
        try:
            click('button_icons/FB Essential cookies.png')
        except:
            pass
        time.sleep(1)
        if _ == tries//2 and not ignore_refresh:
            reload()
    return False

## Open and close window functions 
def open_incognito_window(): #first be hovering over a normal GChrome window to the rightmost window of all your windows
    my_keyboard.press(Key.shift)
    my_keyboard.press(Key.cmd)
    my_keyboard.press('n')
    my_keyboard.release('n')
    my_keyboard.release(Key.cmd)
    my_keyboard.release(Key.shift)

def close_page(bool = False, times = 1):
    if debug: print("Closing page and returning: ", bool)
    if pause_for('button_icons/Close incognito1.png', 15) and debug: print("Clicked Close incognito1.png")
    if pause_for('button_icons/Close incognito2.png', 15) and debug: print("Clicked Close incognito2.png")
    if pause_for('button_icons/Leave.png', 15) and debug: print("Clicked Leave.png")
    return bool



time.sleep(4)



fbs = [
    # ('soniyaa1334x@simaenaga.com', '#xpranto@25#'),
    # ('shimaxc2566@simaenaga.com', '#xpranto@25#'),
    # ('morimjrx555@simaenaga.com', '#xpranto@25#'),
    # ('joymiaxc246@catgroup.uk', '#xpranto@25#'),
    ('xjjantcomx445@exdonuts.com', '#xpranto@25#'),
    ('rima3468888@exdonuts.com', '#xpranto@25#'),
    ('joy2467sss@exdonuts.com', '#xpranto@25#'),
    ('mimxn24784@exdonuts.com', '#xpranto@25#'),
    ('anikaxn14653@exdonuts.com', '#xpranto@25#'),
    ('jobaanikax3467@exdonuts.com', '#xpranto@25#'),
    ('priyaxc36421@exdonuts.com', '#xpranto@25#'),
    ('samiakhan48873@exdonuts.com', '#xpranto@25#'),
    ('nargissikdarcnx2641@exdonuts.com', '#xpranto@25#'),
    ('nargisxhaque1341@exdonuts.com', '#xpranto@25#'),
    ('ayeshaxhossain1343@exdonuts.com', '#xpranto@25#'),
    ('yasminxsikdar245@exdonuts.com', '#xpranto@25#'),
]
instas = {
    'last_connected': 19,
    'accounts': [
        ('skjbdcoerinverweoir0', 'FGbEQpMUL'),
        ('skjbdcoerinverweoir2', '5G6puvxeD7b'),
        ('skjbdcoerinverweoir5', 'mkoOcAYaQSB'),
        ('skjbdcoerinverweoir6', 'eyaqsFDxK9'),
        ('skjbdcoerinverweoir13', 'BPCNR3Mm5'),
        ('skjbdcoerinverweoir16', '5Afxp0sDQ'),
        ('skjbdcoerinverweoir18', 'O8AjaTMhpr'),
        ('skjbdcoerinverweoir19', 'd9EnXxVb0j'),
        ('skjbdcoerinverweoir20', '4UlwcxKQcc'),
        ('skjbdcoerinverweoir21', 'pVUCMFeFwPt'),
        ('skjbdcoerinverweoir23', 'PfRYvla5C'),
        ('skjbdcoerinverweoir24', 'cUVuj07Lk'),
        ('skjbdcoerinverweoir25', 'voWrofYpepV'),
        ('skjbdcoerinverweoir28', 'cfmrvo8h'),
        ('skjbdcoerinverweoir31', 'UxB8nYCSkoG'),
        ('skjbdcoerinverweoir33', 'Vngnd8A2'),
        ('skjbdcoerinverweoir34', 'jKRrRqngL'),
        ('skjbdcoerinverweoir35', 'KU9KpVHZ1vh'),
        ('skjbdcoerinverweoir36', '82pDcSTM'),
        ('skjbdcoerinverweoir37', 'TidSta9ykx'),
        ('skjbdcoerinverweoir38', 'fEaRucC8UoP'),
        ('skjbdcoerinverweoir39', 'hX8DA4I9'),
        ('skjbdcoerinverweoir40', 'zCZVYNV0W'),
        ('skjbdcoerinverweoir47', 'lIaiqvuX'),
        ('skjbdcoerinverweoir48', 'YUypiYh51U6'),
        ('skjbdcoerinverweoir49', 'jYXCAfiAj'),
        ('skjbdcoerinverweoir51', 'bKG6V0RKTk'),
        ('skjbdcoerinverweoir53', 'SYKZ1cLwndP'),
        ('skjbdcoerinverweoir55', 'otAhDQ8NKBL'),
        ('skjbdcoerinverweoir56', 'ZInSXR4bo'),
        ('skjbdcoerinverweoir58', 'qZZV84uYsN'),
        ('skjbdcoerinverweoir62', '87hFrbH2Qv'),
    ]
}

results = dict()
for i in range(len(fbs)):
    print(change_vpn())
    fb = fbs[i]
    results[i], page_name = facebook(fb)
    if results[i] == True:
        print(i, results[i], fb, instas['accounts'][instas['last_connected']], page_name)
    else:
        print(i, results[i], fb)
    print(datetime.datetime.fromtimestamp(int(time.time())), '\n\n')

print(time.time()-start)
print(results) 



time.sleep(30)


## PUT MANAGEMENT EMAIL IN BIO FOR PROMO (OR MANAGE DMS)


### For creating instas
instas = [
    ('helen9adamsrow', 'RZ3XbsDg51J'),
    ('margaret8johnsonxtk', 't8LGGEqyunx'),
    ('lisa2pereztsl', 'zRwsnZUVio'),
    ('helen9harrisulj', '1SwRv6kdbg0'),
    ('jennifer4thompsonomx', 'U4k4jrJOV'),
    ('karen5lopezdrx', 'edGXirIEXT'),
    ('ruth3nelsonili', 'qBRGIbauM'),
    ('linda9harriskhf', 'kMA8l9uD'),
    ('laura7hillvpu', 'GN046OF14P'),
    ('lisa6rodriguezemp', '09Zn3bjGl'),
    ('karen2leeceh', '6fzNMvLzu'),
    ('margaret4phillipsuai', '7oXRZgwN53D'),
    ('donna1robertsihc', 'TnepMsF7nX'),
    ('mary0martinezyfb', 'N930kMezRiZ'),
    ('jennifer0adamsfin', 'giDeAwJLMN'),
    ('susan0kingurz', 'pThp8K0qR'),
    ('sandra2hallswl', 'EWEHJr836Jy'),
    ('carol5harrisgnx', 'Qeom4Mt6Ru'),
    ('donna4adamsmgf', 'r2QB2qt6e'),
    ('lisa9campbellrft', 'e9BE3PntT'),
    ('betty5taylorwoo', 'huBLgmUHVjS'),
    ('patricia8brownraj', 'ePgwPxPU5J'),
    ('nancy4williamsbys', 'PBIxoxIQAl'),
    ('lisa7scottedh', 'msrGbxgch6A'),
    ('susan5johnsonjpp', 'jsxwLVSLoY'),
    ('mary1brownzwt', 'Q1XgyCls'),
    ('linda0greenrgt', 'LBNrhRTIYVc'),
    ('carol9brownwjm', 'R0Bgsy0e3p'),
    ('kimberly9kingtaw', 'pICQyTlWC'),
    ('helen0lewisssm', 'ndoJFpiek'),
    ('sarah0collinspal', 'EMYSIjR2tD'),
    ('sandra9adamsznb', 'ITT2rcedp'),
    ('karen7wrightaeh', 'jH07xXHw'),
    ('michelle3carteroae', '8UkbStfC7'),
    ('sarah4taylorxfm', 'fSKOFfy2q'),
    ('donna1mitchellkts', 'Hg02lT7rzu'),
    ('elizabeth2martineztto', 'OHn0g9sOC7n'),
    ('kimberly1jacksonaaw', 'rUT8l1SCU'),
    ('kimberly2millerrtk', 'C7MExn2f'),
    ('jennifer3turnerepv', 'q5aUa47wHYa'),
    ('nancy2evansrwp', '3tCOXC4hb'),
    ('deborah2johnsonnyy', 'C4N5admfY'),
    ('maria9edwardsmzt', 'QOGGV2ltIC'),
    ('betty0harriszru', 'sE7pyz6rhbT'),
    ('betty5mitchellccz', 'aTROUVXkP'),
    ('michelle8andersonkhk', 'RuYT8rFLi'),
    ('deborah0perezbnb', 'N7MrcXClms'),
    ('maria0scottjxq', 'MG4OARyLFz'),
    ('sharon0lewisuwe', 'm0mGM8H1ls'),
    ('sharon6martineztfk', 'apqdBxGpA'),
#     ('deborah9andersonavl', 'GLq98GPB9Dl'),
#     ('mary7andersonbwl', 'Q8vJJUH1PYz'),
#     ('maria5nelsonrja', 'fEGvGo9uBX'),
#     ('susan2mitchellbud', 'tbB2nQSud'),
#     ('jennifer5martinezyhn', '10Hv3TuOd'),
#     ('nancy5younggdm', 'L1iXll5c1G'),
#     ('barbara9adamstkc', 'WMwEMxYjKM'),
#     ('carol7allencht', 'wkgHcWABxP'),
#     ('elizabeth2gonzalezjvb', '928NKHwmXm'),
#     ('laura6robertstzy', 'CCLS5LwWc'),
#     ('carol4johnsonzdc', '18Z8J4nokbu'),
#     ('lisa0harriseyc', 'GnlnIMT276l'),
#     ('sarah1edwardsvoz', 'Att7v2cTCh'),
#     ('michelle7hillvty', 'zZwltJ0Awk6'),
#     ('helen7taylorjrh', '8DapNVtO'),
#     ('ruth0smithjfu', 'N8hTiCfCPX'),
#     ('barbara2adamsdzt', 'E2hlbFJi24'),
#     ('susan1mitchellxfj', 'LIQwmniGRc'),
#     ('sharon8evansjjk', 'NaeFVm3lL'),
#     ('lisa7taylorqir', 'W1Okp6YG1'),
#     ('margaret5campbelllbl', 'j9Q2fxXGH04'),
#     ('carol1harrisgfk', 'CYcfKAuyBSI'),
#     ('nancy5evansdji', '2JU01M2yRyy'),
#     ('nancy8jacksonkhc', 'p5mqOkmh'),
#     ('maria5lewisioe', '7pyVEikMFb'),
#     ('deborah6bakerikn', 'tZhu39rHF'),
#     ('nancy2lewisoyp', '1OalICrh2Jc'),
#     ('maria8smithkup', '5XQHomaHgh5'),
#     ('betty8mitchellvzm', 'fyvXXEoi'),
#     ('betty1carterfdm', 'QCaDKbCOX'),
#     ('linda5mooreqkz', 'jMusydAts'),
#     ('margaret1johnsonuil', 'A0XSmef6KDW'),
#     ('ruth9kingsgz', 'EyUU3Z1HYl7'),
#     ('linda5edwardsyio', '79RUkBQJH'),
#     ('lisa8wilsonjtr', 'SMiAzfSPJ'),
#     ('laura8turnerwik', 'L8VMXuQ7QC'),
#     ('betty8hernandezqip', 'F0QhT4wDU'),
#     ('deborah2perezpqa', 'et2HwuduKT'),
#     ('susan7collinsosi', 'DVY3FxJibxc'),
#     ('linda9cartergkh', 'o1ozqFHG1z7'),
#     ('jennifer5gonzalezskc', 'fAt0z3gWQ'),
#     ('lisa2evansaab', 'fzxcqTfZrCk'),
#     ('ruth.9moorezam', 'mLaIpSVEz'),
#     ('ruth2youngykm', '2KIdZKvf1IY'),
#     ('linda6rodriguezody', 'AFAT86L3GQ'),
#     ('jennifer9thompsonwvl', 'JRLGmpEl9A'),
#     ('barbara8taylorrrm', 'AiWaUTire'),
#     ('sarah7robinsonnwu', 'zRqvICjD6w'),
#     ('deborah6walkerkth', 'rSyRex1ft5'),
#     ('mary5martinezbvl', 'Z16PwE1BEvc'),
#     ('dorothy7andersonhlh', 'R1ITocGvhD'),
#     ('nancy6scottafd', 'K6M6Z72Cj2M'),
#     ('dorothy8collinsmia', 'yDvegpLT8'),
#     ('donna1johnsonfyu', 'k5gBUiUXMMK'),
#     ('donna7collinstme', 'HiPq1EvCLRx'),
#     ('deborah2collinsurb', 'DC0eBUiTH'),
#     ('sharon5millerwkx', 'nwL7dlwuC'),
#     ('sarah0wilsonrzt', 'VISXJGOW3'),
#     ('barbara6turnermnr', '2bBGGLzl'),
#     ('elizabeth9carterrkf', 'JYCitRo9Tcp'),
#     ('sharon8bakerecr', 'EaubYVfjj'),
#     ('margaret5taylorscw', 'JcAEcD6sgqY'),
#     ('nancy7evansday', 'R7Gv5ZjpqC8'),
#     ('sharon4wrightdqk', '19HBE5f617'),
#     ('donna1hernandezmkp', 'VVGN62knB'),
#     ('carol4hernandezwtz', 'ITeAkCFHmYn'),
#     ('ruth1clarkkjn', 'UPIBNtjT3'),
#     ('margaret1robinsonfci', 'q3O4jgPGN'),
#     ('sarah0millerfaz', 'ltWI6fMwH'),
#     ('patricia5moorekqx', 'BzYMe0lq'),
#     ('sarah2milleraqo', '71noXCSU4si'),
#     ('helen1smithezp', 'vZPMsU872'),
#     ('linda2edwardswoz', 'UmHSZDSUDsn'),
#     ('jennifer8harrisevo', 'dFRTkrVnY'),
#     ('susan3robertsgnm', 'rFaFLZwG'),
#     ('nancy0carterucv', 'FBcEpbh7B'),
#     ('nancy3gonzalezsnj', 'SERtHIygEiH'),
#     ('linda1hernandezdcz', '9agVeoCGeoc'),
#     ('betty8campbellrud', '8ZvhnPwXv'),
#     ('sandra7adamsscu', 'RscbbpZFco'),
#     ('dorothy0davisgbx', 'JE11c8O6Z'),
#     ('sharon6youngxsv', 'IPFMFvD6KET'),
#     ('helen9smithndv', 'UELgqRxk8'),
#     ('barbara6williamswrs', 'VqbHEp4FGk'),
#     ('sharon2robertsesg', 'tlpBdanYdHb'),
#     ('sharon9campbellxgn', 'aLZSWp7Bt'),
#     ('karen8greenelr', 'gj9mLN1pEF'),
#     ('deborah6jonesjyq', 'zqay1Ksgr'),
#     ('susan8hernandezlsk', 'j0KTvjhME0'),
#     ('sandra8clarkylx', '34xCdle7U'),
#     ('betty6thomasxhz', 'ICEOHJfLzYD'),
#     ('patricia9jacksondjr', 'vT0ugntAO'),
#     ('ruth7carterpdu', 'zw8YOh5L67v'),
#     ('helen2nelsonirl', 'AXlTbY1wH'),
#     ('maria3hillosz', 'NcLZLhC0Wy'),
#     ('kimberly2carterscp', 'PiBHXxcdr'),
#     ('maria6millerjeg', 'NanEFZjM7O'),
#     ('laura7jacksonazm', 'z3unwRwMaV'),
#     ('karen0perezdeb', 'kRexmitDi'),
#     ('donna2thomaszcc', 'MqbfPZnG8pZ'),
]
new_infos = [(f'aeorfutttggoenibar{i}',f'Testing {i}',f'{i}th one yippie yip',True) 
             for i in range(50)]
results = dict()

# pfp_directory = 'PFPs'
# orig_file = f'{pfp_directory}/moremarionovembre.jpg'
# for new_info in new_infos:
#     name = new_info[0]
#     new_file = f'{pfp_directory}/{name}.jpg'
#     shutil.copy(orig_file, new_file)


####################
# Make sure tempPFPs is the default folder
####################
for i in range(len(new_infos)):
    print(change_vpn())
    insta = instas[i]
    new_info = new_infos[i]
    results[i] = instagram(insta, new_info)
    print((insta, new_info), results[i])
    print(datetime.datetime.fromtimestamp(int(time.time()-start)), '\n\n')

print(time.time()-start)
print(results)