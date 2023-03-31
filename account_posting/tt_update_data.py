import os
import requests
from data import tiktok_data_indiv, tiktok_captions_indiv, tiktok_data_popular, save_files

def query(account):
    cookies = {
        '_ttp': '289J0zFF3tfkEFKeyLDCZKFwDMC',
        'tiktok_webapp_theme': 'light',
        'tt_csrf_token': 'r16ny1BX-ESae4IUXYwaSlnIqU3bSLqKJGvQ',
        'passport_csrf_token': '43ed0a56987b053feb953b798a8ab69a',
        'passport_csrf_token_default': '43ed0a56987b053feb953b798a8ab69a',
        's_v_web_id': 'verify_ldgr2ah9_xz7m8a1G_7Lit_4xlj_985M_JMIPWGVpbMZN',
        'd_ticket': '156ce90a06b2b94cae934a6bcdac0274024ea',
        'uid_tt': 'ca756457013b4db955360f56b19678518583b7e30c2753eecd5e9d6afc8d650b',
        'uid_tt_ss': 'ca756457013b4db955360f56b19678518583b7e30c2753eecd5e9d6afc8d650b',
        'sid_tt': 'a76d4ca06ba5c894586138c7d158fe98',
        'sessionid': 'a76d4ca06ba5c894586138c7d158fe98',
        'sessionid_ss': 'a76d4ca06ba5c894586138c7d158fe98',
        'store-idc': 'useast5',
        'store-country-code': 'us',
        'store-country-code-src': 'uid',
        'tt-target-idc': 'useast5',
        'tt-target-idc-sign': 'J2zC8abDjFPdDukSUlAP9z669_pAxKquT9QkKSvHByOXmSl7e-NPfVfyeZdnnQFQSMwCErEYDMuV032IZMH5Py0Fjv-xioY4iEXxB1L4tXc93xMceauR1FpTj3FIfD9LEKTpE3u8Yry-S9xaA4K0I2Ee-FamDwL-8gjMRArr8Sdb2GzlDdcysInt9DMG_W2fcDNA2vAIc6Ndt6wzVq9p6trVpW6BfYJpo4LQtm5es02KQVdLjvM99tlS41ojW84RQHERJyQMzJRTmMOyeU4VmvmWE49bZougUPmA2MVRcNEPW8BtdxQfCuhBpm5lAuGq5a4JpiMBnsKTuft0SaX1wqZLLKmyBzc98q7Y6ZbZHtDEnXfFUuchAjQCwiQ63RYN4F0Bm6CxrWE97T8Ew_J0pU6j8LnWOUc_7iXSedv-tYWyyhOtQvmvM0RAvDx0AYcGG0Uh9hul_sGapwedBqezMt4OG92aXp0i8DX1TvNat-WmXFSe2PsCaN1RwxmMy5Xa',
        'csrf_session_id': '0fd659681307d0f9d9cf261c8d0e0b99',
        'passport_fe_beating_status': 'true',
        'cmpl_token': 'AgQQAPNSF-RMpbPrI8_GZh0S-RWI0x5Yv6zZYMpuPA',
        '__tea_cache_tokens_1988': '{%22user_unique_id%22:%227166372563806291502%22%2C%22timestamp%22:1674958582630%2C%22_type_%22:%22default%22}',
        'sid_guard': 'a76d4ca06ba5c894586138c7d158fe98%7C1677026254%7C5184000%7CSun%2C+23-Apr-2023+00%3A37%3A34+GMT',
        'sid_ucp_v1': '1.0.0-KDJhMDkyYWQwZTkwYTNiYzQ0ZDE3NThhNjA4ZTgwZGE4YjI2OTdhY2IKIAiriNPyhK3z6mMQzsfVnwYYswsgDDDbm9eeBjgCQPEHEAQaB3VzZWFzdDUiIGE3NmQ0Y2EwNmJhNWM4OTQ1ODYxMzhjN2QxNThmZTk4',
        'ssid_ucp_v1': '1.0.0-KDJhMDkyYWQwZTkwYTNiYzQ0ZDE3NThhNjA4ZTgwZGE4YjI2OTdhY2IKIAiriNPyhK3z6mMQzsfVnwYYswsgDDDbm9eeBjgCQPEHEAQaB3VzZWFzdDUiIGE3NmQ0Y2EwNmJhNWM4OTQ1ODYxMzhjN2QxNThmZTk4',
        'tt_chain_token': '+7hqfC9Fp2bQ45CHIVx3EQ==',
        '_abck': 'E372DE3F8F68C9482D8CA6BD492A5E99~0~YAAQPzoZuK8xPIeGAQAAfxDctAkaVGi0/IEKojaWzsy9LHgAdw3fRcfgXTUPV4ElOUQeNdrG6oZGWDFd+cPtADJuqgcnHSBqBOQsnKdHkSjVofSvaF3pN+mHUgTVQmHIGsQA9tvjKQ1DwMBhWhDkwHmetny+763GMZZumYGZiyEL4CI94KwFR1tUipwW/6eFMPNd5V94KqUE0pFUMiLAXhnX4rEV6J0TzTQRSmTLetphe98kiWSLGSqHwapTwGPPt2NiVwf+MMwtwMUDegvAzP05jy4bdnVjS9nKiagmKaBNK1dVb+/NefNLsvtOZ6C+La3oIfIYH1zqGWJEoAUamxe8Wa/kodZrqQ7VQeXYjZg0V4sx9mJdCFy7ErLc+ujwcOjdrF3SJmHG9TCHP6a8t+UmJp/DvmAe~-1~-1~-1',
        'bm_sz': 'BB6842AFC43042B89B89BDA309226CEE~YAAQPzoZuLIxPIeGAQAAfxDctBOr5wEOVfrm4TjGGpHmBZAlbi2eGf6KJVEUXh3kGAwr8pQccC949pulMAh621OnQjUrBeXm5stBitbsEjuxAv92DadgKS6rV9brIryZT7RsOfyF1IyDnoPXXEyRcnIa+lSMU5NA+q0kHfEWyQ3EHA3KugLYHqOplTXYmXjQZXzPgtxUhA2il+YE22xK4ol1BvyukwAaynEAsEVDUPeLkCLhyCv+j8dZ/30gLvOouLtAUEZCvqRPPbieeD+gn9v9DYE11IaXjND3SqnCS5UD3i4=~4408373~4538934',
        'ak_bmsc': 'D3DDBB60951382FD6183425B22C99411~000000000000000000000000000000~YAAQPzoZuLUxPIeGAQAAmRnctBO5dl+d1ztr80Ib06boNDgz2ps24+viCgnaJ4Xs4Gf9oMj01wwNpwyHrhpGX2uJKw1S0ubofRKNBCDoPiXNImLoSR2FJh01TvLTjTuRrMx7UMiPVG4Q2LBHVKZ3ELQdxbXjIU7Kol1tU2MoPlm2IBzFVA/eYtN+1VaSUSQINoFaGhxxXceQF2BWZHwNpSOm5Aith70I/WuB3HEG2QtHnUdaOquZUn51UChyBnU2xiRiqzFbXTWkV9sMAVnHtRkjx6vzh29fsyfFEnmJXxO8WKaypwXEMu6EGnKfFNxEEI7VjDVB+LnNsWNuKuG+rXMH5iwwZIBaQ8dtYR3prYEHA2MfjZK8cmf41WPSRqEJdoFSK8PjZ1ABCXdv0O0Mr4el8LAxu86EYYOJiR7Xn8gDt/4NRP3JZsUwfdTqTWNZSnqC+FVMR5YzPxFZEoQquxHUEO4ZyYxqH08U9xsdWXFW/btqnumCRhw=',
        'msToken': 'WPpwKEkDI2qHKKKhxE2H2cdGDu2Pw-br0NzqxsjsXec0Ler_Uhsg4d6GHOzko-X35nU1cKIT388LMxj3vDaVo-7LAhiZJkZ1NyffppIv7E5nxaGIvzK2Y5QAQU4G1DBuFy22UssIV7jj7mrlmJsi',
        'bm_sv': 'F71DAFE3C25B9EB8CEC3F72A034558DF~YAAQPzoZuPsxPIeGAQAA0PfdtBOoWadiyraqRJmHT28S5hcPb9n1NDhN05cZNY1fhPpoSzxus0onORo2s1bciWyeh5K0UdjZ4YBjotYOcyaIQ7n+NSgamQC8RccXSpvxHOolINPr4Yv0h77H488hcy5xdT4B+d+EBkDhfq/l9oaIxaTwFE9s1T33sKVcrNXcTYYgg7tRleHuSbgvXEbHtVRgVXjwTrCAUvgichV9lLK1Q15sQJPCWi02HzTC7Kaq~1',
        'ttwid': '1%7CT_5sZDUaUw2lnkHwrKmEqusBeEqkapMM7ie9gQ5aWgY%7C1678071694%7C209a0d3a94e0f2fbfc29ab916da026015af8658ffe321362c4b53e272cefa8b5',
        'odin_tt': '1be8b5f7ffce17dbbe12b6ba04151262e5deb0971021876ad1bb20cfc83ed91da3f560e2ca8bd2182cf033c30a64087e9bb22c7c3350a49a1cc21ef20381ea056f6e5976eb2f83cc9a8ff4a7fe3275e4',
        'msToken': 'qC3nUMeJvGo2AaHbM3phwpT469tCtn_ePHw8bCX0OmCQuoAF758er1ZWOMZLfBPaQ9DtnvuNwq11KQbGyYL2Cthl012xp11Bp8TNtlPQ_E9VFxcpvn7qP9clBiGrRl9lINZ2ct48w5Z9vFrH0_Ks',
    }

    headers = {
        'authority': 'www.tiktok.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': '_ttp=289J0zFF3tfkEFKeyLDCZKFwDMC; tiktok_webapp_theme=light; tt_csrf_token=r16ny1BX-ESae4IUXYwaSlnIqU3bSLqKJGvQ; passport_csrf_token=43ed0a56987b053feb953b798a8ab69a; passport_csrf_token_default=43ed0a56987b053feb953b798a8ab69a; s_v_web_id=verify_ldgr2ah9_xz7m8a1G_7Lit_4xlj_985M_JMIPWGVpbMZN; d_ticket=156ce90a06b2b94cae934a6bcdac0274024ea; uid_tt=ca756457013b4db955360f56b19678518583b7e30c2753eecd5e9d6afc8d650b; uid_tt_ss=ca756457013b4db955360f56b19678518583b7e30c2753eecd5e9d6afc8d650b; sid_tt=a76d4ca06ba5c894586138c7d158fe98; sessionid=a76d4ca06ba5c894586138c7d158fe98; sessionid_ss=a76d4ca06ba5c894586138c7d158fe98; store-idc=useast5; store-country-code=us; store-country-code-src=uid; tt-target-idc=useast5; tt-target-idc-sign=J2zC8abDjFPdDukSUlAP9z669_pAxKquT9QkKSvHByOXmSl7e-NPfVfyeZdnnQFQSMwCErEYDMuV032IZMH5Py0Fjv-xioY4iEXxB1L4tXc93xMceauR1FpTj3FIfD9LEKTpE3u8Yry-S9xaA4K0I2Ee-FamDwL-8gjMRArr8Sdb2GzlDdcysInt9DMG_W2fcDNA2vAIc6Ndt6wzVq9p6trVpW6BfYJpo4LQtm5es02KQVdLjvM99tlS41ojW84RQHERJyQMzJRTmMOyeU4VmvmWE49bZougUPmA2MVRcNEPW8BtdxQfCuhBpm5lAuGq5a4JpiMBnsKTuft0SaX1wqZLLKmyBzc98q7Y6ZbZHtDEnXfFUuchAjQCwiQ63RYN4F0Bm6CxrWE97T8Ew_J0pU6j8LnWOUc_7iXSedv-tYWyyhOtQvmvM0RAvDx0AYcGG0Uh9hul_sGapwedBqezMt4OG92aXp0i8DX1TvNat-WmXFSe2PsCaN1RwxmMy5Xa; csrf_session_id=0fd659681307d0f9d9cf261c8d0e0b99; passport_fe_beating_status=true; cmpl_token=AgQQAPNSF-RMpbPrI8_GZh0S-RWI0x5Yv6zZYMpuPA; __tea_cache_tokens_1988={%22user_unique_id%22:%227166372563806291502%22%2C%22timestamp%22:1674958582630%2C%22_type_%22:%22default%22}; sid_guard=a76d4ca06ba5c894586138c7d158fe98%7C1677026254%7C5184000%7CSun%2C+23-Apr-2023+00%3A37%3A34+GMT; sid_ucp_v1=1.0.0-KDJhMDkyYWQwZTkwYTNiYzQ0ZDE3NThhNjA4ZTgwZGE4YjI2OTdhY2IKIAiriNPyhK3z6mMQzsfVnwYYswsgDDDbm9eeBjgCQPEHEAQaB3VzZWFzdDUiIGE3NmQ0Y2EwNmJhNWM4OTQ1ODYxMzhjN2QxNThmZTk4; ssid_ucp_v1=1.0.0-KDJhMDkyYWQwZTkwYTNiYzQ0ZDE3NThhNjA4ZTgwZGE4YjI2OTdhY2IKIAiriNPyhK3z6mMQzsfVnwYYswsgDDDbm9eeBjgCQPEHEAQaB3VzZWFzdDUiIGE3NmQ0Y2EwNmJhNWM4OTQ1ODYxMzhjN2QxNThmZTk4; tt_chain_token=+7hqfC9Fp2bQ45CHIVx3EQ==; _abck=E372DE3F8F68C9482D8CA6BD492A5E99~0~YAAQPzoZuK8xPIeGAQAAfxDctAkaVGi0/IEKojaWzsy9LHgAdw3fRcfgXTUPV4ElOUQeNdrG6oZGWDFd+cPtADJuqgcnHSBqBOQsnKdHkSjVofSvaF3pN+mHUgTVQmHIGsQA9tvjKQ1DwMBhWhDkwHmetny+763GMZZumYGZiyEL4CI94KwFR1tUipwW/6eFMPNd5V94KqUE0pFUMiLAXhnX4rEV6J0TzTQRSmTLetphe98kiWSLGSqHwapTwGPPt2NiVwf+MMwtwMUDegvAzP05jy4bdnVjS9nKiagmKaBNK1dVb+/NefNLsvtOZ6C+La3oIfIYH1zqGWJEoAUamxe8Wa/kodZrqQ7VQeXYjZg0V4sx9mJdCFy7ErLc+ujwcOjdrF3SJmHG9TCHP6a8t+UmJp/DvmAe~-1~-1~-1; bm_sz=BB6842AFC43042B89B89BDA309226CEE~YAAQPzoZuLIxPIeGAQAAfxDctBOr5wEOVfrm4TjGGpHmBZAlbi2eGf6KJVEUXh3kGAwr8pQccC949pulMAh621OnQjUrBeXm5stBitbsEjuxAv92DadgKS6rV9brIryZT7RsOfyF1IyDnoPXXEyRcnIa+lSMU5NA+q0kHfEWyQ3EHA3KugLYHqOplTXYmXjQZXzPgtxUhA2il+YE22xK4ol1BvyukwAaynEAsEVDUPeLkCLhyCv+j8dZ/30gLvOouLtAUEZCvqRPPbieeD+gn9v9DYE11IaXjND3SqnCS5UD3i4=~4408373~4538934; ak_bmsc=D3DDBB60951382FD6183425B22C99411~000000000000000000000000000000~YAAQPzoZuLUxPIeGAQAAmRnctBO5dl+d1ztr80Ib06boNDgz2ps24+viCgnaJ4Xs4Gf9oMj01wwNpwyHrhpGX2uJKw1S0ubofRKNBCDoPiXNImLoSR2FJh01TvLTjTuRrMx7UMiPVG4Q2LBHVKZ3ELQdxbXjIU7Kol1tU2MoPlm2IBzFVA/eYtN+1VaSUSQINoFaGhxxXceQF2BWZHwNpSOm5Aith70I/WuB3HEG2QtHnUdaOquZUn51UChyBnU2xiRiqzFbXTWkV9sMAVnHtRkjx6vzh29fsyfFEnmJXxO8WKaypwXEMu6EGnKfFNxEEI7VjDVB+LnNsWNuKuG+rXMH5iwwZIBaQ8dtYR3prYEHA2MfjZK8cmf41WPSRqEJdoFSK8PjZ1ABCXdv0O0Mr4el8LAxu86EYYOJiR7Xn8gDt/4NRP3JZsUwfdTqTWNZSnqC+FVMR5YzPxFZEoQquxHUEO4ZyYxqH08U9xsdWXFW/btqnumCRhw=; msToken=WPpwKEkDI2qHKKKhxE2H2cdGDu2Pw-br0NzqxsjsXec0Ler_Uhsg4d6GHOzko-X35nU1cKIT388LMxj3vDaVo-7LAhiZJkZ1NyffppIv7E5nxaGIvzK2Y5QAQU4G1DBuFy22UssIV7jj7mrlmJsi; bm_sv=F71DAFE3C25B9EB8CEC3F72A034558DF~YAAQPzoZuPsxPIeGAQAA0PfdtBOoWadiyraqRJmHT28S5hcPb9n1NDhN05cZNY1fhPpoSzxus0onORo2s1bciWyeh5K0UdjZ4YBjotYOcyaIQ7n+NSgamQC8RccXSpvxHOolINPr4Yv0h77H488hcy5xdT4B+d+EBkDhfq/l9oaIxaTwFE9s1T33sKVcrNXcTYYgg7tRleHuSbgvXEbHtVRgVXjwTrCAUvgichV9lLK1Q15sQJPCWi02HzTC7Kaq~1; ttwid=1%7CT_5sZDUaUw2lnkHwrKmEqusBeEqkapMM7ie9gQ5aWgY%7C1678071694%7C209a0d3a94e0f2fbfc29ab916da026015af8658ffe321362c4b53e272cefa8b5; odin_tt=1be8b5f7ffce17dbbe12b6ba04151262e5deb0971021876ad1bb20cfc83ed91da3f560e2ca8bd2182cf033c30a64087e9bb22c7c3350a49a1cc21ef20381ea056f6e5976eb2f83cc9a8ff4a7fe3275e4; msToken=qC3nUMeJvGo2AaHbM3phwpT469tCtn_ePHw8bCX0OmCQuoAF758er1ZWOMZLfBPaQ9DtnvuNwq11KQbGyYL2Cthl012xp11Bp8TNtlPQ_E9VFxcpvn7qP9clBiGrRl9lINZ2ct48w5Z9vFrH0_Ks',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    }
    response = requests.get(f'https://www.tiktok.com/@{account}', cookies=cookies, headers=headers)
    return response.text

