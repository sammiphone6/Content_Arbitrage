from account_adding.fsm_functions import facebook_pairing_script, insta_creation_script
from multiprocessing import Process
from account_adding.data import fbs, instas, tiktok_account_data
from account_posting.data import account_data_indiv, fb_app_data, save_fb_app_data, save_account_data_indiv
from account_posting.ig_and_pages_data import get_instagram_id
from account_posting.access_token import update_all_access_tokens, update_access_token, debug_all_access_tokens, debug_access_token, never_expiring_token
from account_posting.insights_sync import get_followers_and_posts
import time
import random
import pandas as pd
import requests

def update():
    global account_data_indiv, fb_app_data, fbs, instas
    facebook_added = False
    new_fb = None
    for facebook_account in fbs.index:
        if len(str(fbs['Access Token'][facebook_account])) > 8 and facebook_account not in fb_app_data.index:

            fb_app_data.loc[facebook_account, 'App ID'] = str(fbs['App ID'][facebook_account])
            print(facebook_account)
            fb_app_data.loc[facebook_account, 'App Secret'] = fbs['App Secret'][facebook_account]
            fb_app_data.loc[facebook_account, 'Access Token'] = fbs['Access Token'][facebook_account]
            save_fb_app_data()

            facebook_added = True
            new_fb = facebook_account
    
    for i in range(len(instas)):
        insta = instas.iloc[i]
        if insta['Facebook Result'] == True and insta['Tiktok username'] not in account_data_indiv.index and insta['Facebook account'] in fb_app_data.index:

            account_data_indiv.loc[insta['Tiktok username'], 'IG ID'] = str(get_instagram_id(insta['Facebook account'], fb_app_data['Access Token'][insta['Facebook account']], insta['Page name']))
            account_data_indiv.loc[insta['Tiktok username'], 'FB App Owner'] = insta['Facebook account']
            account_data_indiv.loc[insta['Tiktok username'], 'Hashtag'] = insta['Tiktok username']
            account_data_indiv.loc[insta['Tiktok username'], 'Instagram'] = tiktok_account_data[insta['Tiktok username']]['ig_username']

            save_account_data_indiv()

    ## if facebook_added then get long lived access token
    if facebook_added:
        # if random.choice(range(5)) == 1:
        #     update_all_access_tokens()
        # else:
        update_access_token(new_fb)
        never_expiring_token(new_fb)
            
def active(instagram):

    def get_followers_and_posts(instagram):
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

        response = requests.get(f'https://www.instagram.com/{instagram}/', cookies=cookies, headers=headers)
        text = response.text
        followers = text.split(" Followers")[0].split('content=\"')[-1].replace(',', '')
        posts = text.split(" Posts")[0].split(' ')[-1].replace(',', '')

        # print(followers)
        for abbrev in [('K', 1000), ('M', 1000000)]:
            if abbrev[0] in followers:
                followers = int(followers[:-1]) * abbrev[1]
            if abbrev[0] in posts:
                followers = int(posts[:-1]) * abbrev[1]

        return int(followers), int(posts)
    # time.sleep(5)
    try:
        print(instagram)
        get_followers_and_posts(instagram)
        return True
    except:
        return False


####################
# FOR INSTAS: Make sure tempPFPs is the default folder
# FOR BOTH: Make sure Nord is set up to the right as needed (with France to US in view)
# FOR BOTH: Make sure no pages to the right of the safari/nord split page
# FOR BOTH: Make sure to record screen
####################

# update()
# debug_all_access_tokens()
# update_access_token("khusi6bd009@exdonuts.com")
# debug_access_token("maisha2xbd009@ccmail.uk")
# quit()

### Remove duplicates in update()

# debug_access_token("misty8bd009@ccmail.uk")
# print(active('liverpoolfc_exclusive'))
# print(active('cheesedaily_extras'))
# print(active('jihuhbic_secrets'))
# print(active('dgthe_exclusive'))
# print(active('rollitupk_clips'))
# print(active('tracy.oj_extras'))
# print(active('rauld_secrets'))

# insta_creds['Valid'] = insta_creds.apply(lambda row: active(insta_creds['IG username']), axis = 1)

####
# insta_creds = instas.loc[lambda df: (df['Instagram Result'] == 'True') & (df['Facebook Result'].isnull()), ['Tiktok username', 'Default password', 'Country']]
# insta_creds['IG username'] = insta_creds.apply(lambda row: tiktok_account_data[row['Tiktok username']]['ig_username'], axis = 1)
# first_batch = insta_creds[['IG username', 'Default password']][0:30]
# first_batch['Valid'] = first_batch.apply(lambda row: active(row['IG username']), axis = 1)
# first_batch = first_batch.loc[lambda df: (df['Valid'] == True), ['Valid', 'IG username', 'Default password']]
# print(first_batch)
####

# print(tiktok_account_data['cheesedaily']['ig_username'])
update()
quit()

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
        

