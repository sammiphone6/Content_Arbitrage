import requests
from tt_update_data import update_data
from content_manipulation import tiktok_to_video_data
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


def get_followers(account):
    cookies = {
        'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        'ig_nrcb': '1',
        'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'ds_user_id': '58449324934',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'dpr': '2',
        'sessionid': '58449324934%3A6WUkIv01qfppaB%3A3%3AAYeKXqb2jPfYgYLMle2BdTxBUcenyXwssLMnLkQy-g',
        'fbsr_124024574287414': 'oJNl61zmNXbxQQt86F-dKvdwKey8zGwXJqc26xrUBrk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHlnVUZadEJVdzlZaEItQnlMOTFxa2V1bXdWTWxyNjlrdHBHUTNqVzNwWkNMTExUTElvMjkxR0xQNHYxWmZtcjFuanBYWmtfLUhETGg1VXVBU1BTRC1JN1lUNGRYOFB4Y0FPdThJVTh2a19mYnVhSGVRc2NPWGRxS01Eb0p6WjAxbDhlNjFFOUktTVNNSEctZWVUWnIyQnVhOUJtT2tIVXRYRElLLWt5MkhDbmlaOU9Dczl2V18tamFZYTd5ZDlvdUlkY0lVdG1MWjFjS21mSW1TNU1MVFFSdXpSeWpqSk5YZ1FYV0o3M2Z3d09UWVBhbDdfNDNoaWxDakc5ZDdqTHoydjk1THRzeHdjc3RpTzkyai1JaENpV0VQcm41V2Z4Z2o0eURyTmF2WHVfNGtGU0hobXRhQ2pWS2szeEtxb1hFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9IcUtWZWJiZXJYSW9FbUdVeURGRVdaQnNNcFpDMjB1dFpDU05KdlF4amk3ZnZEQldQQW9yd0pWQVVPYUt6dWFrUDlLQ2o1QlBqZ096c1lmZWlYOWpzRGZmcHZXN0lpM0p4eHV2SUFwcWZWNkIxS1R3a0RCN214eWdXUHJmZkFyWE1IbTRKR0UwT3dER1dRd0ZDa2hnaWwzY1pCMHJaQkh0WU1OWkJaQ2ExMjNvZjM3R1M4QlFaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMTEwfQ',
        'fbsr_124024574287414': '0OIar_YFlfE4JVVr0rI0ud4bxblYd11_A-UHvrOfohE.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQlZXeGVMcnRLX1U0Yi1nZlJrVzl4MHctTC1wZ1dnaS1YMmkyZ2xWM2JKNW1wZ2o2bnpYSlpZOURHWGVuYjh5RktCUWk1eE1DZXkydDJlWGdVR0ppSjhrb0FlSHJCUDlkY3JsTVg2REszZFZLTDF3N2xPUDJOekdibWhFTnpFRHpqLUJGdVg5U2I0RnhYWW14b1JKNm1sT2Zxc3h0UVBGUWpQZXlDMUdiZjVXeXBZWklWNXhLTVR0WHFYRFR3am5HOEg2M0kyWGFOYVBTY1ZZNXM4QzFXVUFYbzRoenFiNlowb20zVTRJdjM1LTNaaDBHOGJjTWh1cjE2ZXVfVUw1elFEYjZPZ3NMV2xyQ05NSW1UdW8yU2RkZE5oTzJWZC1GSkMtZndaOHlCX3pLLVdFU0pCd2lBU09DTi1obndWclRRIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZmNEJYaVpCSnNrYUplNUh5SldLNGFSVldFU2VvRDFCOHFrcGhGT24zb1Q0UlRaQjh3dWlCV2M3akxLSWFSd2RCNUEwWkJHZmVKNG13QnRaQWFkMnJleHpaQXZuckJaQW9WTmljNjJsSUNrZXc0cGJZTUVlMTJZdGNlWkNibHc0eFgzVlh4YUVBUG5qZ1ZjbTBMdkgzSG1Hb3NHdW5hQUpudDQ3bWU2V1hpN3Z1MEdUVjBSTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMjE0fQ',
        'rur': '"NCG\\05458449324934\\0541712089219:01f75cf6177c9dfc392d2257ad437a4a9f177d90d19fab669bd88aa3d6073c451a668b6d"',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; ds_user_id=58449324934; fbm_124024574287414=base_domain=.instagram.com; dpr=2; sessionid=58449324934%3A6WUkIv01qfppaB%3A3%3AAYeKXqb2jPfYgYLMle2BdTxBUcenyXwssLMnLkQy-g; fbsr_124024574287414=oJNl61zmNXbxQQt86F-dKvdwKey8zGwXJqc26xrUBrk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHlnVUZadEJVdzlZaEItQnlMOTFxa2V1bXdWTWxyNjlrdHBHUTNqVzNwWkNMTExUTElvMjkxR0xQNHYxWmZtcjFuanBYWmtfLUhETGg1VXVBU1BTRC1JN1lUNGRYOFB4Y0FPdThJVTh2a19mYnVhSGVRc2NPWGRxS01Eb0p6WjAxbDhlNjFFOUktTVNNSEctZWVUWnIyQnVhOUJtT2tIVXRYRElLLWt5MkhDbmlaOU9Dczl2V18tamFZYTd5ZDlvdUlkY0lVdG1MWjFjS21mSW1TNU1MVFFSdXpSeWpqSk5YZ1FYV0o3M2Z3d09UWVBhbDdfNDNoaWxDakc5ZDdqTHoydjk1THRzeHdjc3RpTzkyai1JaENpV0VQcm41V2Z4Z2o0eURyTmF2WHVfNGtGU0hobXRhQ2pWS2szeEtxb1hFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9IcUtWZWJiZXJYSW9FbUdVeURGRVdaQnNNcFpDMjB1dFpDU05KdlF4amk3ZnZEQldQQW9yd0pWQVVPYUt6dWFrUDlLQ2o1QlBqZ096c1lmZWlYOWpzRGZmcHZXN0lpM0p4eHV2SUFwcWZWNkIxS1R3a0RCN214eWdXUHJmZkFyWE1IbTRKR0UwT3dER1dRd0ZDa2hnaWwzY1pCMHJaQkh0WU1OWkJaQ2ExMjNvZjM3R1M4QlFaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMTEwfQ; fbsr_124024574287414=0OIar_YFlfE4JVVr0rI0ud4bxblYd11_A-UHvrOfohE.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQlZXeGVMcnRLX1U0Yi1nZlJrVzl4MHctTC1wZ1dnaS1YMmkyZ2xWM2JKNW1wZ2o2bnpYSlpZOURHWGVuYjh5RktCUWk1eE1DZXkydDJlWGdVR0ppSjhrb0FlSHJCUDlkY3JsTVg2REszZFZLTDF3N2xPUDJOekdibWhFTnpFRHpqLUJGdVg5U2I0RnhYWW14b1JKNm1sT2Zxc3h0UVBGUWpQZXlDMUdiZjVXeXBZWklWNXhLTVR0WHFYRFR3am5HOEg2M0kyWGFOYVBTY1ZZNXM4QzFXVUFYbzRoenFiNlowb20zVTRJdjM1LTNaaDBHOGJjTWh1cjE2ZXVfVUw1elFEYjZPZ3NMV2xyQ05NSW1UdW8yU2RkZE5oTzJWZC1GSkMtZndaOHlCX3pLLVdFU0pCd2lBU09DTi1obndWclRRIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZmNEJYaVpCSnNrYUplNUh5SldLNGFSVldFU2VvRDFCOHFrcGhGT24zb1Q0UlRaQjh3dWlCV2M3akxLSWFSd2RCNUEwWkJHZmVKNG13QnRaQWFkMnJleHpaQXZuckJaQW9WTmljNjJsSUNrZXc0cGJZTUVlMTJZdGNlWkNibHc0eFgzVlh4YUVBUG5qZ1ZjbTBMdkgzSG1Hb3NHdW5hQUpudDQ3bWU2V1hpN3Z1MEdUVjBSTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMjE0fQ; rur="NCG\\05458449324934\\0541712089219:01f75cf6177c9dfc392d2257ad437a4a9f177d90d19fab669bd88aa3d6073c451a668b6d"',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'viewport-width': '1792',
    }

    response = requests.get(f'https://www.instagram.com/{account}/', cookies=cookies, headers=headers)
    text = response.text
    followers = text.split(" Followers")[0].split('content=\"')[-1]
    posts = text.split(" Posts")[0].split(' ')[-1]

    return int(followers), int(posts)



# accounts = [
    # 'alixhighlights',
    # 'moresabquesada',
    # 'morehaleyybaylee',
    # 'moredaynamarie',
    # 'moreisaakpresley',
    # 'moreonlyjayus',
    # 'morefaithordway',
    # 'morelilnasx',
#     'sydenymayextra',
#     'morebrookemonk',
#     'bre.ckiehill',
#     'speedheshows',
#     'col.schnack',
# ]
# for account in accounts:
#     print(account, get_followers(account))

# account = 'dayynaa'
# print(tiktok_data_indiv[account])
# print(len(tiktok_data_indiv[account]['video_ids']))

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