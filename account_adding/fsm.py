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
from pandas.io.clipboard import clipboard_get, clipboard_set
import cv2
from data import instas, infos, tiktok_account_data, instas_start, open_filedata, save_instas, save_filedata, save_updated_counters


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
        # 'Romania', #only 3/15 worked when others had 7-10 out of 15
        'Singapore',
        # 'Slovenia', # 3/3 for no wifi
        'South Korea',
        'Spain',
        # 'Sweden', #only 1/3 success rate (could try bringing back)
        # 'Switzerland', #only 1/3 success rate (could try bringing back)
        # 'United States', #only 1/3 success rate (could try bringing back)
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
def instagram(insta_creds): #Big Boy

    ## Variable setup
    counters = open_filedata('data/insta_creation_counters.txt')
    infos_start = counters['infos']
    if infos_start >= len(infos):
        print("ALL INFOS USED")
        quit()

    ## Checks incognito is open
    open_incognito_window()
    if not catch_ig_cookie_popup("You’ve gone Incognito", type = 'contains', tries = 5, similarity='flexible'): #pause_for('button_icons/incognito/incognito.png', tries = 5):
        close_page(False)
        change_vpn()
        if debug: print("Couldn't load incognito")
        return instagram(insta_creds)

    directory = 'button_icons/instagram_account_info'

    ## Checks instagram is loaded
    if debug: print("Loading instagram")
    load_instagram()
    if not catch_ig_cookie_popup(f'{directory}/Insta Log In.png', tries = 10): 
        close_page(False)
        change_vpn()
        if debug: print("Couldn't find insta log in")
        return instagram(insta_creds)

    ## Sign into instagram
    if debug: print("Entering insta creds")
    enter_instagram_credentials(insta_creds)
    
    if catch_ig_cookie_popup(f'{directory}/challenge thrown.png', tries = 1, ignore_refresh = True): 
        if debug: print("Challenge thrown")
        return close_page(False, screenshot_loc = insta_creds)
    if debug: print("No challenge thrown")

    if catch_ig_cookie_popup("suspended", type = 'contains', tries = 1, ignore_refresh = True, similarity='flexible'): 
        if debug: print("Account Suspended")
        return close_page(False, screenshot_loc = insta_creds)
    if debug: print("Account not suspended")
    
    if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 5, ignore_refresh = True, similarity='flexible1'):
        if catch_ig_cookie_popup(f'{directory}/accounts onetap.png', tries = 1, ignore_refresh = True):
            if debug: print("Needed to reload page")
            reload()
        else:
            if debug: print("Needed to press enter again")
            enter()
        if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 5, ignore_refresh = True, similarity='flexible1'): return close_page(False, screenshot_loc = insta_creds)
    if debug: print("Login confirmed")

    ## Start to switch to business account
    go_to_switch_business()
    if not catch_ig_cookie_popup('Business', type = 'contains', tries = 15): return close_page(False, screenshot_loc = insta_creds)
    if debug: print("Switched to business page")

    ## Finish switching to business account
    finish_switching()
    if debug: print("Finished steps to switch to business account")
    if not catch_ig_cookie_popup('Switch to personal account', type = 'contains', tries = 22, similarity='flexible'):
        go_to_switch_business()
        if not catch_ig_cookie_popup('Business', type = 'contains', tries = 15): return close_page(False, screenshot_loc = insta_creds)
        if debug: print("Switched to business page")

        ## Finish switching to business account
        finish_switching()
        if debug: print("Finished steps to switch to business account")
        if not catch_ig_cookie_popup('Switch to personal account', type = 'contains', tries = 22, similarity='flexible'): return close_page(False, screenshot_loc = insta_creds)


    if debug: print("Successfully switched to business account")

    ## Finish updating account info
    time.sleep(4)

    ## Create info details and save all updated counters and data
    info_details = tiktok_account_data[infos[infos_start]]

    instas.loc[lambda df: df['Default username'] == insta_creds[0], 'Tiktok username'] = infos[infos_start]
    save_instas()
    
    infos_start += 1 # Make sure this is after we update instas with Tiktok username
    save_updated_counters(infos_start=infos_start)

    return close_page(update_account_info(info_details), screenshot_loc = insta_creds)

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

