from tt_update_data import open_filedata, save_filedata, update_data
from ig_post_functions import post_reel, test_post
from misc_functions import announce_pause, max_factor_under, get_account_data_popular, get_fb_app_data
import os
import time


tiktok_data_indiv = open_filedata('tiktok_data_indiv.txt')
tiktok_captions_indiv = open_filedata('tiktok_captions_indiv.txt')
start = time.time()
working = 0
for account in tiktok_data_indiv:
    tiktok_link = "https://www.tiktok.com/@therock/video/7204259192939597098"
    working += 1 if test_post(account, tiktok_link, tiktok_captions_indiv["7190876960480873771"]) else 0
    time.sleep(6)
end = time.time()

print("Total accounts: ", len([acc for acc in tiktok_data_indiv]), 
      "\nAmount working: ", working, 
      "\nAmount not working: ", len([acc for acc in tiktok_data_indiv])-working, 
      "\nRuntime: ", int(end - start))