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

def get_account_data_financial():
    filename = f'{folder}/account_data_financial.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    df['IG ID'] = df['IG ID'].astype(str)
    return df

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

def get_financial_tts():
    filename = f'{folder}/tt_account_financial.csv'
    df = pd.read_csv(filename).set_index('TT Account')
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

def get_tiktok_data_financial():
    return open_filedata(f'{folder}/tiktok_data_financial.txt')


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
    save_filedata(f'{folder}/tiktok_data_financial.txt', tiktok_data_financial)
    
## INITIALIZE DATABASES FOR OTHER FILES

account_data_indiv = get_account_data_indiv()
account_data_financial = get_account_data_financial()
account_data_popular = get_account_data_popular()
fb_app_data = get_fb_app_data()

tiktok_data_indiv = get_tiktok_data_indiv()
tiktok_captions_indiv = get_tiktok_capions_indiv()
tiktok_data_popular = get_tiktok_data_popular()
tiktok_data_financial = get_tiktok_data_financial()
financial_tts = get_financial_tts()


exclude = [
    'nasdaily',
    'jostasy',
    # 'petermckinnon',
    'baby_simba47',
    'tiffandchan',
]
email_exclude = [
    'rrrobr578@gmail.com', 
    'lolitkhan667@exdonuts.com',
    'tonmoykhan685@exdonuts.com',
    'sumaiya8bd009@ccmail.uk',
    'endrishyti027@yahoo.com',
    'shanta2bd009@ccmail.uk',
    'khusi6bd009@exdonuts.com',
]
exclude += [acc for acc in list(account_data_indiv.index) if account_data_indiv['FB App Owner'][acc] in email_exclude]