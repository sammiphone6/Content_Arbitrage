import requests
import time
from account_adding.data import instas, tiktok_account_data

from bs4 import BeautifulSoup


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


