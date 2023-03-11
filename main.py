from ig_post_functions import post_round_indiv, post_round_popular
from misc_functions import announce_pause
import time
import datetime

## Just comment out whichever one you don't want
post_types = [
    'indiv',
    'popular',
]


start = time.time()
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

