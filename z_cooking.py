import time
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Key
from pynput.mouse import Button
import pyautogui
import os
from tt_update_data import open_filedata, save_filedata
from misc_functions import announce_pause, get_account_data
from ig_post_functions import post_reel
from exclude import exclude

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

    for i in range (89, num_tiktoks): #change back to just numtiktoks
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

    caption = ""
    try:
        caption = html_text.split('&quot;')[1]
    except:
        pass
    

    return (link, caption)

def clean_duplicates(arr):
    res = []
    [res.append(x) for x in arr if x not in res]
    return res

def update_data(name, directory):
    tiktok_data_popular = open_filedata("tiktok_data_popular.txt")
    
    arr = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if(f[-5:] != ".html"):
            os.remove(f)
        else:
            print(f)
            link, caption = get_filedata(f)
            arr.append((link, caption))
            # print(link[-19:], '\t', caption, '\n')
    # print(tiktok_data_popular)
    # print(len(arr))

    if(name in tiktok_data_popular):
        tiktok_data_popular[name]['videos'] = clean_duplicates(tiktok_data_popular[name]['videos'] + arr)
    else:
        tiktok_data_popular[name] = {'last_posted': -1, 'videos': clean_duplicates(arr)}
        
    save_filedata("tiktok_data_popular.txt", tiktok_data_popular)


tiktok_data_popular = open_filedata("tiktok_data_popular.txt")
account_data = get_account_data()

def go_post():
    tiktok_data_popular = open_filedata("tiktok_data_popular.txt")
    account_data = get_account_data()

    for name in tiktok_data_popular:#tiktok_data_popular:
        if(name not in exclude):
            if(tiktok_data_popular[name]['last_posted'] < len(tiktok_data_popular[name]['videos']) - 1):
                announce_pause(5)
                tt_link, tt_caption = tiktok_data_popular[name]['videos'][tiktok_data_popular[name]['last_posted']+1]
                tt_caption += f" #{account_data['Hashtag'][name]}" #ADD THEIR NAME TO THIS HANDLE
                
                post_reel(name, tt_link, tt_caption)
                tiktok_data_popular[name]['last_posted'] += 1
                save_filedata("tiktok_data_popular.txt", tiktok_data_popular)
            print(f"POST ROUND COMPLETED.")

# save_tiktok_links(300)

# update_data('basketball', 'basketball')

# tiktok_data_popular = open_filedata("tiktok_data_popular.txt")
# print(len(tiktok_data_popular['basketball']['videos']))
go_post()
go_post()
go_post()
go_post()


