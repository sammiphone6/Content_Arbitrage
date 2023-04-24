import requests
import time
from account_adding.data import instas, tiktok_account_data

from bs4 import BeautifulSoup

def main_query(instagram):

    cookies = {
        # 'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        # 'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        # 'ig_nrcb': '1',
        # 'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        # 'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        # 'ds_user_id': '58449324934',
        # 'fbm_124024574287414': 'base_domain=.instagram.com',
        # 'dpr': '2',
        'sessionid': '58449324934%3A6WUkIv01qfppaB%3A3%3AAYdGMv78y09PSs_x8R9T8wNX-inYyh8wlQw36U_tliU',
        # 'fbsr_124024574287414': 'rqr1VJV2CVwlt4UcU5wpwI993BoxFa_E8Py297YP_wI.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ3NncTNJNHlWc1FlLXpQZXp2UU9MZEZuSTJwMU5hc2dxSzN0eEpGY1NwRmk3U1pGM1JHVFdOWGZCV3FxN3RDdEkxYUVERjJleG15NVhuaFBQMzJONDA3Q2JlaDYyRUZkSGo5dnlLSW9ERi1mQU1tM0ZwM0xsQ25nYmszc19WNzUzeEp5al9Id2l0QV9lMTVIaDkxZWlHVkVoUlZHRzNySDRiWlA0TlNqem1ONW1HYS0yZDRid3ktd2FwaWhJOG1JaE9DTnh2dTVHWVhSY2djenV5WVRkaEpaaHRnRFVab05nQVdqYVpGZHo2a2ZJSTBFWVNaYTc5UFBLVU5zWnVNUjBWWVBxQTlPdXRzZmJHaG9TQkxhSjdIV1NXbl9MRDJwREJRS0pNRXNHRU5jZEdxN25FU3lGLUpJYzNLZzhReUVfb2M3VlF3RERtUzBBUEFvbTg2T1pZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUM1Nm9wNG96NVpBZ0VKbU9FWkFJTkpXa3N1ZkNpQVhQV0h5b2oyVTZraTFxc0tWVzg2RmRzVUZrWkNTd21KelBkYWJBWkNDVXlFcHFIOE9Nc1lTV3JBM05jS0lHcFZocktTVlpDUXRxQWtXZVVqNXlwMEhaQmhib3lnWkE1Vkc5QkNnVVNya1E4YlN1Mk9welFmTHlGY2ZaQVFiS0J6NEtqYlU4d1ZSaE04enIyS3dnZFpCUFpCTW9aRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyMjc0MjAzfQ',
        # 'fbsr_124024574287414': 'kTNlhz3ubA5AvAbbMf1TubHw1of46y8AbMS1tFjCtpk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ0NQZ19oSFBubGFxUE1KQ09KaXQyVk5XZEpCN1RnbEJDcnREN3ZqWDVTY0VGRFlmMy1nMDlqZFlpS09BcTBMTWdXbDFpS2RPSDdtU0RiZDdYZVIzZnBWVjgwWVFBV1NOSmt2QXRhdDZ5T3hSWVByUnpPUW9aZmdDcF9mV1RuZzFDUXRRZk81MV9ZcUgyZllBc1I3UEFBZ1hEQU9DZEh3c1R5NGV4dkY0RVFsbXRRTkxidUtBRHhiRWloZDlyYnJyU2VhZ0xTaXNoajY0UE5SdHhhM19zNlFrQ1V0bXh4RWJXOGo0SWxhLXRBWWJmNmxwOEpSNGx4ZlZOS2dUMl9Ubmt1RzZ2dkc3TGttMGJ3dE1CeGhJbXJqWE1TVWJwZE1KQkRBa0oyV2xnSjdjMmplMTdFdENiRExLT1pDN1hjcmlvUE1wYlU0dzZ6MVJWM0dYelVaOEdyIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUg0bXlyZWZLZUFjUFlVYXFLWFpDVXpMa2pDZXFrME9NOW9YTjg0ZEtvM2p3djVGZHF4NVNaQUNaQnl4aUl5dlFobnkzRTR4M2ZUSkZnM2xqbEpqMmo1QWwyUENuUVBIT3NGWkFRZkNwdms0cDRvVTM3bEpJa1VVYVdNYzE0SktEeG03UzQ1YnBpWHV2WkM3aG9IcGxCNTV5M29aQkJSVFdWYnNpY2JPVDcxaUFzNW1aQVlpSklaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyMjc2MzMxfQ',
        # 'rur': '"NCG\\05458449324934\\0541713812372:01f7e69b866b577bb93dd7149ece670d024a662bbdfee20dbe734167333adff7c2043118"',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; ds_user_id=58449324934; fbm_124024574287414=base_domain=.instagram.com; dpr=2; sessionid=58449324934%3A6WUkIv01qfppaB%3A3%3AAYdGMv78y09PSs_x8R9T8wNX-inYyh8wlQw36U_tliU; fbsr_124024574287414=rqr1VJV2CVwlt4UcU5wpwI993BoxFa_E8Py297YP_wI.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ3NncTNJNHlWc1FlLXpQZXp2UU9MZEZuSTJwMU5hc2dxSzN0eEpGY1NwRmk3U1pGM1JHVFdOWGZCV3FxN3RDdEkxYUVERjJleG15NVhuaFBQMzJONDA3Q2JlaDYyRUZkSGo5dnlLSW9ERi1mQU1tM0ZwM0xsQ25nYmszc19WNzUzeEp5al9Id2l0QV9lMTVIaDkxZWlHVkVoUlZHRzNySDRiWlA0TlNqem1ONW1HYS0yZDRid3ktd2FwaWhJOG1JaE9DTnh2dTVHWVhSY2djenV5WVRkaEpaaHRnRFVab05nQVdqYVpGZHo2a2ZJSTBFWVNaYTc5UFBLVU5zWnVNUjBWWVBxQTlPdXRzZmJHaG9TQkxhSjdIV1NXbl9MRDJwREJRS0pNRXNHRU5jZEdxN25FU3lGLUpJYzNLZzhReUVfb2M3VlF3RERtUzBBUEFvbTg2T1pZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUM1Nm9wNG96NVpBZ0VKbU9FWkFJTkpXa3N1ZkNpQVhQV0h5b2oyVTZraTFxc0tWVzg2RmRzVUZrWkNTd21KelBkYWJBWkNDVXlFcHFIOE9Nc1lTV3JBM05jS0lHcFZocktTVlpDUXRxQWtXZVVqNXlwMEhaQmhib3lnWkE1Vkc5QkNnVVNya1E4YlN1Mk9welFmTHlGY2ZaQVFiS0J6NEtqYlU4d1ZSaE04enIyS3dnZFpCUFpCTW9aRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyMjc0MjAzfQ; fbsr_124024574287414=kTNlhz3ubA5AvAbbMf1TubHw1of46y8AbMS1tFjCtpk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ0NQZ19oSFBubGFxUE1KQ09KaXQyVk5XZEpCN1RnbEJDcnREN3ZqWDVTY0VGRFlmMy1nMDlqZFlpS09BcTBMTWdXbDFpS2RPSDdtU0RiZDdYZVIzZnBWVjgwWVFBV1NOSmt2QXRhdDZ5T3hSWVByUnpPUW9aZmdDcF9mV1RuZzFDUXRRZk81MV9ZcUgyZllBc1I3UEFBZ1hEQU9DZEh3c1R5NGV4dkY0RVFsbXRRTkxidUtBRHhiRWloZDlyYnJyU2VhZ0xTaXNoajY0UE5SdHhhM19zNlFrQ1V0bXh4RWJXOGo0SWxhLXRBWWJmNmxwOEpSNGx4ZlZOS2dUMl9Ubmt1RzZ2dkc3TGttMGJ3dE1CeGhJbXJqWE1TVWJwZE1KQkRBa0oyV2xnSjdjMmplMTdFdENiRExLT1pDN1hjcmlvUE1wYlU0dzZ6MVJWM0dYelVaOEdyIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUg0bXlyZWZLZUFjUFlVYXFLWFpDVXpMa2pDZXFrME9NOW9YTjg0ZEtvM2p3djVGZHF4NVNaQUNaQnl4aUl5dlFobnkzRTR4M2ZUSkZnM2xqbEpqMmo1QWwyUENuUVBIT3NGWkFRZkNwdms0cDRvVTM3bEpJa1VVYVdNYzE0SktEeG03UzQ1YnBpWHV2WkM3aG9IcGxCNTV5M29aQkJSVFdWYnNpY2JPVDcxaUFzNW1aQVlpSklaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyMjc2MzMxfQ; rur="NCG\\05458449324934\\0541713812372:01f7e69b866b577bb93dd7149ece670d024a662bbdfee20dbe734167333adff7c2043118"',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'viewport-width': '1792',
    }

    response = requests.get(f'https://www.instagram.com/{instagram}/', cookies=cookies, headers=headers)
    return response

def get_id(instagram):
    
    response = main_query(instagram)
    text = response.text
    # delim = "\"page_id\":\"profilePage_"
    delim = "\"user_id\":\""
    id = text.split(delim)[1].split("\"")[0]
    return id

