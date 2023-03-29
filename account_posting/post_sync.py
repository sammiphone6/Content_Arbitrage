from ig_post_functions import update_and_post_indiv, post_popular
from misc_functions import announce_pause
from multiprocessing import Process, Manager
from data import account_data_indiv, account_data_popular, exclude, tiktok_data_indiv, tiktok_captions_indiv, tiktok_data_popular, save_files
import time
import random


def posts_sync(accounts):
    def post(account, indiv_data, indiv_captions, popular_data):
        if account in account_data_indiv.index:
            print('Posting ', account)
            result = update_and_post_indiv(account, tt_data = True)
            print('FINISHED', account)
            if result[1] != 0: indiv_data[account] = result[1] 
            if result[2] != 0: indiv_captions = indiv_captions.update(result[2])
        if account in account_data_popular.index:
            result = post_popular(account, tt_data = True)
            if result[1] != 0: popular_data[account] = result[1]
    
    def runInParallel():
        with Manager() as manager:
            tt_indiv_data = manager.dict()
            tt_indiv_captions = manager.dict()
            tt_popular_data = manager.dict()
            
            proc = []
            for account in accounts:
                p = Process(target=post, args=(account, tt_indiv_data, tt_indiv_captions, tt_popular_data))
                proc.append(p)
                p.start()
            for p in proc:
                p.join()
            tiktok_data_indiv.update(tt_indiv_data)
            tiktok_captions_indiv.update(tt_indiv_captions)
            tiktok_data_popular.update(tt_popular_data)
            save_files()

    start = time.time()
    runInParallel()

    end = time.time()
    print("Posting Complete")
    print(end-start, "\n")

