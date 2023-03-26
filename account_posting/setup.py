import pprint
from data import open_filedata, save_filedata
import time
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
    
    account_results = dict()

    ## Query Tiktok
                    # text = query(account)
    with open(f'{account}.txt', 'r') as file:
        text = file.read()
    
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
    #TODO

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

accounts_data = get_data(accounts, 10)
## Run when land and change the tiktok query in analysis() and we now have all the data for these tiktok accounts. Maybe remove the time.sleep(0.5) or add a changevpn

save_filedata('tiktok_accounts_data.txt', accounts_data)


### Get more good cheap instas https://accsmarket.com/en/catalog/instagram/pva 
### Also, fully automate by getting their name, pfp from tiktok, make some generic bio formula,
### And while creating a new account you can easily test available usernames from the ten we might want
### Bio formula should include not impersonating.