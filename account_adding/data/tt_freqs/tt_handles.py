import requests
from account_posting.data import save_filedata

accounts = []
countries = ['us', 'fr', 'gb', 'de', 'it', 'es', 'pt', 'in', 'cn', 'jp']
for country in countries:
    cookies = {
    '_ga': 'GA1.2.64026851.1678582994',
    '_gid': 'GA1.2.373650356.1678582994',
    '_gat': '1',
    }

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': '_ga=GA1.2.64026851.1678582994; _gid=GA1.2.373650356.1678582994; _gat=1',
    'If-None-Match': 'W/"67b49-UCe2kpeVAUpGMAWW4EZStLAZ5Bw"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    }

    params = {
    'limit': '100',
    'country': {country},
    }

    response = requests.get('https://tokfluence.com/top', params=params, cookies=cookies, headers=headers)
    print(response)

    text = response.text
    signal = "tiktok.com/@"
    c_accounts = [token.split("\"")[0] for token in text.split(signal)[1:]]
    accounts += c_accounts
print(accounts)
print(len(accounts))
save_filedata('tt_handles.txt', accounts)
