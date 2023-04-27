import requests
import string
import time
import uuid, string, random
from account_posting.ig_defines import proxies
from multiprocessing import Process, Manager

proxy_nums = [22, 25, 36]

def search_ig(name, letter):

    cookies = {
        'dpr': '2',
        'mid': 'ZEhniQAEAAFgugIQEbknNVUuFWBr',
        'ig_did': 'F8D20428-5CD9-4209-97BF-E9295CBED142',
        'ig_nrcb': '1',
        'datr': 'h2dIZEyHo6vhbap52eIyJF-z',
        'csrftoken': 'EB5jBVMP3hHiOtEyW7ii0U7oxOuAILA8',
        'ds_user_id': '58399727995',
        'sessionid': '58399727995%3AHZ252yJAzyX0fY%3A2%3AAYdsNQSSqtwdm4Nbt4JMaEfsz-yixWMZtpGtPaAyPg',
        'rur': '"CLN\\05458399727995\\0541714002763:01f76475604c6c314632cf38bce557080ded77bf9f96e8eca11ded599fcbf6e10e95799f"',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'dpr=2; mid=ZEhniQAEAAFgugIQEbknNVUuFWBr; ig_did=F8D20428-5CD9-4209-97BF-E9295CBED142; ig_nrcb=1; datr=h2dIZEyHo6vhbap52eIyJF-z; csrftoken=EB5jBVMP3hHiOtEyW7ii0U7oxOuAILA8; ds_user_id=58399727995; sessionid=58399727995%3AHZ252yJAzyX0fY%3A2%3AAYdsNQSSqtwdm4Nbt4JMaEfsz-yixWMZtpGtPaAyPg; rur="CLN\\05458399727995\\0541714002763:01f76475604c6c314632cf38bce557080ded77bf9f96e8eca11ded599fcbf6e10e95799f"',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'viewport-width': '1792',
        'x-asbd-id': '198387',
        'x-csrftoken': 'EB5jBVMP3hHiOtEyW7ii0U7oxOuAILA8',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR1siIjf3bkj4nrI-0LmUjm3EMNhlxOlvl2xXIUC-3yYY20x',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'context': 'blended',
        'query': name + letter,
        'rank_token': '0.2668054778771136',
        'include_reel': 'true',
        'search_surface': 'web_top_search',
    }

    response = requests.get('https://www.instagram.com/api/v1/web/search/topsearch/', params=params, cookies=cookies, headers=headers)
    json = response.json()
    results = []
    print(0, response)
    # import pprint
    # pp = pprint.PrettyPrinter(depth=6)
    for user in json['users']:
        # print(user)
        full_name = user['user']['full_name']
        if full_name == name:
            results.append(user['user']['username'])
    return results

def find_all(name):
    all = []
    for letter in string.ascii_lowercase:
        time.sleep(2)
        find = search_ig(name, letter)
        # print(find)
        all += [r for r in find if r not in all]
    return all