def get_reels(instagram, num_reels = 12):

    def get_reels_from_id(id, num_reels):
        cookies = {
            # 'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
            # 'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
            # 'ig_nrcb': '1',
            # 'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
            # 'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
            # 'ds_user_id': '58449324934',
            # 'fbm_124024574287414': 'base_domain=.instagram.com',
            # 'dpr': '2',
            # 'sessionid': '58449324934%3A6WUkIv01qfppaB%3A3%3AAYdGMv78y09PSs_x8R9T8wNX-inYyh8wlQw36U_tliU',
            # 'fbsr_124024574287414': 'rqr1VJV2CVwlt4UcU5wpwI993BoxFa_E8Py297YP_wI.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ3NncTNJNHlWc1FlLXpQZXp2UU9MZEZuSTJwMU5hc2dxSzN0eEpGY1NwRmk3U1pGM1JHVFdOWGZCV3FxN3RDdEkxYUVERjJleG15NVhuaFBQMzJONDA3Q2JlaDYyRUZkSGo5dnlLSW9ERi1mQU1tM0ZwM0xsQ25nYmszc19WNzUzeEp5al9Id2l0QV9lMTVIaDkxZWlHVkVoUlZHRzNySDRiWlA0TlNqem1ONW1HYS0yZDRid3ktd2FwaWhJOG1JaE9DTnh2dTVHWVhSY2djenV5WVRkaEpaaHRnRFVab05nQVdqYVpGZHo2a2ZJSTBFWVNaYTc5UFBLVU5zWnVNUjBWWVBxQTlPdXRzZmJHaG9TQkxhSjdIV1NXbl9MRDJwREJRS0pNRXNHRU5jZEdxN25FU3lGLUpJYzNLZzhReUVfb2M3VlF3RERtUzBBUEFvbTg2T1pZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUM1Nm9wNG96NVpBZ0VKbU9FWkFJTkpXa3N1ZkNpQVhQV0h5b2oyVTZraTFxc0tWVzg2RmRzVUZrWkNTd21KelBkYWJBWkNDVXlFcHFIOE9Nc1lTV3JBM05jS0lHcFZocktTVlpDUXRxQWtXZVVqNXlwMEhaQmhib3lnWkE1Vkc5QkNnVVNya1E4YlN1Mk9welFmTHlGY2ZaQVFiS0J6NEtqYlU4d1ZSaE04enIyS3dnZFpCUFpCTW9aRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyMjc0MjAzfQ',
            # 'fbsr_124024574287414': 'T3OEiJxiVGxSoVuiKj_PA_rzNLYWbZ5TPD9SmHiF0ic.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRF9ISEc2MXR2SW9CbXZ4OFhBemFJWHh2LUl6Qmt6b1FaWEVfaGpzZnpNT1Z1YkxxYUc5MFZxOGM5aHNWaUwyZWdPMkFtOVBXRnFnN0pGUUIwVXpyS2tuX1o2anFmRS16RXZPX1Z3QVV3VnM3N0ZQSFhRcXBwWTJEcEhfaGkzZ3JsNTk1OWNuNVdKUk5IV1AtZlpJdW1fVjVjb01POWJnZVQ0V0t5amlfT084RW1uTFFMeWpXS01IR2hFWFh1c2pYNy1nNHA2b3J5bDlrN0NwaFlaRzdfelppaUE1aW1EUm85WmdfMVRWSVFaUjUtVnROMk45NXlDM0VwbHhyNmRlamNGbHJja0pGWEx3d1lDY3M5d3ZqTWRNeG44NDZVZktvY0UwZEozd3RqQXVQeHBEQ1Vna09pdERjTDV1M2RZTWcxbzZiWExfOGhUdEo3Z2FUYlBYOUdaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFJazh6TlRVQjBjOWhLSnZISEQ4YmVoM3Q3aUM3QVdaQVNOOEFobVExenNLUlBDOWo3am1NMWZTczdsM0RLYnhSa0Nva1FvMU5UNTBGeGIzWkE1TzBrcEloWkJoT0hkYlNFc0p1Y3hrRW92OGs5aTZLNG5Wd0xmNUNGOGJYTFpBaVlKeWI3c3RzYWNjbUZBaHV3Sm0wVlh4elpBSEMzMjIyVzZoYklnaUkwZTlYZVk3VEo4WkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjI3NDM0MX0',
            # 'rur': '"NAO\\05458449324934\\0541713810380:01f76da12094fc17c9d4c5fa447a17cda40e7b3f7da9e80e1982469db478257beef0daa7"',
        }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; ds_user_id=58449324934; fbm_124024574287414=base_domain=.instagram.com; dpr=2; sessionid=58449324934%3A6WUkIv01qfppaB%3A3%3AAYdGMv78y09PSs_x8R9T8wNX-inYyh8wlQw36U_tliU; fbsr_124024574287414=rqr1VJV2CVwlt4UcU5wpwI993BoxFa_E8Py297YP_wI.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ3NncTNJNHlWc1FlLXpQZXp2UU9MZEZuSTJwMU5hc2dxSzN0eEpGY1NwRmk3U1pGM1JHVFdOWGZCV3FxN3RDdEkxYUVERjJleG15NVhuaFBQMzJONDA3Q2JlaDYyRUZkSGo5dnlLSW9ERi1mQU1tM0ZwM0xsQ25nYmszc19WNzUzeEp5al9Id2l0QV9lMTVIaDkxZWlHVkVoUlZHRzNySDRiWlA0TlNqem1ONW1HYS0yZDRid3ktd2FwaWhJOG1JaE9DTnh2dTVHWVhSY2djenV5WVRkaEpaaHRnRFVab05nQVdqYVpGZHo2a2ZJSTBFWVNaYTc5UFBLVU5zWnVNUjBWWVBxQTlPdXRzZmJHaG9TQkxhSjdIV1NXbl9MRDJwREJRS0pNRXNHRU5jZEdxN25FU3lGLUpJYzNLZzhReUVfb2M3VlF3RERtUzBBUEFvbTg2T1pZIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUM1Nm9wNG96NVpBZ0VKbU9FWkFJTkpXa3N1ZkNpQVhQV0h5b2oyVTZraTFxc0tWVzg2RmRzVUZrWkNTd21KelBkYWJBWkNDVXlFcHFIOE9Nc1lTV3JBM05jS0lHcFZocktTVlpDUXRxQWtXZVVqNXlwMEhaQmhib3lnWkE1Vkc5QkNnVVNya1E4YlN1Mk9welFmTHlGY2ZaQVFiS0J6NEtqYlU4d1ZSaE04enIyS3dnZFpCUFpCTW9aRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyMjc0MjAzfQ; fbsr_124024574287414=T3OEiJxiVGxSoVuiKj_PA_rzNLYWbZ5TPD9SmHiF0ic.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRF9ISEc2MXR2SW9CbXZ4OFhBemFJWHh2LUl6Qmt6b1FaWEVfaGpzZnpNT1Z1YkxxYUc5MFZxOGM5aHNWaUwyZWdPMkFtOVBXRnFnN0pGUUIwVXpyS2tuX1o2anFmRS16RXZPX1Z3QVV3VnM3N0ZQSFhRcXBwWTJEcEhfaGkzZ3JsNTk1OWNuNVdKUk5IV1AtZlpJdW1fVjVjb01POWJnZVQ0V0t5amlfT084RW1uTFFMeWpXS01IR2hFWFh1c2pYNy1nNHA2b3J5bDlrN0NwaFlaRzdfelppaUE1aW1EUm85WmdfMVRWSVFaUjUtVnROMk45NXlDM0VwbHhyNmRlamNGbHJja0pGWEx3d1lDY3M5d3ZqTWRNeG44NDZVZktvY0UwZEozd3RqQXVQeHBEQ1Vna09pdERjTDV1M2RZTWcxbzZiWExfOGhUdEo3Z2FUYlBYOUdaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUFJazh6TlRVQjBjOWhLSnZISEQ4YmVoM3Q3aUM3QVdaQVNOOEFobVExenNLUlBDOWo3am1NMWZTczdsM0RLYnhSa0Nva1FvMU5UNTBGeGIzWkE1TzBrcEloWkJoT0hkYlNFc0p1Y3hrRW92OGs5aTZLNG5Wd0xmNUNGOGJYTFpBaVlKeWI3c3RzYWNjbUZBaHV3Sm0wVlh4elpBSEMzMjIyVzZoYklnaUkwZTlYZVk3VEo4WkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjI3NDM0MX0; rur="NAO\\05458449324934\\0541713810380:01f76da12094fc17c9d4c5fa447a17cda40e7b3f7da9e80e1982469db478257beef0daa7"',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/jackdoherty/reels/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'viewport-width': '1792',
            'x-asbd-id': '198387',
            'x-csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
            'x-ig-app-id': '936619743392459',
            # 'x-ig-www-claim': 'hmac.AR3T24zTBrAocWPHWdKcr7KMSB7XrdkyqICzGYB_rpLAZLj4',
            # 'x-instagram-ajax': '1007365265',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'target_user_id': id,
            'page_size': num_reels,
            'include_feed_video': 'true',
        }

        response = requests.post('https://www.instagram.com/api/v1/clips/user/', cookies=cookies, headers=headers, data=data)
        json = response.json()

        # import pprint
        # pp = pprint.PrettyPrinter(depth=6)

        # item = json['items'][11]
        for item in json['items']:
            print(item['media']['video_versions'][0]['url'], None if item['media']['caption'] == None else item['media']['caption']['text'], '\n')

        print(len(json['items']))

    get_reels_from_id(get_id(instagram), num_reels)

