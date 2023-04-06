import pandas as pd
import pickle
import numpy as np
import time
import datetime

## FILE METHODS
def open_filedata(filename):
    file = open(filename, 'rb')
    filedata = pickle.load(file)
    return filedata

def save_filedata(filename, filedata):
    file = open(filename, 'wb')
    pickle.dump(filedata, file)
    file.close()


## DATA METHODS
folder = 'data'

def get_fbs():
    filename = f'{folder}/fbs.csv'
    with open(filename) as file:
        data = [token.split(',') for token in file.read().split('\n')]
    return data

def get_instas():
    filename = f'{folder}/instas.csv'
    df = pd.read_csv(filename)
    return df

def get_fbs():
    filename = f'{folder}/fbs.csv'
    df = pd.read_csv(filename)
    return df

def get_infos():
    return open_filedata('data/infos.txt')

def get_tiktok_data():
    return open_filedata('data/tiktok_accounts_data.txt')

## Save Methods
def save_csv(filename, filedata):
    data = '\n'.join([','.join(token) for token in filedata])
    with open(filename, 'w') as file:
        file.write(data)
    return data

def save_instas():
    filename = f'{folder}/instas.csv'
    instas.to_csv(filename, index = False)

def save_fbs():
    filename = f'{folder}/fbs.csv'
    fbs.to_csv(filename, index = False)

def save_updated_counters(instas_start = None, infos_start = None):
    counters = open_filedata('data/insta_creation_counters.txt')

    if instas_start != None: counters.update({'instas': instas_start})
    if infos_start != None: counters.update({'infos': infos_start})

    save_filedata('data/insta_creation_counters.txt', counters)

def save():
    pass
    
# print(datetime.datetime.fromtimestamp(1680738339.0))

# save_updated_counters(instas_start = 0, infos_start = 0)
# save_updated_counters(instas_start = 1)

## INITIALIZE DATABASES FOR OTHER FILES

instas = get_instas()
infos = get_infos()
tiktok_account_data = get_tiktok_data()

counters = open_filedata('data/insta_creation_counters.txt')
instas_start = counters['instas']
infos_start = counters['infos']

fbs = get_fbs()



# print(len(infos))
# [infos.append(acc) for acc in tiktok_account_data if acc not in infos]
# print(len(infos))
# save_filedata('data/infos.txt', infos)

# print('counters: ', counters)
# for name in tiktok_account_data:
#     if name not in ['hannahstocking', 'hoopsnation', 'bilalahy', 'noahschnapp', 'mattiapolibio', 'coupleontour']:
#         tiktok_account_data[name]['tt_name'] = tiktok_account_data[name]['tt_name'].replace('&amp;', '&')
#         tiktok_account_data[name]['tt_bio'] = tiktok_account_data[name]['tt_bio'].replace('&amp;', '&')
#         tiktok_account_data[name]['ig_name'] = tiktok_account_data[name]['ig_name'].replace('&amp;', '&')
#         tiktok_account_data[name]['ig_bio'] = tiktok_account_data[name]['ig_bio'].replace('&amp;', '&')
# print(tiktok_account_data)

# save_filedata('data/tiktok_accounts_data.txt', tiktok_account_data)

# print(pd.concat(instas, pd.DataFrame({'Facebook account': [0]*600})))
# print(instas)
# values = [np.nan]*600
# instas['Facebook account'] = values
# instas['Page name'] = values
# instas['Facebook Result'] = values
# instas['Facebook Screenshot'] = values
# instas['Facebook Timestamp'] = values
# save_instas()
# print(instas)