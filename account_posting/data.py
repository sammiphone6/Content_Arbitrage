import pandas as pd
import pickle
import requests
import time


## FILE METHODS
def open_filedata(filename):
    file = open(filename, 'rb')
    filedata = pickle.load(file)
    return filedata

def save_filedata(filename, filedata):
    file = open(filename, 'wb')
    pickle.dump(filedata, file)
    file.close()


## DATA GET METHODS
folder = 'account_posting/data'

def get_account_data_financial():
    filename = f'{folder}/account_data_financial.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    df['IG ID'] = df['IG ID'].astype(str)
    return df

def get_account_data_indiv():
    filename = f'{folder}/account_data_indiv.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    df['IG ID'] = df['IG ID'].astype(str)
    return df

def get_account_data_popular():
    filename = f'{folder}/account_data_popular.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    df['IG ID'] = df['IG ID'].astype(str)
    return df

def get_financial_tts():
    filename = f'{folder}/tt_account_financial.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    return df

def get_fb_app_data():
    filename = f'{folder}/fb_app_data.csv'
    df = pd.read_csv(filename).set_index('Email')
    df['App ID'] = df['App ID'].astype(str)
    df['Proxy'] = df['Proxy'].astype(str)
    return df

def get_tiktok_data_indiv():
    return open_filedata(f'{folder}/tiktok_data_indiv.txt')

def get_tiktok_capions_indiv():
    return open_filedata(f'{folder}/tiktok_captions_indiv.txt')

def get_tiktok_data_popular():
    return open_filedata(f'{folder}/tiktok_data_popular.txt')

def get_tiktok_data_financial():
    return open_filedata(f'{folder}/tiktok_data_financial.txt')

def get_proxy_data():
    filename = f"{folder}/webshare_proxy.txt"
    with open(filename, 'r') as file:
        proxy_data_txt = file.read()

    proxy_data_list = proxy_data_txt.split('\n')
    proxy_data_dict = {}
    for i in range(len(proxy_data_list)):
        proxy_data_dict[i+1] = proxy_data_list[i]
    return proxy_data_dict


## SAVE METHODS
def save_account_data_indiv():
    filename = f'{folder}/account_data_indiv.csv'
    account_data_indiv.to_csv(filename)

def save_account_data_popular():
    filename = f'{folder}/account_data_popular.csv'
    account_data_popular.to_csv(filename)

def save_fb_app_data():
    filename = f'{folder}/fb_app_data.csv'
    fb_app_data.to_csv(filename)

def save_files():
    save_filedata(f'{folder}/tiktok_data_indiv.txt', tiktok_data_indiv)
    save_filedata(f'{folder}/tiktok_captions_indiv.txt', tiktok_captions_indiv)
    save_filedata(f'{folder}/tiktok_data_popular.txt', tiktok_data_popular)
    save_filedata(f'{folder}/tiktok_data_financial.txt', tiktok_data_financial)
    
## INITIALIZE DATABASES FOR OTHER FILES

account_data_indiv = get_account_data_indiv()
account_data_financial = get_account_data_financial()
account_data_popular = get_account_data_popular()
fb_app_data = get_fb_app_data()

tiktok_data_indiv = get_tiktok_data_indiv()
tiktok_captions_indiv = get_tiktok_capions_indiv()
tiktok_data_popular = get_tiktok_data_popular()
tiktok_data_financial = get_tiktok_data_financial()
financial_tts = get_financial_tts()

proxy_data = get_proxy_data()