def get_following(instagram, relationship):

    def get_part_of_following(instagram, start, relationship = 'following'):
        cookies = {
            'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
            'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
            'ig_nrcb': '1',
            'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
            'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
            'ds_user_id': '58449324934',
            'fbm_124024574287414': 'base_domain=.instagram.com',
            'dpr': '2',
            'fbsr_124024574287414': 'M2-8Jqtd5wJq0M0Jc0voCItl_drn2FxV1N8DAAMcejQ.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ1FoQTZMZW80VnRQTERZOWRlUDFyamJrTU9OTjBmZTBfU200bTZUcmI4M2RjaFBaQWROWUpIRUNYZW1kbHU4UFR0MkFsQU9NQzkzdVdjbXk2YjBQSjdJQ1hkWHRfeW5pNGN3M2Fqd2F1S09Sb3hzMTRTSE5VcUllXy04QkFKUlhKbzRkZHd5Zm9YaXpBeWlEalE0UmdIbjBhR0Y3Q2trcWQ5NmViRXhXX2t1WXgzY2Y1ZFlpdWpnVVhOLUR3YzdoYUVIaURKTUVEV2tqUWk4TTNUMGo0MTY3WEI2OFdoX25NT3dSUDhLWDNranM1NWxpa0JnUVFwMXlNYnJOWm9TcDhuRU5icGRnSC1nQlZKRWRFX3hPQ2I4T09kSzV5ZjE2NGx4anBpdTNORzlQTExZRmthRjhHVFE4Vl9FZ2I3LVhFRllvMkJlbzNvQ1dmaWtuUGY2U0ZnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZvTTYxWkJXY3ZZaVhFUVpCMDYyaGVpQm02alBKMVJaQ2laQTVud25QNHZpbUlRV0lZQjRVdWJaQ3hoNlBmSWVVWVFmSHpHbGRmME55bGx3WkJoTGFaQnZ2Z2lYWEFoVHpFbDk2NDNRREZCQ1FqSVlyejR4Y0xubzlqS1BOWkFJd1loeVZIdk1RSk5LQ3hDWXVxRmFEWkNXRDJRc2tGa3huamV2eTdVQ2xkWVh1NEcwQVlLWkFzNjRaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyMjg4NzA5fQ',
            'sessionid': '58449324934%3A6WUkIv01qfppaB%3A3%3AAYdC-RNC3Ca1X_oXnit58OzLEzxK75xofoQBeC3_Y60',
            'rur': '"NAO\\05458449324934\\0541713824720:01f73cd6c56be33df0b2e7652d3d9b62ce88233849d7e859122dd052615da230ecbe68d3"',
        }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; ds_user_id=58449324934; fbm_124024574287414=base_domain=.instagram.com; dpr=2; fbsr_124024574287414=M2-8Jqtd5wJq0M0Jc0voCItl_drn2FxV1N8DAAMcejQ.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ1FoQTZMZW80VnRQTERZOWRlUDFyamJrTU9OTjBmZTBfU200bTZUcmI4M2RjaFBaQWROWUpIRUNYZW1kbHU4UFR0MkFsQU9NQzkzdVdjbXk2YjBQSjdJQ1hkWHRfeW5pNGN3M2Fqd2F1S09Sb3hzMTRTSE5VcUllXy04QkFKUlhKbzRkZHd5Zm9YaXpBeWlEalE0UmdIbjBhR0Y3Q2trcWQ5NmViRXhXX2t1WXgzY2Y1ZFlpdWpnVVhOLUR3YzdoYUVIaURKTUVEV2tqUWk4TTNUMGo0MTY3WEI2OFdoX25NT3dSUDhLWDNranM1NWxpa0JnUVFwMXlNYnJOWm9TcDhuRU5icGRnSC1nQlZKRWRFX3hPQ2I4T09kSzV5ZjE2NGx4anBpdTNORzlQTExZRmthRjhHVFE4Vl9FZ2I3LVhFRllvMkJlbzNvQ1dmaWtuUGY2U0ZnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZvTTYxWkJXY3ZZaVhFUVpCMDYyaGVpQm02alBKMVJaQ2laQTVud25QNHZpbUlRV0lZQjRVdWJaQ3hoNlBmSWVVWVFmSHpHbGRmME55bGx3WkJoTGFaQnZ2Z2lYWEFoVHpFbDk2NDNRREZCQ1FqSVlyejR4Y0xubzlqS1BOWkFJd1loeVZIdk1RSk5LQ3hDWXVxRmFEWkNXRDJRc2tGa3huamV2eTdVQ2xkWVh1NEcwQVlLWkFzNjRaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyMjg4NzA5fQ; sessionid=58449324934%3A6WUkIv01qfppaB%3A3%3AAYdC-RNC3Ca1X_oXnit58OzLEzxK75xofoQBeC3_Y60; rur="NAO\\05458449324934\\0541713824720:01f73cd6c56be33df0b2e7652d3d9b62ce88233849d7e859122dd052615da230ecbe68d3"',
            # 'referer': 'https://www.instagram.com/chriscrpyto/following/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'viewport-width': '1792',
            'x-asbd-id': '198387',
            'x-csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3T24zTBrAocWPHWdKcr7KMSB7XrdkyqICzGYB_rpLAZDSf',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'count': 200,
            'max_id': start,
        }

        response = requests.get(
            f'https://www.instagram.com/api/v1/friendships/{get_id(instagram)}/{relationship}/',
            params=params,
            cookies=cookies,
            headers=headers,
        )

        json = response.json()
        following = [user['username'] for user in json['users']]
        return following

    following = []
    ship = []
    prev = -1
    i = 0
    j = 0
    while len(following) != prev:
        prev = len(following)
        print(len(following))
        [following.append(f) for f in get_part_of_following(instagram, start = 200*i, relationship = relationship) if f not in following]
        print(len(following))
        i += 1
        while j < len(following):
            person = following[j]
            res = text_in_caption(person)
            print(res, person)
            if res == True: ship.append(person)
            j += 1
        print(ship)
    return following

def text_in_caption(instagram, desired_text = 'ship'): #this works well for shipping
    response = main_query(instagram)
    text = response.text

    delim = '<script type=\"application/json\"'
    first_part = text.split(delim)
    return desired_text in first_part

chris_followers = ['mcgarry', 'thenuova.concierge', 'aqua_house_milos', 'jmaulino',
                    'trilly.dante', 'arizonaarose', 'emmalilkendeyy', 'leah0carroll',
                      'strawberrymilkmob', 'natalie.reynolds', 'tgriffshoots', 'waterwippinevan',
                        'moe.capital', 'alexh459', 'mattyr_ecom', 'nickclegg', 'lexinicolex',
                          'markhmendez', 'sophierothschild', 'watchoutforalex', 'bentossell',
                            'anastasiachernen', 'wtfcora', 'charlierothkopf', 'peqqa', 'mateusfabiani',
                              'tina.u1', 'citareservations', 'thefakebirkinslayer', 'ivglitched', 'nextel',
                                'je6se', 'philipps_lifestyle_', 'lukebelmar', 'mrbelmar', 'samuelsnell', 'skylerprks',
                                  'irasigman', 'andrew.weber12', 'mobamby', 'joshuabooker', 'ansab3', 'stxrsu', 
                                  'kylegjoyce', 'stevenmillow', 'j_bach', 'paulribot', 'blocked', 'ace', 'freezer',
                                    'dvminics', 'doa', 'moonidotai', 'phoebeisobelx', 'raybueno.ai', '_davidmorris',
                                      'audreyspiller', 'kayy_jane', '7slavic', 'ericaa.jeann', 'kinley_turner', 'luthergales',
                                        'kaitlynbubolz', 'stephaniehurleyy', 'ty.vem', 'alexandrapaull_', 'zayinbrown',
                                          'trottersjewellersuk', 'ercfilings', 'cambriacapizzi', 'yashabh', '6', '5',
                                            'ahmadtofficial', 'ntungbach', 'benbelack', 'carsonkrecow', 'theaadoraa',
                                              'gmoneyy4ll', 'ophorawater', 'daisycalvertt', 'joshfoxceo', 'amoeller',
                                                'j4ckld', 'aymankhan25', 'kndall', 'garybrecka', 'ykcally', 
                                                'carterjamisn', 'gideon.___', '-beem', 'shadesofgame', 'law.in.dubai', 'iishtheceo', 'gabrielle_moses2', 'enrxgn', '0gbobby.eth', 'wwflight', 'cryptoanish', 'gisringhausen', 'dociaga', 'chasefayez', 'charizard', 'tenielllee', 'hunterdnelson', 'ecombrothers', 'flyblade', 'cuebanks', 'kira.rhyne', 'immattmann', 'dotcomnik', 'kaleb', 'sushibyscratchrestaurants', 'wiresonly', 'chefhuyle', 'udsstudio', 'tannerkesel', 'splashpj', 'ercgoat', 'tuckergenal', 'ecomdustin', 'nouhdavis', 'sebb', 'jvnior', 'shyonq', 'generations', 'mitchell', 'dempsikeegan', 'sydney.hudson', 'itsfaridnaimi', 'emma.furr', 'vahe_gmsla', 'brandonhamam', 'wow', '777kloud', 'blankplsceholder', 'pineapplepaintedlime', 'risdomlin', 'dogedillionaire', 'sydneyposey_', 'itsjosecintron', 'iamtiagz', 'billyhowell', 'cassiuscuvee', 'theabdulkareem', 'joeyxbruno', 'cameronhowrd', 'ulyaanaaaa.off', 'alexrae_x', 'sam_strouse', 'ellachandler29', 'ryan.leroy', 'jonjafari', 'maxoregan21', 'sellclocks', 'neeltpt', 'realj0sef', 'reillysanders', 'adelakf', 'faiz', 'themartiniloverr', 'emmapoole16', 'lilyfreedman_', 'ceoryanwhite', 'ameerhussainn', 'notmiche', 'yasminesara_', 'vladazzam', 'that.lara', 'chloetenggren', 'sara_bay2k', 'aliyah.torrez', 'keanawachter', 'hayleycherepak', 'hannahvbuck', 'gi.marinelli', 'reeagaann', 'aubriannaberger', 'dashadova', 'laura.sthn', 'isabellacking', 'kevking23', 'capitalclub', 'scott.hilse', 'biaheza', 'makayla.moss', 'madelinehendrickss', 'orlandocsantiago', 'kiilleyyy', 'breesemaroc', 'adriaenblack', 'heyevantan', 'heystevetan', 'brinleytuverson', 'earn', 'diptyque', 'outhw8', 'lucanetz', 'zachdfriedman', 'maths']

