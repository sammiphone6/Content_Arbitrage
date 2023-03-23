
## Main script

print("Starting Script...")
initial_wait = 6
time.sleep(initial_wait)

## Once you're in to the instagram you can easily change the pwd and email to be ANYTHING super easily.

instas = [
    ('deborahedwardsf07u2qm', 'dWlQECLf3H9'),
    ('betty_johnsonr1xg15red', '5xQ2FasejH'),
    ('sharonwanderson8eguoxr', 'lF5QzUGN'),
]
new_instas = [
    ('ksjbgcretg1', 'Test 1', 'first one dun good', True),
    ('ksjbgbretg2', 'Test 2', 'ok going stong', True),
    ('ksjbgbretg3', 'Test 3', 'pulled a turkey', True),
]
fbs = [
    ('shybag399@heisei.be', 'xpranto@25'),
    ('ofrow481@digdig.org', 'xpranto@25'),
    ('robdimtw@prin.be', '@xpranto@25#'),
]
for i in range(len(new_instas)): #change back to just numtiktoks
    old_insta, new_info, fb = instas[i], new_instas[i], fbs[i]
    insta = (new_info[0], old_insta[1])
    if i > 0:
        update_instagram_settings(old_insta, new_info)
    print('i: ', i, '\tfb: ', fb, '\tinsta: ', insta, '\t', add_fb_page_and_link_instagram(fb, insta))
    print(time.time()-start)



# fb = ('hasoarpit@kmail.li', '#xpranto@2t#')
# old_insta = ('carolrobinson7388659', 'YzunPMY2QR5')
# new_info = ('wrtovroniwfeee', 'Temp Instadedg', 'biggest tempozzy', True)

# insta = (new_info[0], old_insta[1])
# update_instagram_settings(old_insta, new_info)



# current = ('ouerhwweroff', '4BrJflhQY')
# update_account_info(info)



end = time.time()
print("All ", len(creds), " facebook accounts complete!\n")
print("It took ", (int)(end-start), " seconds to run (", (int)((end-start)/len(creds)), " seconds per account on average).")

# ('kev.within', 'Kevin', 'The best clips of Kevin (not impersonating).', True)
## If there's a problem connecting the insta account to fb page, just try a diff insta account.



# import pyautogui as auto
# import webbrowser
# import time


# site = "https://www.youtube.com/"
# webbrowser.open_new_tab(site)
# time.sleep(5)
# x, y = auto.locateCenterOnScreen('test.png')
# print(x)
# print(y)
# try:
#     auto.click(x,y)
#     print('clicked')
# except:
#     print("Not Found")

# win = pygetwindow.getWindowsWithTitle('windownname')[0]
# win.size = (1600, 900)