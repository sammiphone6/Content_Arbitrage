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


start = time.time()
my_keyboard = keyboard.Controller()
my_mouse = mouse.Controller()


## VPN (by clicking NordVPN App)
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
    print(1)
    for _ in range(3):
        print(pause_for(f'button_icons/Nord/{country}.png', tries = 5))
        print(2)
        time.sleep(2)
    
    for _ in range(2):
        print(3)
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
    print(4)
    return country

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
    if not pause_for('button_icons/incognito/incognito.png', tries = 5):
        close_page(False)
        change_vpn()
        return instagram(insta_creds, new_account_info)

    directory = 'button_icons/instagram_account_info'

    ## Checks instagram is loaded
    load_instagram()
    if not catch_ig_cookie_popup(f'{directory}/Insta Log In.png', tries = 10): 
        close_page(False)
        change_vpn()
        return instagram(insta_creds, new_account_info)

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
    if not catch_ig_cookie_popup('Switch to personal account', type = 'contains', tries = 22, similarity='flexible'): return close_page(False)

    ## Finish updating account info
    time.sleep(4)
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
    if tries == 2:
        return
    
    directory = 'button_icons/instagram_business_account'
    if not pause_for(f'{directory}/Business.png', 10): return finish_switching(tries = tries+1)
    if not pause_for(f'{directory}/Next.png', 10): return finish_switching(tries = tries+1)
    if not pause_for(f'{directory}/Next.png', 10): return finish_switching(tries = tries+1)
    if not pause_for(f'{directory}/Art.png', 20): return finish_switching(tries = tries+1)
    if not pause_for(f'{directory}/Done.png', 10): return finish_switching(tries = tries+1)
    if not pause_for(f"{directory}/Don't use.png", 10): return finish_switching(tries = tries+1)
    if not pause_for(f'{directory}/Done.png', 10): return finish_switching(tries = tries+1)

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
    if catch_ig_cookie_popup('Manage your connected', type = 'contains', tries = 3, similarity='flexible'): #Then AC
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
        return len([t for t in text if not match(t, result, similarity)]) == 0

def match(text, result, similarity):
    if similarity == 1:
        return text in result
    
    if similarity == 'flexible':
        return len(fuzzysearch.find_near_matches(text, result, max_l_dist=2)) > 0

## This alternates between checking for cookie and checking for result we want.
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
    pause_for('button_icons/Close incognito1.png', 2)
    pause_for('button_icons/Close incognito2.png', 2)
    pause_for('button_icons/Leave.png', 2)
    return bool




time.sleep(4)



