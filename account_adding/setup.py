import requests
from data import open_filedata, save_filedata
from tt_update_data import query
import time
import pprint
from multiprocessing import Process, Manager

folder = 'data/tt_freqs'
tiktok_bfs = open_filedata(f'{folder}/tiktok_bfs.txt')
tiktok_bfs = sorted(tiktok_bfs, key=lambda x: int(x[2]), reverse = True)
## We now have all 28k tiktok_bfs queries sorted by likes in decreasing order

accounts = []
[accounts.append(entry[1]) for entry in tiktok_bfs if entry[1] not in accounts]
## We now have all ~27k tiktoks usernames

def analysis(account, num_vids):
    def get_element(text, delim1, delim2, index = 1):
        return text.split(delim1)[index].split(delim2)[0]
    
    def check_username(username):
        ## AVAILBLE -> TRUE
        ## NOT AVAILABLE -> FALSE

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
        # print(response.text)
        return "This username isn't available." not in response.text

    def get_best_username(usernames):
        if isinstance(usernames, list) or isinstance(usernames, tuple):
            for username in usernames:
                if check_username(username): return username
            return False
        else:
            usernames = [
                f"{account}official",
                f"{account}highlights",
                f"bestof{''.join(account_results['name'].split()[0])}",
                f"{account}_exclusive",
                f"{account}_secrets",
            ]
            return get_best_username(usernames)

    
    account_results = dict()

    ## Query Tiktok
    text = query(account)
    
    ## Get rate of posting
    created_time = get_element(text, "\"createTime\":\"", "\"", index = num_vids+1) #text.split(signal)[num_vids+1].split("\"")[0]
    timespan = time.time() - int(created_time)
    rate = timespan/num_vids
    account_results['posting_rate'] = round(rate/3600, 2)

    ## Get total likes
    account_results['likes'] = get_element(text, "\"heartCount\":", ",")

    ## Get total followers
    account_results['followers'] = get_element(text, "\"authorStats\":{\"followerCount\":", ",")

    ## Get total following
    account_results['following'] = get_element(text, "\"followingCount\":", ",")

    ## Get number of videos
    account_results['videos'] = get_element(text, ",\"videoCount\":", ",")

    ## Get name
    account_results['name'] = get_element(text, "Watch the latest video from ", " (")

    ## Get bio
    account_results['bio'] = get_element(text, 'Followers. ', "Watch the latest video from ")

    ## Get PFP
    account_results['pfp'] = get_element(text, '\"og:image\" content=\"', "\"")

    ## Get respective insta username
    account_results['username'] = get_best_username(account)

    return account_results

def get_data(accounts, num_vids):
    responses = dict()
    def compute(responses, account):
        try:
            responses[account] = analysis(account, num_vids)
        except:
            pass
    
    def runInParallel():
        with Manager() as manager:
            m_resps = manager.dict()
            proc = []
            for i in range(len(accounts)):
                account = accounts[i]
                p = Process(target=compute, args=(m_resps, account))
                proc.append(p)
                p.start()
                time.sleep(0.5)
                print(i, '/', len(accounts))
                # if(i % 10 == 0):
                #     time.sleep(4)
            for p in proc:
                p.join()
            responses.update(m_resps)

    runInParallel()
    return responses

start = time.time()
accounts = ['alixearle', 'faithordway7', 'therock', 'selenagomez', 'loganpaul', 'lukebelmar']
accounts_data = get_data(accounts, 10)
pp = pprint.PrettyPrinter(depth=6)
pp.pprint(accounts_data)
print(time.time()-start)
# ## Run when land and change the tiktok query in analysis() and we now have all the data for these tiktok accounts. Maybe remove the time.sleep(0.5) or add a changevpn

# save_filedata('tiktok_accounts_data.txt', accounts_data)


### Get more good cheap instas https://accsmarket.com/en/catalog/instagram/pva 
### Also, fully automate by getting their name, pfp from tiktok, make some generic bio formula,
### And while creating a new account you can easily test available usernames from the ten we might want
### Bio formula should include not impersonating.