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




start = time.time()
my_keyboard = keyboard.Controller()
my_mouse = mouse.Controller()

## VPN (todo)
def change_vpn():
    countries = [
        # 'France', 
        'Greece',
        # 'Iceland', 
        'Israel',
        'Mexico',
        # 'Norway',
        'Slovenia',
        'South Korea',
        # 'Spain',
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
        return len([t for t in text if not match(t, result, similarity)]) == 0

def match(text, result, similarity):
    if similarity == 1:
        return text in result
    
    if similarity == 'flexible':
        return len(fuzzysearch.find_near_matches(text, result, max_l_dist=2)) > 0

## Facebook Functions
def facebook(fb_creds): #Big Boy
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
        return facebook(fb_creds)
    
    ## Sign into facebook
    enter_facebook_credentials(fb_creds)
    if not catch_fb_cookie_popup('Welcome to Facebook,', type = 'contains', tries = 15): return close_page(False), 0

    ## Start to create page
    go_to_create_page()
    if not catch_fb_cookie_popup(f'{directory}/Page name.png'): return close_page(False), 0

    ## Submit page
    page_name = add_and_submit_page_details()
    pyautogui.moveTo(200, 100)
    if not catch_fb_cookie_popup(f'{directory}/Next.png', tries = 12): return close_page(False), 0

    ## Finish page setup
    continue_page_setup()
    if not catch_fb_cookie_popup('Manage Page', type = 'contains', tries = 15): return close_page(False), 0

    ## Go to link instagram:
    visit_link_instagram()
    if not catch_fb_cookie_popup(['Connect', 'ccount', 'stagram'], type = 'contains', tries = 15, similarity = 'flexible'): return close_page(False), 0

    ## Connect account steps:
    connect_account_steps()
    if not catch_ig_cookie_popup(f'{directory}/IG prompt.png', 20): return close_page(False), 0 ##Might need 2? check this

    ## Enter instagram login
    instas['last_connected']+=1
    print("instas['last_connected']:", instas['last_connected'])
    enter_instagram_credentials(instas['accounts'][instas['last_connected']])
    if not catch_ig_cookie_popup(['Home', 'Search'], type = 'contains', tries = 5, ignore_refresh = True):
        enter()
        if not catch_ig_cookie_popup(['Home', 'Search'], type = 'contains', tries = 10, ignore_refresh = False): return close_page(False, 2), 0

    ## Select not now and confirm success
    if not (catch_ig_cookie_popup(f'{directory}/Not now.png', tries = 6) or 
            catch_ig_cookie_popup(f'{directory}/Not now2.png', tries = 6)): return close_page(False, 2), 0

    ## Confirm it says success
    connected = pause_for(f'{directory}/IG connected.png', 10)
    pause_for(f'{directory}/Account connected done.png',4)

    review_needed = pause_for(f'{directory}/Review needed.png', 2)

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
    if not pause_for('button_icons/incognito/incognito.png', tries = 5): return close_page(False)

    directory = 'button_icons/instagram_account_info'

    ## Checks instagram is loaded
    load_instagram()
    if not catch_ig_cookie_popup(f'{directory}/Insta Log In.png', tries = 10): return close_page(False)

    ## Sign into instagram
    enter_instagram_credentials(insta_creds)
    if not catch_ig_cookie_popup(['Home', 'Search'], type = 'contains', tries = 5, ignore_refresh = True):
        enter()
        if not catch_ig_cookie_popup(['Home', 'Search'], type = 'contains', tries = 5, ignore_refresh = True): return close_page(False)

    ## Start to switch to business account
    go_to_switch_business()
    if not catch_ig_cookie_popup('Business', type = 'contains', tries = 15): return close_page(False)

    ## Finish switching to business account
    finish_switching()
    if not catch_ig_cookie_popup('Switch to personal account', type = 'contains', tries = 15): return close_page(False)

    ## Finish updating account info
    if update_account_info(new_account_info) != 'Account Center':
        if not catch_ig_cookie_popup(new_account_info[:3], type = 'contains', tries = 5, similarity = 'flexible'): return close_page(False)

    return close_page(True)

def load_instagram():
    searchbar()
    time.sleep(1)

    type('https://www.instagram.com/')
    time.sleep(1)

    enter()
    time.sleep(2)   

def enter_instagram_credentials(insta_cred):
    time.sleep(1)

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

def finish_switching():
    directory = 'button_icons/instagram_business_account'
    pause_for(f'{directory}/Business.png', 5)
    pause_for(f'{directory}/Next.png', 5)
    pause_for(f'{directory}/Next.png', 5)
    pause_for(f'{directory}/Art.png', 5)
    pause_for(f'{directory}/Done.png', 5)
    pause_for(f"{directory}/Don't use.png", 5)
    pause_for(f'{directory}/Done.png', 5)

def update_account_info(insta_info): #For this to work, make sure that PFP is on 
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
    catch_ig_cookie_popup(f'{directory}/X account center.png', tries = 2)
    if catch_ig_cookie_popup('Manage your connected', type = 'contains', tries = 3): #Then AC
        #Do pfp and bio first
        if update_pfp:
            # pause_for(f'{directory}/AC change pfp.png')
            update_pfp_on_account(username, AC = False)
            # update_pfp_on_account(username, AC = True)
            # pause_for(f'{directory}/AC save.png')

        pause_for(f'{directory}/Bio.png', 3)
        select_all()
        time.sleep(0.5)
        type(bio)
        time.sleep(0.5)
        pause_for(f'{directory}/Submit.png', 3)
        pause_for(f'{directory}/Profile saved.png', 15)
        
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

        time.sleep(1)
        return "Account Center"

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
        if pause_for(f'{directory}/Profile saved.png', 15):
            time.sleep(1)
            return 'PROFILE SAVED'
    


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

def catch_ig_cookie_popup(file, tries=10, type = 'pause', similarity = 1, ignore_refresh = False):
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
            if _%3 == 0: click('button_icons/IG Essential cookies.png') 
            elif _%3 == 1: click('button_icons/IG Essential cookies2.png')
            else: click('button_icons/instagram_account_info/No notifications.png')
        except:
            pass
        time.sleep(1)
        if _ == tries//2 and not ignore_refresh:
            reload()
    return False

def close_page(bool = False, times = 1):
    pause_for('button_icons/Close incognito1.png', 2)
    pause_for('button_icons/Close incognito2.png', 2)
    pause_for('button_icons/Leave.png', 2)
    # for _ in range(times):
    #     my_keyboard.press(Key.cmd)
    #     my_keyboard.press('w')
    #     my_keyboard.release('w')
    #     my_keyboard.release(Key.cmd)
    #     time.sleep(2)

    #     if not pause_for('button_icons/Leave.png', 2):
    #         enter()
    #     time.sleep(2)
    return bool

## This alternates between checking for cookie and checking for result we want.
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

def fb_login(fb_cred, tries = 0):
    if(tries == 2):
        return 'FB LOGIN FAILED'
    
    directory = 'button_icons/facebook'
    searchbar()
    time.sleep(1)

    type('https://www.facebook.com/?sk=welcome')
    time.sleep(1)

    enter()
    time.sleep(2)

    catch_fb_cookie_popup()
    if not pause_for(f'{directory}/facebook.png', 10):
        reload()
        time.sleep(8)
        return fb_login(fb_cred, tries = tries+1)

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

    if pause_for(f'{directory}/Welcome.png', 5):
        return 'FB LOGIN SUCCESSFUL'
    elif contains('Welcome to Facebook,'):
        return 'FB LOGIN SUCCESSFUL'
    
    return fb_login(fb_cred, tries = tries+1)

def create_page():
    directory = 'button_icons/facebook'
    searchbar()
    time.sleep(1)

    type('https://www.facebook.com/pages/creation/?ref_type=launch_point')
    time.sleep(1)

    enter()
    pause_for(f'{directory}/Page name.png')

    page_name = 'goodpage' + str(int(1000000 + random.random()*9000000))
    type(page_name)
    time.sleep(1)

    pause_for(f'{directory}/Category.png')
    type('des')
    pause_for(f'{directory}/Design.png')

    pause_for(f'{directory}/Create page.png')
    my_mouse.position = (100,100)

    if pause_for(f'{directory}/Too many pages.png', 2):
        return 'TOO MANY PAGES', page_name
    
    if pause_for(f'{directory}/Account restricted.png', 2):
        return 'ACCOUNT RESTRICTED', page_name
    
    if not pause_for(f'{directory}/Next.png', 10): return 'PAGE FAILED', page_name
    if not pause_for(f'{directory}/Next.png', 5): return 'PAGE FAILED', page_name
    if not pause_for(f'{directory}/Skip.png', 5): return 'PAGE FAILED', page_name
    if not pause_for(f'{directory}/Next.png', 5): return 'PAGE FAILED', page_name
    if not pause_for(f'{directory}/Done.png', 5): return 'PAGE FAILED', page_name
    if not pause_for(f'{directory}/Not now fb page.png', 15): return 'PAGE FAILED', page_name
    return 'PAGE CREATED', page_name

def link_account(tries = 0):
    if(tries == 2):
        return 'LINKING INITIATION FAILED'
    
    directory = 'button_icons/facebook'

    searchbar()
    time.sleep(1)

    type('https://www.facebook.com/settings/?tab=linked_instagram')
    time.sleep(1)

    enter()

    if not pause_for(f'{directory}/Connect account.png', 10): link_account(tries = tries +1) 
    if not pause_for(f'{directory}/Connect.png'): link_account(tries = tries +1) 
    if not pause_for(f'{directory}/Confirm.png'): link_account(tries = tries +1) 

    return 'LINKING INITIATION SUCCESSFUL'

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

    if not pause_for(f'{directory}/Not now.png', 10):
        reload()
        pause_for(f'{directory}/Not now.png', 10)
    connected = pause_for(f'{directory}/IG connected.png', 10)
    pause_for(f'{directory}/Account connected done.png',4)

    review_needed = pause_for(f'{directory}/Review needed.png', 2)
    
    if connected and not review_needed:
        return 'ACCOUNT CONNECTED'
    else:
        return 'ACCOUNT CONNECTION FAILED'


def regular_ig_login(insta_cred, tries = 0):
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

    catch_ig_cookie_popup()
    if pause_for(f'{directory}/IG successful login.png', 5): ## Now you're logged into instagram
        return True
    elif pause_for(f"{directory}/Couldn't connect.png", 3):
        pass
    elif pause_for(f"{directory}/Incorrect password.png", 3):
        return 'INCORRECT PASSWORD'
    elif pause_for(f"{directory}/Account suspended.png", 3):
        return 'ACCOUNT SUSPENDED'
    
    if(tries == 2):
        return 'FIRST INSTAGRAM LOGIN FAILED'
    return regular_ig_login(insta_cred, tries = tries+1)

def switch_logged_in_instagram_to_business():
    directory = 'button_icons/instagram_business_account'
    searchbar()
    time.sleep(1)

    type('https://www.instagram.com/accounts/convert_to_professional_account/')
    time.sleep(1)

    enter()

    catch_ig_cookie_popup()
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
    time.sleep(3)


### Get more good cheap instas https://accsmarket.com/en/catalog/instagram/pva 
### Also, fully automate by getting their name, pfp from tiktok, make some generic bio formula,
### And while creating a new account you can easily test available usernames from the ten we might want
### Bio formula should include not impersonating.


## Complex Processes
#Incomplete
def update_instagram_settings(insta_cred, new_account_info):
    open_incognito_window()
    login_result = regular_ig_login(insta_cred[:2]) 
    if login_result in ['ACCOUNT SUSPENDED', 'FIRST INSTAGRAM LOGIN FAILED', 'INCORRECT PASSWORD']: 
        close_page()
        return login_result

    switch_logged_in_instagram_to_business() # Now we should be automatically redirected here https://www.instagram.com/accounts/edit/
    update_account_info(new_account_info)
    close_page()
    return True

    # Need to (1) figure out how to select pfp in our filesystem (or some other solution)
    # (2) verify usernames are available ahead of time

#Complete
def add_fb_page_and_link_instagram(fb_creds, insta_creds):
    open_incognito_window()
    login_result = fb_login(fb_creds)
    if login_result in ['FB LOGIN FAILED']: return login_result, None

    page_result, page_name = create_page()
    if page_result in ['TOO MANY PAGES', 'ACCOUNT RESTRICTED', 'PAGE FAILED']:
        close_page()
        return page_result, None
    
    link_initiation_result = link_account()
    if link_initiation_result in ['LINKING INITIATION FAILED']:
        close_page()
        return link_initiation_result, None
    
    result = fb_connect_ig_login(insta_creds)
    if result in ['ACCOUNT CONNECTION FAILED']:
        close_page()
        return result, None
    if result in ['ACCOUNT CONNECTED']:
        close_page()
        return result, page_name
    
    return "SOMETHING WENT WRONG"


# from pandas.io.clipboard import clipboard_get
# text = clipboard_get()                                                     
# print(text)

time.sleep(4)
# directory = 'button_icons/facebook'
# x = facebook(('VullnetBakux@outlook.com', 'xpranto@#25'))
# print(x)

fbs = [
    # ('nogix74525@xrmop.com', 'aldjdkdb472#@'),
    # ('mameda7607@xrmop.com', 'sodjdkdsjdk2938#'),
    # ('mijelif653@xrmop.com', 'sldjfj2837#@'),
    # ('mohig22298@wmila.com', 'lsjfjfdkd273#'),
    # ('sicav76156@xrmop.com', 'aldofjfks2773#'),
    # ('mebekij257@xrmop.com', 'lsjdfivj1262#@'),
    # ('jadifam323@trejni.com', 'vssbsggGshzfGsgz'),
    # ('xiyace1378@tajwork.com', 'qwteurvcdd'),
    # ('sacofa8303@trejni.com', 'xxbncnfruhr.'),
    # ('nodareb791@trejni.com', 'teurititi'),
    # ('pajew90939@trejni.com', 'cdhfjfkfg'),
    # ('kewaxe2906@tajwork.com', 'tehfngn'),
    # ('yeyow90065@trejni.com', 'cdbfngnn'),
    # ('satida4960@trejni.com', 'vdjfjgkt'),
    # ('waweyoj590@trejni.com', 'vxbxncn'),
    # ('giyiyo7403@tajwork.com', 'ggdhdjfj'),
    # ('nohese5524@trejni.com', 'dvjfjgjte'),
    # ('cagelop177@tajwork.com', 'yritktuy'),
    # ('nabafi1763@trejni.com', 'gdjrjtje'),
    # ('jitiwak206@tajwork.com', 'fdhfjgk'),
    # ('haget59461@tajwork.com', 'erhtvyc'),
    # ('fidil66995@trejni.com', 'trititr'),
    # ('gakana5302@tajwork.com', 'eeuriti'),
    # ('larewes754@tajwork.com', 'gdjdifig'),
    # ('tasaxo8188@tajwork.com', 'yritoyooy'),
    # ('porojat143@tajwork.com', 'vshdjfjjf'),
    # ('toxakid701@trejni.com', 'zccbnnfut'),
    # ('sigiwe4210@tajwork.com', 'deuritit'),
    # ('hitexon827@tajwork.com', 'fdjfkkgk'),
    # ('wigecax660@trejni.com', 'gdjgjyjuj'),
    # ('harhmousumi3@gmail.com', 'Swas#237'),
    # ('xeses71014@zufrans.com', 'Alexcaf543'),
    # ('seanwilson333222@gmail.com', 'seanwilson3211233'),
    # ('coreymjohnson677@gmail.com', '1818512429'),
    ('shimaggq134@simaenaga.com', '#xpranto@25#'),
    ('shimaxc16161@simaenaga.com', '#xpranto@25#'),
    ('mimxbb1818@simaenaga.com', '#xpranto@25#'),
    ('yagoj96926@xrmop.com', '#xpranto@25#'),
]
instas = {
    'last_connected': 13,
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









#### For creating instas
# instas = [
#     ('smithsteven6r4e7e', 'FGbEQpMUL'),
#     ('wrightjeffuukitn', 'yAJBnd2m'),
#     ('nelsonlindaedfgf6', '5G6puvxeD7b'),
#     ('bakermargaretiabh8c', 'ywMoEim00'),
#     ('robertspaul7dmnif', 'sacjS9OA3'),
#     ('jacksonmichaelnvtfdp', 'mkoOcAYaQSB'),
#     ('mooremichelleb5ykoh', 'eyaqsFDxK9'),
#     ('brownmichaelvyckgm', 'IPnjlEJs7n6'),
#     ('parkerbarbara9gx8ov', '56uNz7tHY'),
#     ('joneshelenuhvapx', 'e4UMdvL0z'),
#     ('carterkarenmcq8tt', 'G0Ka0xgz'),
#     ('thompsonruthyziipk', 'JpXaTMCy3'),
#     ('carterkimberlyeobhay', 'nMAmSCFfK'),
#     ('rodriguezedward1vf1ae', 'BPCNR3Mm5'),
#     ('martinanthonyij98u2', 'dFFTIb2av4'),
#     ('moorekaren6yt4g2', 'VXCViARV4W'),
#     ('greenjamesc6avz7', '5Afxp0sDQ'),
#     ('pereznancyodo6vb', 'QIxoMmSOidj'),
#     ('moorekennethsz2a3l', 'O8AjaTMhpr'),
#     ('bakerdonna2nuanz', 'd9EnXxVb0j'),
#     ('allenjamesswf7ty', '4UlwcxKQcc'),
#     ('mitchellcaroluxw2oy', 'pVUCMFeFwPt'),
#     ('rodriguezrichardaj1lqx', 'uzJCYE3RQ'),
#     ('robertsnancya8xx1x', 'PfRYvla5C'),
#     ('jacksonrobert4n38pv', 'cUVuj07Lk'),
#     ('johnsonpatriciann6yzn', 'voWrofYpepV'),
#     ('hernandezcharlesox4cz1', 'dpt7ANXFnEl'),
#     ('bakerlaurajy43vb', 'pGVHfShG4bf'),
#     ('edwardsrobert7kfnos', 'cfmrvo8h'),
#     ('phillipskimberly74zh7q', 'aFW7OHP6C'),
#     ('gonzalezjeffz11nsf', 'S1ZAlix4'),
#     ('martinsandraefaj2s', 'UxB8nYCSkoG'),
#     ('adamslauraz7eczn', 'u4M1iOW0'),
#     ('evansbettysbdexc', 'Vngnd8A2'),
#     ('brownelizabethgedprt', 'jKRrRqngL'),
#     ('joneskimberly7p74wu', 'KU9KpVHZ1vh'),
#     ('wilsonwilliamydeji9', '82pDcSTM'),
#     ('martinsarah5txwlv', 'TidSta9ykx'),
#     ('martinezjoseph6nn7wr', 'fEaRucC8UoP'),
#     ('hernandezsharon7wrf3m', 'hX8DA4I9'),
#     ('bakergeorgehxqsup', 'zCZVYNV0W'),
#     ('whitedonnacl737w', '81IGJM3e'),
#     ('hillwilliampgjtq4', 'BuNr2v2lgrL'),
#     ('robertsjameshsw8e5', 'Zm58nzwv'),
#     ('smithdonaldsi46di', 'AFvqkNlDSuY'),
#     ('thomasjennifertru171', '6yxuCvsY'),
#     ('mitchellronaldfhptwj', 'osNTtTv1O7'),
#     ('perezjoseph493m5y', 'lIaiqvuX'),
#     ('johnsonanthony3i65ej', 'YUypiYh51U6'),
#     ('greenkevin8va9wf', 'jYXCAfiAj'),
#     ('smithbarbarayoxnou', '0VZRzZMd'),
#     ('wilsonnancyiedk84', 'bKG6V0RKTk'),
#     ('parkerjameszii8mm', 'R8hjFdEZyU'),
#     ('harrischarleszoh1k5', 'SYKZ1cLwndP'),
#     ('robertsjasonu4w7yt', '1TInZmvmrds'),
#     ('thomasjames6s38g4', 'otAhDQ8NKBL'),
#     ('youngjohn2j853b', 'ZInSXR4bo'),
#     ('thompsonmargaretrm5w1x', 'v8UjSDnj'),
#     ('wilsonpaulw5vp65', 'qZZV84uYsN'),
#     ('robinsonbettye7vw8w', 'bJD8lw7rNvz'),
#     ('wilsoncarol5rto5t', '1uhOrgpKSc'),
#     ('turnerkimberlyhx17n4', 'pFIQKgxa9Eh'),
#     ('bakerhelen169gzl', '87hFrbH2Qv'),
#     ('wilsonmichaelt2pnhu', 'cFRtFSYgON'),
#     ('perezdavidy7918q', 'wJEZxyuo'),
#     ('allenkennethtlmgum', 'jMzBPpsCM'),
# ]
# new_infos = [(f'skjbdcoerinverweoir{i}',f'Testing {i}',f'{i}th one dun gucc gucci',True) 
#              for i in range(66)]
# results = dict()

# ####################
# # Make sure tempPFPs is the default folder
# ####################
# for i in [1, 3, 4, 7, 8, 9, 10, 11, 12, 14, 15, 17]:
#     print(change_vpn())
#     insta = instas[i]
#     new_info = new_infos[i]
#     results[i] = instagram(insta, new_info)
#     print((insta, new_info), results[i])
#     print(datetime.datetime.fromtimestamp(int(time.time())), '\n\n')

# print(time.time()-start)
# print(results)