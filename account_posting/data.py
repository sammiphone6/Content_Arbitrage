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
    'reedtwinz',
    'miyaevarenae',
    'batzair',
    'its.marianne.faith',
    'readchoi',
    'victoriabachlet',
    'rauld33',
    'celia_7721',
    'kamtunechi',
    'robbieroket',
    'bobbie',
    'demibagby',
    'damedamian',
    'kaileenleilani',
    'athenafawn',
    'paigezilba',
    'insecthaus_adi',
    'allieschnacky',
]
email_exclude = [
    'rrrobr578@gmail.com', 
    'lolitkhan667@exdonuts.com',
    'tonmoykhan685@exdonuts.com',
    'sumaiya8bd009@ccmail.uk',
    'endrishyti027@yahoo.com',
    'shanta2bd009@ccmail.uk',
    'khusi6bd009@exdonuts.com',
    'andigurakuqi079@yahoo.com',
]
email_exclude += [ #blocked for spam - wait till friday evening to post
    'sam@ercfilings.us',
    'digitalempiremgmt2@gmail.com',
    'digitalempiremgmt3@gmail.com',
    'maishax1bd009@ccmail.uk',
    'mirajahanbd091@ccmail.uk',
    'yasminbd009sikdar@ccmail.uk',
    'glenduro047@yahoo.com',
    'lamiyaaktherbd464@ccmail.uk',
    'fahima1bd099@ccmail.uk',
    'gazmirshyti048@yahoo.com',
    'nazminbdislam09@ccmail.uk',
    'noelbaku074@yahoo.com',
    'glenloshi064@yahoo.com',
    'sadiaqueenbd574@ccmail.uk',
    'maisha3bd009@ccmail.uk',
    'rimakhan464@ccmail.uk',
    'nargisxhaque5763@exdonuts.com',
    'taniya6bd0093@ccmail.uk',
    'nilima3bd009@ccmail.uk',
    'maisha2xbd009@ccmail.uk',
    'morimjrx555@simaenaga.com',
    'samiaxhadi46@exdonuts.com',
    'saimakhanbd09@ccmail.uk',
    'sumaiya9bd009@ccmail.uk',
    'shimakhanbd110@ccmail.uk',
    'adritabd809@ccmail.uk',
]
# email_exclude += ['sam@ercfilings.us', 'digitalempiremgmt2@gmail.com',
#        'digitalempiremgmt3@gmail.com', 'shimaxc2566@simaenaga.com',
#        'morimjrx555@simaenaga.com', 'yasminbd009sikdar@ccmail.uk',
#        'shimakhanbd110@ccmail.uk', 'sadiyabd109@exdonuts.com',
#        'nilima3bd009@ccmail.uk', 'maishax1bd009@ccmail.uk',
#        'maisha2xbd009@ccmail.uk', 'sumaiya9bd009@ccmail.uk',
#        'maisha3bd009@ccmail.uk', 'nazminbdislam09@ccmail.uk',
#        'fahima1bd099@ccmail.uk', 'saimakhanbd09@ccmail.uk',
#        'adritabd809@ccmail.uk', 'sumaiyasscbd009@ccmail.uk',
#        'taniya6bd0093@ccmail.uk', 'gazmirshyti048@yahoo.com',
#        'noelbaku074@yahoo.com', 'lamiyaaktherbd464@ccmail.uk',
#        'glenloshi064@yahoo.com', 'sadia2bd0@exdonuts.com',
#        'lolitkhan667@exdonuts.com', 'glenduro047@yahoo.com',
#        'sadiaqueenbd574@ccmail.uk', 'tonmoykhan685@exdonuts.com',
#        'rimakhan464@ccmail.uk', 'nargisxhaque5763@exdonuts.com',
#        'sumaiya4bd008@ccmail.uk', 'sumaiya8bd009@ccmail.uk',
#        'endrishyti027@yahoo.com', 'mirajahanbd091@ccmail.uk',
#        'shanta2bd009@ccmail.uk', 'samiaxhadi46@exdonuts.com',
#        'khusi6bd009@exdonuts.com', 'misty8bd009@ccmail.uk',
#        'ritukhan1bd009@ccmail.uk', 'riyakhanxff7u@ccmail.uk',
#        'saimiragolli094@yahoo.com', 'albanxhafa095@yahoo.com',
#        'andigurakuqi079@yahoo.com', 'genciagolli096@yahoo.com',
#        'glenbrahimi092@yahoo.com', 'noelgurakuqi091@yahoo.com',
#        'erionshyti095@yahoo.com', 'gencizane092@yahoo.com',
#        'alesandroshyti096@yahoo.com']

exclude += [acc for acc in list(account_data_indiv.index) if account_data_indiv['FB App Owner'][acc] in email_exclude]