exclude = [
    'nasdaily',
    'jostasy',
    # 'petermckinnon',
    'baby_simba47',
    'tiffandchan',
    'reedtwinz',
    'miyaevarenae',
    'batzair',
    'its.marianne.faith',
    'readchoi',
    'victoriabachlet',
    'rauld33',
    'celia_7721',
    'kamtunechi',
    'robbieroket',
    'bobbie',
    'demibagby',
    'damedamian',
    'kaileenleilani',
    'athenafawn',
    'paigezilba',
    'insecthaus_adi',
    'allieschnacky',
    'frankielapenna',
    'meredithduxbury', #not banned, just not under same business manager
    'kevwithin', #not banned, just not under same business manager
    'saraecheagaray',
    'rug',
    'thesalguerofam',
    'enews',
    'esthalla',
    'miwmiucat',
    'nataliejanesings',
    'brenna.kaci',
    'nintendo.grl',
    'hanbity',
    'glitterandlazers',
    'iamkengi1',
    'campuzanoabelardo',
    'sofiaelizabeths',
    'wizardblazd',
    'therealclaybaby',
    'lukasrieger',
    'zsmittty',
    'tatyanddavon',
    'memira.x',
    'xowiejones',
    'gibz_',
    'mjgrimsley1001',
    'madisonbeer',
    'brycemckenzie',

    'kingbach',
    'chipgirlhere',
    'd_shaba',
    'grandadjoe1933',
    'lilyxgarcia',
    'garyvee',
    'paulfoisy',
    'charlieputh',
    'partyshirt',
    'officialautumnrose',
    'theyknowgeo',
]
email_exclude = [
    'rrrobr578@gmail.com', 
    'lolitkhan667@exdonuts.com',
    'tonmoykhan685@exdonuts.com',
    'sumaiya8bd009@ccmail.uk',
    'endrishyti027@yahoo.com',
    'shanta2bd009@ccmail.uk',
    'khusi6bd009@exdonuts.com',
    'andigurakuqi079@yahoo.com',
    'albankola096@yahoo.com',
]
# email_exclude += [ #blocked for spam - wait till friday evening to post
#     'sam@ercfilings.us',
#     'digitalempiremgmt2@gmail.com',
#     'digitalempiremgmt3@gmail.com',
#     'maishax1bd009@ccmail.uk',
#     'mirajahanbd091@ccmail.uk',
#     'yasminbd009sikdar@ccmail.uk',
#     'glenduro047@yahoo.com',
#     'lamiyaaktherbd464@ccmail.uk',
#     'fahima1bd099@ccmail.uk',
#     'gazmirshyti048@yahoo.com',
#     'nazminbdislam09@ccmail.uk',
#     'noelbaku074@yahoo.com',
#     'glenloshi064@yahoo.com',
#     'sadiaqueenbd574@ccmail.uk',
#     'maisha3bd009@ccmail.uk',
#     'rimakhan464@ccmail.uk',
#     'nargisxhaque5763@exdonuts.com',
#     'taniya6bd0093@ccmail.uk',
#     'nilima3bd009@ccmail.uk',
#     'maisha2xbd009@ccmail.uk',
#     'morimjrx555@simaenaga.com',
#     'samiaxhadi46@exdonuts.com',
#     'saimakhanbd09@ccmail.uk',
#     'sumaiya9bd009@ccmail.uk',
#     'shimakhanbd110@ccmail.uk',
#     'adritabd809@ccmail.uk',
#     'sadiyabd109@exdonuts.com',
#     'sumaiya4bd008@ccmail.uk',
# ]
# # email_exclude += ['sam@ercfilings.us', 'digitalempiremgmt2@gmail.com',
#        'digitalempiremgmt3@gmail.com', 'shimaxc2566@simaenaga.com',
#        'morimjrx555@simaenaga.com', 'yasminbd009sikdar@ccmail.uk',
#        'shimakhanbd110@ccmail.uk', 'sadiyabd109@exdonuts.com',
#        'nilima3bd009@ccmail.uk', 'maishax1bd009@ccmail.uk',
#        'maisha2xbd009@ccmail.uk', 'sumaiya9bd009@ccmail.uk',
#        'maisha3bd009@ccmail.uk', 'nazminbdislam09@ccmail.uk',
#        'fahima1bd099@ccmail.uk', 'saimakhanbd09@ccmail.uk',
#        'adritabd809@ccmail.uk', 'sumaiyasscbd009@ccmail.uk',
#        'taniya6bd0093@ccmail.uk', 'gazmirshyti048@yahoo.com',
#        'noelbaku074@yahoo.com', 'lamiyaaktherbd464@ccmail.uk',
#        'glenloshi064@yahoo.com', 'sadia2bd0@exdonuts.com',
#        'lolitkhan667@exdonuts.com', 'glenduro047@yahoo.com',
#        'sadiaqueenbd574@ccmail.uk', 'tonmoykhan685@exdonuts.com',
#        'rimakhan464@ccmail.uk', 'nargisxhaque5763@exdonuts.com',
#        'sumaiya4bd008@ccmail.uk', 'sumaiya8bd009@ccmail.uk',
#        'endrishyti027@yahoo.com', 'mirajahanbd091@ccmail.uk',
#        'shanta2bd009@ccmail.uk', 'samiaxhadi46@exdonuts.com',
#        'khusi6bd009@exdonuts.com', 'misty8bd009@ccmail.uk',
#        'ritukhan1bd009@ccmail.uk', 'riyakhanxff7u@ccmail.uk',
#        'saimiragolli094@yahoo.com', 'albanxhafa095@yahoo.com',
#        'andigurakuqi079@yahoo.com', 'genciagolli096@yahoo.com',
#        'glenbrahimi092@yahoo.com', 'noelgurakuqi091@yahoo.com',
#        'erionshyti095@yahoo.com', 'gencizane092@yahoo.com',
#        'alesandroshyti096@yahoo.com']