# following = get_following("georgeanisimow")
# print(following)
# print(len(following))

get_following('dropship', relationship='followers')

# george_following = ['lucid.diorr', 'aleksandra_sandrik_', 
#                     'anton_shef', 'richrussiankids', 'artyomxx', 'danielfield63', 'yrebryk', 'addiss_b', 'connorkauff', '___k_a_t_e___2002', 'doroteamurray', '_pozdno_kati', 'anna_and_kids', 'mrseroff', 'bankofgrails', 'losangelesbucketlist', 'stella__bear', 'silverboiiii', '_t1mma', 'camillezjohnson', 'dorian_mrtn__', 'nick.daglas', 'diptyque', 'livelovebym', 'dr3', 'vcbrags', 'yulliasakova', 'andu.c', 'hiinikita', 'bradeazy', 'noellehear', 'vanderpernt', 'thatmtxdancer', 'belllacosta', 'hunterkellyy', 'polina_zhagula', 'iamadam6', 'sneshaa23', 'silver.julia', 'jackriedle', 'ashhole_miles', 'giannicures', 'saintagln', 'elizavetayaroslavovna', 'postn0vskii', 'valeriagruzdeva', 'venturekaepital', 'ryansandytos', 'diego_against_the_world', 'alisonsarzoza', 'isaakpresley', 'tim.d.brown', 'nickkrogers', 'sal.g_', 'caleb_circle', 'calmegor', 'gordonfishh', 'chasegarveydaniels', 'eli_ba_bal', 'insiderbusiness', 'lucky13nick', 'elizabeth.grosss', 'emma.caitie', 'justinhornn', 'esteban.https', 'keyysus', 'maazvohraa', 'metav3rse', 'littlemissjacob', 'justinreed', 'gwvr.y', '_molly_blair', 'archdigest', 'jacob_hak', 'valerielepelch', 'flishy', 'dariagustaya', 'okunevaa.k', 'bonkers4memes', 'olesyainwonderlands', 'imlandnn', 'begachevanina', 'erewhonmarket', 'aziztazi90', 'saimaglushchenko', 'max.louis', 'alex.holtt', 'alexandriatrainer', '1.unplugged.6', 'theminadoll', 'matiascve', 'karinadolgihh', 'fedo_ju', 'haileyrbr', 'issac_2_._0', 'j3rm1e', 'ryanhtang', '_vanessarivera_', 'aryacharmchi', 'mayagarinee', 'ophorawater', 'ruben_loza', 'greysongasaway', 'gigi.benedict', 'dazydubs', 'negusflex', 'babypupsiii', 'yodamianb', 'imlandn', 'damian.brunton', 'jamiecharoen', 'officialvpowers', 'mckinleyrichardson', 'artdrivers', 'ellinamz', 'arseniybogdanas', 'iamkatyalebedeva', 'traneblow', 'ariadnajacob', 'itsluxcity', 'savenko__', 'jackdoherty', 'sashkemene', '_averina_ss', 'kaehla', 'arinajoyful', 'alishasmearman', 'thepowerfuldeez', 'perchik_katya', 'memezar', 'irinnamik', 'jax_bu', 'kiana._.c', 'ellie._.sb', 'cobysayyah', 'artifaxing', 'classystreetwear', 'annatessakoehler', 'stephanie.wise', 'polinces', 'isabelledelceaa', 'losers._.101', 'mimichellelove', 'bogomyako', 'i_have_no_memes96_v2', 'lordhomie', 'elina.supernova', 'jennastover_', 'tunaparpar', 'minnetdinov', 'highsnobiety', 'west_la_memes', 'trill_henderson', 'lovatooforu', 'brianwedd', 'sergeybogomyako', 'yungstary', 'tierrangray', 'paskuda.ru', 'soobole.va', 'iamjc4', 'nicolesussman', 'kev2024', 'imaristuart', 'ben.baak', 'annabkenn', 'kari.sh__', 'alisa.ch', 'alexandra.wallacee', 'instatroll_football', 'laceyvjames', 'zubzn', 'natashaashapiro', 'argynam', 'ketrin__melnikova', 'rollton_keeper', 'timkurt', 'paul_shab', 'shalena55', 'christopher.brownn', 'daviddobrik', 'lahikes', 'wvyrose', 'phillipsmichael7', 'sorb_freshstart', 'able.raf', 'edward.baksheev', 'david.huntzinger', 'j.brilez', 'skppde', 'mszkodon', 'ntshkncr', 'dankophilia', 'elisabeth_anisimow', 'beibeihuei', 'belan_sergey', 'legacykgbmember', 'castingspb_nastya', 'jenfny', 'kondratyevdev', '178polina', 'eliasymer', 's_kaukiainen', 'jackdeckers', 'eduardhatesinsta', 'schweezy_lv', 'veronicaputilina', 'queenviki_', 'quinnlfrt', 'footballtransfersdaily', 'mishka_os_', 'bilochenko.an', 'dashisnthere', 'dirkdean83', 'ahmetinan5734', 'sonyarusu', 'prosto_noone', 'chrisallmeid', 'alexiwesti', 'mboconnor_', 'fiveze', 'anthony.shumate', 'elennaowen', 'colton4th', 'konnorparis', 'iamaksik', 'mantitspodcast', 'madysontostado', 'lucifenaa', 'lexizzlemanizzl', 'katya.khov', 'vivienne_og', 'animage.fun', 'nene_mal_', 'irelandob_', 'alan.roof', 'sloanesiegel', 'katyascotts', 'sophia.randolph', 'zak.cosman', 'mashagovdyak', 'supersnake', 'cali_playa', 'iamtiagz', 'cinephile.club', 'daleguey', 'geoorgiaaa', 'kzntsv.a._', 'leondorrenberg', 'rozazlina', 'maria.diamond', 'onlyjayus', 'elizavetaabulina', 'jack.cathcart', 'pisnova', 'oiiikrosbii', 'chriscrpyto', 'yamilka_cerro', 'lev_beylin', 'theclubjesus', 'neresating', 'alexisdixn', 'amandasolley', 'nnstsyy', 'mulleavyy', 'kate_tii_', 'dcohen_', 'ashleyrowen', 'kslr', 'conradsmithh', 'anthonyjoshua', 'erik_uae77', 'highsnobietydesign', 'tasiachernenkova', 'ericbryanstone', 'vitorized', 'overheardla', 'itssarcasmqueenn', 'rimeamary', 'marckycox', 'leon_jose_nati', 'anovellance', '_evan_weiss', 'joshebroni', 'mo_wad', 'brandon.rusin', 'ftbl', 'sydneyness', 'datastuffplus', 'noragolling', 'notrussiandaddyyy', 'archived.dreams', 'iamelenapetrova_', 'tanamongeau', 'mattzworld', 'nataliengibson', 'sofiarazuvaeva', 'taobeach', 'alex.chon', 'elysebillig', 'matthewjgl', 'iknowx2', 'timooxxaa', 'arianaaobrien', 'dan4k40', 'russiansinlondon', 'bbellaawhite', 'jordan_bleu', 'georgia_hinds', 'hvostov', 'svetik2935', 'gmst.elio', 'dianchix', 'karante_kid', 'f0ai6', 'georgezhang1', 'madisonshamoun', 'kay.lahuang', 'transfers', 'inna.alisultanova', 'soccermemes', 'svetlyachyok_', 'joey_agena', 'codelibaby', 'dose.ofmemes', 'ihategum', 'baloban_nik', 'mimoshapeligrosa', 'nicole___hart', 'avavonn', 'eluna.ai', 'mattsworldd', 'olchasilyutina', 'irasigman', 'sashkemene2', 'clodgod', 'karelykris', 'oleksandra.km_', 'chelseafc', 'batyaindahouse', 'sumfattytuna', 'meganaalexis', 'gabefelipe7', 'augustfouts', 'natalierebelle', 'polayna888', 'ms.monicafrench', 'konma_', 'orelthebro', 'premierleague', 'nemyagky', 'loganpgarretson', 'sammyhauser', 'alex.matin25', 'worldstar', 'laurencsilver', '_techmech', 'maxwellmcclung', 'asyasari_', 'paryakoubi', 'greta_eriksson', 'walkkeerrr', 'cha_cha_chito', 'hayleylanger', 'alisanroze', 'pinkpersianprincess', 'jackie.curtis', 'samxfrank', 'ricardomendes1', 'sevazhidkov', 'anastasiachernen', 'c.shotya', 'bdavve', 'starboyzwrld', 'bigneverlose', 'amobi_noble', 'alzimin', 'vladlarionov', 'mertsalihkilic', 'kaleb_miner', 'michael_haambayi', 'elizavetka___', 'lennart', 'markel.0ff', 'f.a.s.e.l', 'kirillzzy', 'alxmamaev', 'sckromniy', 'sethmoberg', 'ta.m.ii', 'officialjrod', 'oxytrips', 'laaaaadaaaaa', 'nefedovskayaaa', 'alinalipova', 'sparringhighlights', 'rnbstellar', 'sammiphone.6', 'alwaysmirza', 'brandonpomo', 'julietskyyy', '_k_a_r_i_s_h_o_k_', 'rritarrose', 'the.lurv', 'daddysam', 'bella.garc', 'prayingforexits', 'raymondsilverman', 'aidan.moyer', 'marksamorodskikh', 'sonya.yurieff', 'readymade_official', 'steph_ml', 'napenshe', 'abbyrifkin', 'imc0smo', 'blgdrvletta', 'malaakwehba', 'bwahlb', 'sean_grindal', 'igntvaa', 'alexeykomok', 'soniaaabutenko', 'anna_kohh_', 'zaywilson', 'samhutch9', 'petjia', 'chantellnat', 'sabrinajordanmusic', 'teogreen15', 'loganpaul', 'klj_offcial', 'omg_its_er1c', 'ivan.ivanchanko', 'sway.camm', 'dot_domain', 'mapkyckzn', 'visubal', 'a_rutkovskii', 'th3fac3of3llay', 'chelsea.purdum', 'miamalkova', 'rachelonassis', 'brfootball', 'helenasoph', 'daniel_bosche', 'idealist.world', 'tuckergenal', 'taylor.geller', 'ivan_elevate', 'alepshua', 'lizazel', 'thenoejose', 'kelly.konis', 'christabel_ji', 'imwithandreas', 'leraxbb', 'takemetochurch.__', 'by_kanatchicovaa', 'adrien_nav', 'goshaginyan', 'champagnepapi', 'artyshatilov', 'lnterestingasfuck', 'darydolgova_', 'fokshhh', 'arinamitt', 'goodfelllaa', 'kcarrieee', 'trtmdvk', 'savannahyassin', 'brooklynrjackson', 'kellyypriebe', 'fsi16', 'rey.na.na', 'mckinneygoes2', 'peach_mari_', 'elizaveta_kondrateva', 'mark_sarabia', 'alex_gamb', 'showtimefletchh', 'johnnyguazz', 'gress.polya', 'lovusooo', 'mindplaydnb', 'daniella.thomas', 'savingconnie', 'cortneycgibson', 'erikgarci.a', 'a.a.ronmoreno', 'alissa.su', 'itsqcp', 'russian.lawyer', 'kvirkvelia_levan', 'arline.scotton', 'drtacoo', 'chels.mo', 'daddysteve', 'teresaning', 'shinigami_anya', 'myselfasemily', 'vlrgrzdv', 'tzaharcheva', 'painful_memes.v2', 'norathesilkyterrier', 'robdaplugg', 'benktaytay', 'niicobritt', 'pickuplinesdj', 'aiahmariah', 'escapizmeee', 'lalaogvenice', 'laurendavidi', 'nicojordan_1', 'arielagati', 'lerka_eklerka', 'arjundoom']

