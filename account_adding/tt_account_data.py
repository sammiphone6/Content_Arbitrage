import requests
from data import open_filedata, save_filedata
import time
import pprint
from multiprocessing import Process, Manager
import random

folder = 'data/tt_freqs'
tiktok_bfs = open_filedata(f'{folder}/tiktok_bfs.txt')
tiktok_bfs = sorted(tiktok_bfs, key=lambda x: int(x[2]), reverse = True)
## We now have all 28k tiktok_bfs queries sorted by likes in decreasing order

accounts = []
[accounts.append(entry[1]) for entry in tiktok_bfs if entry[1] not in accounts]
## We now have all ~27k tiktoks usernames

def analysis(account, num_vids):
    def get_element(text, delim1, delim2, index = 1):
        return text.split(delim1)[index].split(delim2)[0]
    
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

    def get_pfp(account, text):
        tries = 0
        while tries < 4:
            if tries > 0:
                text = query(account)
            tokens = text.split('\"')
            for i in range(len(tokens)):
                token = tokens[i]
                try:
                    if token.index('https://p16-sign') == 0 and tokens[i-2] == "og:image": return token
                except:
                    pass
            tries += 1

    def check_username(username):
        ## AVAILBLE -> TRUE
        ## NOT AVAILABLE -> FALSE

        cookies = {
            # 'dpr': '2',
            # 'csrftoken': 'ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr',
            # 'mid': 'ZCbL0QAEAAG2s8tbvORyKr1ojdID',
            # 'ig_did': 'A826ECAF-2499-4076-BE4B-86F1DC0F1A8B',
            # 'ig_nrcb': '1',
            # 'datr': 'ycsmZDOym4SoVV8SY7uM0df5',
        }

        headers = {
            # 'authority': 'www.instagram.com',
            # 'accept': '*/*',
            # 'accept-language': 'en-US,en;q=0.9',
            # 'content-type': 'application/x-www-form-urlencoded',
            # # 'cookie': 'dpr=2; csrftoken=ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr; mid=ZCbL0QAEAAG2s8tbvORyKr1ojdID; ig_did=A826ECAF-2499-4076-BE4B-86F1DC0F1A8B; ig_nrcb=1; datr=ycsmZDOym4SoVV8SY7uM0df5',
            # 'origin': 'https://www.instagram.com',
            # 'referer': 'https://www.instagram.com/accounts/emailsignup/',
            # 'sec-ch-prefers-color-scheme': 'light',
            # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            # 'sec-ch-ua-mobile': '?0',
            # 'sec-ch-ua-platform': '"macOS"',
            # 'sec-fetch-dest': 'empty',
            # 'sec-fetch-mode': 'cors',
            # 'sec-fetch-site': 'same-origin',
            # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
            # 'viewport-width': '1792',
            # 'x-asbd-id': '198387',
            'x-csrftoken': 'ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr',
            # 'x-ig-app-id': '936619743392459',
            # 'x-ig-www-claim': '0',
            # 'x-instagram-ajax': '1007221364',
            # 'x-requested-with': 'XMLHttpRequest',
            # 'x-web-device-id': 'A826ECAF-2499-4076-BE4B-86F1DC0F1A8B',
        }

        data = {
            'email': '',
            'username': username,
            'first_name': '',
            'opt_into_one_tap': 'false',
        }

        response = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        # print(response.text)
        return "This username isn't available." not in response.text

    def get_best_username(usernames):
        if isinstance(usernames, list) or isinstance(usernames, tuple):
            for username in usernames:
                if check_username(username): return username
            return False
        elif isinstance(usernames, str):
            ignore = [0, 1, 2, 3, 5, 6, 7, 8, 9]
            account_stripped = usernames
            
            for c in ignore:
                account_stripped = account_stripped.replace(str(c), '')
            
            usernames = [
                f"{account_stripped}_clips",
                f"{account_stripped}_exclusive",
                f"{account_stripped}_extras",
                f"{account_stripped}_highlights",
                f"{account_stripped}_secrets",
            ]
            random.shuffle(usernames)
            # usernames = [
            #     f"{account}official",
            #     f"{account}highlights",
            #     f"bestof{''.join(account_results['name'].split()[0])}",
            # ]
            return get_best_username(usernames)

    
    account_results = dict()

    ### TIKTOK DATA
    ## Query Tiktok
    text = query(account)
    # with open(f'{account}.txt', 'w') as file:
    #     file.write(text)

    ## Get rate of posting
    created_time = get_element(text, "\"createTime\":\"", "\"", index = num_vids+1) #text.split(signal)[num_vids+1].split("\"")[0]
    timespan = time.time() - int(created_time)
    rate = timespan/num_vids
    account_results['tt_posting_rate'] = round(rate/3600, 2)

    ## Get total likes
    account_results['tt_likes'] = get_element(text, "\"heartCount\":", ",")

    ## Get total followers
    account_results['tt_followers'] = get_element(text, "\"authorStats\":{\"followerCount\":", ",")

    ## Get total following
    account_results['tt_following'] = get_element(text, "\"followingCount\":", ",")

    ## Get number of videos
    account_results['tt_videos'] = get_element(text, ",\"videoCount\":", ",")
    
    ## Get name
    account_results['tt_name'] = get_element(text, "Watch the latest video from ", " (")
    if len(account_results['tt_name']) > 100:
        account_results['tt_name'] = get_element(text, "\"></style><title data-rh=\"true\">", " (")
    account_results['tt_name'] = account_results['tt_name'].replace('&amp;', '&')

    ## Get bio
    account_results['tt_bio'] = get_element(text, 'Followers. ', "Watch the latest video from ")
    account_results['tt_bio'] = account_results['tt_bio'].replace('&amp;', '&')

    ## Get PFP
    account_results['tt_pfp'] = get_pfp(account, text)

    # ## Make IG username
    account_results['ig_username'] = get_best_username(account)

    ## Make IG pfp
    account_results['ig_pfp'] = f"{account_results['ig_username']}.jpg"
    with open(f"PFPs/{account_results['ig_pfp']}", 'wb') as file:
        file.write(requests.get(account_results['tt_pfp']).content)

    ## Make IG email
    account_results['ig_email'] = f"{account_results['ig_username'].split('_')[0].lower()}@talent.promo"

    ## Make IG Name
    capitalized = account_results['tt_name'][0].isupper()
    end_word = account_results['ig_username'].split('_')[-1]
    account_results['ig_name'] = f"{account_results['tt_name']} {end_word[0].upper() if capitalized else end_word[0].lower()}{end_word[1:]}"

    ## Make IG bio
    if account_results['ig_username'].split('_')[-1] == 'exclusive': 
        depends = f"{account_results['ig_name'][-1]} {'Content' if capitalized else 'content'}!! (not impersonating)"
    elif account_results['ig_username'].split('_')[-1] == 'secrets': 
        depends = f" {'Content' if capitalized else 'content'}!! (not impersonating)"
    else: 
        depends = f"{account_results['ig_name'][-1]}!! (not impersonating)"

    account_results['ig_bio'] = f"{account_results['ig_name'][:-1]}{depends}"
    account_results['ig_bio'] += f"\nFollow for the best clips 🔽"
    account_results['ig_bio'] += f"\nBusiness: {account_results['ig_email']}, Telegram: @talentpromo"

    return account_results

