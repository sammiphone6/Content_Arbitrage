from tt_update_data import update_data
from ig_post_functions import test_post, update_and_post_indiv, create_and_post_reel
from misc_functions import announce_pause, video_queue_indiv, video_queue_popular, access_token_details
from access_token import get_long_lived_access_token, debug_access_token
from data import account_data_indiv, account_data_popular, fb_app_data, tiktok_data_indiv, tiktok_captions_indiv, tiktok_data_popular, open_filedata, save_filedata, save_files
import datetime
import os
import numpy as np
import pandas as pd
import pprint
import matplotlib.pyplot as plt

account = 'dayynaa'
print(tiktok_data_indiv[account])
print(len(tiktok_data_indiv[account]['video_ids']))

# data1 = {
#     'a': {'2/18': 1, '2/19': 2, '2/20': 3},
#     'b': {'2/18': 2, '2/19': 3, '2/20': 4},
#     'c': {'2/18': 3, '2/19': 4, '2/20': 5},
# }
# df1 = pd.DataFrame(data1)

# data2 = {
#     'd': {'2/19': 2, '2/20': 3, '2/21': 4},
#     'b': {'2/19': 5, '2/20': 4, '2/21': 5},
#     'c': {'2/19': 4, '2/20': 5, '2/21': 6},
# }
# df2 = pd.DataFrame(data2)

# df = pd.read_csv('data/stats.csv')
# data = df.to_dict()
# for acc in [acc for acc in data] + [acc for acc in data2]:
#     if acc in data and acc not in data2:
#         pass
#     elif acc in data2 and acc not in data:
#         data[acc] = data2[acc]
#     elif acc in data and acc in data2:
#         data[acc].update(data2[acc])

# df = pd.DataFrame(data)

# df3 = pd.DataFrame({'account': ['a', 'b', 'c'], '2/18': [1, 2, 3], '2/19': [2, 3, 4], '2/20': [3, 4, 5]})

# print(df1)
# print(df2)
# print(df)


# tiktok_accounts = open_filedata('tiktok_bfs.txt')
# likes = sorted([int(tt[2]) for tt in tiktok_accounts])[::-1]
# # print(likes)
# x = [i+1 for i in range(len(likes))] #[10, 20, 50, 100, 250, 500, 1000, 2000]
# df = pd.DataFrame({'x': x, 'y': likes})
# # x = [1000000*e for e in x]
# df.plot(kind='bar', stacked=True)
# plt.yscale('log')
# plt.show()





# tt_handles = open_filedata('data/tt_freqs/tt_handles.txt')
# tiktok_accounts = open_filedata('data/tt_freqs/tiktok_bfs.txt')
# pp = pprint.PrettyPrinter(depth=6)
# x = [acc for acc in tiktok_accounts if acc[1] in ['onlyjayus', 'jackdoherty', 'loganmillerx', 'isaakpresley', 'rickyireland', 'faithordway7', 'alexyoumazzo', 'sam_hutchinson', 'bradeazy']]
# pp.pprint(x)
# print(len(x))
# print(tiktok_accounts[554:559])
# print(len([tt for tt in tt_handles if tt in [tt[1] for tt in tiktok_accounts]]))
# print('fabiancrfx' in [tt[1] for tt in tiktok_accounts])
# print(tt_handles[45:50])
# print(len(tt_handles))
# print(sum([int(elem[2]) for elem in tiktok_accounts]))
# pp.pprint(sorted(tiktok_accounts, key = lambda tt: int(tt[2]), reverse = True)[:100])
# video_queue_indiv()
# video_queue_popular()

# print(tiktok_data_indiv['alixearle']['video_ids'][71])
# for account in ["kevwithin"]:
#     update_and_post_indiv(account)


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

# x = open_filedata('data/tt_acc_generation/tt_rates.txt')
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', 2000)
# pd.set_option('display.float_format', '{:20,.2f}'.format)
# pd.set_option('display.max_colwidth', None)
# print(x)