import requests
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
import pandas as pd
from PIL import Image
import pytesseract
import fuzzysearch
import pyautogui
from pandas.io.clipboard import clipboard_get, clipboard_set
import cv2
from account_adding.data import instas, infos, tiktok_account_data, instas_start, fbs, open_filedata, save_instas, save_fbs, save_filedata, save_updated_counters


start = time.time()
my_keyboard = keyboard.Controller()
my_mouse = mouse.Controller()
debug = True


## VPN (by clicking NordVPN App)
def change_vpn(country = None):
    countries = [
        'France', 
        'Greece',
        'Iceland', 
        'Ireland',
        'Israel',
        # 'Italy', # Testing to see if it's countries fault of facebook account's fault
        # 'Japan', # Sometimes just doesn't work?
        'Luxembourg',
        'Mexico',
        # 'New Zealand', #can't create any facebook pages or sometimes even login from here
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
    if country == None or country not in countries: country = random.choice(countries)
    print(country)
    for _ in range(3):
        pause_for(f'account_adding/button_icons/Nord/{country}.png', tries = 5)
        wait(2)
    
    for _ in range(2):
        pause_for(f'account_adding/button_icons/Nord/Safari.png', tries = 5)
    
    waits = 0
    connected = False
    while not connected:
        if waits > 3:
            return change_vpn()
        wait(1)
        if not (contains('ERROR') or contains('Connecting to')):
            connected = True
        waits += 1
    return country

def wait(t):
    new_t = (1+(random.random()-0.5)/2.5)*t # Essentially 0.8t <= t < 1.2t
    time.sleep(new_t)

## Facebook Functions
def facebook(fb_creds, insta): #Big Boy
    directory = 'account_adding/button_icons/facebook'

    ## Checks incognito is open
    open_incognito_window()
    if not pause_for('account_adding/button_icons/incognito/incognito.png', tries = 5): return close_page(False, screenshot_loc=fb_creds, section='fb'), 0
    if debug: print('Incognito window opened')

    ## Checks facebook is loaded
    load_facebook()
    if not catch_fb_cookie_popup(f'{directory}/facebook.png', tries = 15): 
        close_page()
        wait(4)
        change_vpn()
        return facebook(fb_creds, insta)
    wait(3) #This makes sure you don't recognize the facebook logo, and have a cookie popup come as
    catch_fb_cookie_popup(f'{directory}/facebook.png', tries = 5) # you're typing since that changes languag of cookie, etc.
    if debug: print('Facebook opened')

    ## Sign into facebook
    enter_facebook_credentials(fb_creds)
    if debug: print('Facebook credentials entered')
    set_last_page_date(fb_creds) ## Potentially consider removing this (it sets last page date to last login time so we don't repeatedly login to the same account if there is an issue)
    if catch_fb_cookie_popup(f'{directory}/Get started.png', tries = 6): finish_accepting_data()
    if not catch_fb_cookie_popup([f'{directory}/Welcome to Facebook.png', f'{directory}/Facebook home.png', f'{directory}/FB home.png', f'{directory}/Stories.png'], tries = 5): 
        if contains(['suspended your account', 'days left', 'not visible'], similarity='flexible') or contains(['we need you to agree', 'following items'], similarity='flexible') or contains(['upload a photo', 'We use this photo'], similarity='flexible'):
            set_last_page_date(fb_creds, value = 5000000000)
        return close_page(False, screenshot_loc=fb_creds, section='fb'), 0
    if debug: print('Facebook log in successful')

    ## Start to create page
    go_to_create_page()
    if not catch_fb_cookie_popup(f'{directory}/Page name.png'): return close_page(False, screenshot_loc=fb_creds, section='fb'), 0
    if debug: print('Creating facebook page')

    ## Submit page
    page_name = add_and_submit_page_details()
    set_last_page_date(fb_creds)
    increment_num_pages(fb_creds)
    pyautogui.moveTo(200, 100)
    if catch_fb_cookie_popup(f'{directory}/Save2.png', tries = 6, ignore_refresh=True):
        set_last_page_date(fb_creds, value = 5000000000)
        return close_page(False, screenshot_loc=fb_creds, section='fb'), 0
    
    ## Add phone number if needed
    if add_phone_number() and debug: print('Phone number added')

    if not catch_fb_cookie_popup(f'{directory}/Next.png', tries = 8): return close_page(False, screenshot_loc=fb_creds, section='fb'), 0
    if debug: print('Page creation successful')

    ## Finish page setup
    continue_page_setup()
    if not catch_fb_cookie_popup(['Manage Page', 'Professional dashboard'], type = 'contains', tries = 20, similarity = 'flexible1'): return close_page(False, screenshot_loc=fb_creds, section='fb'), 0
    if debug: print('Page setup complete')

    ## Go to link instagram:
    visit_link_instagram()
    if not catch_fb_cookie_popup(['Connect', 'ccount', 'stagram'], type = 'contains', tries = 15, similarity = 'flexible1'): 
        print("Failed to visit link instagram page, trying again")
        visit_link_instagram()
        if not catch_fb_cookie_popup(['Connect', 'ccount', 'stagram'], type = 'contains', tries = 15, similarity = 'flexible1'): 
            return close_page(False, screenshot_loc=fb_creds, section='fb'), 0
    if debug: print('Now on connect instagram account page')

    ## Connect account steps:
    connect_account_steps()
    if not catch_ig_cookie_popup([f'{directory}/IG prompt.png', f'{directory}/number.png'], 20): 
        ## Go to link instagram:
        visit_link_instagram()
        if not catch_fb_cookie_popup(['Connect', 'ccount', 'stagram'], type = 'contains', tries = 15, similarity = 'flexible1'): return close_page(False, screenshot_loc=fb_creds, section='fb'), 0
        if debug: print('Now on connect instagram account page')

        ## Connect account steps:
        connect_account_steps()
        if not catch_ig_cookie_popup([f'{directory}/IG prompt.png', f'{directory}/number.png'], 20): 
            return close_page(False, screenshot_loc=fb_creds, section='fb'), 0
    if debug: print('Opened instagram redirect for connection')

    ## Enter instagram login
    global INSTA_CONNECT
    INSTA_CONNECT= True
    print("insta: ", tiktok_account_data[insta['Tiktok username']]['ig_username'])
    enter_instagram_credentials((tiktok_account_data[insta['Tiktok username']]['ig_username'], insta['Default password']))
    if debug: print('Instagram credentials entered')
    if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 10, ignore_refresh = True):
        if debug: print('Couldnt login, will press enter again')

        enter()
        if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 14, ignore_refresh = False): return close_page(False, 2, screenshot_loc=fb_creds, section='fb'), 0
    if debug: print('Instagram login successful')

    ## Select not now and confirm success
    if not catch_ig_cookie_popup([f'{directory}/Not now.png', f'{directory}/Not now2.png'], tries = 8): return close_page(False, 2, screenshot_loc=fb_creds, section='fb'), 0
    if debug: print('Pressed not now after successful IG login')


    ## Confirm it doesn't want us to login again
    if not catch_fb_cookie_popup('Facebook', type = 'contains', tries = 6, similarity = 'flexible1'):
        if catch_ig_cookie_popup([f'{directory}/IG prompt.png', f'{directory}/number.png'], 7):
            if debug: print('Requesting instagram login again')
            enter_instagram_credentials((tiktok_account_data[insta['Tiktok username']]['ig_username'], insta['Default password']))
            if debug: print('Instagram credentials entered')
            if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 10, ignore_refresh = True):
                if debug: print('Couldnt login, will press enter again')

                enter()
                if not catch_ig_cookie_popup(['Home', 'Search', 'Explore'], type = 'contains', tries = 14, ignore_refresh = False): return close_page(False, 2, screenshot_loc=fb_creds, section='fb'), 0
            if debug: print('Instagram login successful')

            ## Select not now and confirm success
            catch_ig_cookie_popup([f'{directory}/Not now.png', f'{directory}/Not now2.png'], tries = 8)
            if debug: print('Pressed not now after successful IG login')

    ## Confirm it says success

    connected = catch_fb_cookie_popup(f'{directory}/IG connected.png', tries=12)
    if debug: print('Connected result: ', connected)
    
    if pause_for(f'{directory}/Account connected done.png',4) and debug: print('Account successfully connected')

    review_needed = pause_for(f'{directory}/Review needed.png', 2)
    if debug: print('Review needed...' if review_needed else 'Review not needed :)')

    return close_page((connected or 
                       catch_fb_cookie_popup(['Managing connected accounts', 'Allow access to'], type = 'contains', tries = 10, similarity = 'flexible')
                       ) 
                       and not review_needed, 
                      screenshot_loc=fb_creds, section='fb'), page_name

