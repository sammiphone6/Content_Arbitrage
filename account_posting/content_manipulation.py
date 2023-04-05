import requests
from bs4 import BeautifulSoup
import os
import random
import time

def tiktok_to_download_url1(tiktok_link): #tiktokdownload.online
    cookies = {
        '__cflb': '0H28vWmzwPGiuttmmTwiKXSWqswTA1RDekXSXY9zBTH',
        '_ga': 'GA1.2.1655815031.1677121198',
        '_gid': 'GA1.2.326448368.1677121198',
        '_gat_UA-3524196-9': '1',
    }

    headers = {
        'authority': 'tiktokdownload.online',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cflb=0H28vWmzwPGiuttmmTwiKXSWqswTA1RDekXSXY9zBTH; _ga=GA1.2.1655815031.1677121198; _gid=GA1.2.326448368.1677121198; _gat_UA-3524196-9=1',
        'hx-current-url': 'https://tiktokdownload.online/',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://tiktokdownload.online',
        'referer': 'https://tiktokdownload.online/',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': tiktok_link,
        'locale': 'en',
        'tt': 'Y2s3dTQ2',
    }

    response = requests.post('https://tiktokdownload.online/abc', params=params, cookies=cookies, headers=headers, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a', href=True):
        return link['href']

def tiktok_to_download_url2(tiktok_link): #savetik.co
    cookies = {
        '.AspNetCore.Antiforgery.vmpBg8YRfdE': 'CfDJ8F3EzyHODftOuDVASknfNW82Icr5reXHjD2FRVwA-OvMwNEWKdsem7A8Xi8id6m_dXOOWtf0WfaSsZSagF1BVkIY6rau7AMgGf14ad7WyIcfoZTbdVJBB5IW9xMvWcvLqJfN8kPaUf3qRHvbMQp_uQE',
        '_ga': 'GA1.2.1572329233.1680115619',
        '_gid': 'GA1.2.466044715.1680115619',
        '_gat_gtag_UA_88358110_1': '1',
        '__atuvc': '1%7C13',
        '__atuvs': '642487a1a9993922000',
        '__atssc': 'google%3B1',
    }

    headers = {
        'authority': 'savetik.co',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '.AspNetCore.Antiforgery.vmpBg8YRfdE=CfDJ8F3EzyHODftOuDVASknfNW82Icr5reXHjD2FRVwA-OvMwNEWKdsem7A8Xi8id6m_dXOOWtf0WfaSsZSagF1BVkIY6rau7AMgGf14ad7WyIcfoZTbdVJBB5IW9xMvWcvLqJfN8kPaUf3qRHvbMQp_uQE; _ga=GA1.2.1572329233.1680115619; _gid=GA1.2.466044715.1680115619; _gat_gtag_UA_88358110_1=1; __atuvc=1%7C13; __atuvs=642487a1a9993922000; __atssc=google%3B1',
        'origin': 'https://savetik.co',
        'referer': 'https://savetik.co/en',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '__RequestVerificationToken': 'CfDJ8F3EzyHODftOuDVASknfNW-Mik1IMiFlzs7D3IrGn0pjjZi1WGDD-7gIaTXoukOMnQH8ONwINZes0-rySWzrMvC0qWQ7iExRTmrfUGFItR6yHJCpTFMZ0J58gPWjGju_jI0JJNsGQ99AiDK9JQB8ixU',
        'q': tiktok_link,
    }
    response = requests.post('https://savetik.co/api/ajaxSearch', cookies=cookies, headers=headers, data=data)
    text = response.text
    if 'Error: The Video ID could not be obtained.' in text: return 0

    download_link = [token for token in text.split(r'\u0022') if 'https://download.tik-cdn.com/dl/' in token][1]
    return download_link

def tiktok_to_download_url(tiktok_link):
    return tiktok_to_download_url2(tiktok_link)

def tiktok_to_video_data(tiktok_link): #savetik.co
    cookies = {
        '.AspNetCore.Antiforgery.vmpBg8YRfdE': 'CfDJ8F3EzyHODftOuDVASknfNW82Icr5reXHjD2FRVwA-OvMwNEWKdsem7A8Xi8id6m_dXOOWtf0WfaSsZSagF1BVkIY6rau7AMgGf14ad7WyIcfoZTbdVJBB5IW9xMvWcvLqJfN8kPaUf3qRHvbMQp_uQE',
        '_ga': 'GA1.2.1572329233.1680115619',
        '_gid': 'GA1.2.466044715.1680115619',
        '_gat_gtag_UA_88358110_1': '1',
        '__atuvc': '1%7C13',
        '__atuvs': '642487a1a9993922000',
        '__atssc': 'google%3B1',
    }

    headers = {
        'authority': 'savetik.co',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '.AspNetCore.Antiforgery.vmpBg8YRfdE=CfDJ8F3EzyHODftOuDVASknfNW82Icr5reXHjD2FRVwA-OvMwNEWKdsem7A8Xi8id6m_dXOOWtf0WfaSsZSagF1BVkIY6rau7AMgGf14ad7WyIcfoZTbdVJBB5IW9xMvWcvLqJfN8kPaUf3qRHvbMQp_uQE; _ga=GA1.2.1572329233.1680115619; _gid=GA1.2.466044715.1680115619; _gat_gtag_UA_88358110_1=1; __atuvc=1%7C13; __atuvs=642487a1a9993922000; __atssc=google%3B1',
        'origin': 'https://savetik.co',
        'referer': 'https://savetik.co/en',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '__RequestVerificationToken': 'CfDJ8F3EzyHODftOuDVASknfNW-Mik1IMiFlzs7D3IrGn0pjjZi1WGDD-7gIaTXoukOMnQH8ONwINZes0-rySWzrMvC0qWQ7iExRTmrfUGFItR6yHJCpTFMZ0J58gPWjGju_jI0JJNsGQ99AiDK9JQB8ixU',
        'q': tiktok_link,
    }
    response = requests.post('https://savetik.co/api/ajaxSearch', cookies=cookies, headers=headers, data=data)
    text = response.text
    if 'Error: The Video ID could not be obtained.' in text: return 0
    try:
        video_data = [token for token in text.split(r'\u0022') if 'https://v16m-default.akamaized.net' in token][1]
        return video_data
    except:
        return 0

def download_file(download_link, downloaded_file_name):
    chunk_size = 256
    url = download_link

    r = requests.get(url, stream = True)

    with open(downloaded_file_name, "wb") as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)

