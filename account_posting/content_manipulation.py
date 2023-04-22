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

### ONLY FUNCTIONS STILL USED (the rest are old and less efficient)

def tiktok_to_video_data(tiktok_link): #savetik.co

    cookies = {
        # '_ga': 'GA1.2.1572329233.1680115619',
        # '__atssc': 'google%3B2',
        # '__atuvc': '9%7C13',
        '.AspNetCore.Antiforgery.vmpBg8YRfdE': 'CfDJ8G6Ms0dcEMZLhHcqR2TDLfJ0CA6AZin432-7pxOfzio9v1EjaRvgDQO-RqW6KnwOy0KXIsqlV2GqKJUjnS5kOqcHWRzTzwziyMg0P6NpvtLtcqvVACZUBDWI0dJuttwIuPwqCkrPxMQ1DrW-XOrVxw8',
    }

    headers = {
        # 'authority': 'savetik.co',
        # 'accept': '*/*',
        # 'accept-language': 'en-US,en;q=0.9',
        # 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # # 'cookie': '_ga=GA1.2.1572329233.1680115619; __atssc=google%3B2; __atuvc=9%7C13; .AspNetCore.Antiforgery.vmpBg8YRfdE=CfDJ8G6Ms0dcEMZLhHcqR2TDLfJ0CA6AZin432-7pxOfzio9v1EjaRvgDQO-RqW6KnwOy0KXIsqlV2GqKJUjnS5kOqcHWRzTzwziyMg0P6NpvtLtcqvVACZUBDWI0dJuttwIuPwqCkrPxMQ1DrW-XOrVxw8',
        # 'origin': 'https://savetik.co',
        # 'referer': 'https://savetik.co/en?q=https%3A%2F%2Fwww.tiktok.com%2F@kirill_mist%2Fvideo%2F7131948387317959982',
        # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"macOS"',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-origin',
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        # 'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '__RequestVerificationToken': 'CfDJ8G6Ms0dcEMZLhHcqR2TDLfLv93kZ_lJ4fhwQ2egSJjeFhxpitveaVlOaE0Vt7t9NiUlot864Ewcnc-haelMuoldunSV5NLrEktyAJ3raXs9JYt-Elsb9NT7i15xKrV2fQ-OSm_4b73mg0wKMVo0ymR0',
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

def youtube_to_video_data(youtube_link):

    cookies = {
        # 'uid': '5e5c384de599e54e',
        # '_ga': 'GA1.2.1561705660.1682106662',
        # '_gid': 'GA1.2.554388407.1682106662',
        # 'push': '100',
        # 'outputStats': '38',
        # 'clickAds': '48',
        # '_ym_uid': '1682106662795802399',
        # '_ym_d': '1682106662',
        # '_ym_isad': '1',
        # '_ym_visorc': 'b',
        # 'laravel_session': 'eyJpdiI6IlRQeWd5bmdKSEQ1MzNrYTFkUXBIMkE9PSIsInZhbHVlIjoiZHNFWUdDZ1dkYVlNWjRGd3p2bGl4ZXpDSGRnNytGR1RhYmtQUEY3VDk2aHVXeUNxNmZaNVVzOHZlajFNREx1NU1XcUc0YzJkVXAveFdZbUZTS0VpcDU3TWdMU3lWQy85dnVPN1BVYXpjUVpEa1pTazl3TkgyUjEwU1o0cVVnUzYiLCJtYWMiOiIwODhlYzcwMGZmNWE2NWI5ODY0OTY2YjkwOGJmNmM0ZGRkODVjNjgyMGE3MWI1ODhiZDY5MjRiM2Q4ZTk1MDkxIiwidGFnIjoiIn0%3D',
    }

    headers = {
        'authority': 'ssyoutube.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        # 'cookie': 'uid=5e5c384de599e54e; _ga=GA1.2.1561705660.1682106662; _gid=GA1.2.554388407.1682106662; push=100; outputStats=38; clickAds=48; _ym_uid=1682106662795802399; _ym_d=1682106662; _ym_isad=1; _ym_visorc=b; laravel_session=eyJpdiI6IlRQeWd5bmdKSEQ1MzNrYTFkUXBIMkE9PSIsInZhbHVlIjoiZHNFWUdDZ1dkYVlNWjRGd3p2bGl4ZXpDSGRnNytGR1RhYmtQUEY3VDk2aHVXeUNxNmZaNVVzOHZlajFNREx1NU1XcUc0YzJkVXAveFdZbUZTS0VpcDU3TWdMU3lWQy85dnVPN1BVYXpjUVpEa1pTazl3TkgyUjEwU1o0cVVnUzYiLCJtYWMiOiIwODhlYzcwMGZmNWE2NWI5ODY0OTY2YjkwOGJmNmM0ZGRkODVjNjgyMGE3MWI1ODhiZDY5MjRiM2Q4ZTk1MDkxIiwidGFnIjoiIn0%3D',
        'origin': 'https://ssyoutube.com',
        # 'referer': 'https://ssyoutube.com/en74/youtube-video-downloader',
        # 'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"macOS"',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-origin',
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        # 'x-requested-with': 'XMLHttpRequest',
    }

    json_data = {
        'url': youtube_link,
    }

    response = requests.post('https://ssyoutube.com/api/convert', cookies=cookies, headers=headers, json=json_data)
    json = response.json()
    link = json['url'][1]['url'].split("&title=")[0]
    return link

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

def tiktok_to_webhosted_link(link, speed = None):
    if 'tiktok.com' in link: video_data = tiktok_to_video_data(link)
    if 'youtube.com' in link: video_data = youtube_to_video_data(link)
    if speed in [None, 0, '0'] or video_data == 0:
        return video_data
    else:
        return speed_up(video_data, float(speed))