def load_facebook():
    searchbar()
    wait(1)

    type('https://www.facebook.com/?sk=welcome')
    wait(1)

    enter()
    wait(2)

def enter_facebook_credentials(fb_cred):
    tab()
    wait(1)

    email, password = fb_cred
    type(email)
    wait(1)

    tab()
    wait(1)

    type(password)
    wait(1)

    enter()
    wait(2)

def finish_accepting_data():
    directory = 'account_adding/button_icons/facebook'
    pause_for([f'{directory}/Accept and Continue.png', f'{directory}/Accept and Continue2.png'], tries = 8)
    pause_for(f'{directory}/Close.png', tries = 8)

def go_to_create_page():
    searchbar()
    wait(1)

    type('https://www.facebook.com/pages/creation/?ref_type=launch_point')
    wait(1)

    enter()
    wait(1)

def increment_num_pages(fb_creds):
    if len([char for char in str(fbs['Num pages'][fb_creds[0]]) if char not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']]) > 1:
        fbs['Num pages'][fb_creds[0]] = 1
    else:
        fbs['Num pages'][fb_creds[0]] = int(fbs['Num pages'][fb_creds[0]]) + 1
    save_fbs()

def set_last_page_date(fb_creds, value = None):
    fbs['Last page date'][fb_creds[0]] = int(time.time()) if value == None else value
    save_fbs()

def add_and_submit_page_details():
    directory = 'account_adding/button_icons/facebook'

    page_name = 'Goodpage' + str(int(time.time()) % 10000000) #make sure this starts with a capital letter
    type(page_name)
    wait(1)

    pause_for(f'{directory}/Category.png', 6)
    type('des')
    pause_for(f'{directory}/Design.png', 15)

    pause_for(f'{directory}/Create page.png', 5)
    my_mouse.position = (100,100)

    return page_name

def add_phone_number():
    directory = 'account_adding/button_icons/facebook'
    if pause_for(f'{directory}/Phone number.png', 5):
        number = random.choice([_ for _ in range(3108970000, 3108979999)])
        type(str(number))
        wait(12)
        return True
    return False

def continue_page_setup():
    directory = 'account_adding/button_icons/facebook'
    wait(15)
    pause_for([f'{directory}/Next.png', f'{directory}/Next2.png'], 5)
    pause_for([f'{directory}/Skip.png'], 5)
    pause_for([f'{directory}/Next.png', f'{directory}/Next2.png'], 5)
    pause_for([f'{directory}/Done.png', f'{directory}/Done2.png'], 5)
    pause_for([f'{directory}/Not now fb page{i}.png' for i in ['', '2']], 14)

def visit_link_instagram():
    searchbar()
    wait(1)

    type('https://www.facebook.com/settings/?tab=linked_instagram')
    wait(1)

    enter()
    wait(1)

def connect_account_steps(tries = 0):
    if tries > 2:
        return False
    
    directory = 'account_adding/button_icons/facebook'
    
    def try_again(tries):
        reload()
        return connect_account_steps(tries = tries + 1)

    if not pause_for(f'{directory}/Connect account.png', 10): try_again(tries + 1)
    if not pause_for(f'{directory}/Connect.png', 10): try_again(tries + 1)
    if not pause_for(f'{directory}/Confirm.png', 10): try_again(tries + 1)
    
    wait(2)
    return True


## Instagram Functions
def instagram(insta_creds): #Big Boy

    ## Variable setup
    counters = open_filedata('account_adding/data/insta_creation_counters.txt')
    infos_start = counters['infos']
    if infos_start >= len(infos):
        print("ALL INFOS USED")
        quit()

    ## Checks incognito is open
    open_incognito_window()
    if not catch_ig_cookie_popup("You’ve gone Incognito", type = 'contains', tries = 5, similarity='flexible'): #pause_for('account_adding/button_icons/incognito/incognito.png', tries = 5):
        close_page(False)
        change_vpn()
        if debug: print("Couldn't load incognito")
        return instagram(insta_creds)

    directory = 'account_adding/button_icons/instagram_account_info'

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
    wait(4)

    ## Create info details and save all updated counters and data
    info_details = tiktok_account_data[infos[infos_start]]

    instas.loc[lambda df: df['Default username'] == insta_creds[0], 'Tiktok username'] = infos[infos_start]
    save_instas()
    
    infos_start += 1 # Make sure this is after we update instas with Tiktok username
    save_updated_counters(infos_start=infos_start)

    return close_page(update_account_info(info_details), screenshot_loc = insta_creds)

def load_instagram():
    searchbar()
    wait(1)

    type('https://www.instagram.com/')
    wait(1)

    enter()
    wait(2)   

def enter_instagram_credentials(insta_cred):
    wait(3)

    username, password = insta_cred
    type(username, type = 'type')
    wait(0.5+random.random())

    tab()
    wait(0.5+random.random())

    type(password, type = 'type')
    wait(0.5+random.random())

    enter()
    wait(2)

def go_to_switch_business():
    searchbar()
    wait(1)

    type('https://www.instagram.com/accounts/convert_to_professional_account/')
    wait(1)

    enter()
    wait(1)

def finish_switching(tries = 0):
    if debug: print("finish_switching tries: ", tries)
    if tries == 2:
        return
    
    directory = 'account_adding/button_icons/instagram_business_account'
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
    if not catch_ig_cookie_popup(file = f"{directory}/Don't use.png", tries = 15, ignore_refresh=True, business=True): return finish_switching(tries = tries+1)
    if debug: print("Clicked Don't use")
    if not catch_ig_cookie_popup(file = f'{directory}/Done.png', tries = 10, ignore_refresh=True, business=True): return finish_switching(tries = tries+1)
    if debug: print("Clicked Done")

def update_account_info(info_details, tries = 0): #For this to work, make sure that PFP is on 
    if tries == 2:
        return False
    
    directory = 'account_adding/button_icons/instagram_account_info'
    
    def update_pfp_on_account(username, prev_pfp = False, AC = False): #AC = accounts center setup
        pfp_directory = 'account_adding/PFPs'
        new_file = None
        for file in os.listdir(pfp_directory):
            if file[:len(username)+1] == f'{username}.' and len (file) <= len(username)+5: #.jpeg is longest
                orig_file = f'{pfp_directory}/{file}'
                new_file = f'{pfp_directory}/temp_PFPs/{file}'
                shutil.copy(orig_file, new_file)

                if AC:
                    pause_for(f'{directory}/AC upload new photo.png', 4)
                    ## See what happens on an earlier account if updating pfp and account center (likley not needed for a while)
                else:
                    pause_for(f'{directory}/Change profile photo.png', 4)
                    pause_for(f'{directory}/Upload new photo.png', 2)
                wait(5)

                down()
                wait(2)

                enter()
                wait(6) ## PFP should now be updated
                os.remove(new_file)## REMOVE PFP FROM FOLDER
                pause_for(f'{directory}/Cancel.png', 2)
                return
    
    username = info_details['ig_username']
    name = info_details['ig_name']
    bio = info_details['ig_bio']
    email = info_details['ig_email']
    update_pfp = True
    print('to be ig username: ', username)

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
        wait(0.5)
        type(bio)
        wait(0.5)
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
        wait(0.5)
        type(name)
        wait(0.5)
        if not pause_for(f'{directory}/AC done.png'): return False
        if debug: print("Name changed")

        if not pause_for(f'{directory}/AC change username.png'): return False
        if not pause_for(f'{directory}/AC username.png'): return False
        select_all()
        wait(0.5)
        type(username)
        wait(0.5)
        if not pause_for(f'{directory}/Username available.png', tries = 8): return False
        if debug: print("Username available")
        if not pause_for(f'{directory}/AC done.png'): return False
        if debug: print("Username changed")

        wait(1)
        return True

    ## ADD EMAIL FOR BOTH CASES
    else:
        if debug: print("Normal settings layout (not accounts center)")
        if update_pfp:
            update_pfp_on_account(username, AC = False)
            if debug: print("Pfp updated")

        pause_for(f'{directory}/Name.png', 3)
        select_all()
        wait(0.5)
        type(name)
        wait(0.5)
        if debug: print("Name added")

        pause_for(f'{directory}/Username.png', 3)
        select_all()
        wait(0.5)
        type(username)
        wait(0.5)
        if debug: print("Username added")

        pause_for(f'{directory}/Bio.png', 3)
        select_all()
        wait(1.5)
        type(bio)
        wait(2.5)
        if debug: print("Bio added")

        pause_for(f'{directory}/Email.png', 3)
        select_all()
        wait(0.5)
        type(email)
        wait(0.5)
        if debug: print("Email added")

        pause_for(f'{directory}/Submit.png', 3)
        if not pause_for(f'{directory}/Profile saved.png', 15): return update_account_info(info_details, tries = tries + 1)
        if debug: print("Profile successfully saved")
        
        return catch_ig_cookie_popup([username, name], type = 'contains', tries = 5, similarity = 'flexible')
    

## FB Developer App Functions
def developer(fb_creds): #Big Boy
    directory = 'account_adding/button_icons/facebook'

    ## Checks incognito is open
    open_incognito_window()
    if not pause_for('account_adding/button_icons/incognito/incognito.png', tries = 5): return close_page(False), 0, 0, 0
    if debug: print('Incognito window opened')

    ## Checks facebook is loaded
    load_facebook()
    if not catch_fb_cookie_popup(f'{directory}/facebook.png', tries = 15): 
        close_page()
        wait(4)
        change_vpn()
        return developer(fb_creds)
    wait(3) #This makes sure you don't recognize the facebook logo, and have a cookie popup come as
    catch_fb_cookie_popup(f'{directory}/facebook.png', tries = 5) # you're typing since that changes languag of cookie, etc.
    if debug: print('Facebook opened')

    ## Sign into facebook
    enter_facebook_credentials(fb_creds)
    if debug: print('Facebook credentials entered')
    if not catch_fb_cookie_popup('Welcome to Facebook,', type = 'contains', tries = 15): return close_page(False), 0, 0, 0
    if debug: print('Facebook log in successful')
    
    directory = 'account_adding/button_icons/developer'

    ## Go to create account page
    load_developer_site()
    if not catch_fb_cookie_popup(f'{directory}/Create account.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Create account page loaded')

    ## Click continue
    if not catch_fb_cookie_popup(f'{directory}/Continue.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Continue was clicked')
    wait(3)

    ## Go to credit card page and add payment method
    go_to_add_credit_card()

    if not add_credit_card(): return close_page(False), 0, 0, 0
    if debug: print('Entering card number')

    if not enter_card_info(): return close_page(False), 0, 0, 0
    if debug: print('Card info entered')
    wait(10)

    if not catch_fb_cookie_popup([f'{directory}/Mastercard.png', f'{directory}/Mastercard2.png', f'{directory}/Mastercard3.png', f'{directory}/Default.png'], tries = 5): 
        if not catch_fb_cookie_popup([f'{directory}/Three dots.png'], tries = 5) and catch_fb_cookie_popup([f'{directory}/Edit.png'], tries = 5): return close_page(False), 0, 0, 0
    if debug: print('Card info saved')
    
    if not refresh_and_remove_card(): return close_page(False), 0, 0, 0
    if debug: print('Card info removed')
    if not catch_fb_cookie_popup([f'{directory}/Developer.png', f'{directory}/Developer2.png', f'{directory}/Other.png', f'{directory}/Circle.png'], tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Developer/Other/option clicked')
    if not catch_fb_cookie_popup(f'{directory}/Complete registration.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Registration completed')

    ### REGISTRATION COMPLETE

    ## Create app
    if not catch_fb_cookie_popup(f'{directory}/Create app.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Clicked Create app')

    # Accounts for the "Setup Facebook Login" or "Other" page
    if pause_for([f'{directory}/Other house.png', f'{directory}/Other house2.png', f'{directory}/Other2.png', f'{directory}/Explore.png', f'{directory}/Other3.png'], tries = 4, confidence = 0.75): pause_for(f'{directory}/Next other.png', tries = 3)

    if not catch_fb_cookie_popup(f'{directory}/Business icon.png', tries = 10, confidence = 0.6): return close_page(False), 0, 0, 0
    if debug: print('Clicked Business icon')
    if not catch_fb_cookie_popup(f'{directory}/Next.png', tries = 20): return close_page(False), 0, 0, 0
    if debug: print('Clicked Next')
    if not fill_app_details(fb_creds): return close_page(False), 0, 0, 0
    if debug: print('App created')
    
    if catch_fb_cookie_popup(['Add products', 'app creation process', 'Users throttled', 'App Events'], type = 'contains', tries = 20) and debug: print ('Now on Dashboard')
    wait(5)
    enter()

    if not catch_fb_cookie_popup(f'{directory}/Settings.png', tries = 10): return close_page(False), 0, 0, 0
    if debug: print('Clicked Settings')
    if not catch_fb_cookie_popup(f'{directory}/Settings basic.png', tries = 10): return close_page(False), 0, 0, 0
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
    wait(1)

    type('https://developers.facebook.com/async/registration')
    wait(1)

    enter()
    wait(2)

def go_to_add_credit_card():
    new_tab()
    wait(1)
    
    searchbar()
    wait(1)

    type('https://secure.facebook.com/facebook_pay/?referrer=settings')
    wait(1)

    enter()
    wait(2)

def add_credit_card(tries = 0):
    if tries >= 2:
        return False
    
    def retry():
        if debug: print("Trying again to add card")
        reload()
        return add_credit_card(tries=tries+1)
    
    directory = 'account_adding/button_icons/developer'
    
    if not catch_fb_cookie_popup([f'{directory}/Add payment method{i}.png' for i in ['', '2', '3']], tries = 9): return retry()
    if debug: print('Now adding payment method')

    ## Select credit card
    if not catch_fb_cookie_popup([f'{directory}/Card icon.png', f'{directory}/Credit or debit.png', f'{directory}/Card info page.png'] , tries = 10, ignore_miscs=True): return retry()
    if debug: print('Selected credit or debit card')

    if not pause_for(f'{directory}/Card number.png', tries = 16): return retry()

    return True

def enter_card_info():
    directory = 'account_adding/button_icons/developer'
    
    cards = [
        ['5268760042189857', '0427', '574', '02139'],
        ['5268760042725387', '0427', '029', '02139'],
        ['5268760044862261', '0427', '594', '02139'],
        ['5268760048505437', '0427', '200', '02139'],
        ['5268760046618687', '0427', '501', '02139'],
        ['5268760047292821', '0427', '608', '02139'],
        ['5268760043859573', '0427', '424', '02139'],
        ['5268760041163515', '0427', '405', '02139'],
        ['5268760042969050', '0427', '777', '02139'],
        ['5268760049937522', '0427', '013', '02139'],
        ['5268760049681252', '0427', '493', '02139'],
    ]
    card = random.choice(cards)

    type(card[0])
    wait(1)

    tab()
    wait(1)

    type(card[1])
    wait(1)

    tab()
    wait(1)

    type(card[2])
    wait(1)

    tab()
    wait(1)

    enter()
    wait(1)

    for _ in range(1):
        type('u')
        wait(1)

    enter()
    wait(1)

    shift_tab()
    wait(1)

    type(card[3])
    wait(1)

    return pause_for(f'{directory}/Save.png', tries = 12)

def refresh_and_remove_card():
    directory = 'account_adding/button_icons/developer'
    
    if not pause_for(f'{directory}/Registration dialog.png', 10): return False
    wait(1)

    reload()
    if not pause_for(f'{directory}/Confirm email.png', tries = 10): return False
    if debug: print('Email confirmed')

    if not pause_for(f'{directory}/Payments.png', 10): return False
    wait(1)

    if not pause_for(f'{directory}/Remove card.png', 10): return False
    if not pause_for(f'{directory}/Remove.png', 10): return False

    close_tab()
    wait(1)
    return True

def fill_app_details(fb_creds):
    directory = 'account_adding/button_icons/developer'

    tab()
    wait(1)

    type('MyApp')
    wait(8)
    if not pause_for(f'{directory}/Create app2.png', 10): return False
    if pause_for(f'{directory}/Password box.png', 6): 
        wait(2)
        type(fb_creds[1])
        wait(1)
        return pause_for(f'{directory}/Submit.png', 10)

    return True

def get_app_id():
    directory = 'account_adding/button_icons/developer'
    if not catch_fb_cookie_popup(f'{directory}/App ID.png', tries = 20): return False

    my_mouse.click(Button.left, 2)
    wait(1)
    copy()
    wait(2)
    return clipboard_get()

def get_app_secret():
    directory = 'account_adding/button_icons/developer'
    if not catch_fb_cookie_popup(f'{directory}/Show.png', tries = 20): return False
    wait(10)
    if not catch_fb_cookie_popup(f'{directory}/App Secret.png', tries = 20): return False

    my_mouse.click(Button.left, 2)
    wait(1)
    copy()
    wait(2)
    return clipboard_get()

def add_instagram_graph_api():
    directory = 'account_adding/button_icons/developer'
    if pause_for(f'{directory}/Dashboard.png', tries = 5) and debug: print("Clicked return to Dashboard")
    if catch_fb_cookie_popup(['Add products', 'app creation process', 'Users throttled', 'App Events'], type = 'contains', tries = 20) and debug: print ('Back on Dashboard')
    wait(5)
    enter()
    for _ in range(12):
        down()
    return pause_for(f'{directory}/Instagram graph api.png', tries = 20, click_type = 'br')

def add_business_login():
    directory = 'account_adding/button_icons/developer'
    if pause_for(f'{directory}/Dashboard.png', tries = 5) and debug: print("Clicked return to Dashboard")
    if catch_fb_cookie_popup(['Add products', 'app creation process', 'Users throttled', 'App Events'], type = 'contains', tries = 20) and debug: print ('Back on Dashboard')
    wait(5)
    enter()
    for _ in range(30):
        down()
    if not pause_for(f'{directory}/FB login.png', tries = 20, click_type = 'br'): return False
    if not pause_for(f'{directory}/Redirect uri.png', tries = 20): return False
    type('https://www.youtube.com')
    wait(1)
    enter()
    return pause_for(f'{directory}/Save changes.png', tries = 20)

def create_access_token():
    directory = 'account_adding/button_icons/developer'
    
    wait(4)
    searchbar()
    wait(1)

    type('https://developers.facebook.com/tools/explorer/')
    wait(1)
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
        wait(0.2)
        type(permission)
        wait(0.2)
        down()
        wait(0.2)
        enter()
        wait(0.2)

    if not pause_for(f'{directory}/Generate access token.png', tries = 10): return False
    
    t = 10

    allow = True
    for i in range(10):
        if allow and pause_for(f'{directory}/Allow.png', tries = 2): 
            pause_for(f'{directory}/Continue3.png', tries = 2)
            allow = False
        if pause_for(f'{directory}/Continue as.png', tries = 2): break
        if i == 9: return False

    for _ in range(3):
        pause_for(f'{directory}/Opt in to all.png', tries = t)
        pause_for(f'{directory}/Continue2.png', tries = t)
    pause_for(f'{directory}/Save2.png', tries = t)
    pause_for(f'{directory}/Got it.png', tries = t)
    if not pause_for(f'{directory}/Copy token.png', tries = 15): return False

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
    pause_for([f'account_adding/button_icons/Reload.png', f'account_adding/button_icons/Refresh continue.png'], 2)
    wait(5)

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
    if isinstance(file, str):
        x, y = pyautogui.locateCenterOnScreen(image = file, confidence = confidence)
        pyautogui.click(x/2, y/2)
    elif isinstance(file, list) and len(file) == 1: 
        click(file[0])
    elif isinstance(file, list):
        try: 
            click(file[0])
            wait(1)
        except:
            click(file[1:])
            wait(1)

def click_br(file, confidence = 0.85):
    if isinstance(file, str):
        img = cv2.imread(file)
        x, y = pyautogui.locateCenterOnScreen(image = file, confidence = confidence)
        x, y = x + img.shape[1]/2, y + img.shape[0]/2
        pyautogui.click(x/2, y/2)
    elif isinstance(file, list) and len(file) == 1: 
        click(file[0])
    elif isinstance(file, list):
        try: 
            click(file[0])
        except:
            click(file[1:])
    

def enter(): #if enter doesn't work, press space, usually has same effect
    # my_keyboard.press(Key.enter)
    pyautogui.press(['enter'])

def type(text, type = 'copy'):
    # if '\n' not in text:
    #     my_keyboard.type(text)

    # else:    
    lines = text.split('\n')

    if len(lines) == 3 and 'talent.promo, Telegram:' in lines[2]:
        lines = [lines[0], lines[1], lines[2].split(', ')[0], lines[2].split(', ')[1]]

    first = True
    for line in lines:
        if not first:
            enter()
            wait(1)

        if type == 'copy':
            str(line).replace('🔽', '👇')
            clipboard_set(line)
            wait(0.5)
            paste()
        elif type == 'type':
            for char in line:
                my_keyboard.type(char)
                wait(0.12)
        
        wait(1)
        first = False

def searchbar():
    my_keyboard.press(Key.cmd)
    my_keyboard.press('l')
    my_keyboard.release('l')
    my_keyboard.release(Key.cmd)


## Comparator functions         # Maybe change all your wait()'s to have 5% variance via a pause function
def pause_for(file, tries = 20, click_type = 'center'):
    for _ in range(tries):
        try:
            if click_type == 'center':
                click(file)
            elif click_type == 'br':
                click_br(file)
            return True
        except:
            wait(1)
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
        return len([t for t in text if match(t, result, similarity)]) >= max(1, (len(text)+1)//2)

def match(text, result, similarity):
    if similarity == 1:
        return text in result
    
    if similarity == 'flexible':
        return len(fuzzysearch.find_near_matches(text, result, max_l_dist=2)) > 0
    if similarity == 'flexible1':
        return len(fuzzysearch.find_near_matches(text, result, max_l_dist=1)) > 0

## This alternates between checking for cookie and checking for result we want.
def catch_ig_cookie_popup(file, tries=10, type = 'pause', similarity = 1, ignore_refresh = False, business = False, account_center = False, confidence = 0.85):
    for _ in range(tries):
        try:
            if type == 'pause':
                click(file, confidence)
            elif type == 'contains':
                if not contains(file, similarity): raise Exception 
            return True
        except:
            pass
        try:
            if business:
                click('account_adding/button_icons/instagram_business_account/Continue.png') 
            if account_center:
                click('Manage your connected')
            else:
                if _%3 == 0: click(['account_adding/button_icons/IG Essential cookies.png', 'account_adding/button_icons/IG Essential cookies2.png']) 
                elif _%3 == 1: click(['account_adding/button_icons/IG Essential cookies3.png', 'account_adding/button_icons/IG Essential cookies4.png'])
                else: click('account_adding/button_icons/instagram_account_info/No notifications.png', 'account_adding/button_icons/instagram_account_info/Allow cookies.png')
        except:
            pass
        wait(1)
        if _ == tries//2 and not ignore_refresh:
            reload()
    return False

def catch_fb_cookie_popup(file, tries=10, type = 'pause', similarity = 1, ignore_refresh = False, ignore_miscs = False, confidence = 0.85):
    for _ in range(tries):
        try:
            if type == 'pause':
                click(file, confidence)
            elif type == 'contains':
                if not contains(file, similarity): raise Exception 
            return True
        except:
            pass
        try:
            if not ignore_miscs: 
                if _ % 2 == 0: click(['account_adding/button_icons/FB Essential cookies.png', 'account_adding/button_icons/FB Essential cookies2.png'])
                else: click(['account_adding/button_icons/facebook/X.png', 'account_adding/button_icons/facebook/Allow all cookies.png'])
        except:
            pass
        wait(1)
        if _ == tries//2 and not ignore_refresh:
            reload()
            wait(5)
            # enter() #weird situation where facebook login page would refresh and before we could click on facebook logo + type in answer this enter would submit for us :( let's see if things work without this enter...
    return False

## Open and close window functions 
def open_incognito_window(): #first be hovering over a normal GChrome window to the rightmost window of all your windows
    my_keyboard.press(Key.shift)
    my_keyboard.press(Key.cmd)
    my_keyboard.press('n')
    my_keyboard.release('n')
    my_keyboard.release(Key.cmd)
    my_keyboard.release(Key.shift)

def close_page(bool = False, times = 1, screenshot_loc = None, section = 'insta'):
    if debug: print("Closing page and returning: ", bool)

    if screenshot_loc != None:
        file = f'{section}_screenshots/{screenshot_loc[0]}.png'
        pyautogui.screenshot(f'account_adding/{file}')
        if section == 'insta':
            instas.loc[lambda df: df['Default username'] == screenshot_loc[0], 'Instagram Screenshot'] = file
        elif section == 'fb':
            instas.loc[lambda df: df['Facebook account'] == screenshot_loc[0], 'Facebook Screenshot'] = file
        save_instas()

    if pause_for('account_adding/button_icons/Close incognito1.png', 15) and debug: print("Clicked Close incognito1.png")
    if pause_for('account_adding/button_icons/Close incognito2.png', 15) and debug: print("Clicked Close incognito2.png")
    if pause_for('account_adding/button_icons/Leave.png', 5) and debug: print("Clicked Leave.png")


    return bool


def incorporate(insta_df): #Semi Big Boy
    facebook_account = insta_df['Facebook account']
    print(facebook_account)
    if all([pd.isnull(string) for string in [fbs.loc[facebook_account, tag] for tag in ['App ID', 'App Secret', 'Access Token']]]):
        fb_creds = (facebook_account, fbs['Facebook password'][facebook_account])
        result, app_id, app_secret, short_lived_token = developer(fb_creds)
        print(result, app_id, app_secret, short_lived_token)
        if result == False:
            set_last_page_date(fb_creds, 5000000000)
        elif result == True:
            fbs['App ID'][facebook_account] = int(app_id)
            fbs['App Secret'][facebook_account] = app_secret
            fbs['Access Token'][facebook_account] = short_lived_token
            save_fbs()

def get_followers(account):
    cookies = {
        'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        'ig_nrcb': '1',
        'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'ds_user_id': '58449324934',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'dpr': '2',
        'sessionid': '58449324934%3A6WUkIv01qfppaB%3A3%3AAYeKXqb2jPfYgYLMle2BdTxBUcenyXwssLMnLkQy-g',
        'fbsr_124024574287414': 'oJNl61zmNXbxQQt86F-dKvdwKey8zGwXJqc26xrUBrk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHlnVUZadEJVdzlZaEItQnlMOTFxa2V1bXdWTWxyNjlrdHBHUTNqVzNwWkNMTExUTElvMjkxR0xQNHYxWmZtcjFuanBYWmtfLUhETGg1VXVBU1BTRC1JN1lUNGRYOFB4Y0FPdThJVTh2a19mYnVhSGVRc2NPWGRxS01Eb0p6WjAxbDhlNjFFOUktTVNNSEctZWVUWnIyQnVhOUJtT2tIVXRYRElLLWt5MkhDbmlaOU9Dczl2V18tamFZYTd5ZDlvdUlkY0lVdG1MWjFjS21mSW1TNU1MVFFSdXpSeWpqSk5YZ1FYV0o3M2Z3d09UWVBhbDdfNDNoaWxDakc5ZDdqTHoydjk1THRzeHdjc3RpTzkyai1JaENpV0VQcm41V2Z4Z2o0eURyTmF2WHVfNGtGU0hobXRhQ2pWS2szeEtxb1hFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9IcUtWZWJiZXJYSW9FbUdVeURGRVdaQnNNcFpDMjB1dFpDU05KdlF4amk3ZnZEQldQQW9yd0pWQVVPYUt6dWFrUDlLQ2o1QlBqZ096c1lmZWlYOWpzRGZmcHZXN0lpM0p4eHV2SUFwcWZWNkIxS1R3a0RCN214eWdXUHJmZkFyWE1IbTRKR0UwT3dER1dRd0ZDa2hnaWwzY1pCMHJaQkh0WU1OWkJaQ2ExMjNvZjM3R1M4QlFaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMTEwfQ',
        'fbsr_124024574287414': '0OIar_YFlfE4JVVr0rI0ud4bxblYd11_A-UHvrOfohE.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQlZXeGVMcnRLX1U0Yi1nZlJrVzl4MHctTC1wZ1dnaS1YMmkyZ2xWM2JKNW1wZ2o2bnpYSlpZOURHWGVuYjh5RktCUWk1eE1DZXkydDJlWGdVR0ppSjhrb0FlSHJCUDlkY3JsTVg2REszZFZLTDF3N2xPUDJOekdibWhFTnpFRHpqLUJGdVg5U2I0RnhYWW14b1JKNm1sT2Zxc3h0UVBGUWpQZXlDMUdiZjVXeXBZWklWNXhLTVR0WHFYRFR3am5HOEg2M0kyWGFOYVBTY1ZZNXM4QzFXVUFYbzRoenFiNlowb20zVTRJdjM1LTNaaDBHOGJjTWh1cjE2ZXVfVUw1elFEYjZPZ3NMV2xyQ05NSW1UdW8yU2RkZE5oTzJWZC1GSkMtZndaOHlCX3pLLVdFU0pCd2lBU09DTi1obndWclRRIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZmNEJYaVpCSnNrYUplNUh5SldLNGFSVldFU2VvRDFCOHFrcGhGT24zb1Q0UlRaQjh3dWlCV2M3akxLSWFSd2RCNUEwWkJHZmVKNG13QnRaQWFkMnJleHpaQXZuckJaQW9WTmljNjJsSUNrZXc0cGJZTUVlMTJZdGNlWkNibHc0eFgzVlh4YUVBUG5qZ1ZjbTBMdkgzSG1Hb3NHdW5hQUpudDQ3bWU2V1hpN3Z1MEdUVjBSTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMjE0fQ',
        'rur': '"NCG\\05458449324934\\0541712089219:01f75cf6177c9dfc392d2257ad437a4a9f177d90d19fab669bd88aa3d6073c451a668b6d"',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; ds_user_id=58449324934; fbm_124024574287414=base_domain=.instagram.com; dpr=2; sessionid=58449324934%3A6WUkIv01qfppaB%3A3%3AAYeKXqb2jPfYgYLMle2BdTxBUcenyXwssLMnLkQy-g; fbsr_124024574287414=oJNl61zmNXbxQQt86F-dKvdwKey8zGwXJqc26xrUBrk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHlnVUZadEJVdzlZaEItQnlMOTFxa2V1bXdWTWxyNjlrdHBHUTNqVzNwWkNMTExUTElvMjkxR0xQNHYxWmZtcjFuanBYWmtfLUhETGg1VXVBU1BTRC1JN1lUNGRYOFB4Y0FPdThJVTh2a19mYnVhSGVRc2NPWGRxS01Eb0p6WjAxbDhlNjFFOUktTVNNSEctZWVUWnIyQnVhOUJtT2tIVXRYRElLLWt5MkhDbmlaOU9Dczl2V18tamFZYTd5ZDlvdUlkY0lVdG1MWjFjS21mSW1TNU1MVFFSdXpSeWpqSk5YZ1FYV0o3M2Z3d09UWVBhbDdfNDNoaWxDakc5ZDdqTHoydjk1THRzeHdjc3RpTzkyai1JaENpV0VQcm41V2Z4Z2o0eURyTmF2WHVfNGtGU0hobXRhQ2pWS2szeEtxb1hFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9IcUtWZWJiZXJYSW9FbUdVeURGRVdaQnNNcFpDMjB1dFpDU05KdlF4amk3ZnZEQldQQW9yd0pWQVVPYUt6dWFrUDlLQ2o1QlBqZ096c1lmZWlYOWpzRGZmcHZXN0lpM0p4eHV2SUFwcWZWNkIxS1R3a0RCN214eWdXUHJmZkFyWE1IbTRKR0UwT3dER1dRd0ZDa2hnaWwzY1pCMHJaQkh0WU1OWkJaQ2ExMjNvZjM3R1M4QlFaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMTEwfQ; fbsr_124024574287414=0OIar_YFlfE4JVVr0rI0ud4bxblYd11_A-UHvrOfohE.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQlZXeGVMcnRLX1U0Yi1nZlJrVzl4MHctTC1wZ1dnaS1YMmkyZ2xWM2JKNW1wZ2o2bnpYSlpZOURHWGVuYjh5RktCUWk1eE1DZXkydDJlWGdVR0ppSjhrb0FlSHJCUDlkY3JsTVg2REszZFZLTDF3N2xPUDJOekdibWhFTnpFRHpqLUJGdVg5U2I0RnhYWW14b1JKNm1sT2Zxc3h0UVBGUWpQZXlDMUdiZjVXeXBZWklWNXhLTVR0WHFYRFR3am5HOEg2M0kyWGFOYVBTY1ZZNXM4QzFXVUFYbzRoenFiNlowb20zVTRJdjM1LTNaaDBHOGJjTWh1cjE2ZXVfVUw1elFEYjZPZ3NMV2xyQ05NSW1UdW8yU2RkZE5oTzJWZC1GSkMtZndaOHlCX3pLLVdFU0pCd2lBU09DTi1obndWclRRIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZmNEJYaVpCSnNrYUplNUh5SldLNGFSVldFU2VvRDFCOHFrcGhGT24zb1Q0UlRaQjh3dWlCV2M3akxLSWFSd2RCNUEwWkJHZmVKNG13QnRaQWFkMnJleHpaQXZuckJaQW9WTmljNjJsSUNrZXc0cGJZTUVlMTJZdGNlWkNibHc0eFgzVlh4YUVBUG5qZ1ZjbTBMdkgzSG1Hb3NHdW5hQUpudDQ3bWU2V1hpN3Z1MEdUVjBSTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMjE0fQ; rur="NCG\\05458449324934\\0541712089219:01f75cf6177c9dfc392d2257ad437a4a9f177d90d19fab669bd88aa3d6073c451a668b6d"',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'viewport-width': '1792',
    }

    instagram = tiktok_account_data[account]['ig_username']

    response = requests.get(f'https://www.instagram.com/{instagram}/', cookies=cookies, headers=headers)
    text = response.text
    followers = text.split(" Followers")[0].split('content=\"')[-1].replace(',', '')
    return followers if len(followers) < 6 else None

# directory = 'account_adding/button_icons/developer'
# print(catch_fb_cookie_popup(f'{directory}/Business icon.png', tries = 10, confidence = 0.85))
wait(4)

INSTA_CONNECT = False
def facebook_pairing_script():
    results = dict()
    start = time.time()

    i = 0
    insta_creds = instas.loc[lambda df: (df['Instagram Result'] == 'True') & (df['Facebook Result'].isnull()), ['Tiktok username', 'Default password', 'Country']]
    print(insta_creds)
    insta = insta_creds.iloc[i]
    try:
        if get_followers(insta['Tiktok username']) == None: 
            print('Banned: ', insta)
            instas.loc[instas['Tiktok username'] == insta['Tiktok username'], 'Instagram Result'] = "Banned"
            save_instas()
            i+=1
            return facebook_pairing_script()
    except:
        print("Failed geting follower count for ", insta['Tiktok username'])

    print(insta_creds)
    # while i < len(insta_creds):
    global INSTA_CONNECT
    INSTA_CONNECT = False
    print(insta)
    country = change_vpn(insta['Country'])
    print(country)

    try:
        def get_fb_account(country):
            for fb_account in fbs.index:
                c = fbs['Country'][fb_account]
                d = fbs['Last page date'][fb_account]
                if len(str(c))<5 or c == country:
                    if len(str(d))<5 or (d < time.time()-7*24*60*60):
                        print(fb_account)
                        return fb_account
            return None
        
        fb = get_fb_account(insta['Country'])
        pwd = fbs['Facebook password'][fb]
        print(fb)
        if fb == None: raise Exception
    except:
        print("No Facebook available for ", country, ". Quitting now...", f" i={i}, Time: {datetime.datetime.fromtimestamp(int(time.time()))}, Run time: {datetime.datetime.fromtimestamp(int(time.time()-start))} ")
        quit()

    fbs['Country'][fb] = country
    save_fbs()
    fb_creds = (fb, pwd)
    results[i], page_name = facebook(fb_creds, insta)
    if results[i] == True:
        print(i, results[i], fb_creds, tiktok_account_data[insta['Tiktok username']]['ig_username'], insta['Default password'], page_name, country)
    else:
        print(i, results[i], fb_creds, page_name, country)

    if INSTA_CONNECT: 
        instas.loc[instas['Tiktok username'] == insta['Tiktok username'], 'Facebook account'] = fb
        instas.loc[instas['Tiktok username'] == insta['Tiktok username'], 'Page name'] = page_name
        instas.loc[instas['Tiktok username'] == insta['Tiktok username'], 'Facebook Result'] = results[i]
        instas.loc[instas['Tiktok username'] == insta['Tiktok username'], 'Facebook Screenshot'] = f"fb_screenshots/{fb}.png"
        instas.loc[instas['Tiktok username'] == insta['Tiktok username'], 'Facebook Timestamp'] = int(time.time())
        save_instas()
        i += 1

    recent = instas.loc[instas['Tiktok username'] == insta['Tiktok username'], 'Facebook Result']
    if len(recent) >= 1 and recent.iloc[0] == True:
        incorporate(instas.loc[instas['Tiktok username'] == insta['Tiktok username']].iloc[0])

    print(datetime.datetime.fromtimestamp(int(time.time())), '\n\n')

    print(time.time()-start)
    # print(results) 


####################
# Make sure tempPFPs is the default folder
# Make sure Nord is set up to the right as needed (with France to US in view)
# Make sure no pages to the right of the safari/nord split page
# Make sure to record screen
####################

def insta_creation_script():
    global instas, instas_start
    results = dict()
    start = time.time()

    while instas_start < len(instas):
        country = change_vpn()
        print(country)

        insta = (instas['Default username'][instas_start], instas['Default password'][instas_start])
        instas.at[instas_start, 'Country'] = country
        save_instas()

        results[instas_start] = instagram(insta)
        print((insta), results[instas_start], country)
        instas.at[instas_start, 'Instagram Result'] = results[instas_start]
        save_instas()

        instas_start += 1
        save_updated_counters(instas_start=instas_start)
        print(datetime.datetime.fromtimestamp(int(time.time()-start)), '\n\n')
        print("Starting next one... (you could pause here)")

    print(time.time()-start)
    print(results)