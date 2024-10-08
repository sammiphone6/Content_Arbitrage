from account_posting.ig_post_functions import post_round_indiv, post_round_popular, run_tests, posts_sync, update_and_post_indiv, postReel, post_sam_frank
from account_posting.insights_sync import get_insights, plot_barchart
from account_posting.misc_functions import announce_pause
from account_posting.access_token import debug_all_access_tokens, update_all_access_tokens, update_access_token, never_expiring_token, debug_access_token
from account_posting.data import account_data_indiv, account_data_popular, exclude, email_exclude, tiktok_data_indiv, tiktok_data_popular, fb_app_data, save_files
import datetime
import time
from account_posting.ig_defines import proxies

start = time.time()
def post_all(post_types, hashtags = True):
    accounts = []
    if 'indiv' in post_types: accounts += [acc for acc in account_data_indiv.index if acc not in exclude]
    if 'popular' in post_types: accounts += [acc for acc in account_data_popular.index if acc not in exclude]

    for _ in range(1):
        if accounts: posts_sync(accounts, hashtags = hashtags)

    print("DONE POSTING")
    end = time.time()
    print(end - start, '\n\n')


###### EDIT BELOW ######

## Just comment out whichever one you don't want
post_types = [
    'indiv',
    'popular',
]

# time.sleep(600)
# post_sam_frank(p = 0.5)
# posts_sync(['alixearle', 'sabquesada', 'onlyjayus', 'dayynaa', 'haleyybaylee', 'isaakpresley', 'faithordway7', 'fcbayern'])
# posts_sync(['onlyjayus', 'dayynaa', 'haleyybaylee', 'isaakpresley', 'faithordway7', 'fcbayern'])
# debug_all_access_tokens()

# update_and_post_indiv('breckiehill', increment=False)
# update_and_post_indiv('noelleleyva', increment=False)

run_tests(deep_test=False)
get_insights(sort = 'impressions')
post_all(post_types, hashtags = False)
# plot_barchart(show=True) #per day
# plot_barchart(days=30, log_scale=True, cumulative=True) #per acct

###### EDIT ABOVE ######


print("DONE RUNNING")
end = time.time()
print(end - start)
print ("Finished at ", datetime.datetime.fromtimestamp(time.time()))

