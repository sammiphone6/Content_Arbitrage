from account_posting.ig_post_functions import post_round_indiv, post_round_popular, run_tests, posts_sync, update_and_post_indiv, postReel, post_sam_frank
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


post_sam_frank(p = 0.35)
# posts_sync(['alixearle', 'sabquesada', 'onlyjayus', 'dayynaa', 'haleyybaylee', 'isaakpresley', 'faithordway7', 'fcbayern'])
# posts_sync(['onlyjayus', 'dayynaa', 'haleyybaylee', 'isaakpresley', 'faithordway7', 'fcbayern'])
# debug_all_access_tokens()

# run_tests(deep_test=False)
get_insights(sort = 'impressions')
# post_all(post_types, hashtags = False)
# plot_barchart(show=True) #per day
# plot_barchart(days=30, log_scale=True, cumulative=True) #per acct

###### EDIT ABOVE ######


print("DONE RUNNING")
end = time.time()
print(end - start)
print ("Finished at ", datetime.datetime.fromtimestamp(time.time()))

# spcyysamm = [
#     'https://www.tiktok.com/@spcyysamm/video/7224914904942251310',
#     'https://www.tiktok.com/@spcyysamm/video/7224571889782443310',
#     'https://www.tiktok.com/@spcyysamm/video/7224236393202027818',
#     'https://www.tiktok.com/@spcyysamm/video/7222735840106007850',
#     'https://www.tiktok.com/@spcyysamm/video/7222377541586160942',
#     'https://www.tiktok.com/@spcyysamm/video/7222735840106007850',
#     'https://www.tiktok.com/@spcyysamm/video/7222377541586160942',
#     'https://www.tiktok.com/@spcyysamm/video/7222377010629217582',
#     'https://www.tiktok.com/@spcyysamm/video/7222366674740137259',
#     'https://www.tiktok.com/@spcyysamm/video/7221549642931293486',
#     'https://www.tiktok.com/@spcyysamm/video/7221519962978962730',
#     'https://www.tiktok.com/@spcyysamm/video/7220575554221706542',
#     'https://www.tiktok.com/@spcyysamm/video/7220509951049993514',
#     'https://www.tiktok.com/@spcyysamm/video/7219746718332554542',
#     'https://www.tiktok.com/@spcyysamm/video/7219334206755720491',
#     'https://www.tiktok.com/@spcyysamm/video/7219017261900746026',
#     'https://www.tiktok.com/@spcyysamm/video/7218246032218524970',
#     'https://www.tiktok.com/@spcyysamm/video/7217911569378856238',
#     'https://www.tiktok.com/@spcyysamm/video/7217531885369576747',
#     'https://www.tiktok.com/@spcyysamm/video/7215994429943860523',
#     'https://www.tiktok.com/@spcyysamm/video/7215242994713251118',
#     'https://www.tiktok.com/@spcyysamm/video/7215242397444328747',
#     'https://www.tiktok.com/@spcyysamm/video/7215240420387786027',
#     'https://www.tiktok.com/@spcyysamm/video/7214114027331423534',
#     'https://www.tiktok.com/@spcyysamm/video/7213766716625554731',
#     'https://www.tiktok.com/@spcyysamm/video/7213766265121344811',
#     'https://www.tiktok.com/@spcyysamm/video/7212751681162087726',
#     'https://www.tiktok.com/@spcyysamm/video/7212706289158278442',
#     'https://www.tiktok.com/@spcyysamm/video/7212705951411948843',
#     'https://www.tiktok.com/@spcyysamm/video/7212705793970375979',
#     'https://www.tiktok.com/@spcyysamm/video/7212321202243800366',
#     'https://www.tiktok.com/@spcyysamm/video/7212321143007579438',
#     'https://www.tiktok.com/@spcyysamm/video/7208974843100843306',
#     'https://www.tiktok.com/@spcyysamm/video/7208974571394059566',
#     'https://www.tiktok.com/@spcyysamm/video/7208974464631999786',
#     'https://www.tiktok.com/@spcyysamm/video/7208267098190236974',
#     'https://www.tiktok.com/@spcyysamm/video/7208266999326149930',
#     'https://www.tiktok.com/@spcyysamm/video/7208216127145545003',
#     'https://www.tiktok.com/@spcyysamm/video/7207940104021675307',
#     'https://www.tiktok.com/@spcyysamm/video/7207932922588957994',
#     'https://www.tiktok.com/@spcyysamm/video/7207932688311897390',
#     'https://www.tiktok.com/@spcyysamm/video/7204516651788766507',
#     'https://www.tiktok.com/@spcyysamm/video/7204516334061866286',
#     'https://www.tiktok.com/@spcyysamm/video/7203825321118829867',
#     'https://www.tiktok.com/@spcyysamm/video/7203825321118829867',
#     'https://www.tiktok.com/@spcyysamm/video/7202337677956402475',
#     'https://www.tiktok.com/@spcyysamm/video/7202336574430907691',
# ]

# spcysam = [
#     'https://www.tiktok.com/@spcysam/video/7146710235565067522',
#     'https://www.tiktok.com/@spcysam/video/7143012019871042818',
#     'https://www.tiktok.com/@spcysam/video/7142969730721271042',
#     'https://www.tiktok.com/@spcysam/video/7142601104956591362',
#     'https://www.tiktok.com/@spcysam/video/7141798371764817153',
#     'https://www.tiktok.com/@spcysam/video/7141482085465820417',
#     'https://www.tiktok.com/@spcysam/video/7140781375057136897',
#     'https://www.tiktok.com/@spcysam/video/7140417077524925697',
#     'https://www.tiktok.com/@spcysam/video/7140335963057704193',
#     'https://www.tiktok.com/@spcysam/video/7139638219905207554',
#     'https://www.tiktok.com/@spcysam/video/7138944603750698241',
#     'https://www.tiktok.com/@spcysam/video/7138913511425494274',
#     'https://www.tiktok.com/@spcysam/video/7138190271648484610',
#     'https://www.tiktok.com/@spcysam/video/7136133253810982146',
#     'https://www.tiktok.com/@spcysam/video/7134780864541510914',
#     'https://www.tiktok.com/@spcysam/video/7134499701663010049',
#     'https://www.tiktok.com/@spcysam/video/7134130362384403713',
#     'https://www.tiktok.com/@spcysam/video/7133644675075935489',
#     'https://www.tiktok.com/@spcysam/video/7133635791456128257',
# ]

# simp_for_samfrank = [
#     'https://www.tiktok.com/@simp_for_samfrank/video/7223701513200323883',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7216857137404808494',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7216293937143811374',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7213605477735796014',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7211122374337367338',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7210747622510939435',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7209339883599564075',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7206689234160209195',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7204827121376726318',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7203829287059770666',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7200140809553874219',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7198245652999064878',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7195527048339770666',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7194822793954102574',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7190359161518181678',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7188982804271631659',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7185087359237557546',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7179390122876521771',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7179339709796191531',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7171542549692173610',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7171409630751591726',
# ]

# print(len(spcyysamm) + len(spcysam) + len(simp_for_samfrank))