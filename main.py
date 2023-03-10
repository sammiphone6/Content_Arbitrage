from tt_update_data import open_filedata, save_filedata, update_data
from ig_post_functions import post_reel, do_round_of_posting
from misc_functions import announce_pause, max_factor_under, get_account_data_indiv
import time
import datetime
from exclude import exclude

# tiktok_data_indiv = open_filedata('tiktok_data_indiv.txt')
# tiktok_captions_indiv = open_filedata('tiktok_captions_indiv.txt')



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