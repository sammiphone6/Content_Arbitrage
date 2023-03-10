import pandas as pd 
import time
from tt_update_data import open_filedata, save_filedata, update_data
from exclude import exclude

def announce_pause(sec):
    print("currently pausing for ", sec, " seconds if you want to stop program")
    time.sleep(sec/2)
    print("halfway done")
    time.sleep(sec/2)
    print("done pausing")

def max_factor_under(l, n):
    test_list = [i for i in range(l)][::-1]
    for i in test_list:
        if n%i == 0:
            return i
    return 1

def get_account_data_indiv():
    filename = 'account_data_indiv.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    return df

def get_account_data_popular():
    filename = 'account_data_popular.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    return df

def get_fb_app_data():
    filename = 'fb_app_data.csv'
    df = pd.read_csv(filename).set_index('Email')
    return df


