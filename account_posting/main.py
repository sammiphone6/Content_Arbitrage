from ig_post_functions import post_round_indiv, post_round_popular, run_tests, posts_sync
from insights_sync import get_insights, plot_barchart
from misc_functions import announce_pause
from data import account_data_indiv, account_data_popular, exclude
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
    'indiv',
    'popular',
]

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