def update_account_info(info_details, tries = 0): #For this to work, make sure that PFP is on 
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
                time.sleep(8) ## PFP should now be updated
                os.remove(new_file)## REMOVE PFP FROM FOLDER
                return
    
    username = info_details['ig_username']
    name = info_details['ig_name']
    bio = info_details['ig_bio']
    email = info_details['ig_email']
    update_pfp = True


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

        catch_ig_cookie_popup(f'{directory}/Bio.png', tries = 3, account_center=True)
        select_all()
        time.sleep(0.5)
        type(bio)
        time.sleep(0.5)
        if debug: print("Bio added")
        catch_ig_cookie_popup(f'{directory}/Submit.png', tries = 3, account_center=True)
        pause_for(f'{directory}/Profile saved.png', 15)
        if debug: print("Profile saved")
        
        pause_for(f'{directory}/Accounts center.png', 8)
        if debug: print("Clicked on 'See more in accounts center'")
        if not catch_ig_cookie_popup(f'{directory}/IG account center 1.png', account_center=True): 
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

    ## ADD EMAIL FOR BOTH CASES
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
        time.sleep(1.5)
        type(bio)
        time.sleep(2.5)
        if debug: print("Bio added")

        pause_for(f'{directory}/Email.png', 3)
        select_all()
        time.sleep(0.5)
        type(email)
        time.sleep(0.5)
        if debug: print("Email added")

        pause_for(f'{directory}/Submit.png', 3)
        if not pause_for(f'{directory}/Profile saved.png', 15): return update_account_info(info_details, tries = tries + 1)
        if debug: print("Profile successfully saved")
        
        return catch_ig_cookie_popup([username, name], type = 'contains', tries = 5, similarity = 'flexible')
    
## FB Developer App Functions
def developer(fb_creds):
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
    
    directory = 'button_icons/developer'

    ## Go to create account page
    load_developer_site()
    if not catch_fb_cookie_popup(f'{directory}/Create account.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Create account page loaded')

    ## Click continue
    if not catch_fb_cookie_popup(f'{directory}/Continue.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Continue was clicked')

    ## Go to credit card page and add payment method
    add_credit_card()
    if not catch_fb_cookie_popup(f'{directory}/Add payment method.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Now adding payment method')

    ## Select credit card
    if not catch_fb_cookie_popup(f'{directory}/Credit or debit.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Selected credit or debit card')

    ## Select credit card
    if not catch_fb_cookie_popup(f'{directory}/Card info page.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Now on card info page')

    if not catch_fb_cookie_popup(f'{directory}/Card number.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Entering card number')

    if not enter_card_info(): return close_page(False), 0, 0, 0
    if debug: print('Card info entered')
    time.sleep(10)

    if not catch_fb_cookie_popup(f'{directory}/Mastercard.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Card info saved')
    
    if not refresh_and_remove_card(): return close_page(False), 0, 0, 0
    if debug: print('Card info removed')
    if not catch_fb_cookie_popup(f'{directory}/Developer.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Developer clicked')
    if not catch_fb_cookie_popup(f'{directory}/Complete registration.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Registration completed')

    ### REGISTRATION COMPLETE

    ## Create app
    if not catch_fb_cookie_popup(f'{directory}/Create app.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Clicked Create app')

    if not catch_fb_cookie_popup(f'{directory}/Business icon.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Clicked Business icon')
    if not catch_fb_cookie_popup(f'{directory}/Next.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Clicked Next')
    if not fill_app_details(fb_creds): return close_page(False), 0, 0, 0
    if debug: print('App created')
    time.sleep(10)
    enter()

    if not catch_fb_cookie_popup(f'{directory}/Settings.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Clicked Settings')
    if not catch_fb_cookie_popup(f'{directory}/Settings basic.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Clicked Settings basic')
    
    app_id = get_app_id()
    if not app_id: return close_page(False), 0, 0, 0
    if debug: print('App ID saved')

    app_secret = get_app_secret()
    if not app_secret: return close_page(False), 0, 0, 0
    if debug: print('App secret saved')
    if debug: print(app_id, app_secret)

    if not add_instagram_graph_api(): return close_page(False), 0, 0, 0
    if debug: print('Instagram graph API added')
    if not add_business_login(): return close_page(False), 0, 0, 0
    if debug: print('FB login added')

    short_lived_token = create_access_token()
    if not short_lived_token: return close_page(False), 0, 0, 0

    return close_page(True), app_id, app_secret, short_lived_token

def load_developer_site():
    searchbar()
    time.sleep(1)

    type('https://developers.facebook.com/async/registration')
    time.sleep(1)

    enter()
    time.sleep(2)

def add_credit_card():
    new_tab()
    time.sleep(1)
    
    searchbar()
    time.sleep(1)

    type('https://secure.facebook.com/facebook_pay/?referrer=settings')
    time.sleep(1)

    enter()
    time.sleep(2)