def host_file_online(downloaded_file_name):
    files= {
        'reqtype': (None, 'fileupload'),
        'time': (None, '1h'),
        'fileToUpload': open(downloaded_file_name, 'rb'),
    }
    response = requests.post('https://litterbox.catbox.moe/resources/internals/api.php', files=files)
    return response.text
    
def tiktok_to_webhosted_link_old(tiktok_link):
    print(1)
    download_link = tiktok_to_download_url(tiktok_link)
    print(2)
    if len(str(download_link)) < 5:
        print(tiktok_link, ' gave download link: ', download_link)
        return 0
    rand = str(int(100000*random.random()))
    print(3)

    directory = 'temp_vids'
    download_file_name = os.path.join(directory, f"temporary{tiktok_link[-6:-1]}--{rand}.mp4")
    print(4)
    download_file(download_link, download_file_name)
    print(5)
    webhosted_link = host_file_online(download_file_name)
    print(6)
    os.remove(download_file_name)

    return webhosted_link

def speed_up(web_hosted_tt_link, speed): # 0.5 < speed < 2
    debug = False

    response1 = requests.get('https://ezgif.com/video-speed?url='+web_hosted_tt_link)
    text1 = response1.text
    if debug: print(text1)

    link1 = text1.split('.mp4')[0].split("\"")[-1]+'.mp4'
    if debug: print('link1', link1)
    headers = {
        'authority': 'ezgif.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://ezgif.com',
        'referer': 'https://ezgif.com/video-speed/ezgif-1-47fe12ce2a.mp4',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'ajax': 'true',
    }

    data = {
        'file': link1.split('/')[-1],
        'multiplier': speed,
        'apply_audio': 'on',
    }
    response2 = requests.post(f'https://ezgif.com/video-speed/{link1}', params=params, headers=headers, data=data)
    text2 = response2.text

    link2 = "https://im" + text2.split('.mp4')[0].split("src=\"//im")[-1]+'.mp4'
    if debug: print('link2', link2)
    return link2

def tiktok_to_webhosted_link(tiktok_link, speed = None):
    video_data = tiktok_to_video_data(tiktok_link)
    if speed == None:
        return video_data
    else:
        return speed_up(video_data, float(speed))
        

# this link is missing though
# tt_link = "https://v19.tiktokcdn-us.com/739320ac7d3f2046c90592277527dbc1/642a4a46/video/tos/useast5/tos-useast5-ve-0068c003-tx/2a448767afc042d584af3bd35e017ff3/?a=1233&ch=0&cr=0&dr=0&cd=0%7C0%7C0%7C0&cv=1&br=3590&bt=1795&cs=0&ds=6&ft=kJrRfy7oZ-10PD1Kf05Xg9wdbNJ5vEeC~&mime_type=video_mp4&qs=0&rc=NjxoOGRpZDs7O2g2ZWc3NUBpajNtczM6ZnNvaTMzZzczNEBjMC4uXmItNS8xMV8uY15gYSNrazJhcjQwLmNgLS1kMS9zcw%3D%3D&l=2023040221384107E48AB50AF470FE7DDE"
# speed = 1.16

# links = [
#     'https://www.tiktok.com/@burnt_pellet_bbq/video/7046058551474687237',
#     # 'https://www.tiktok.com/@tyrecordslol/video/7203020961937984814',
#     # 'https://www.tiktok.com/@holliskitten/video/7176299886608911658',
#     # 'https://www.tiktok.com/@dunk_fmvp/video/7172582923382672683',
#     # 'https://www.tiktok.com/@kirill_mist/video/7131948387317959982',
#     # 'https://www.tiktok.com/@sophiebouts/video/7118489020610530565',
# ]
# start = time.time()
# for link in links:
#     print("\nLINK STARTING: ", link)

#     video_data = tiktok_to_video_data(link)
#     print('download url', video_data)
#     speed_url = speed_up(video_data, speed)
#     print('url', speed_url)
#     print(time.time()-start)
