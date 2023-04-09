from account_adding.fsm_functions import facebook_pairing_script, insta_creation_script
from multiprocessing import Process
from account_adding.data import fbs, instas, tiktok_account_data
from account_posting.data import account_data_indiv, fb_app_data, save_fb_app_data, save_account_data_indiv
from account_posting.ig_and_pages_data import get_instagram_id
from account_posting.access_token import update_all_access_tokens
import time
import pandas as pd

# def runInParallel(*fns):
#     proc = []
#     for fn in fns:
#         p = Process(target=fn)
#         p.start()
#         proc.append(p)
#     for p in proc:
#         p.join()

def update():
    global account_data_indiv, fb_app_data
    while(True):
        facebook_added = False
        for facebook_account in fbs.index:
            if len(str(fbs['Access Token'][facebook_account])) > 8 and facebook_account not in fb_app_data.index:
                new_row = dict()
                new_row['Email'] = facebook_account
                new_row['App ID'] = fbs['App ID'][facebook_account]
                new_row['App Secret'] = fbs['App Secret'][facebook_account]
                new_row['Access Token'] = fbs['Access Token'][facebook_account]

                print(fb_app_data)
                fb_app_data = fb_app_data.append(pd.DataFrame(new_row, index=new_row['Email'], columns=fb_app_data.columns))#new_row, index = ['Email'], columns = fb_app_data.columns)
                print(fb_app_data)
                save_fb_app_data()

                facebook_added = True
        
        for i in range(len(instas)):
            insta = instas.iloc[i]
            if insta['Facebook Result'] == True and insta['Tiktok username'] not in account_data_indiv.index and insta['Facebook account'] in fbs.index:
                new_row = dict()
                new_row['TT Account'] = insta['Tiktok username']
                new_row['IG ID'] = get_instagram_id(fb_app_data.loc[fb_app_data['Email'] == insta['Facebook account'], 'Access Token'].iloc[0,0], insta['Page name'])
                new_row['FB App Owner'] = insta['Facebook account']
                new_row['Hashtag'] = insta['Tiktok username']
                new_row['Instagram'] = tiktok_account_data[insta['Tiktok username']]['ig_username']

                account_data_indiv = account_data_indiv.append(new_row, ignore_index = True)
                save_account_data_indiv()

        ## if facebook_added then get long lived access token
        if facebook_added:
            update_all_access_tokens()

        time.sleep(60*15)


####################
# FOR INSTAS: Make sure tempPFPs is the default folder
# FOR BOTH: Make sure Nord is set up to the right as needed (with France to US in view)
# FOR BOTH: Make sure no pages to the right of the safari/nord split page
# FOR BOTH: Make sure to record screen
####################


types = [
    'insta',
    # 'facebook',
]

if 'insta' in types:
    insta_creation_script()


if 'facebook' in types: 
    while True: 
        facebook_pairing_script()
        update()