def enter_card_info():
    directory = 'button_icons/developer'
    
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

    tab()
    time.sleep(1)

    enter()
    time.sleep(1)

    for _ in range(4):
        type('u')
        time.sleep(1)

    enter()
    time.sleep(1)

    shift_tab()
    time.sleep(1)

    type('02139')
    time.sleep(1)

    return catch_fb_cookie_popup(f'{directory}/Save.png', tries = 20)

def refresh_and_remove_card():
    directory = 'button_icons/developer'
    
    if not pause_for(f'{directory}/Registration dialog.png', 10): return False
    time.sleep(1)

    reload()
    if not pause_for(f'{directory}/Confirm email.png', tries = 10): return False
    if debug: print('Email confirmed')

    if not pause_for(f'{directory}/Payments.png', 10): return False
    time.sleep(1)

    if not pause_for(f'{directory}/Remove card.png', 10): return False
    if not pause_for(f'{directory}/Remove.png', 10): return False

    close_tab()
    time.sleep(1)
    return True

def fill_app_details(fb_creds):
    directory = 'button_icons/developer'

    tab()
    time.sleep(1)

    type('MyApp')
    time.sleep(1)
    if not pause_for(f'{directory}/Create app2.png', 10): return False
    time.sleep(5)
    type(fb_creds[1])
    time.sleep(1)

    return pause_for(f'{directory}/Submit.png', 10)

def get_app_id():
    directory = 'button_icons/developer'
    if not catch_fb_cookie_popup(f'{directory}/App ID.png', tries = 20): return False

    my_mouse.click(Button.left, 2)
    time.sleep(1)
    copy()
    time.sleep(2)
    return clipboard_get()

def get_app_secret():
    directory = 'button_icons/developer'
    if not catch_fb_cookie_popup(f'{directory}/Show.png', tries = 20): return False
    time.sleep(10)
    if not catch_fb_cookie_popup(f'{directory}/App Secret.png', tries = 20): return False

    my_mouse.click(Button.left, 2)
    time.sleep(1)
    copy()
    time.sleep(2)
    return clipboard_get()

def add_instagram_graph_api():
    directory = 'button_icons/developer'
    pause_for(f'{directory}/Dashboard.png', tries = 5)
    time.sleep(10)
    enter()
    for _ in range(10):
        down()
    return pause_for(f'{directory}/Instagram graph api.png', tries = 20, click_type = 'br')

def add_business_login():
    directory = 'button_icons/developer'
    pause_for(f'{directory}/Dashboard.png', tries = 5)
    time.sleep(10)
    enter()
    for _ in range(30):
        down()
    if not pause_for(f'{directory}/FB login.png', tries = 20, click_type = 'br'): return False
    if not pause_for(f'{directory}/Redirect uri.png', tries = 20): return False
    type('https://www.youtube.com')
    time.sleep(1)
    enter()
    return pause_for(f'{directory}/Save changes.png', tries = 20)

def create_access_token():
    directory = 'button_icons/developer'
    
    searchbar()
    time.sleep(1)

    type('https://developers.facebook.com/tools/explorer/')
    time.sleep(1)
    enter()

    permissions = [
        'instagram_shopping_tag_products',
        'ads_management',
        'ads_read',
        'business_management',
        'page_events',
        'pages_manage_ads',
        'pages_manage_cta',
        'pages_manage_engagement',
        'pages_manage_instant_articles',
        'pages_manage_metadata',
        'pages_manage_posts',
        'pages_messaging',
        'pages_messaging_subscriptions',
        'pages_read_engagement',
        'pages_read_user_content',
        'pages_show_list',
        'read_page_mailboxes',
        'catalog_management',
        'instagram_basic',
        'instagram_content_publish',
        'instagram_manage_comments',
        'instagram_manage_insights',
        'instagram_manage_messages',
        'leads_retrieval',
        'manage_fundraisers',
        'publish_video',
        'read_insights',
    ]

    for permission in permissions:
        pause_for(f'{directory}/Add a permission.png', tries = 10)
        time.sleep(0.2)
        type(permission)
        time.sleep(0.2)
        down()
        time.sleep(0.2)
        enter()
        time.sleep(0.2)

    if not pause_for(f'{directory}/Generate access token.png', tries = 10): return False
    pause_for(f'{directory}/Continue3.png', tries = 10)
    pause_for(f'{directory}/Continue as.png', tries = 10)
    for _ in range(3):
        pause_for(f'{directory}/Opt in to all.png', tries = 10)
        pause_for(f'{directory}/Continue2.png', tries = 10)
    pause_for(f'{directory}/Save2.png', tries = 10)
    pause_for(f'{directory}/Got it.png', tries = 10)
    if not pause_for(f'{directory}/Copy token.png', tries = 10): return False

    short_lived_token = clipboard_get()
    return short_lived_token



