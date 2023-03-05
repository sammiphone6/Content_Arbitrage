from tt_update_data import open_filedata, save_filedata
from tt_download_tiktoks import download_tiktoks_and_update_database
from ig_post_functions import post_reel
from misc_functions import announce_pause, max_factor_under, get_account_data
import time
import datetime
from exclude import exclude

account_data = get_account_data()
## --------------------------------------------------------------------------------------##
## THIS USES PYNPUT / GOOGLE SHEETS AND IS NEEDED MANUALLY ON THE COMPUTER. DON'T FORGET ##
num_accounts = len(account_data.index) - 4
print(num_accounts)
batch_size = 7 #max_factor_under(15, num_accounts)
download_tiktoks_and_update_database(batch_size, num_accounts)
## --------------------------------------------------------------------------------------##

tiktok_data_indiv = open_filedata('tiktok_data_indiv.txt')
tiktok_captions_indiv = open_filedata('tiktok_captions_indiv.txt')

def do_round_of_posting():
    num_posts = 0
    num_accounts = 0
    for account in tiktok_data_indiv:
        if(account not in exclude and tiktok_data_indiv[account]["last_posted"] < len(tiktok_data_indiv[account]["video_ids"]) - 1):
            vid_id = tiktok_data_indiv[account]["video_ids"][tiktok_data_indiv[account]["last_posted"]+1]
            tt_link = f"https://tiktok.com/@{account}/video/{vid_id}/"
            tt_caption = tiktok_captions_indiv[vid_id] + f" #{account_data['Hashtag'][account]}" #ADD THEIR NAME TO THIS HANDLE
            
            post_reel(account, tt_link, tt_caption)
            tiktok_data_indiv[account]["last_posted"] += 1 
            save_filedata("tiktok_data_indiv.txt", tiktok_data_indiv)
            num_posts+=1
        num_accounts+=1
        announce_pause(4)
    print(f"POSTING ROUND COMPLETED: {num_posts} POSTS MADE ACROSS {num_accounts} ACCOUNTS.")
    return num_posts



start = time.time()
num_posts = -1
# while(num_posts != 0):
for _ in range(1):
    num_posts = do_round_of_posting()
    # announce_pause(15*60)
print("DONE RUNNING")
end = time.time()
print(end - start)
print ("Finished at ", datetime.datetime.fromtimestamp(time.time()))











## AFTER WRITING, YOU WILL REPLACE THE ABOVE CODE WITH A "CATCHUP_POSTS" FUNCTION WHERE ALL THE
## UNPOSTED VIDEO_IDS FOR EACH ACCOUNT ARE POSTED. MOVE THIS FUNCTION TO ANOTHER FILE TO KEEP
## THIS MAIN FILE CLEAN