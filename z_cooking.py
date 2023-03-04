import time
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button
import pyautogui
import os
from tt_update_data import open_filedata, save_filedata
from misc_functions import announce_pause

def save_tiktok_links(num_tiktoks):
    start = time.time()

    def next_tab():
        with pyautogui.hold('ctrl'):
            pyautogui.press(['tab'])

    def paste():
        my_keyboard.press(Key.cmd)
        my_keyboard.press("v")
        my_keyboard.release("v")
        my_keyboard.release(Key.cmd)

    def save(i):
        my_keyboard.press(Key.cmd)
        my_keyboard.press("s")
        my_keyboard.release("s")
        my_keyboard.release(Key.cmd)
        time.sleep(wait_time)        
        my_keyboard.type(str(i))
        time.sleep(wait_time)
        my_keyboard.press(Key.enter)


    def down():
        pyautogui.press(['down'])

    def up():
        pyautogui.press(['up'])

    def click():
        my_mouse.click(Button.left)

    def process(i):
        save(i)
        time.sleep(wait_time)
        up()
        time.sleep(wait_time)

    ## ------------------------
    ## Variables

    initial_wait = 6
    wait_time = 1.2
    ## Variables
    ## ------------------------

    print("Starting Script...")
    time.sleep(initial_wait)
    my_keyboard = keyboard.Controller()
    my_mouse = mouse.Controller()

    for i in range (num_tiktoks):
        process(i)

    end = time.time()
    print("All ", num_tiktoks, " complete!\n")
    print("It took ", (int)(end-start), " seconds to run (", (int)((end-start)/num_tiktoks), " seconds per account on average).")



def get_filedata(filename):
    with open(filename) as file:
        html_text = file.read()

    search_text = "/video/"
    start_index = html_text.index(search_text)
    remaining_text = html_text[start_index+len(search_text):]

    end_index = min(remaining_text.index("\""), remaining_text.index("?"))
    remaining_text = remaining_text[:end_index]

    ids = remaining_text.split("\",\"")

    starting_text = html_text[:start_index]
    starting_text = starting_text[::-1][:starting_text[::-1].index('ptth')+4][::-1]

    link = starting_text + '/video/' + remaining_text

    caption = html_text.split('&quot;')[1]

    return (link, caption)


def update_data():
    directory = 'cooking'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if(f[-5:] != ".html"):
            os.remove(f)
        else:
            link, caption = get_filedata(f)
            arr.append((link, caption))
            print(link[-19:], '\t', caption, '\n')
    return arr


# save_tiktok_links(50)
arr = []
update_data()
print(arr)
print(len(arr))


def do_round_of_posting():
    num_posts = 0
    num_accounts = 0
    for account in tiktok_data_indiv:
        if(account not in exclude and tiktok_data_indiv[account]["last_posted"] < len(tiktok_data_indiv[account]["video_ids"]) - 1):
            vid_id = tiktok_data_indiv[account]["video_ids"][tiktok_data_indiv[account]["last_posted"]+1]
            tt_link = f"https://tiktok.com/@{account}/video/{vid_id}/"
            tt_caption = tiktok_captions_indiv[vid_id] + f" #{account_data['Hashtag'][account]}" #ADD THEIR NAME TO THIS HANDLE
            
            post_reel(account, tt_link, tt_caption)
            tiktok_data_indiv[account]["last_posted"] += 1 
            save_filedata("tiktok_data_indiv.txt", tiktok_data_indiv)
            num_posts+=1
        num_accounts+=1
        announce_pause(4)
    print(f"POSTING ROUND COMPLETED: {num_posts} POSTS MADE ACROSS {num_accounts} ACCOUNTS.")
    return num_posts



# start = time.time()
# num_posts = -1
# # while(num_posts != 0):
# for _ in range(1):
#     num_posts = do_round_of_posting()
#     # announce_pause(15*60)
# print("DONE RUNNING")
# end = time.time()
# print(end - start)
