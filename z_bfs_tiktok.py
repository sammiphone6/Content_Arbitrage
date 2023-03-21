import requests
from data import open_filedata, save_filedata
from tt_update_data import query
import time
import pprint


def query_id(id):
    cookies = {
        # 'tt_csrf_token': 'cIo4PKSU-WZqSdhF_AMwQDVsr0_Q0TxrlOic',
        # 'tt_chain_token': 'gtTFLw7UFVpzPrZhCjYzOQ==',
    }

    headers = {
        'authority': 'us.tiktok.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'tt_csrf_token=cIo4PKSU-WZqSdhF_AMwQDVsr0_Q0TxrlOic; tt_chain_token=gtTFLw7UFVpzPrZhCjYzOQ==',
        'origin': 'https://www.tiktok.com',
        'referer': 'https://www.tiktok.com/',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    params = {
        'aid': '1988',
        # 'app_language': 'en',
        # 'app_name': 'tiktok_web',
        # 'battery_info': '0.89',
        # 'browser_language': 'en-US',
        # 'browser_name': 'Mozilla',
        # 'browser_online': 'true',
        # 'browser_platform': 'MacIntel',
        # 'browser_version': '5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        # 'channel': 'tiktok_web',
        # 'cookie_enabled': 'true',
        # 'count': '30',
        # # 'device_id': '7213046521720899118',
        # 'device_platform': 'web_pc',
        # 'focus_state': 'true',
        # 'from_page': 'user',
        # 'history_len': '2',
        # 'is_fullscreen': 'true',
        # 'is_page_visible': 'true',
        # 'noUser': '0',
        # 'os': 'mac',
        # # 'pageId': '6853255256688919557',
        # 'priority_region': '',
        # 'referer': '',
        # 'region': 'US',
        # 'scene': '15',
        # 'screen_height': '1120',
        # 'screen_width': '1792',
        # 'tz_name': 'America/New_York',
        # 'userId': '6853255256688919557',
        # 'userId': '7008473615676294149',
        'userId': f'{id}',
        # 'webcast_language': 'en',
        # 'msToken': '',
        # 'X-Bogus': 'DFSzswVON-xANJcutcyqrr7TlqCz',
        # '_signature': '_02B4Z6wo00001GvpzmwAAIDD.z-VYkKKJeRr6crAAH7rbc',
    }

    response = requests.get('https://us.tiktok.com/node/share/discover', params=params, cookies=cookies, headers=headers)

    text = response.text
    tokens = text.split(r'{"cardItem":{"id":"')[1:]
    name_identifier = r'","subTitle":"@'
    like_identifier = r',"likes":'
    accounts = [(token[:token.index('\"')], 
                 token[token.index(name_identifier)+len(name_identifier):][:token[token.index(name_identifier)+len(name_identifier):].index('\"')],
                 token[token.index(like_identifier)+len(like_identifier):][:token[token.index(like_identifier)+len(like_identifier):].index(',\"')])
                 for token in tokens if name_identifier in token]

    return accounts

def get_id_likes_from_account(account):
    cookies = {
        # 'ttwid': '1%7C2Rth92njUKQvbSULTJtZs3A5Yk1wRPqMGZPGCD5HNak%7C1679437672%7C80df38dbd6c4d4dfd9963039f9a6db654a709bc5139a15f4752986fbaa40e271',
        # 'tt_csrf_token': 'hpN4MAtT-PdWw6JI_xY5agR0AcQUsmO5cz8o',
        # 'tt_chain_token': 'O79VabvRbP8BMEAC7JiNyg==',
        # 'tiktok_webapp_theme': 'light',
        # '__tea_cache_tokens_1988': '{%22_type_%22:%22default%22%2C%22user_unique_id%22:%227213129831176963590%22%2C%22timestamp%22:1679437674986}',
        # 'csrf_session_id': '9570dbe07cf2618480130fd23c812302',
        # 'ttwid': '1%7C2Rth92njUKQvbSULTJtZs3A5Yk1wRPqMGZPGCD5HNak%7C1679437676%7C27a65ee5369f9dd8bf668f34267a5348c10618da7e03bc2a28be934195ea3f1b',
        # 'msToken': 'PeC6Jnj1gfjSak652Q82LhIZ144jMSj_H3vqTS523hHYDUVyyToEjCEDFv0ckPa01sWoHSwSQuTXOm0NCLlWhhfZ3lNkBNLyFwXD9pnSmbaRa0-INnIygroY87a7GuucP17BPEfM9Hwk5A==',
        # 'msToken': 'PeC6Jnj1gfjSak652Q82LhIZ144jMSj_H3vqTS523hHYDUVyyToEjCEDFv0ckPa01sWoHSwSQuTXOm0NCLlWhhfZ3lNkBNLyFwXD9pnSmbaRa0-INnIygroY87a7GuucP17BPEfM9Hwk5A==',
    }

    headers = {
        'authority': 'www.tiktok.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'ttwid=1%7C2Rth92njUKQvbSULTJtZs3A5Yk1wRPqMGZPGCD5HNak%7C1679437672%7C80df38dbd6c4d4dfd9963039f9a6db654a709bc5139a15f4752986fbaa40e271; tt_csrf_token=hpN4MAtT-PdWw6JI_xY5agR0AcQUsmO5cz8o; tt_chain_token=O79VabvRbP8BMEAC7JiNyg==; tiktok_webapp_theme=light; __tea_cache_tokens_1988={%22_type_%22:%22default%22%2C%22user_unique_id%22:%227213129831176963590%22%2C%22timestamp%22:1679437674986}; csrf_session_id=9570dbe07cf2618480130fd23c812302; ttwid=1%7C2Rth92njUKQvbSULTJtZs3A5Yk1wRPqMGZPGCD5HNak%7C1679437676%7C27a65ee5369f9dd8bf668f34267a5348c10618da7e03bc2a28be934195ea3f1b; msToken=PeC6Jnj1gfjSak652Q82LhIZ144jMSj_H3vqTS523hHYDUVyyToEjCEDFv0ckPa01sWoHSwSQuTXOm0NCLlWhhfZ3lNkBNLyFwXD9pnSmbaRa0-INnIygroY87a7GuucP17BPEfM9Hwk5A==; msToken=PeC6Jnj1gfjSak652Q82LhIZ144jMSj_H3vqTS523hHYDUVyyToEjCEDFv0ckPa01sWoHSwSQuTXOm0NCLlWhhfZ3lNkBNLyFwXD9pnSmbaRa0-INnIygroY87a7GuucP17BPEfM9Hwk5A==',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://www.tiktok.com/@{account}', cookies=cookies, headers=headers)

    text = response.text
    id_identifier = r',"userId":"'
    id = text.split(id_identifier)[1][:text.split(id_identifier)[1].index('\"')]
    likes_identifier = r'/LikeAction"},"userInteractionCount":'
    likes = text.split(likes_identifier)[1][:text.split(likes_identifier)[1].index('}')]
    
    return (id, account, likes)

tiktok_accounts = open_filedata('tiktok_bfs.txt')

# query_id('6745191554350760966') # BFS starting at the rock

threshold = 10 * 1000 * 1000
i = 8750
while i < len(tiktok_accounts):
    save_filedata('tiktok_bfs.txt', tiktok_accounts)
    new_tiktoks = query_id(tiktok_accounts[i][0])
    [tiktok_accounts.append(tt) for tt in new_tiktoks if tt not in tiktok_accounts and int(tt[2]) > threshold]
    print(len(new_tiktoks), len(tiktok_accounts))
    i+=1
    print(i, ' iterations complete, ... ', len(tiktok_accounts)-i, ' remaining.')
    # time.sleep(1.7)

# pp = pprint.PrettyPrinter(depth=6)
# pp.pprint(tiktok_accounts[6808:6812])
# print(len(tiktok_accounts))

# for tt in tiktok_accounts:
#     if tt[1] == 'livvy':
#         print(tt)

