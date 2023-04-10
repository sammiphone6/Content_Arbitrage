from account_adding.fsm_functions import facebook_pairing_script, insta_creation_script
from multiprocessing import Process
from account_adding.data import fbs, instas, tiktok_account_data
from account_posting.data import account_data_indiv, fb_app_data, save_fb_app_data, save_account_data_indiv
from account_posting.ig_and_pages_data import get_instagram_id
from account_posting.access_token import update_all_access_tokens, debug_all_access_tokens
import time
import pandas as pd

def update():
    global account_data_indiv, fb_app_data, fbs, instas
    facebook_added = False
    for facebook_account in fbs.index:
        if len(str(fbs['Access Token'][facebook_account])) > 8 and facebook_account not in fb_app_data.index:

            fb_app_data.loc[facebook_account, 'App ID'] = str(fbs['App ID'][facebook_account])
            fb_app_data.loc[facebook_account, 'App Secret'] = fbs['App Secret'][facebook_account]
            fb_app_data.loc[facebook_account, 'Access Token'] = fbs['Access Token'][facebook_account]
            save_fb_app_data()

            facebook_added = True
    
    for i in range(len(instas)):
        insta = instas.iloc[i]
        if insta['Facebook Result'] == True and insta['Tiktok username'] not in account_data_indiv.index and insta['Facebook account'] in fb_app_data.index:
            
            account_data_indiv.loc[insta['Tiktok username'], 'IG ID'] = str(get_instagram_id(insta['Facebook account'], fb_app_data['Access Token'][insta['Facebook account']], insta['Page name']))
            account_data_indiv.loc[insta['Tiktok username'], 'FB App Owner'] = insta['Facebook account']
            account_data_indiv.loc[insta['Tiktok username'], 'Hashtag'] = insta['Tiktok username']
            account_data_indiv.loc[insta['Tiktok username'], 'Instagram'] = tiktok_account_data[insta['Tiktok username']]['ig_username']

            save_account_data_indiv()

    ## if facebook_added then get long lived access token
    if facebook_added:
        update_all_access_tokens()




####################
# FOR INSTAS: Make sure tempPFPs is the default folder
# FOR BOTH: Make sure Nord is set up to the right as needed (with France to US in view)
# FOR BOTH: Make sure no pages to the right of the safari/nord split page
# FOR BOTH: Make sure to record screen
####################


types = [
    # 'insta',
    'facebook',
]

if 'insta' in types:
    insta_creation_script()


if 'facebook' in types: 
    while True: 
        facebook_pairing_script()
        update()
        

