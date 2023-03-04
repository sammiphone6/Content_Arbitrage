import time
from pynput import keyboard
from pynput.keyboard import Key
import pyautogui
import math
from tt_update_data import update_data

def download_tiktok_htmls_via_pynput(batch_size, num_accounts):
    start = time.time()

    def close_tab():
        my_keyboard.press(Key.cmd)
        my_keyboard.press("w")
        my_keyboard.release("w")
        my_keyboard.release(Key.cmd)

    def save_html():
        my_keyboard.press(Key.cmd)
        my_keyboard.press("s")
        my_keyboard.release("s")
        my_keyboard.release(Key.cmd)
        time.sleep(small_buffer)
        my_keyboard.press(Key.enter)
        my_keyboard.release(Key.enter)

    def save_and_close(j):
        save_html()
        time.sleep(wait_time)
        close_tab()
        time.sleep(wait_time)


    ## ------------------------
    ## Variables
    batch_size = batch_size
    total_accounts = num_accounts #should be a multiple of batch size

    initial_wait = 6
    small_buffer = 1.5
    wait_time = 2.2
    load_time = 8 + batch_size
    ## Variables
    ## ------------------------

    print("Starting Script...")
    time.sleep(initial_wait)
    my_keyboard = keyboard.Controller()

    full_cycles = total_accounts // batch_size
    partial_cycle = total_accounts % batch_size
    extra_cycle = 0 if partial_cycle==0 else 1
    for i in range (full_cycles+extra_cycle):
        
        ## Accounting for partial cycle offset
        if(i==full_cycles):
            batch_size = partial_cycle

        ## Select batch size
        time.sleep(small_buffer)
        with pyautogui.hold('shift'):
            for _ in range(batch_size-1):
                pyautogui.press(['down'])

        ## Enter site
        time.sleep(wait_time)
        with pyautogui.hold('option'):
            pyautogui.press(['enter'])

        time.sleep(load_time)
        ## Copy and record
        for j in range(batch_size):
            save_and_close(j)

        for _ in range(batch_size):
            pyautogui.press(['down'])

        time.sleep(wait_time)
        if (i != full_cycles):
            print((i+1)*batch_size, " of ", total_accounts, " accounts complete")

    end = time.time()
    print("All ", total_accounts, " complete!\n")
    print("It took ", (int)(end-start), " seconds to run (", (int)((end-start)/total_accounts), " seconds per account on average).")

def download_tiktoks_and_update_database(batch_size, num_accounts):
    download_tiktok_htmls_via_pynput(batch_size, num_accounts)
    update_data()
