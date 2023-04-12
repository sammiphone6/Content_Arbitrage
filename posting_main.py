from account_posting.ig_post_functions import post_round_indiv, post_round_popular, run_tests, posts_sync, update_and_post_indiv
from account_posting.insights_sync import get_insights, plot_barchart
from account_posting.misc_functions import announce_pause
from account_posting.access_token import debug_all_access_tokens, update_all_access_tokens
from account_posting.data import account_data_indiv, account_data_popular, exclude, tiktok_data_indiv, save_files
import datetime
import time

start = time.time()
def post_all(post_types):
    accounts = []
    if 'indiv' in post_types: accounts += [acc for acc in account_data_indiv.index if acc not in exclude]
    if 'popular' in post_types: accounts += [acc for acc in account_data_popular.index if acc not in exclude]

    for _ in range(1):
        if accounts: posts_sync(accounts)

    print("DONE POSTING")
    end = time.time()
    print(end - start, '\n\n')


###### EDIT BELOW ######

## Just comment out whichever one you don't want
post_types = [
    # 'indiv',
    # 'popular',
]
    
# posts_sync(['newt', 'nickaufmann', 'lgndfrvr', 'datrie'])
# update_all_access_tokens()
# debug_all_access_tokens()

run_tests(deep_test=False)
get_insights()
# post_all(post_types)
plot_barchart() #per day
plot_barchart(days=30, log_scale=True, cumulative=True) #per acct

###### EDIT ABOVE ######


print("DONE RUNNING")
end = time.time()
print(end - start)
print ("Finished at ", datetime.datetime.fromtimestamp(time.time()))