exclude += [acc for acc in list(account_data_indiv.index) if account_data_indiv['FB App Owner'][acc] in email_exclude]


# def active(instagram):

#     def get_followers_and_posts(instagram):
#         cookies = {
#             'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
#             'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
#             'ig_nrcb': '1',
#             'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
#             'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
#             'ds_user_id': '58449324934',
#             'fbm_124024574287414': 'base_domain=.instagram.com',
#             'dpr': '2',
#             'sessionid': '58449324934%3A6WUkIv01qfppaB%3A3%3AAYeKXqb2jPfYgYLMle2BdTxBUcenyXwssLMnLkQy-g',
#             'fbsr_124024574287414': 'oJNl61zmNXbxQQt86F-dKvdwKey8zGwXJqc26xrUBrk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHlnVUZadEJVdzlZaEItQnlMOTFxa2V1bXdWTWxyNjlrdHBHUTNqVzNwWkNMTExUTElvMjkxR0xQNHYxWmZtcjFuanBYWmtfLUhETGg1VXVBU1BTRC1JN1lUNGRYOFB4Y0FPdThJVTh2a19mYnVhSGVRc2NPWGRxS01Eb0p6WjAxbDhlNjFFOUktTVNNSEctZWVUWnIyQnVhOUJtT2tIVXRYRElLLWt5MkhDbmlaOU9Dczl2V18tamFZYTd5ZDlvdUlkY0lVdG1MWjFjS21mSW1TNU1MVFFSdXpSeWpqSk5YZ1FYV0o3M2Z3d09UWVBhbDdfNDNoaWxDakc5ZDdqTHoydjk1THRzeHdjc3RpTzkyai1JaENpV0VQcm41V2Z4Z2o0eURyTmF2WHVfNGtGU0hobXRhQ2pWS2szeEtxb1hFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9IcUtWZWJiZXJYSW9FbUdVeURGRVdaQnNNcFpDMjB1dFpDU05KdlF4amk3ZnZEQldQQW9yd0pWQVVPYUt6dWFrUDlLQ2o1QlBqZ096c1lmZWlYOWpzRGZmcHZXN0lpM0p4eHV2SUFwcWZWNkIxS1R3a0RCN214eWdXUHJmZkFyWE1IbTRKR0UwT3dER1dRd0ZDa2hnaWwzY1pCMHJaQkh0WU1OWkJaQ2ExMjNvZjM3R1M4QlFaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMTEwfQ',
#             'fbsr_124024574287414': '0OIar_YFlfE4JVVr0rI0ud4bxblYd11_A-UHvrOfohE.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQlZXeGVMcnRLX1U0Yi1nZlJrVzl4MHctTC1wZ1dnaS1YMmkyZ2xWM2JKNW1wZ2o2bnpYSlpZOURHWGVuYjh5RktCUWk1eE1DZXkydDJlWGdVR0ppSjhrb0FlSHJCUDlkY3JsTVg2REszZFZLTDF3N2xPUDJOekdibWhFTnpFRHpqLUJGdVg5U2I0RnhYWW14b1JKNm1sT2Zxc3h0UVBGUWpQZXlDMUdiZjVXeXBZWklWNXhLTVR0WHFYRFR3am5HOEg2M0kyWGFOYVBTY1ZZNXM4QzFXVUFYbzRoenFiNlowb20zVTRJdjM1LTNaaDBHOGJjTWh1cjE2ZXVfVUw1elFEYjZPZ3NMV2xyQ05NSW1UdW8yU2RkZE5oTzJWZC1GSkMtZndaOHlCX3pLLVdFU0pCd2lBU09DTi1obndWclRRIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZmNEJYaVpCSnNrYUplNUh5SldLNGFSVldFU2VvRDFCOHFrcGhGT24zb1Q0UlRaQjh3dWlCV2M3akxLSWFSd2RCNUEwWkJHZmVKNG13QnRaQWFkMnJleHpaQXZuckJaQW9WTmljNjJsSUNrZXc0cGJZTUVlMTJZdGNlWkNibHc0eFgzVlh4YUVBUG5qZ1ZjbTBMdkgzSG1Hb3NHdW5hQUpudDQ3bWU2V1hpN3Z1MEdUVjBSTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMjE0fQ',
#             'rur': '"NCG\\05458449324934\\0541712089219:01f75cf6177c9dfc392d2257ad437a4a9f177d90d19fab669bd88aa3d6073c451a668b6d"',
#         }