def available_gmail(name):
    proxy = proxies(random.choice(proxy_nums))
    cookies = {
        '__Host-GAPS': '1:u9G0T0rTyo3Vt0MVCQWCPGwHZg1jkg:lzk1XvQz-Fy_P6bN',
        'NID': '511=a_B-kDofGjI39gYhy7cOXSQLbTJccMY1xGCuKVOdS_OwAbd9n2vwypzTQUZF04Wa4KthM58PU-x6OsvLea9PEMHSx23WPNIVvYEd9y4uYsx2hQK9CCEkKE76xfsBWR36YIvnEswvjUVIe-L1DkMmXFlmAQt5h0LnXeIRWdomNEs',
    }

    headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # 'cookie': '__Host-GAPS=1:u9G0T0rTyo3Vt0MVCQWCPGwHZg1jkg:lzk1XvQz-Fy_P6bN; NID=511=a_B-kDofGjI39gYhy7cOXSQLbTJccMY1xGCuKVOdS_OwAbd9n2vwypzTQUZF04Wa4KthM58PU-x6OsvLea9PEMHSx23WPNIVvYEd9y4uYsx2hQK9CCEkKE76xfsBWR36YIvnEswvjUVIe-L1DkMmXFlmAQt5h0LnXeIRWdomNEs',
        'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-same-domain': '1',
    }

    params = {
        'hl': 'en-GB',
        '_reqid': '51985',
        'rt': 'j',
    }

    data = f'continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&f.req=%5B%22AEThLlxPgLeF9X4pDr0D6HC7KYZgzTFnmV0-erEVDU1R4DQQ4ryr_Z218-xeOyAo7x1cg_kp4tRQF3fXIjeT9fAp3za2ceyziD5rxneyv_5R9Sp7GibBlN-vSjZwZ8GKGQuse1uTf3970ZkTn4KpYac3ri-j91WNYoAnyWjWePD1_7dTwzLY-DFHQqMw_bkmx0MSTyxBklVTJxtDrSzbRbcgdYcM_SoJpg%22%2C%22%22%2C%22%22%2C%22'
    data += f'{name}%22%2Ctrue%2C%22S269319110%3A1682447165729799%22%2C1%5D&azt=AFoagUUkPZtfm6zlIVbcze0GgJC1A6J80g%3A1682447165751&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22SG%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cfalse%2C1%2C%22%22%2Cnull%2Cnull%2C1%5D&gmscoreversion=undefined&'

    response = requests.post(
        'https://accounts.google.com/_/signup/webusernameavailability',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        proxies=proxy
    )
    text = response.text
    num = text[text.index("\",")+2]
    # print(num)
    return str(num) == str(1)


def backup_email(m_resps, name):
    i = random.choice(proxy_nums)
    proxy = proxies(i)
    data = {
        "_csrftoken":
        "".join(
            random.choices(string.ascii_lowercase +
                        string.ascii_uppercase + string.digits,
                        k=32)),
        "username":
        name,
        "guid":
        uuid.uuid4(),
        "device_id":
        uuid.uuid4()
    }
    head = {
        "user-agent":
        f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"
    }
    response = requests.post(
        "https://i.instagram.com/api/v1/accounts/send_password_reset/",
        headers=head,
        data=data,
        proxies=proxy)
    print(i, response)
    text = response.text
    # print(text)
    if "obfuscated_email" not in text: return False
    if "@gmail.com" not in text: return False

    email_username = text.split("@gmail.com")[0].replace(' ', '\"').split("\"")[-1]
    print(email_username)
    if (name[0] == email_username[0] and name[-1] == email_username[-1]):
        m_resps.append(name)
        return True
    return False

def find_all_valids(m_resps, name):
    # print("Doing name: ", name)
    potential_accounts = find_all(name)
    # print("Potential accounts: ", potential_accounts)

    def runInParallel(names):
        with Manager() as manager:
            m_resps = manager.list()
            proc = []
            for name in names:
                p = Process(target=backup_email, args=(m_resps, name))
                proc.append(p)
                p.start()
                time.sleep(0.8)
            for p in proc:
                p.join()
            return list(m_resps)

    gmail_backed = runInParallel(potential_accounts)
    # print("Gmail backed: ", gmail_backed)
    valid_accounts = [g for g in gmail_backed if available_gmail(g)]
    print(f"Valid accounts for {name}: ", valid_accounts)
    m_resps += valid_accounts
    return valid_accounts

def runInParallel(names):

    with Manager() as manager:
        m_resps = manager.list()
        proc = []
        for name in names:
            p = Process(target=find_all_valids, args=(m_resps, name))
            proc.append(p)
            p.start()
            time.sleep(60)
        for p in proc:
            p.join()
        print("ALL VALID: ", list(m_resps))

names = [
    # 'eangelo',
    # 'nielgca',
    # 'athalia',
    # 'addosin',
    # 'ugustus',
    # 'laudia',
    # 'aemrn',
    # 'onique',
    'enevieve',
    'ovanni',
    'lexzdnaer',
    'axton',
    'asisus',
    'atrert',
    'nruquie',
    'inlocn',
    'ourtney',
]

runInParallel(names)