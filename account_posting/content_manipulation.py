import requests
from bs4 import BeautifulSoup
import os
import random

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

# print(tiktok_to_download_url2('https://www.tiktok.com/@leogreatindianasmr/video/7198871579336576302'))

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
    
def tiktok_to_webhosted_link(tiktok_link):
    download_link = tiktok_to_download_url(tiktok_link)
    if len(str(download_link)) < 5:
        print(tiktok_link, ' gave download link: ', download_link)
        return 0
    rand = str(int(100000*random.random()))

    directory = 'temp_vids'
    download_file_name = os.path.join(directory, f"temporary{tiktok_link[-6:-1]}--{rand}.mp4")

    download_file(download_link, download_file_name)
    webhosted_link = host_file_online(download_file_name)
    os.remove(download_file_name)

    return webhosted_link
