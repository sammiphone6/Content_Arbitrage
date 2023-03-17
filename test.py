from data import tiktok_data_indiv, tiktok_captions_indiv
from ig_post_functions import test_post
from misc_functions import announce_pause
import os
import time


tiktok_data_indiv
tiktok_captions_indiv
start = time.time()
working = 0
for account in tiktok_data_indiv:
    tiktok_link = "https://www.tiktok.com/@therock/video/7204259192939597098"
    working += 1 if test_post(account) else 0
    time.sleep(6)
end = time.time()

print("Total accounts: ", len([acc for acc in tiktok_data_indiv]), 
      "\nAmount working: ", working, 
      "\nAmount not working: ", len([acc for acc in tiktok_data_indiv])-working, 
      "\nRuntime: ", int(end - start))