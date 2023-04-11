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


## DATA GET METHODS
folder = 'account_posting/data'

def get_account_data_indiv():
    filename = f'{folder}/account_data_indiv.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    df['IG ID'] = df['IG ID'].astype(str)
    return df

def get_account_data_popular():
    filename = f'{folder}/account_data_popular.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    df['IG ID'] = df['IG ID'].astype(str)
    return df

def get_fb_app_data():
    filename = f'{folder}/fb_app_data.csv'
    df = pd.read_csv(filename).set_index('Email')
    df['App ID'] = df['App ID'].astype(str)
    return df

def get_tiktok_data_indiv():
    return open_filedata(f'{folder}/tiktok_data_indiv.txt')

def get_tiktok_capions_indiv():
    return open_filedata(f'{folder}/tiktok_captions_indiv.txt')

def get_tiktok_data_popular():
    return open_filedata(f'{folder}/tiktok_data_popular.txt')


## SAVE METHODS
def save_account_data_indiv():
    filename = f'{folder}/account_data_indiv.csv'
    account_data_indiv.to_csv(filename)

def save_account_data_popular():
    filename = f'{folder}/account_data_popular.csv'
    account_data_popular.to_csv(filename)

def save_fb_app_data():
    filename = f'{folder}/fb_app_data.csv'
    fb_app_data.to_csv(filename)

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
    'jostasy',
    'petermckinnon',
]
exclude += [acc for acc in list(account_data_indiv.index) if account_data_indiv['FB App Owner'][acc] == 'rrrobr578@gmail.com']