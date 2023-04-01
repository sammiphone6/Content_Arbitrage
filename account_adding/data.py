import pandas as pd
import pickle

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

def save():
    pass
    

## INITIALIZE DATABASES FOR OTHER FILES

instas = get_instas()
infos = get_infos
tiktok_account_data = get_tiktok_data()