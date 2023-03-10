import os
import requests
from data import tiktok_data_indiv, tiktok_captions_indiv, tiktok_data_popular, save_filedata

def get_caption(filename, id):
    with open(filename) as file:
        html_text = file.read()

    search_text = id + "\",\"desc\":\""
    start_index = html_text.index(search_text)
    remaining_text = html_text[start_index+len(search_text):]

    caption = remaining_text.split("\"")[0]
    return caption

def get_filedata(filename):
    with open(filename) as file:
        html_text = file.read()

    search_text = "{\"user-post\":{\"list\":[\""
    start_index = html_text.index(search_text)
    remaining_text = html_text[start_index+len(search_text):]

    end_index = remaining_text.index("\"]")
    remaining_text = remaining_text[:end_index]

    ids = remaining_text.split("\",\"")

    link_username_index = html_text.index("/video/" + ids[0])
    trimmed_text = html_text[:link_username_index]
    reversed_text = trimmed_text[::-1]
    reversed_username = reversed_text.split('/')[0] #@ character still there
    username = reversed_username[::-1][1:] #reverse and remove @

    ## ADD GET_CAPTION FOR EACH ID SOMEWHERE HERE
    for id in ids:
        tiktok_captions_indiv[id] = get_caption(filename, id)

    return (username, ids[::-1])

def update_data():
    directory = 'tt_htmls'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if(f[-5:] != ".html"):
            os.remove(f)
        else:
            username, ids = get_filedata(f)
            os.remove(f) #CHANGE FOR EASY DEBUGGING

            if username not in tiktok_data_indiv:
                tiktok_data_indiv[username] = {'last_posted': -1, 'video_ids': ids}
            else:
                for id in ids:
                    if id not in tiktok_data_indiv[username]['video_ids']:
                        tiktok_data_indiv[username]['video_ids'].append(id)

    ## SAVE UPDATED DATA
    try:
        save_filedata('tiktok_data_indiv.txt', tiktok_data_indiv)
    except:
        print("Something went wrong saving tiktok_data_indiv")

    try:
        save_filedata('tiktok_captions_indiv.txt', tiktok_captions_indiv)
    except:
        print("Something went wrong saving tiktok_captions_indiv")