# fbs = [
#     # ('nogix74525@xrmop.com', 'aldjdkdb472#@'),
#     # ('mameda7607@xrmop.com', 'sodjdkdsjdk2938#'),
#     # ('mijelif653@xrmop.com', 'sldjfj2837#@'),
#     # ('mohig22298@wmila.com', 'lsjfjfdkd273#'),
#     # ('sicav76156@xrmop.com', 'aldofjfks2773#'),
#     # ('mebekij257@xrmop.com', 'lsjdfivj1262#@'),
#     # ('jadifam323@trejni.com', 'vssbsggGshzfGsgz'),
#     # ('xiyace1378@tajwork.com', 'qwteurvcdd'),
#     # ('sacofa8303@trejni.com', 'xxbncnfruhr.'),
#     # ('nodareb791@trejni.com', 'teurititi'),
#     # ('pajew90939@trejni.com', 'cdhfjfkfg'),
#     # ('kewaxe2906@tajwork.com', 'tehfngn'),
#     # ('yeyow90065@trejni.com', 'cdbfngnn'),
#     # ('satida4960@trejni.com', 'vdjfjgkt'),
#     # ('waweyoj590@trejni.com', 'vxbxncn'),
#     # ('giyiyo7403@tajwork.com', 'ggdhdjfj'),
#     # ('nohese5524@trejni.com', 'dvjfjgjte'),
#     # ('cagelop177@tajwork.com', 'yritktuy'),
#     # ('nabafi1763@trejni.com', 'gdjrjtje'),
#     # ('jitiwak206@tajwork.com', 'fdhfjgk'),
#     # ('haget59461@tajwork.com', 'erhtvyc'),
#     # ('fidil66995@trejni.com', 'trititr'),
#     # ('gakana5302@tajwork.com', 'eeuriti'),
#     # ('larewes754@tajwork.com', 'gdjdifig'),
#     # ('tasaxo8188@tajwork.com', 'yritoyooy'),
#     # ('porojat143@tajwork.com', 'vshdjfjjf'),
#     # ('toxakid701@trejni.com', 'zccbnnfut'),
#     # ('sigiwe4210@tajwork.com', 'deuritit'),
#     # ('hitexon827@tajwork.com', 'fdjfkkgk'),
#     # ('wigecax660@trejni.com', 'gdjgjyjuj'),
#     # ('harhmousumi3@gmail.com', 'Swas#237'),
#     # ('xeses71014@zufrans.com', 'Alexcaf543'),
#     # ('seanwilson333222@gmail.com', 'seanwilson3211233'),
#     # ('coreymjohnson677@gmail.com', '1818512429'),
#     ('shimaggq134@simaenaga.com', '#xpranto@25#'),
#     ('shimaxc16161@simaenaga.com', '#xpranto@25#'),
#     ('mimxbb1818@simaenaga.com', '#xpranto@25#'),
#     ('yagoj96926@xrmop.com', '#xpranto@25#'),
# ]
# instas = {
#     'last_connected': 13,
#     'accounts': [
#         ('skjbdcoerinverweoir0', 'FGbEQpMUL'),
#         ('skjbdcoerinverweoir2', '5G6puvxeD7b'),
#         ('skjbdcoerinverweoir5', 'mkoOcAYaQSB'),
#         ('skjbdcoerinverweoir6', 'eyaqsFDxK9'),
#         ('skjbdcoerinverweoir13', 'BPCNR3Mm5'),
#         ('skjbdcoerinverweoir16', '5Afxp0sDQ'),
#         ('skjbdcoerinverweoir18', 'O8AjaTMhpr'),
#         ('skjbdcoerinverweoir19', 'd9EnXxVb0j'),
#         ('skjbdcoerinverweoir20', '4UlwcxKQcc'),
#         ('skjbdcoerinverweoir21', 'pVUCMFeFwPt'),
#         ('skjbdcoerinverweoir23', 'PfRYvla5C'),
#         ('skjbdcoerinverweoir24', 'cUVuj07Lk'),
#         ('skjbdcoerinverweoir25', 'voWrofYpepV'),
#         ('skjbdcoerinverweoir28', 'cfmrvo8h'),
#         ('skjbdcoerinverweoir31', 'UxB8nYCSkoG'),
#         ('skjbdcoerinverweoir33', 'Vngnd8A2'),
#         ('skjbdcoerinverweoir34', 'jKRrRqngL'),
#         ('skjbdcoerinverweoir35', 'KU9KpVHZ1vh'),
#         ('skjbdcoerinverweoir36', '82pDcSTM'),
#         ('skjbdcoerinverweoir37', 'TidSta9ykx'),
#         ('skjbdcoerinverweoir38', 'fEaRucC8UoP'),
#         ('skjbdcoerinverweoir39', 'hX8DA4I9'),
#         ('skjbdcoerinverweoir40', 'zCZVYNV0W'),
#         ('skjbdcoerinverweoir47', 'lIaiqvuX'),
#         ('skjbdcoerinverweoir48', 'YUypiYh51U6'),
#         ('skjbdcoerinverweoir49', 'jYXCAfiAj'),
#         ('skjbdcoerinverweoir51', 'bKG6V0RKTk'),
#         ('skjbdcoerinverweoir53', 'SYKZ1cLwndP'),
#         ('skjbdcoerinverweoir55', 'otAhDQ8NKBL'),
#         ('skjbdcoerinverweoir56', 'ZInSXR4bo'),
#         ('skjbdcoerinverweoir58', 'qZZV84uYsN'),
#         ('skjbdcoerinverweoir62', '87hFrbH2Qv'),
#     ]
# }

# results = dict()
# for i in range(len(fbs)):
#     print(change_vpn())
#     fb = fbs[i]
#     results[i], page_name = facebook(fb)
#     if results[i] == True:
#         print(i, results[i], fb, instas['accounts'][instas['last_connected']], page_name)
#     else:
#         print(i, results[i], fb)
#     print(datetime.datetime.fromtimestamp(int(time.time())), '\n\n')

# print(time.time()-start)
# print(results) 






## PUT MANAGEMENT EMAIL IN BIO FOR PROMO (OR MANAGE DMS)


