import requests
from bs4 import BeautifulSoup
import os

def tiktok_to_download_url(tiktok_link):
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
        'time': (None, '12h'),
        'fileToUpload': open(downloaded_file_name, 'rb'),
    }
    response = requests.post('https://litterbox.catbox.moe/resources/internals/api.php', files=files)
    return response.text

def tiktok_to_webhosted_link(tiktok_link):
    download_link = tiktok_to_download_url(tiktok_link)
    if len(str(download_link)) < 3:
        return 0
    download_file_name = "temporary.mp4"

    download_file(download_link, download_file_name)
    webhosted_link = host_file_online(download_file_name)
    os.remove(download_file_name)

    return webhosted_link