def get_links_and_captions(account):
    text = query(account)
    tokens = text.split("\"")
    links = [token for token in tokens if f"https://www.tiktok.com/@{account}/video/" in token]

    captions = dict()
    for link in links:
        vid_id = link.split("/video/")[-1].strip('/') #check no slash on the end
        identifier = "{\"id\":\"" + vid_id + "\",\"desc\":\""
        caption = text[text.index(identifier) + len(identifier) :].split('\"')[0]
        # caption = " ".join([word for word in caption.split(" ") if ('🫶🏼' not in word)]) #to filter emojis (add later)
        captions[vid_id] = caption

    return links, captions

def update_data(account):
    links, captions = get_links_and_captions(account)

    if account not in tiktok_data_indiv:
        tiktok_data_indiv[account] = {'last_posted': -1, 'video_ids': []}

    for link in links[::-1]:
        vid_id = str(link.split("/video/")[-1].strip('/'))
        if vid_id not in tiktok_data_indiv[account]['video_ids']:
            tiktok_data_indiv[account]['video_ids'].append(vid_id)

    tiktok_captions_indiv.update(captions)

    ## SAVE UPDATED DATA
    save_files()

def increment_last_posted_indiv(account):
    tiktok_data_indiv[account]["last_posted"] += 1
    save_files()

def increment_last_posted_popular(account):
    tiktok_data_popular[account]["last_posted"] += 1
    save_files()


