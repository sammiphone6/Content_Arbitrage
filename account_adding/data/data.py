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
    with open(filename) as file:
        data = [token.split(',') for token in file.read().split('\n')]
    return data

def get_new_instas():
    filename = f'{folder}/new_instas.csv'
    with open(filename) as file:
        data = [token.split(',') for token in file.read().split('\n')]
    return data

def get_ready_accounts():
    filename = f'{folder}/ready_accounts.csv'
    with open(filename) as file:
        data = [token.split(',') for token in file.read().split('\n')]
    return data


## Save Methods
def save_csv(filename, filedata):
    data = '\n'.join([','.join(token) for token in filedata])
    with open(filename, 'w') as file:
        file.write(data)
    return data

def save():
    save_filedata(f'{folder}/counters.txt', counters)
    save_csv(f'{folder}/ready_accounts.csv', ready_accounts)
    save_csv(f'{folder}/fbs.csv', fbs)
    

## INITIALIZE DATABASES FOR OTHER FILES

fbs = get_fbs()
instas = get_instas()
new_instas = get_new_instas()
ready_accounts = get_ready_accounts()
counters = open_filedata('data/counters.txt')

# save_csv(f'{folder}/ready_accounts.csv', [['email1@', 'pwd1', '2'], ['email2@', 'pwd2', '2']])