## Simple functions
def tab():
    pyautogui.press(['tab'])

def new_tab():
    my_keyboard.press(Key.cmd)
    my_keyboard.press("t")
    my_keyboard.release("t")
    my_keyboard.release(Key.cmd)

def close_tab():
    my_keyboard.press(Key.cmd)
    my_keyboard.press("w")
    my_keyboard.release("w")
    my_keyboard.release(Key.cmd)

def shift_tab():
    my_keyboard.press(Key.shift)
    my_keyboard.press(Key.tab)
    my_keyboard.release(Key.tab)
    my_keyboard.release(Key.shift)

def copy():
    my_keyboard.press(Key.cmd)
    my_keyboard.press("c")
    my_keyboard.release("c")
    my_keyboard.release(Key.cmd)

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

def click_br(file, confidence = 0.85):
    img = cv2.imread(file)
    x, y = pyautogui.locateCenterOnScreen(image = file, confidence = confidence)
    x, y = x + img.shape[1]/2, y + img.shape[0]/2
    pyautogui.click(x/2, y/2)

def enter(): #if enter doesn't work, press space, usually has same effect
    # my_keyboard.press(Key.enter)
    pyautogui.press(['enter'])

def type(text):
    # if '\n' not in text:
    #     my_keyboard.type(text)

    # else:    
    lines = text.split('\n')
    first = True
    for line in lines:
        if not first:
            enter()
            time.sleep(1)

        str(line).replace('🔽', '👇')
        clipboard_set(line)
        time.sleep(0.5)

        paste()
        time.sleep(1)
        first = False

def searchbar():
    my_keyboard.press(Key.cmd)
    my_keyboard.press('l')
    my_keyboard.release('l')
    my_keyboard.release(Key.cmd)


## Comparator functions         # Maybe change all your time.sleep()'s to have 5% variance via a pause function
def pause_for(file, tries = 20, click_type = 'center'):
    for _ in range(tries):
        try:
            if click_type == 'center':
                click(file)
            elif click_type == 'br':
                click_br(file)
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
def catch_ig_cookie_popup(file, tries=10, type = 'pause', similarity = 1, ignore_refresh = False, business = False, account_center = False):
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
            if account_center:
                click('Manage your connected')
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

def close_page(bool = False, times = 1, screenshot_loc = None):
    if debug: print("Closing page and returning: ", bool)

    if screenshot_loc != None:
        file = f'insta_screenshots/{screenshot_loc[0]}.png'
        pyautogui.screenshot(file)
        instas.loc[lambda df: df['Default username'] == screenshot_loc[0], 'Screenshot'] = file
        save_instas()

    if pause_for('button_icons/Close incognito1.png', 15) and debug: print("Clicked Close incognito1.png")
    if pause_for('button_icons/Close incognito2.png', 15) and debug: print("Clicked Close incognito2.png")
    if pause_for('button_icons/Leave.png', 5) and debug: print("Clicked Leave.png")


    return bool



time.sleep(4)


# def others():
#     fbs = [

#     ]

#     for i in range(len(fbs)):
#         country = change_vpn()
#         print(country)
#         fb = fbs[i]
#         results[i], page_name = facebook(fb)
#         if results[i] == True:
#             print(i, results[i], fb, instas['accounts'][instas['last_connected']], page_name, country)
#         else:
#             print(i, results[i], fb, page_name, country)
#         print(datetime.datetime.fromtimestamp(int(time.time())), '\n\n')





