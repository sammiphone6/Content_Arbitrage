from ig_post_functions import post_round_indiv, post_round_popular
from test_sync import run_tests
from insights_sync import get_insights, plot_barchart
from misc_functions import announce_pause
from post_sync import posts_sync
from data import account_data_indiv, account_data_popular, exclude
import datetime
import time

start = time.time()

# run_tests(deep_test=False)
# get_insights()
# plot_barchart() #per day
# plot_barchart(days=30, log_scale=True, cumulative=True) #per acct

## Just comment out whichever one you don't want
post_types = [
    'indiv',
    'popular',
]

accounts = []
if 'indiv' in post_types: accounts += [acc for acc in account_data_indiv.index if acc not in exclude]
if 'popular' in post_types: accounts += [acc for acc in account_data_popular.index if acc not in exclude]

for i in range(1):
    posts_sync(accounts)


print("DONE RUNNING")
end = time.time()
print(end - start)
print ("Finished at ", datetime.datetime.fromtimestamp(time.time()))

