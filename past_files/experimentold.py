import requests

def check_username(username):
    cookies = {
        # 'dpr': '2',
        # 'csrftoken': 'ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr',
        # 'mid': 'ZCbL0QAEAAG2s8tbvORyKr1ojdID',
        # 'ig_did': 'A826ECAF-2499-4076-BE4B-86F1DC0F1A8B',
        # 'ig_nrcb': '1',
        # 'datr': 'ycsmZDOym4SoVV8SY7uM0df5',
    }

    headers = {
        # 'authority': 'www.instagram.com',
        # 'accept': '*/*',
        # 'accept-language': 'en-US,en;q=0.9',
        # 'content-type': 'application/x-www-form-urlencoded',
        # # 'cookie': 'dpr=2; csrftoken=ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr; mid=ZCbL0QAEAAG2s8tbvORyKr1ojdID; ig_did=A826ECAF-2499-4076-BE4B-86F1DC0F1A8B; ig_nrcb=1; datr=ycsmZDOym4SoVV8SY7uM0df5',
        # 'origin': 'https://www.instagram.com',
        # 'referer': 'https://www.instagram.com/accounts/emailsignup/',
        # 'sec-ch-prefers-color-scheme': 'light',
        # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"macOS"',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-origin',
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        # 'viewport-width': '1792',
        # 'x-asbd-id': '198387',
        'x-csrftoken': 'ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr',
        # 'x-ig-app-id': '936619743392459',
        # 'x-ig-www-claim': '0',
        # 'x-instagram-ajax': '1007221364',
        # 'x-requested-with': 'XMLHttpRequest',
        # 'x-web-device-id': 'A826ECAF-2499-4076-BE4B-86F1DC0F1A8B',
    }

    data = {
        'email': '',
        'username': username,
        'first_name': '',
        'opt_into_one_tap': 'false',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)
    return "This username isn't available." not in response.text

def check_usernames(usernames, suffixes):
    names_to_test = [f'{username}{suffix}' for username in usernames for suffix in suffixes]

    results = dict()
    for name in names_to_test:
        print('\n\n', name)
        results[name] = check_username(name)
        print(results[name])

    print(results)

usernames = ['jorge']
suffixes = ['official', 'highlights']
check_usernames(usernames, suffixes)