# not_followback = []
# for person in george_following:
#     person_following = get_following(person)
#     res = 'georgeanisimow' in person_following
#     print(res, person)
#     if res == False: not_followback.append(person)

# print(not_followback)



# yes = []
# for person in chris_followers:
#     res = text_in_caption(person)
#     print(res, person)
#     if res == True:
#         yes.append(res)

# print(yes)


# import requests

# cookies = {
#     'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
#     'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
#     'ig_nrcb': '1',
#     'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
#     'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
#     'ds_user_id': '58449324934',
#     # 'fbm_124024574287414': 'base_domain=.instagram.com',
#     'dpr': '2',
#     'sessionid': '58449324934%3A6WUkIv01qfppaB%3A3%3AAYe6TQ4xq1PhA_eKkAveGMFc7CxYBoPWpDhVPRNDWKY',
#     # 'fbsr_124024574287414': '-jFv-agCxB2mLKRThxgWJXqn_9VkNYUC-AWk5OnxA2U.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRFY4aUgxMlQ3ZHhMSFVlOWt1YTU4U3Q1TnpiZFpRYVhOdVRSbldMS2F0cDBEWW9aY3dRYTQ5NWdHbHhVQ2F3Z2RXNXhYdUxxd1hJODcxejZ0MHR6VkJ2NmRTQnNqRFBCQkcyU0dMQ0hyWXNSN2NkVkZDZTVQeWxqZi04SGtQeHNjSWF4VEJ1R1labnNJS21qeG1EbmFGZDhiTjBkZllMbUptbUxxUHk4cGtVdFhFRE1ZU0sxRTdpVTdfTlE5THIwaWItTUtfc1ZEOWg0VWx4R0tfMnlucU85cE9xczltSVB6TTkyQ0g2OE5PZ2s2RHQxOWdoMWdCN3BvQzBjd0dsS2hGdjZmQU9PY055ZHZhN2lhc3VvaGRxZlVkeEVzLUVsd3F4OGQ5dmhKekozR2c5REVRR092TW9ySDB0UVpRcUhUQ0ZOUG9FV1NQOWg2OS0tN3hGSmhaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQURwckM5R2ZwNzFoT3pTV3JqcUpTaml3OVlLUldLdXU4cnhnWEJaQk9xN0o5aThUZHdkNTdWZUFqUFpCcGlwR0tkV3ZJR3RPQzdLZzZaQnZRMEs4NmdNUlhnZlpDaTNQSGVqNUFzOGVkNmZIc0dxbnlicFFra1BBWDQzbzVsTmRGWU1IWUlxTlU3MkZ4UXc4Z1BjbG90S296WGx4blpDUmVKUkpQZTI1cmZ3b2lXb2h3NUIwWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjIxMTkzMX0',
#     # 'fbsr_124024574287414': '-jFv-agCxB2mLKRThxgWJXqn_9VkNYUC-AWk5OnxA2U.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRFY4aUgxMlQ3ZHhMSFVlOWt1YTU4U3Q1TnpiZFpRYVhOdVRSbldMS2F0cDBEWW9aY3dRYTQ5NWdHbHhVQ2F3Z2RXNXhYdUxxd1hJODcxejZ0MHR6VkJ2NmRTQnNqRFBCQkcyU0dMQ0hyWXNSN2NkVkZDZTVQeWxqZi04SGtQeHNjSWF4VEJ1R1labnNJS21qeG1EbmFGZDhiTjBkZllMbUptbUxxUHk4cGtVdFhFRE1ZU0sxRTdpVTdfTlE5THIwaWItTUtfc1ZEOWg0VWx4R0tfMnlucU85cE9xczltSVB6TTkyQ0g2OE5PZ2s2RHQxOWdoMWdCN3BvQzBjd0dsS2hGdjZmQU9PY055ZHZhN2lhc3VvaGRxZlVkeEVzLUVsd3F4OGQ5dmhKekozR2c5REVRR092TW9ySDB0UVpRcUhUQ0ZOUG9FV1NQOWg2OS0tN3hGSmhaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQURwckM5R2ZwNzFoT3pTV3JqcUpTaml3OVlLUldLdXU4cnhnWEJaQk9xN0o5aThUZHdkNTdWZUFqUFpCcGlwR0tkV3ZJR3RPQzdLZzZaQnZRMEs4NmdNUlhnZlpDaTNQSGVqNUFzOGVkNmZIc0dxbnlicFFra1BBWDQzbzVsTmRGWU1IWUlxTlU3MkZ4UXc4Z1BjbG90S296WGx4blpDUmVKUkpQZTI1cmZ3b2lXb2h3NUIwWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjIxMTkzMX0',
#     # 'rur': '"NAO\\05458449324934\\0541713747980:01f7a3c994c645c3a8bc0fe81e48435392eef9f6f111ed7f371ae6481fcb61cf52192bec"',
# }

