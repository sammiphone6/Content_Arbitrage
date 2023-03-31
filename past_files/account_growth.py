from data.data import fbs, instas, new_instas, ready_accounts, counters, save
from fsm_logic import update_instagram_settings, add_fb_page_and_link_instagram, change_vpn
import time


## Steps to check before running:
## Make sure temp_PFPs folder is default
## Make sure temp_PFPs is empty and all needed pfps for running are in PFPs folder


## Main script
print("Starting Script...")
# print(counters)
# for key in counters:
#     counters[key] = 0
# save()
# print(counters)
counters['instas']=1
start = time.time()
initial_wait = 6
time.sleep(initial_wait)

## Once you're in to the instagram you can easily change the pwd and email to be ANYTHING super easily.
def announce_pause(sec):
    print("currently pausing for ", sec, " now is time to change vpn")
    time.sleep(sec/2)
    print("halfway done")
    time.sleep(sec/2)
    print("done pausing")

def process(old_insta, new_info, fb):
    insta = (new_info[0], old_insta[1])
    change_vpn()

    insta_result = update_instagram_settings(old_insta, new_info)
    if insta_result in ['ACCOUNT SUSPENDED', 'FIRST INSTAGRAM LOGIN FAILED', 'INCORRECT PASSWORD']:
        print(insta_result, ': ', old_insta)
        return insta_result
    
    fb_result = add_fb_page_and_link_instagram(fb, insta)
    print('fb_result: ', fb_result, fb)
    return fb_result


while ((counters['fbs'] < len(fbs)) and (counters['instas'] < len(instas)) and (counters['new_instas'] < len(new_instas))):
    ## Instantiation
    while(int(fbs[counters['fbs']][2]) > int(time.time()-60*60*24*5)):
        counters['fbs'] += 1
    old_insta, new_info, fb = instas[counters['instas']], new_instas[counters['new_instas']], fbs[counters['fbs']]
    

    result = process(old_insta = old_insta, new_info = new_info, fb = fb[:2])
    if result in ['ACCOUNT SUSPENDED', 'FIRST INSTAGRAM LOGIN FAILED', 'INCORRECT PASSWORD']:
        counters['instas'] += 1
    else:
        counters['new_instas'] += 1
        fbs[counters['fbs']][2] = str(int(time.time()))
        result, page_name = result
        if result not in ['ACCOUNT CONNECTION FAILED', 'ACCOUNT CONNECTED']:
            counters['fbs'] += 1
        elif result in ['ACCOUNT CONNECTION FAILED']:
            counters['instas'] += 1
            counters['fbs'] += 1
        elif result in ['ACCOUNT CONNECTED']:
            ready_accounts += [(
                new_info[0],  #username
                old_insta[1], #pwd
                new_info[1],  #name
                new_info[2],  #bio
                fb[0],        #facebook email
                page_name,    #pagename
            )]
            counters['instas'] += 1
            counters['fbs'] += 1
    save()
    print('counters: ', counters, '\nready_accounts: ', ready_accounts)

    announce_pause(30)

    print(time.time()-start)










end = time.time()
print("Done")
# print("All ", len(creds), " facebook accounts complete!\n")
# print("It took ", (int)(end-start), " seconds to run (", (int)((end-start)/len(creds)), " seconds per account on average).")

# ('kev.within', 'Kevin', 'The best clips of Kevin (not impersonating).', True)
## If there's a problem connecting the insta account to fb page, just try a diff insta account.


    # print('fb: ', fbs[counters['fbs']], '\told_insta: ', instas[counters['instas']], '\new_info: ', new_instas[counters['new_instas']], 
    #       '\ninsta_result: ', insta, '\nfb: ', fb_result, '\tfb: ',)