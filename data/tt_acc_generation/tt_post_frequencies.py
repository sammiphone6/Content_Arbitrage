from tt_update_data import query
from data import open_filedata, save_filedata
from multiprocessing import Process, Manager
import pandas as pd
import time

def post_freq(account, num_vids):
    text = query(account)
    signal = "\"createTime\":\""
    created_time = text.split(signal)[num_vids+1].split("\"")[0]
    timespan = time.time() - int(created_time)
    rate = timespan/num_vids
    return round(rate/3600, 2)

def rates():
    df = pd.DataFrame()
    for account in responses:
        rate = responses[account]
        new_row = dict()
        new_row['account'] = account
        new_row['rate'] = rate
        if(df.empty):
            for key in new_row:
                new_row[key] = [new_row[key]]
            df = pd.DataFrame(new_row)
        else:
            df = df.append(new_row, ignore_index = True)
    return df.sort_values(by=['rate'], ascending = True).reset_index(drop = True)

def get_rates(accounts, num_vids):
    def compute(responses, account):
        try:
            responses[account] = post_freq(account, num_vids)
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

    start = time.time()
    runInParallel()

    stats = rates()
    save_filedata('tt_rates.txt', stats)
    print(stats, "\n")

    end = time.time()
    print(end-start, "\n")

responses = dict()
accounts = open_filedata('tt_handles.txt')
import random
 
arr_nodup = []
[arr_nodup.append(acc) for acc in accounts if acc not in arr_nodup]
# n=len(arr_nodup)-1
# arr = []
# for i in range(n):
#     random_index = random.randint(0, n-i)
#     temp = accounts.pop(random_index)
#     arr.append(temp)
# print(arr[:20])

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.float_format', '{:20,.2f}'.format)
pd.set_option('display.max_colwidth', None)

get_rates(arr_nodup, 25)
# get_rates(['funny.vse', 'alixxxx', 'alixearle'], 10)