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

def get_account_data_indiv():
    filename = f'{folder}/account_data_indiv.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    return df

def get_account_data_popular():
    filename = f'{folder}/account_data_popular.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    return df

def get_fb_app_data():
    filename = f'{folder}/fb_app_data.csv'
    df = pd.read_csv(filename).set_index('Email')
    return df

def get_tiktok_data_indiv():
    return open_filedata(f'{folder}/tiktok_data_indiv.txt')

def get_tiktok_capions_indiv():
    return open_filedata(f'{folder}/tiktok_captions_indiv.txt')

def get_tiktok_data_popular():
    return open_filedata(f'{folder}/tiktok_data_popular.txt')

def save_files():
    save_filedata(f'{folder}/tiktok_data_indiv.txt', tiktok_data_indiv)
    save_filedata(f'{folder}/tiktok_captions_indiv.txt', tiktok_captions_indiv)
    save_filedata(f'{folder}/tiktok_data_popular.txt', tiktok_data_popular)
    
## INITIALIZE DATABASES FOR OTHER FILES

account_data_indiv = get_account_data_indiv()
account_data_popular = get_account_data_popular()
fb_app_data = get_fb_app_data()

tiktok_data_indiv = get_tiktok_data_indiv()
tiktok_captions_indiv = get_tiktok_capions_indiv()
tiktok_data_popular = get_tiktok_data_popular()

exclude = [
    'nasdaily',
    'petermckinnon'
]