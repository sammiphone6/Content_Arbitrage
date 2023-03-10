from tt_update_data import open_filedata, save_filedata, update_data
from ig_post_functions import post_reel, test_post, update_and_post
from misc_functions import announce_pause, max_factor_under, get_account_data_indiv, get_account_data_popular, get_fb_app_data
from access_token import get_long_lived_access_token
from past_files.debug_access_token import debug_access_token
import datetime
import os
import numpy as np

# tiktok_data_indiv = open_filedata('tiktok_data_indiv.txt')
# tiktok_captions_indiv = open_filedata('tiktok_captions_indiv.txt')
# tiktok_data_popular = open_filedata('tiktok_data_popular.txt')

account = "meredithduxbury"
update_and_post(account)

# account = "meredithduxbury"
# tiktok_link = "https://www.tiktok.com/@therock/video/7204259192939597098"
# test_post(account, tiktok_link, tiktok_captions_indiv["7190876960480873771"])

# print(tiktok_data_indiv, '\n\n\n\n')
# print(tiktok_captions_indiv)

# fb_app_data = get_fb_app_data()
# for acc in fb_app_data.index:
#     if (len(str(fb_app_data['Access Token'][acc])) > 5):
       
#         print('\n\nAcc: ', acc)
#         print(fb_app_data['Access Token'][acc])
#         debug_access_token(acc)




# tiktok_data_indiv = open_filedata('tiktok_data_indiv.txt')
# for account in tiktok_data_indiv:
#     print(account, " : ", tiktok_data_indiv[account]['last_posted'], " : ", len(tiktok_data_indiv[account]['video_ids']))

# tiktok_data_popular = open_filedata('tiktok_data_popular.txt')
# for account in tiktok_data_popular:
#     print(account, " : ", tiktok_data_popular[account]['last_posted'], " : ", len(tiktok_data_popular[account]['videos']))

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