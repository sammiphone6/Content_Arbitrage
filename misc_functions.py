from data import account_data_indiv, account_data_popular, tiktok_data_indiv, tiktok_data_popular, fb_app_data
from access_token import debug_access_token
import time


## MISC METHODS
def announce_pause(sec):
    print("currently pausing for ", sec, " seconds if you want to stop program")
    time.sleep(sec/2)
    print("halfway done")
    time.sleep(sec/2)
    print("done pausing")

def video_queue_indiv(): 
    for account in [acc for acc in tiktok_data_indiv if acc in account_data_indiv.index]:
        last_posted = tiktok_data_indiv[account]['last_posted']
        total = len(tiktok_data_indiv[account]['video_ids'])
        print(account, " : ", last_posted, " : ", total, " : Remaining ", total-last_posted-1)

def video_queue_popular(): 
    for account in [acc for acc in tiktok_data_popular if acc in account_data_popular.index]:
        last_posted = tiktok_data_popular[account]['last_posted']
        total = len(tiktok_data_popular[account]['videos'])
        print(account, " : ", last_posted, " : ", total, " : Remaining ", total-last_posted-1)

def access_token_details():
    for acc in fb_app_data.index:
        if (len(str(fb_app_data['Access Token'][acc])) > 5):
        
            print('\n\nAcc: ', acc)
            print(fb_app_data['Access Token'][acc])
            debug_access_token(acc)