### For creating instas
instas = [
    ('parkerjosephx5ovf5', 'w1uVpMEVl'),
    ('hernandezmaryiitdr4', '3x4ESWwP'),
    ('millerrichard7fq63z', 'qz915VVwoX'),
    ('kingmichellenh37em', 'bsArshPscVD'),
    ('whitedeborahrgybgp', 'ZRaJNMupb'),
    ('walkeranthonymm1jq6', 'uBIfTLe12q'),
    ('scottthomaswclwc2', 'SL9kNhALaa'),
    ('campbellwilliam8jt3a3', 'EQ2fzeuw'),
    ('martinezgeorgerce2e8', '3fVIrm59RNw'),
    ('wrightbettyw52nbn', 'W26v5yK9'),
    ('campbellmark9boyra', 'UDnzhQwJrz4'),
    ('hallkevinmeb4nb', 'jrItPZ0Zo'),
    ('youngjasonakocqd', 'SIcYCumU'),
    ('robertslindafldg8o', 'iXsJGcsu'),
    ('jonescharlesbaeqqg', 'yc3lWBlF'),
    ('mitchellcarolr6yc5z', 'JqSx7Ax9'),
    ('perezmarkl3bbym', 'rO0mxAKTC'),
    ('johnsonkevinxqwr1z', 'dTTBYhmdeKr'),
    ('allenkaren7355ea', 'tRmyaeRP'),
    ('edwardshelenqsw3z1', 'hjc3WbyS0'),
    ('gonzalezpatriciai377uq', 'saB7QGvu'),
    ('jacksonsarah63zjgh', 'qfk5954Gu'),
    ('williamsedwardykuo8y', 'WkH05p236aN'),
    ('perezbettyrcqmq6', 'Zxf9hN4vfuL'),
    ('turnerjason5ksubv', 'xHFxJ31M6AZ'),
    ('thompsonbettyb36hw5', 'qFEOIkSZR5d'),
    ('collinsjasonqvd3ep', 'MgKPhRQCH'),
    ('thomasdonaldhkjvgz', 'dvES8a20'),
    ('kinglauraqhrxh9', 'SzTpb3C3pmN'),
    ('turnerdeborahpbeh5y', '4nsQ7a54M'),
    ('collinsedwardzijl38', 'UEeYZcmQWqo'),
    ('moorerichardcmh5ik', 'vIKgPEC167'),
    ('clarkjeffseghtj', 'lydLAYOpnzl'),
    ('perezjenniferyb81yz', '5CEMGVVv'),
    ('davismarkki12xb', 'CEpR7wFRN'),
    ('younganthonyxc3ckp', 'sqZNa7fI3'),
    ('lewislindadxa4dq', 'WQqLgLPZAAY'),
    ('smithjenniferlobd3g', 'iXnAIaUcDT'),
    ('taylormark2axnk1', 'RklysHF5r'),
    ('smithmargaretx3fiqw', 'rtC3GtDMHe'),
    ('martinjoseph7y5tg9', 'WGu4V3yA'),
    ('kingdonna61pthd', '8h4LvXsRm'),
    ('williamsdorothyyz1ke5', 'ypsyWXuPO'),
    ('hernandezruthfhpqjb', 'ErPmRS4QNX'),
    ('jacksondonnae9il32', 'dUuXs26bKG'),
    ('thomaswilliambikj15', 'OsByJ7Fs7n'),
    ('youngmarkkmmff1', '2bnucPzIj'),
    ('clarklisa41cac5', 'HsqtI9KE1F1'),
    ('nelsondavid6885u1', 'X8OHB4iN'),
    ('perezkimberly6juwf3', '1DQiWRdp'),
]
new_infos = [(f'aeorfuberonerjsns{i}',f'Testing {i}',f'{i}th one yippie yip',True) 
             for i in range(50)]
results = dict()


# pfp_directory = 'PFPs'
# orig_file = f'{pfp_directory}/moremarionovembre.jpg'
# for new_info in new_infos:
#     name = new_info[0]
#     new_file = f'{pfp_directory}/{name}.jpg'
#     shutil.copy(orig_file, new_file)


# time.sleep(4)

####################
# Make sure tempPFPs is the default folder
####################
for i in range(len(new_infos)):
    print(change_vpn())
    insta = instas[i]
    new_info = new_infos[i]
    results[i] = instagram(insta, new_info)
    print((insta, new_info), results[i])
    print(datetime.datetime.fromtimestamp(int(time.time())), '\n\n')

print(time.time()-start)
print(results)