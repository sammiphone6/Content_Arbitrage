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
folder = 'account_adding/data'

# def get_fbs():
#     filename = f'{folder}/fbs.csv'
#     with open(filename) as file:
#         data = [token.split(',') for token in file.read().split('\n')]
#     return data

def get_instas():
    filename = f'{folder}/instas.csv'
    df = pd.read_csv(filename)
    return df

def get_fbs():
    filename = f'{folder}/fbs.csv'
    df = pd.read_csv(filename, index_col='Facebook account')
    df = df.convert_dtypes()
    return df

def get_infos():
    return open_filedata(f'{folder}/infos.txt')

def get_tiktok_data():
    return open_filedata(f'{folder}/tiktok_accounts_data.txt')

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
    fbs.to_csv(filename, index_label='Facebook account')

def save_updated_counters(instas_start = None, infos_start = None):
    counters = open_filedata(f'{folder}/insta_creation_counters.txt')

    if instas_start != None: counters.update({'instas': instas_start})
    if infos_start != None: counters.update({'infos': infos_start})

    save_filedata(f'{folder}/insta_creation_counters.txt', counters)

def save():
    pass
    


## INITIALIZE DATABASES FOR OTHER FILES

instas = get_instas()
infos = get_infos()
tiktok_account_data = get_tiktok_data()

counters = open_filedata(f'{folder}/insta_creation_counters.txt')
instas_start = counters['instas']
infos_start = counters['infos']

fbs = get_fbs()