# headers = {
#     'authority': 'www.instagram.com',
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9',
#     'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
#     # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; ds_user_id=58449324934; fbm_124024574287414=base_domain=.instagram.com; dpr=2; sessionid=58449324934%3A6WUkIv01qfppaB%3A3%3AAYe6TQ4xq1PhA_eKkAveGMFc7CxYBoPWpDhVPRNDWKY; fbsr_124024574287414=-jFv-agCxB2mLKRThxgWJXqn_9VkNYUC-AWk5OnxA2U.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRFY4aUgxMlQ3ZHhMSFVlOWt1YTU4U3Q1TnpiZFpRYVhOdVRSbldMS2F0cDBEWW9aY3dRYTQ5NWdHbHhVQ2F3Z2RXNXhYdUxxd1hJODcxejZ0MHR6VkJ2NmRTQnNqRFBCQkcyU0dMQ0hyWXNSN2NkVkZDZTVQeWxqZi04SGtQeHNjSWF4VEJ1R1labnNJS21qeG1EbmFGZDhiTjBkZllMbUptbUxxUHk4cGtVdFhFRE1ZU0sxRTdpVTdfTlE5THIwaWItTUtfc1ZEOWg0VWx4R0tfMnlucU85cE9xczltSVB6TTkyQ0g2OE5PZ2s2RHQxOWdoMWdCN3BvQzBjd0dsS2hGdjZmQU9PY055ZHZhN2lhc3VvaGRxZlVkeEVzLUVsd3F4OGQ5dmhKekozR2c5REVRR092TW9ySDB0UVpRcUhUQ0ZOUG9FV1NQOWg2OS0tN3hGSmhaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQURwckM5R2ZwNzFoT3pTV3JqcUpTaml3OVlLUldLdXU4cnhnWEJaQk9xN0o5aThUZHdkNTdWZUFqUFpCcGlwR0tkV3ZJR3RPQzdLZzZaQnZRMEs4NmdNUlhnZlpDaTNQSGVqNUFzOGVkNmZIc0dxbnlicFFra1BBWDQzbzVsTmRGWU1IWUlxTlU3MkZ4UXc4Z1BjbG90S296WGx4blpDUmVKUkpQZTI1cmZ3b2lXb2h3NUIwWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjIxMTkzMX0; fbsr_124024574287414=-jFv-agCxB2mLKRThxgWJXqn_9VkNYUC-AWk5OnxA2U.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRFY4aUgxMlQ3ZHhMSFVlOWt1YTU4U3Q1TnpiZFpRYVhOdVRSbldMS2F0cDBEWW9aY3dRYTQ5NWdHbHhVQ2F3Z2RXNXhYdUxxd1hJODcxejZ0MHR6VkJ2NmRTQnNqRFBCQkcyU0dMQ0hyWXNSN2NkVkZDZTVQeWxqZi04SGtQeHNjSWF4VEJ1R1labnNJS21qeG1EbmFGZDhiTjBkZllMbUptbUxxUHk4cGtVdFhFRE1ZU0sxRTdpVTdfTlE5THIwaWItTUtfc1ZEOWg0VWx4R0tfMnlucU85cE9xczltSVB6TTkyQ0g2OE5PZ2s2RHQxOWdoMWdCN3BvQzBjd0dsS2hGdjZmQU9PY055ZHZhN2lhc3VvaGRxZlVkeEVzLUVsd3F4OGQ5dmhKekozR2c5REVRR092TW9ySDB0UVpRcUhUQ0ZOUG9FV1NQOWg2OS0tN3hGSmhaIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQURwckM5R2ZwNzFoT3pTV3JqcUpTaml3OVlLUldLdXU4cnhnWEJaQk9xN0o5aThUZHdkNTdWZUFqUFpCcGlwR0tkV3ZJR3RPQzdLZzZaQnZRMEs4NmdNUlhnZlpDaTNQSGVqNUFzOGVkNmZIc0dxbnlicFFra1BBWDQzbzVsTmRGWU1IWUlxTlU3MkZ4UXc4Z1BjbG90S296WGx4blpDUmVKUkpQZTI1cmZ3b2lXb2h3NUIwWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4MjIxMTkzMX0; rur="NAO\\05458449324934\\0541713747980:01f7a3c994c645c3a8bc0fe81e48435392eef9f6f111ed7f371ae6481fcb61cf52192bec"',
#     'origin': 'https://www.instagram.com',
#     # 'referer': 'https://www.instagram.com/kevinhart4real/',
#     'sec-ch-prefers-color-scheme': 'light',
#     'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
#     'viewport-width': '1792',
# }

# params = {
#     'appid': 'com.instagram.interactions.about_this_account',
#     'params': '{"target_user_id":"6590609","referer_type":"ProfileUsername"}',
#     'type': 'app',
#     '__d': 'www',
#     '__bkv': '63da05bda64dad0fbc1db2d283b310c0cfb4576f492c961af93e68ea3e4ac735',
# }

# data = {
#     '__d': 'www',
#     '__user': '0',
#     '__a': '1',
#     # '__req': '6',
#     # '__hs': '19470.HYP:instagram_web_pkg.2.1..0.0',
#     # 'dpr': '2',
#     # '__ccg': 'EXCELLENT',
#     # '__rev': '1007364892',
#     # '__s': 'mh392g:t79lya:tqwv6r',
#     # '__hsi': '7225045423567813063',
#     # '__dyn': '7xeUmwlE7ibwKBWo2vwAxu13w8CewSwMwNw9G2S0lW4o0B-q1ew65xO0FE2awt81s8hwGwQw9m1YwBgao6C0Mo5W3S7U2cxe0EUjwGzE2swwwNwKwHw8Xxm16wa-7-0iK2S3qazo7u1xwIw8O321bwzwTwKG1pg661pwr8',
#     # '__csr': 'g9IbPkxsoG9qitHvkhWeSull8GlbHZbmGKqmAejAz8_hHBuiiiqiQ9BJ2poLCCAGJ4GmuUrjUyFryGAx2dKE014M81qUc9o58k1hw0yfg2uyiU6G0im0kwEeo621FB4w46eehEuwwUUw5q17wn40IPxu3V0g4Nuxg0gIxe1awhE2Do0A614w0iYU0yG0t6',
#     '__comet_req': '7',
#     'fb_dtsg': 'NAcPcYh0G_FZLvCeBUz31zBT_C2AmlIKsdvkNhWFzaKJ8CLOq0MOR_A:17864789131057511:1679271820',
#     # 'jazoest': '26150',
#     # 'lsd': 'dt_Q7h82torGIb8yw1KsvJ',
#     # '__spin_r': '1007364892',
#     # '__spin_b': 'trunk',
#     # '__spin_t': '1682211976',
# }

# response = requests.post('https://www.instagram.com/async/wbloks/fetch/', params=params, cookies=cookies, headers=headers, data=data)

# print(response.text)
# print('July 2011' in response.text)
# import requests

# url = 'https://ipinfo.io'
# username = 'user-rzt5e8cfbe12a-country-us'
# password = 'AuU1T6n20w'

# proxy = f"http://{username}:{password}@dc.razorproxy.com:8001"
# result = requests.get(url, proxies = {
#   'http': proxy,
#   'https': proxy
# })
# print(result.text)

# url = 'https://ipinfo.io'
# username = 'user-rzt5e8cfbe12a-country-us'
# password = 'AuU1T6n20w'

# proxy = f"http://{username}:{password}@dc.razorproxy.com:8001"
# result = requests.get(url, proxies = {
#   'http': proxy,
#   'https': proxy
# })
# print(result.text)

# long_lived_access_token = 'EAACcW8asEe0BAK5pczqZB6LVc8ghvrhKf3BbqZBcFr2lRTHgITX9mfDRUlCSx3AI2HkDEWbToAIHZClTjraXeRQxbWlbWeq2L2o8hKhOR4opoGAsfC2lgXVhy03126dLKZAdTZBU0GcHeMM8RO1M1qdjLfHFvBtJMwerB0IQAiIcmUcS03qfw'
# long_lived_access_token = 'EAACcW8asEe0BAPxIk8EBh1JWuJUWignTA4sznbbr2FyCsewk0UcbM9ogvGhVcDsQkhuyZB5NTOC042WvEUaHwd3Izx61NPQo6481gwkby5Bj1KPcUtWRnhk1VUi6YDIat4M0OOOR5L3ZCeqRCHy6ZBMhL9YODQs9o0mUgKzznyvPKKc3I09iMOhMlPZC8skZD'
# response = requests.get(f'https://graph.facebook.com/v6.0/me?access_token={long_lived_access_token}')
# print(response['id'])

