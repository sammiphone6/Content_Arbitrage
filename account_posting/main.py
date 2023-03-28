from ig_post_functions import post_round_indiv, post_round_popular
from test_sync import run_tests
from insights_sync import get_insights, plot_barchart
from misc_functions import announce_pause
import datetime
import time

run_tests(deep_test=False)
get_insights()
plot_barchart() #per day
plot_barchart(days=30, log_scale=True, cumulative=True) #per acct

## Just comment out whichever one you don't want
post_types = [
    'indiv',
    'popular',
]

if post_types:
    start = time.time()

    for i in range(2):
        if 'indiv' in post_types:
            for _ in range(1):
                num_posts = post_round_indiv()

        if 'popular' in post_types:
            for _ in range(1):
                post_round_popular()

    print("DONE RUNNING")
    end = time.time()
    print(end - start)
print ("Finished at ", datetime.datetime.fromtimestamp(time.time()))

