from account_posting.ig_post_functions import post_round_indiv, post_round_popular, run_tests, posts_sync, update_and_post_indiv, postReel
from account_posting.insights_sync import get_insights, plot_barchart
from account_posting.misc_functions import announce_pause
from account_posting.access_token import debug_all_access_tokens, update_all_access_tokens, update_access_token, never_expiring_token, debug_access_token
from account_posting.data import account_data_indiv, account_data_popular, exclude, email_exclude, tiktok_data_indiv, tiktok_data_popular, fb_app_data, save_files
import datetime
import time
import requests
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
    # 'indiv',
    # 'popular',
]

# update_and_post_indiv('sabquesada')
link = 'https://v19.tiktokcdn-us.com/5edeecef13f4cb4fe5c6c84d39c4d828/643f707d/video/tos/useast5/tos-useast5-pve-0068-tx/oYDbvekXAWFRYnIEoAeDAL3N5lDEPkxSggB9QF/?a=1233&ch=0&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=3426&bt=1713&cs=0&ds=6&ft=kJrRfy7oZiI0PD1qqmTXg9wNpeeCJEeC~&mime_type=video_mp4&qs=0&rc=Nzg7O2U5NGY8ZGg0OzM0ZkBpMzV0cjc6ZjNpajMzZzczNEBgYGMtMzEuNjExYGMtMl9gYSMtMmgvcjQwZnNgLS1kMS9zcw%3D%3D&l=2023041822391688C51D7A393C921BD1C4'

# {'kevwithin', 'antoniolievano', 'sabquesada', 'partyshirt', 'mjgrimsley1001', 'paulinat', 'fcbarcelona', 'brookemonk_', 'breckiehill', 'officialautumnrose', 'elliezeiler', 'alixearle', 'shangerdanger', 'd_shaba', 'jamescharles', 'paulfoisy', 'itzshauni', 'meredithduxbury', 'onlyjayus', 'calebcoffee', 'rhia.official', 'dayynaa', 'newt'}
# postReel('breckiehill', link, caption='yaaass vanna, check out her OF 🥵 http://gg.gg/13q906', increment = False)


# posts_sync(list({'mjgrimsley1001', 'alixearle', 'antoniolievano', 'officialautumnrose'}))

for p in range(8):
    print(p+1, requests.get('https://ipinfo.io', proxies = proxies(p+1)).json()['ip'])
# update_and_post_indiv('haleyybaylee')

# run_tests(deep_test=False)
# get_insights(sort = 'impressions')
# post_all(post_types, hashtags = False)
# plot_barchart() #per day
# plot_barchart(days=30, log_scale=True, cumulative=True) #per acct

###### EDIT ABOVE ######


print("DONE RUNNING")
end = time.time()
print(end - start)
print ("Finished at ", datetime.datetime.fromtimestamp(time.time()))

