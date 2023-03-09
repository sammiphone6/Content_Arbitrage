from tt_update_data import open_filedata, save_filedata, update_data
from ig_post_functions import post_reel, test_post
from misc_functions import announce_pause, max_factor_under, get_account_data, get_fb_app_data
import datetime
import os


## --------------------------------------------------------------------------------------##
## THIS USES PYNPUT / GOOGLE SHEETS AND IS NEEDED MANUALLY ON THE COMPUTER. DON'T FORGET ##

## --------------------------------------------------------------------------------------##

# update_data()

# tiktok_data_indiv = open_filedata('tiktok_data_indiv.txt')
# tiktok_captions_indiv = open_filedata('tiktok_captions_indiv.txt')
# tiktok_data_popular = open_filedata('tiktok_data_popular.txt')

# account = "gaming"
# tiktok_link = "https://www.tiktok.com/@therock/video/7204259192939597098"
# post_reel(account, tiktok_link, tiktok_captions_indiv["7190876960480873771"])

# print(tiktok_data_indiv, '\n\n\n\n')
# print(tiktok_captions_indiv)



for account in tiktok_data_indiv:
    print(account, " : ", tiktok_data_indiv[account]['last_posted'], " : ", len(tiktok_data_indiv[account]['video_ids']))

# print (datetime.datetime.fromtimestamp(1677252033))
# print (datetime.datetime.fromtimestamp(1677424833))
# print (datetime.datetime.fromtimestamp(1677597635))
# print (datetime.datetime.fromtimestamp(1677770435))

# print (datetime.datetime.fromtimestamp(1677597904))
# tiktok_data_indiv['nasdaily']['last_posted'] += 30
# save_filedata('tiktok_data_indiv.txt', tiktok_data_indiv)
# print(tiktok_data_indiv['nasdaily'])

# update_data()
# print(tiktok_data_indiv)

#### TEST IF SOMETHING WEIRD IS GOING ON WITH DOWNLOADED HTMLS OF INSTAGRAM PAGES ####
# directory = 'tt_htmls'
# for filename in os.listdir(directory):
#     # f = os.path.join(directory, filename)
#     print(filename)
#     print("here")
# print("done")


#### TEST IF AN ACCOUNT IS WORKING ####

# account = "cute cats"
# tiktok_link = "https://www.tiktok.com/@therock/video/7204259192939597098"
# test_post(account, tiktok_link, tiktok_captions_indiv["7190876960480873771"])

#### THEN KILL THE CODE WITH CTRL C ONCE YOU SEE THE CREATED_MEDIA_OBJECT_ID ####