#         headers = {
#             'authority': 'www.instagram.com',
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#             'accept-language': 'en-US,en;q=0.9',
#             'cache-control': 'max-age=0',
#             # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; ds_user_id=58449324934; fbm_124024574287414=base_domain=.instagram.com; dpr=2; sessionid=58449324934%3A6WUkIv01qfppaB%3A3%3AAYeKXqb2jPfYgYLMle2BdTxBUcenyXwssLMnLkQy-g; fbsr_124024574287414=oJNl61zmNXbxQQt86F-dKvdwKey8zGwXJqc26xrUBrk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHlnVUZadEJVdzlZaEItQnlMOTFxa2V1bXdWTWxyNjlrdHBHUTNqVzNwWkNMTExUTElvMjkxR0xQNHYxWmZtcjFuanBYWmtfLUhETGg1VXVBU1BTRC1JN1lUNGRYOFB4Y0FPdThJVTh2a19mYnVhSGVRc2NPWGRxS01Eb0p6WjAxbDhlNjFFOUktTVNNSEctZWVUWnIyQnVhOUJtT2tIVXRYRElLLWt5MkhDbmlaOU9Dczl2V18tamFZYTd5ZDlvdUlkY0lVdG1MWjFjS21mSW1TNU1MVFFSdXpSeWpqSk5YZ1FYV0o3M2Z3d09UWVBhbDdfNDNoaWxDakc5ZDdqTHoydjk1THRzeHdjc3RpTzkyai1JaENpV0VQcm41V2Z4Z2o0eURyTmF2WHVfNGtGU0hobXRhQ2pWS2szeEtxb1hFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9IcUtWZWJiZXJYSW9FbUdVeURGRVdaQnNNcFpDMjB1dFpDU05KdlF4amk3ZnZEQldQQW9yd0pWQVVPYUt6dWFrUDlLQ2o1QlBqZ096c1lmZWlYOWpzRGZmcHZXN0lpM0p4eHV2SUFwcWZWNkIxS1R3a0RCN214eWdXUHJmZkFyWE1IbTRKR0UwT3dER1dRd0ZDa2hnaWwzY1pCMHJaQkh0WU1OWkJaQ2ExMjNvZjM3R1M4QlFaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMTEwfQ; fbsr_124024574287414=0OIar_YFlfE4JVVr0rI0ud4bxblYd11_A-UHvrOfohE.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQlZXeGVMcnRLX1U0Yi1nZlJrVzl4MHctTC1wZ1dnaS1YMmkyZ2xWM2JKNW1wZ2o2bnpYSlpZOURHWGVuYjh5RktCUWk1eE1DZXkydDJlWGdVR0ppSjhrb0FlSHJCUDlkY3JsTVg2REszZFZLTDF3N2xPUDJOekdibWhFTnpFRHpqLUJGdVg5U2I0RnhYWW14b1JKNm1sT2Zxc3h0UVBGUWpQZXlDMUdiZjVXeXBZWklWNXhLTVR0WHFYRFR3am5HOEg2M0kyWGFOYVBTY1ZZNXM4QzFXVUFYbzRoenFiNlowb20zVTRJdjM1LTNaaDBHOGJjTWh1cjE2ZXVfVUw1elFEYjZPZ3NMV2xyQ05NSW1UdW8yU2RkZE5oTzJWZC1GSkMtZndaOHlCX3pLLVdFU0pCd2lBU09DTi1obndWclRRIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZmNEJYaVpCSnNrYUplNUh5SldLNGFSVldFU2VvRDFCOHFrcGhGT24zb1Q0UlRaQjh3dWlCV2M3akxLSWFSd2RCNUEwWkJHZmVKNG13QnRaQWFkMnJleHpaQXZuckJaQW9WTmljNjJsSUNrZXc0cGJZTUVlMTJZdGNlWkNibHc0eFgzVlh4YUVBUG5qZ1ZjbTBMdkgzSG1Hb3NHdW5hQUpudDQ3bWU2V1hpN3Z1MEdUVjBSTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMjE0fQ; rur="NCG\\05458449324934\\0541712089219:01f75cf6177c9dfc392d2257ad437a4a9f177d90d19fab669bd88aa3d6073c451a668b6d"',
#             'sec-ch-prefers-color-scheme': 'light',
#             'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#             'sec-ch-ua-mobile': '?0',
#             'sec-ch-ua-platform': '"macOS"',
#             'sec-fetch-dest': 'document',
#             'sec-fetch-mode': 'navigate',
#             'sec-fetch-site': 'none',
#             'sec-fetch-user': '?1',
#             'upgrade-insecure-requests': '1',
#             'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
#             'viewport-width': '1792',
#         }

#         response = requests.get(f'https://www.instagram.com/{instagram}/', cookies=cookies, headers=headers)
#         text = response.text
#         followers = text.split(" Followers")[0].split('content=\"')[-1].replace(',', '')
#         posts = text.split(" Posts")[0].split(' ')[-1].replace(',', '')

#         # print(followers)
#         for abbrev in [('K', 1000), ('M', 1000000)]:
#             if abbrev[0] in followers:
#                 followers = int(followers[:-1]) * abbrev[1]
#             if abbrev[0] in posts:
#                 followers = int(posts[:-1]) * abbrev[1]

#         return int(followers), int(posts)
#     # time.sleep(5)
#     try:
#         # print(instagram)
#         get_followers_and_posts(instagram)
#         return True
#     except:
#         return False

# for tt in account_data_indiv.index[:]:
#     insta = account_data_indiv['Instagram'][tt]
#     print(insta, active(insta), account_data_indiv['FB App Owner'][tt])
#     time.sleep(3)