#     fbs = [
#         # ('soniyaa1334x@simaenaga.com', '#xpranto@25#'),
#         # ('shimaxc2566@simaenaga.com', '#xpranto@25#'),
#         # ('morimjrx555@simaenaga.com', '#xpranto@25#'),
#         # ('joymiaxc246@catgroup.uk', '#xpranto@25#'),
#         ('xjjantcomx445@exdonuts.com', '#xpranto@25#'),
#         ('rima3468888@exdonuts.com', '#xpranto@25#'),
#         ('joy2467sss@exdonuts.com', '#xpranto@25#'),
#         ('mimxn24784@exdonuts.com', '#xpranto@25#'),
#         ('anikaxn14653@exdonuts.com', '#xpranto@25#'),
#         ('jobaanikax3467@exdonuts.com', '#xpranto@25#'),
#         ('priyaxc36421@exdonuts.com', '#xpranto@25#'),
#         ('samiakhan48873@exdonuts.com', '#xpranto@25#'),
#         ('nargissikdarcnx2641@exdonuts.com', '#xpranto@25#'),
#         ('nargisxhaque1341@exdonuts.com', '#xpranto@25#'),
#         ('ayeshaxhossain1343@exdonuts.com', '#xpranto@25#'),
#         ('yasminxsikdar245@exdonuts.com', '#xpranto@25#'),
#     ]
#     instas = {
#         'last_connected': 19,
#         'accounts': [
#             ('skjbdcoerinverweoir0', 'FGbEQpMUL'),
#             ('skjbdcoerinverweoir2', '5G6puvxeD7b'),
#             ('skjbdcoerinverweoir5', 'mkoOcAYaQSB'),
#             ('skjbdcoerinverweoir6', 'eyaqsFDxK9'),
#             ('skjbdcoerinverweoir13', 'BPCNR3Mm5'),
#             ('skjbdcoerinverweoir16', '5Afxp0sDQ'),
#             ('skjbdcoerinverweoir18', 'O8AjaTMhpr'),
#             ('skjbdcoerinverweoir19', 'd9EnXxVb0j'),
#             ('skjbdcoerinverweoir20', '4UlwcxKQcc'),
#             ('skjbdcoerinverweoir21', 'pVUCMFeFwPt'),
#             ('skjbdcoerinverweoir23', 'PfRYvla5C'),
#             ('skjbdcoerinverweoir24', 'cUVuj07Lk'),
#             ('skjbdcoerinverweoir25', 'voWrofYpepV'),
#             ('skjbdcoerinverweoir28', 'cfmrvo8h'),
#             ('skjbdcoerinverweoir31', 'UxB8nYCSkoG'),
#             ('skjbdcoerinverweoir33', 'Vngnd8A2'),
#             ('skjbdcoerinverweoir34', 'jKRrRqngL'),
#             ('skjbdcoerinverweoir35', 'KU9KpVHZ1vh'),
#             ('skjbdcoerinverweoir36', '82pDcSTM'),
#             ('skjbdcoerinverweoir37', 'TidSta9ykx'),
#             ('skjbdcoerinverweoir38', 'fEaRucC8UoP'),
#             ('skjbdcoerinverweoir39', 'hX8DA4I9'),
#             ('skjbdcoerinverweoir40', 'zCZVYNV0W'),
#             ('skjbdcoerinverweoir47', 'lIaiqvuX'),
#             ('skjbdcoerinverweoir48', 'YUypiYh51U6'),
#             ('skjbdcoerinverweoir49', 'jYXCAfiAj'),
#             ('skjbdcoerinverweoir51', 'bKG6V0RKTk'),
#             ('skjbdcoerinverweoir53', 'SYKZ1cLwndP'),
#             ('skjbdcoerinverweoir55', 'otAhDQ8NKBL'),
#             ('skjbdcoerinverweoir56', 'ZInSXR4bo'),
#             ('skjbdcoerinverweoir58', 'qZZV84uYsN'),
#             ('skjbdcoerinverweoir62', '87hFrbH2Qv'),
#         ]
#     }

#     results = dict()
#     for i in range(len(fbs)):
#         country = change_vpn()
#         print(country)
#         fb = fbs[i]
#         results[i], page_name = facebook(fb)
#         if results[i] == True:
#             print(i, results[i], fb, instas['accounts'][instas['last_connected']], page_name, country)
#         else:
#             print(i, results[i], fb, page_name, country)
#         print(datetime.datetime.fromtimestamp(int(time.time())), '\n\n')

#     print(time.time()-start)
#     print(results) 



#     time.sleep(30)



####################
# Make sure tempPFPs is the default folder
# Make sure Nord is set up to the right as needed (with France to US in view)
# Make sure no pages to the right of the safari/nord split page
# Make sure to record screen
####################
results = dict()

while instas_start < len(instas):
    country = change_vpn()
    print(country)

    insta = (instas['Default username'][instas_start], instas['Default password'][instas_start])
    instas['Country'][instas_start] = country
    save_instas()

    results[instas_start] = instagram(insta)
    print((insta), results[instas_start], country)
    instas['Result'][instas_start] = results[instas_start]
    save_instas()

    instas_start += 1
    save_updated_counters(instas_start=instas_start)
    print(datetime.datetime.fromtimestamp(int(time.time()-start)), '\n\n')
    print("Starting next one... (you could pause here)")

print(time.time()-start)
print(results)