# account_id = 141016978940635
# response = requests.get(f'https://graph.facebook.com/v2.10/{account_id}/accounts?access_token={long_lived_access_token}')
# print(response.text)



# # Define the URL to scrape
# url = "https://en.wikipedia.org/wiki/Live_cattle"

# # Send a GET request to the URL and parse the response using BeautifulSoup
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())
# # Find the first $ amount on the page
# dollar_amount = soup.find('span', class_='currencySymbol').next_sibling

# # Print the dollar amount
# print(dollar_amount)



# def check_username(username):
#     ## AVAILBLE -> TRUE
#     ## NOT AVAILABLE -> FALSE

#     cookies = {
#         # 'dpr': '2',
#         # 'csrftoken': 'ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr',
#         # 'mid': 'ZCbL0QAEAAG2s8tbvORyKr1ojdID',
#         # 'ig_did': 'A826ECAF-2499-4076-BE4B-86F1DC0F1A8B',
#         # 'ig_nrcb': '1',
#         # 'datr': 'ycsmZDOym4SoVV8SY7uM0df5',
#     }

#     headers = {
#         # 'authority': 'www.instagram.com',
#         # 'accept': '*/*',
#         # 'accept-language': 'en-US,en;q=0.9',
#         # 'content-type': 'application/x-www-form-urlencoded',
#         # # 'cookie': 'dpr=2; csrftoken=ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr; mid=ZCbL0QAEAAG2s8tbvORyKr1ojdID; ig_did=A826ECAF-2499-4076-BE4B-86F1DC0F1A8B; ig_nrcb=1; datr=ycsmZDOym4SoVV8SY7uM0df5',
#         # 'origin': 'https://www.instagram.com',
#         # 'referer': 'https://www.instagram.com/accounts/emailsignup/',
#         # 'sec-ch-prefers-color-scheme': 'light',
#         # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#         # 'sec-ch-ua-mobile': '?0',
#         # 'sec-ch-ua-platform': '"macOS"',
#         # 'sec-fetch-dest': 'empty',
#         # 'sec-fetch-mode': 'cors',
#         # 'sec-fetch-site': 'same-origin',
#         # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
#         # 'viewport-width': '1792',
#         # 'x-asbd-id': '198387',
#         'x-csrftoken': 'ozzmHo2Helu0ZhhOAcrW0nMJZfUDvtmr',
#         # 'x-ig-app-id': '936619743392459',
#         # 'x-ig-www-claim': '0',
#         # 'x-instagram-ajax': '1007221364',
#         # 'x-requested-with': 'XMLHttpRequest',
#         # 'x-web-device-id': 'A826ECAF-2499-4076-BE4B-86F1DC0F1A8B',
#     }

#     data = {
#         'email': '',
#         'username': username,
#         'first_name': '',
#         'opt_into_one_tap': 'false',
#     }

#     response = requests.post(
#         'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/',
#         cookies=cookies,
#         headers=headers,
#         data=data,
#     )
#     print(response.text)
#     return "This username isn't available." not in response.text and "A user with that username already exists" not in response.text

# usernames = [
#     # 'Mooni_Savings',
#     # 'investmooni',
#     # 'mooniceo',
#     # 'savingmoney101',
#     # 'financial.wizard777',
#     # 'wizardly.moneyhacks',
#     # 'alphamale.money',
#     # 'retire.smartly',
#     # 'money.like.a.boss',
#     # 'prosper.financials',

#     # 'cryptowatchers',
#     # 'cryptomillions',
#     # 'aaa',
#     # 'blockchain.watchers',
#     # 'winning_in_crypto',
#     # 'crypto_naturals',
#     # 'decentralized_mastery',
#     # 'financial_mastery',
#     # 'fin.zen.mastery',
#     # 'fintips.com',
#     # 'ig.stocks101',
#     # 'stocktrading.tips',

#     'realestate.knowledge',
#     'Mooni_Education',
#     'stockmarketfreedom',
# ]
# for u in usernames:
#     time.sleep(4)
#     if check_username(u):
#         print(u)



# # def get_followers(account):
# #     cookies = {
# #         'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
# #         'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
# #         'ig_nrcb': '1',
# #         'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
# #         'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
# #         'ds_user_id': '58449324934',
# #         'fbm_124024574287414': 'base_domain=.instagram.com',
# #         'dpr': '2',
# #         'sessionid': '58449324934%3A6WUkIv01qfppaB%3A3%3AAYeKXqb2jPfYgYLMle2BdTxBUcenyXwssLMnLkQy-g',
# #         'fbsr_124024574287414': 'oJNl61zmNXbxQQt86F-dKvdwKey8zGwXJqc26xrUBrk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHlnVUZadEJVdzlZaEItQnlMOTFxa2V1bXdWTWxyNjlrdHBHUTNqVzNwWkNMTExUTElvMjkxR0xQNHYxWmZtcjFuanBYWmtfLUhETGg1VXVBU1BTRC1JN1lUNGRYOFB4Y0FPdThJVTh2a19mYnVhSGVRc2NPWGRxS01Eb0p6WjAxbDhlNjFFOUktTVNNSEctZWVUWnIyQnVhOUJtT2tIVXRYRElLLWt5MkhDbmlaOU9Dczl2V18tamFZYTd5ZDlvdUlkY0lVdG1MWjFjS21mSW1TNU1MVFFSdXpSeWpqSk5YZ1FYV0o3M2Z3d09UWVBhbDdfNDNoaWxDakc5ZDdqTHoydjk1THRzeHdjc3RpTzkyai1JaENpV0VQcm41V2Z4Z2o0eURyTmF2WHVfNGtGU0hobXRhQ2pWS2szeEtxb1hFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9IcUtWZWJiZXJYSW9FbUdVeURGRVdaQnNNcFpDMjB1dFpDU05KdlF4amk3ZnZEQldQQW9yd0pWQVVPYUt6dWFrUDlLQ2o1QlBqZ096c1lmZWlYOWpzRGZmcHZXN0lpM0p4eHV2SUFwcWZWNkIxS1R3a0RCN214eWdXUHJmZkFyWE1IbTRKR0UwT3dER1dRd0ZDa2hnaWwzY1pCMHJaQkh0WU1OWkJaQ2ExMjNvZjM3R1M4QlFaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMTEwfQ',
# #         'fbsr_124024574287414': '0OIar_YFlfE4JVVr0rI0ud4bxblYd11_A-UHvrOfohE.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQlZXeGVMcnRLX1U0Yi1nZlJrVzl4MHctTC1wZ1dnaS1YMmkyZ2xWM2JKNW1wZ2o2bnpYSlpZOURHWGVuYjh5RktCUWk1eE1DZXkydDJlWGdVR0ppSjhrb0FlSHJCUDlkY3JsTVg2REszZFZLTDF3N2xPUDJOekdibWhFTnpFRHpqLUJGdVg5U2I0RnhYWW14b1JKNm1sT2Zxc3h0UVBGUWpQZXlDMUdiZjVXeXBZWklWNXhLTVR0WHFYRFR3am5HOEg2M0kyWGFOYVBTY1ZZNXM4QzFXVUFYbzRoenFiNlowb20zVTRJdjM1LTNaaDBHOGJjTWh1cjE2ZXVfVUw1elFEYjZPZ3NMV2xyQ05NSW1UdW8yU2RkZE5oTzJWZC1GSkMtZndaOHlCX3pLLVdFU0pCd2lBU09DTi1obndWclRRIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZmNEJYaVpCSnNrYUplNUh5SldLNGFSVldFU2VvRDFCOHFrcGhGT24zb1Q0UlRaQjh3dWlCV2M3akxLSWFSd2RCNUEwWkJHZmVKNG13QnRaQWFkMnJleHpaQXZuckJaQW9WTmljNjJsSUNrZXc0cGJZTUVlMTJZdGNlWkNibHc0eFgzVlh4YUVBUG5qZ1ZjbTBMdkgzSG1Hb3NHdW5hQUpudDQ3bWU2V1hpN3Z1MEdUVjBSTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMjE0fQ',
# #         'rur': '"NCG\\05458449324934\\0541712089219:01f75cf6177c9dfc392d2257ad437a4a9f177d90d19fab669bd88aa3d6073c451a668b6d"',
# #     }

