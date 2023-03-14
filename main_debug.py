from tt_update_data import update_data
from ig_post_functions import test_post, update_and_post, create_and_post_reel
from misc_functions import announce_pause, video_queue_indiv, video_queue_popular, access_token_details
from access_token import get_long_lived_access_token, debug_access_token
from data import account_data_indiv, account_data_popular, fb_app_data, tiktok_data_indiv, tiktok_captions_indiv, tiktok_data_popular, open_filedata, save_filedata, save_files
import datetime
import os
import numpy as np
import pandas as pd

video_queue_indiv()

# for account in ["fcbayern"]:
#     update_and_post(account)


# account = "meredithduxbury"
# tiktok_link = "https://www.tiktok.com/@therock/video/7204259192939597098"
# test_post(account, tiktok_link, tiktok_captions_indiv["7190876960480873771"])
# for account in tiktok_data_indiv:
#     if "7190876960480873771" in tiktok_data_indiv[account]['video_ids']:
#         print(account)
# print(tiktok_captions_indiv["7190876960480873771"])

# print(datetime.datetime.fromtimestamp(1678567877))

# d = {'1': [], '2':[]}
# for i in range(150):
#     d['1'].append(i)
#     d['2'].append(2*i)
# df = pd.DataFrame.from_dict(d)

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 2000)
# pd.set_option('display.float_format', '{:20,.2f}'.format)
# pd.set_option('display.max_colwidth', None)
# print(df)

# x = open_filedata('data/tt_freqs/tt_rates.txt')
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 2000)
# pd.set_option('display.float_format', '{:20,.2f}'.format)
# pd.set_option('display.max_colwidth', None)
# print(x)