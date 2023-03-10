from data import tiktok_data_indiv, tiktok_data_popular, fb_app_data
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
    for account in tiktok_data_indiv:
        print(account, " : ", tiktok_data_indiv[account]['last_posted'], " : ", len(tiktok_data_indiv[account]['video_ids']))

def video_queue_popular(): 
    for account in tiktok_data_popular:
        print(account, " : ", tiktok_data_popular[account]['last_posted'], " : ", len(tiktok_data_popular[account]['videos']))

def access_token_details():
    for acc in fb_app_data.index:
        if (len(str(fb_app_data['Access Token'][acc])) > 5):
        
            print('\n\nAcc: ', acc)
            print(fb_app_data['Access Token'][acc])
            debug_access_token(acc)

