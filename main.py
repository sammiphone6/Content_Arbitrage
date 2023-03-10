from ig_post_functions import post_round_indiv
from misc_functions import announce_pause
import time
import datetime


start = time.time()

num_posts = -1
for _ in range(1):
    num_posts = post_round_indiv()

print("DONE RUNNING")
end = time.time()
print(end - start)
print ("Finished at ", datetime.datetime.fromtimestamp(time.time()))