def get_data(accounts, num_vids):
    responses = dict()
    def compute(responses, account):
        try:
            responses[account] = analysis(account, num_vids)
        except:
            pass
    
    def runInParallel():
        with Manager() as manager:
            m_resps = manager.dict()
            proc = []
            for i in range(len(accounts)):
                account = accounts[i]
                p = Process(target=compute, args=(m_resps, account))
                proc.append(p)
                p.start()
                time.sleep(1.5)
                print(i, '/', len(accounts))
                if(i % 20 == 0):
                    time.sleep(10)
            for p in proc:
                p.join()
            responses.update(m_resps)

    runInParallel()

    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(responses)

    prev_data = open_filedata('data/tiktok_accounts_data.txt')
    responses.update(prev_data)
    save_filedata('data/tiktok_accounts_data.txt', responses)
    return responses

start = time.time()
accounts = accounts[1000:1100]
random.shuffle(accounts)



def check_username(username):
    ## AVAILBLE -> TRUE
    ## NOT AVAILABLE -> FALSE

    cookies = {
        # 'dpr': '2',
        # 'csrftoken': 'ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr',
        # 'mid': 'ZCbL0QAEAAG2s8tbvORyKr1ojdID',
        # 'ig_did': 'A826ECAF-2499-4076-BE4B-86F1DC0F1A8B',
        # 'ig_nrcb': '1',
        # 'datr': 'ycsmZDOym4SoVV8SY7uM0df5',
    }

    headers = {
        # 'authority': 'www.instagram.com',
        # 'accept': '*/*',
        # 'accept-language': 'en-US,en;q=0.9',
        # 'content-type': 'application/x-www-form-urlencoded',
        # # 'cookie': 'dpr=2; csrftoken=ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr; mid=ZCbL0QAEAAG2s8tbvORyKr1ojdID; ig_did=A826ECAF-2499-4076-BE4B-86F1DC0F1A8B; ig_nrcb=1; datr=ycsmZDOym4SoVV8SY7uM0df5',
        # 'origin': 'https://www.instagram.com',
        # 'referer': 'https://www.instagram.com/accounts/emailsignup/',
        # 'sec-ch-prefers-color-scheme': 'light',
        # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        # 'sec-ch-ua-mobile': '?0',
        # 'sec-ch-ua-platform': '"macOS"',
        # 'sec-fetch-dest': 'empty',
        # 'sec-fetch-mode': 'cors',
        # 'sec-fetch-site': 'same-origin',
        # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        # 'viewport-width': '1792',
        # 'x-asbd-id': '198387',
        'x-csrftoken': 'ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr',
        # 'x-ig-app-id': '936619743392459',
        # 'x-ig-www-claim': '0',
        # 'x-instagram-ajax': '1007221364',
        # 'x-requested-with': 'XMLHttpRequest',
        # 'x-web-device-id': 'A826ECAF-2499-4076-BE4B-86F1DC0F1A8B',
    }

    data = {
        'email': '',
        'username': username,
        'first_name': '',
        'opt_into_one_tap': 'false',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    # print(response.text)
    return "This username isn't available." not in response.text


accounts_data = get_data(accounts, 10)
# accounts_data = open_filedata('data/tiktok_accounts_data.txt')
print(len(accounts_data))
print(time.time()-start)

# print('\n\n\n\n\n')
# for acc in accounts_data:
#     print(acc)
#     for elem in accounts_data[acc]:
#         if elem[:3] == 'ig_':
#             print(elem, accounts_data[acc][elem])


## Make sure you can update the dictionary and resave it each time you do something here


### Get more good cheap instas https://accsmarket.com/en/catalog/instagram/pva 
### Also, fully automate by getting their name, pfp from tiktok, make some generic bio formula,
### And while creating a new account you can easily test available usernames from the ten we might want
### Bio formula should include not impersonating.