# #     headers = {
# #         'authority': 'www.instagram.com',
# #         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# #         'accept-language': 'en-US,en;q=0.9',
# #         'cache-control': 'max-age=0',
# #         # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; ds_user_id=58449324934; fbm_124024574287414=base_domain=.instagram.com; dpr=2; sessionid=58449324934%3A6WUkIv01qfppaB%3A3%3AAYeKXqb2jPfYgYLMle2BdTxBUcenyXwssLMnLkQy-g; fbsr_124024574287414=oJNl61zmNXbxQQt86F-dKvdwKey8zGwXJqc26xrUBrk.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRHlnVUZadEJVdzlZaEItQnlMOTFxa2V1bXdWTWxyNjlrdHBHUTNqVzNwWkNMTExUTElvMjkxR0xQNHYxWmZtcjFuanBYWmtfLUhETGg1VXVBU1BTRC1JN1lUNGRYOFB4Y0FPdThJVTh2a19mYnVhSGVRc2NPWGRxS01Eb0p6WjAxbDhlNjFFOUktTVNNSEctZWVUWnIyQnVhOUJtT2tIVXRYRElLLWt5MkhDbmlaOU9Dczl2V18tamFZYTd5ZDlvdUlkY0lVdG1MWjFjS21mSW1TNU1MVFFSdXpSeWpqSk5YZ1FYV0o3M2Z3d09UWVBhbDdfNDNoaWxDakc5ZDdqTHoydjk1THRzeHdjc3RpTzkyai1JaENpV0VQcm41V2Z4Z2o0eURyTmF2WHVfNGtGU0hobXRhQ2pWS2szeEtxb1hFIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU9IcUtWZWJiZXJYSW9FbUdVeURGRVdaQnNNcFpDMjB1dFpDU05KdlF4amk3ZnZEQldQQW9yd0pWQVVPYUt6dWFrUDlLQ2o1QlBqZ096c1lmZWlYOWpzRGZmcHZXN0lpM0p4eHV2SUFwcWZWNkIxS1R3a0RCN214eWdXUHJmZkFyWE1IbTRKR0UwT3dER1dRd0ZDa2hnaWwzY1pCMHJaQkh0WU1OWkJaQ2ExMjNvZjM3R1M4QlFaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMTEwfQ; fbsr_124024574287414=0OIar_YFlfE4JVVr0rI0ud4bxblYd11_A-UHvrOfohE.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQlZXeGVMcnRLX1U0Yi1nZlJrVzl4MHctTC1wZ1dnaS1YMmkyZ2xWM2JKNW1wZ2o2bnpYSlpZOURHWGVuYjh5RktCUWk1eE1DZXkydDJlWGdVR0ppSjhrb0FlSHJCUDlkY3JsTVg2REszZFZLTDF3N2xPUDJOekdibWhFTnpFRHpqLUJGdVg5U2I0RnhYWW14b1JKNm1sT2Zxc3h0UVBGUWpQZXlDMUdiZjVXeXBZWklWNXhLTVR0WHFYRFR3am5HOEg2M0kyWGFOYVBTY1ZZNXM4QzFXVUFYbzRoenFiNlowb20zVTRJdjM1LTNaaDBHOGJjTWh1cjE2ZXVfVUw1elFEYjZPZ3NMV2xyQ05NSW1UdW8yU2RkZE5oTzJWZC1GSkMtZndaOHlCX3pLLVdFU0pCd2lBU09DTi1obndWclRRIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZmNEJYaVpCSnNrYUplNUh5SldLNGFSVldFU2VvRDFCOHFrcGhGT24zb1Q0UlRaQjh3dWlCV2M3akxLSWFSd2RCNUEwWkJHZmVKNG13QnRaQWFkMnJleHpaQXZuckJaQW9WTmljNjJsSUNrZXc0cGJZTUVlMTJZdGNlWkNibHc0eFgzVlh4YUVBUG5qZ1ZjbTBMdkgzSG1Hb3NHdW5hQUpudDQ3bWU2V1hpN3Z1MEdUVjBSTmtaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgwNTUzMjE0fQ; rur="NCG\\05458449324934\\0541712089219:01f75cf6177c9dfc392d2257ad437a4a9f177d90d19fab669bd88aa3d6073c451a668b6d"',
# #         'sec-ch-prefers-color-scheme': 'light',
# #         'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
# #         'sec-ch-ua-mobile': '?0',
# #         'sec-ch-ua-platform': '"macOS"',
# #         'sec-fetch-dest': 'document',
# #         'sec-fetch-mode': 'navigate',
# #         'sec-fetch-site': 'none',
# #         'sec-fetch-user': '?1',
# #         'upgrade-insecure-requests': '1',
# #         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
# #         'viewport-width': '1792',
# #     }

# #     instagram = tiktok_account_data[account]['ig_username']

# #     response = requests.get(f'https://www.instagram.com/{instagram}/', cookies=cookies, headers=headers)
# #     text = response.text
# #     followers = text.split(" Followers")[0].split('content=\"')[-1].replace(',', '')
# #     return followers if len(followers) < 6 else None

# # # tiktok = 'ben_brainard'
# # # print(tiktok, tiktok_account_data[tiktok]['ig_username'], get_followers(tiktok))

# # tiktoks = [t for t in instas['Tiktok username'] if isinstance(t, str)]

# # total = 0
# # broken = 0
# # for tiktok in sorted(tiktoks):
# #     total += 1
# #     result = get_followers(tiktok)
# #     if result == None: broken += 1
# #     print('total: ', total, ' broken: ', broken, tiktok, tiktok_account_data[tiktok]['ig_username'], result)


# # print(len(tiktok_account_data))




# # import cv2  
# # import numpy as np  
# # import scipy.ndimage as sp
# # import pyautogui
# # import PIL.ImageGrab
# # from account_adding.fsm_functions import pause_for
# # snapshot = PIL.ImageGrab.grab()
# # snapshot.save('pilsc.png')

# # image = cv2.imread("Facebook.png")  
# # template = cv2.imread("Phone number.png")  

# # image = cv2.imread("pilsc.png")  
# # template = cv2.imread("cc.png")  

# # # methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
# # #             'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
# # # for method in methods:
# # #     result = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)  
# # #     loc = np.unravel_index(result.argmax(),result.shape)
# # #     print (method, loc)
# # #     pyautogui.click(loc)


# # directory = 'account_adding/button_icons/facebook'
# # # pause_for([f'{directory}/Next.png', f'{directory}/Next2.png'], 10)
# # pause_for([f'{directory}/Skip.png', f'{directory}/Next2.png'], 5)


# # def find_subimages(primary, subimage, confidence=0.60):
# #   primary_edges = cv2.Canny(primary, 32, 128, apertureSize=3)
# #   subimage_edges = cv2.Canny(subimage, 32,128, apertureSize=3)

# #   result = cv2.matchTemplate(primary_edges, subimage_edges, cv2.TM_CCOEFF_NORMED)
# #   (y, x) = np.unravel_index(result.argmax(),result.shape)

# #   result[result>=confidence]=1.0
# #   result[result<confidence]=0.0
  
# #   ccs = get_connected_components(result)
# #   y,x = correct_bounding_boxes(subimage, ccs)[0]
# #   return ((x[0]+x[1])/2, (y[0]+y[1])/2)

# # def cc_shape(component):
# #   x = component[1].start
# #   y = component[0].start
# #   w = component[1].stop-x
# #   h = component[0].stop-y
# #   return (x, y, w, h)

# # def correct_bounding_boxes(subimage, connected_components):
# #   (image_h, image_w)=subimage.shape[:2]
# #   corrected = []
# #   for cc in connected_components:
# #     (x, y, w, h) = cc_shape(cc)
# #     presumed_x = x+w/2
# #     presumed_y = y+h/2
# #     corrected.append(((presumed_y, presumed_y+image_h), (presumed_x, presumed_x+image_w)))
# #   return corrected

# # def get_connected_components(image):
# #   s = sp.morphology.generate_binary_structure(2,2)
# #   labels,n = sp.measurements.label(image)#,structure=s)
# #   objects = sp.measurements.find_objects(labels)
# #   return objects


# # # x,y = find_subimages(image, template)[0]
# # x = find_subimages(image, template)
# # print(x)
# # r = 2
# # pyautogui.click((x[0]/r, x[1]/r))
# # # print(((x[0]+x[1])/2, (y[0]+y[1])/2))


# # # def draw_bounding_boxes(img,connected_components,max_size=0,min_size=0,color=(0,0,255),line_size=2):
# # #   for component in connected_components:
# # #     if min_size > 0 and area_bb(component)**0.5<min_size: continue
# # #     if max_size > 0 and area_bb(component)**0.5>max_size: continue
# # #     (ys,xs)=component[:2]
# # #     cv2.rectangle(img,(xs.start,ys.start),(xs.stop,ys.stop),color,line_size)

# # # def save_output(infile, outfile, connected_components):
# # #   img = cv2.imread(infile)
# # #   draw_bounding_boxes(img, connected_components)
# # #   cv2.imwrite(outfile, img)

# # # def  find_subimages_from_files(primary_image_filename, subimage_filename, confidence):
# # #   '''
# # #   2d cross correlation we'll run requires only 2D images (that is color images
# # #   have an additional dimension holding parallel color channel info). So we 'flatten'
# # #   all images loaded at this time, in effect making them grayscale.
# # #   There is certainly a lot of info that will be lost in this process, so a better approach
# # #   (running separately on each channel and combining the cross correlations?) is probably
# # #   necessary.  
# # #   '''
# # #   primary = cv2.imread(primary_image_filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
# # #   subimage = cv2.imread(subimage_filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
# # #   return find_subimages(primary, subimage, confidence)


