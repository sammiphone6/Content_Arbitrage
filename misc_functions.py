import pandas as pd 
import time

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

def get_account_data():
    filename = 'account_data.csv'
    df = pd.read_csv(filename).set_index('TT Account')
    return df

def get_fb_app_data():
    filename = 'fb_app_data.csv'
    df = pd.read_csv(filename).set_index('Email')
    return df