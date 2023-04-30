# from igbot.instabot.api.api import API
# import secrets
# import datetime
# import base64
# import rsa
# from Crypto.PublicKey import RSA
# from Cryptodome.Cipher import AES

# def encrypt_password(password):
#     IG_LOGIN_ANDROID_PUBLIC_KEY = "LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUF1enRZOEZvUlRGRU9mK1RkTGlUdAplN3FIQXY1cmdBMmk5RkQ0YjgzZk1GK3hheW14b0xSdU5KTitRanJ3dnBuSm1LQ0QxNGd3K2w3TGQ0RHkvRHVFCkRiZlpKcmRRWkJIT3drS3RqdDdkNWlhZFdOSjdLczlBM0NNbzB5UktyZFBGU1dsS21lQVJsTlFrVXF0YkNmTzcKT2phY3ZYV2dJcGlqTkdJRVk4UkdzRWJWZmdxSmsrZzhuQWZiT0xjNmEwbTMxckJWZUJ6Z0hkYWExeFNKOGJHcQplbG4zbWh4WDU2cmpTOG5LZGk4MzRZSlNaV3VxUHZmWWUrbEV6Nk5laU1FMEo3dE80eWxmeWlPQ05ycnF3SnJnCjBXWTFEeDd4MHlZajdrN1NkUWVLVUVaZ3FjNUFuVitjNUQ2SjJTSTlGMnNoZWxGNWVvZjJOYkl2TmFNakpSRDgKb1FJREFRQUIKLS0tLS1FTkQgUFVCTElDIEtFWS0tLS0tCg=="
#     IG_LOGIN_ANDROID_PUBLIC_KEY_ID = 205

#     key = secrets.token_bytes(32)
#     iv = secrets.token_bytes(12)
#     # time = str(int(datetime.datetime.now().timestamp()))
#     time = '1682733447'

#     base64_decoded_device_public_key = base64.b64decode(
#         IG_LOGIN_ANDROID_PUBLIC_KEY.encode()
#     )

#     public_key = RSA.importKey(base64_decoded_device_public_key)

#     encrypted_aes_key = rsa.encrypt(key, public_key)

#     cipher = AES.new(key, AES.MODE_GCM, iv)
#     cipher.update(time.encode())
#     encrypted_password, tag = cipher.encrypt_and_digest(password.encode())

#     payload = (
#         b"\x01"
#         + str(IG_LOGIN_ANDROID_PUBLIC_KEY_ID).encode()
#         + iv
#         + b"0001"
#         + encrypted_aes_key
#         + tag
#         + encrypted_password
#     )

#     base64_encoded_payload = base64.b64encode(payload)

#     return f"#PWD_INSTAGRAM:4:{time}:{base64_encoded_payload.decode()}"

# def ig_login_request():
#     cookies = {
#         'dpr': '2',
#         'mid': 'ZExm6QAEAAG3RyZl6rrVmYDYlNzv',
#         'ig_did': 'A0448A4C-2E24-4F6B-8408-9C6372BA9202',
#         'ig_nrcb': '1',
#         'datr': '6GZMZNo4wJ6IqmFbyS9WAn2I',
#         'csrftoken': 'UtCMmCiqydgzZBR8KifCdujsgU1dvlsc',
#         'ds_user_id': '59341379259',
#         'rur': '"NAO\\05459341379259\\0541714268353:01f717d3c4ba2722b9074d71615cbd29c53c35d5e9c81bc3a11e41cae319ac8458a6fb3b"',
#     }

#     headers = {
#         'authority': 'www.instagram.com',
#         'accept': '*/*',
#         'accept-language': 'en-US,en;q=0.9',
#         'content-type': 'application/x-www-form-urlencoded',
#         # 'cookie': 'dpr=2; mid=ZExm6QAEAAG3RyZl6rrVmYDYlNzv; ig_did=A0448A4C-2E24-4F6B-8408-9C6372BA9202; ig_nrcb=1; datr=6GZMZNo4wJ6IqmFbyS9WAn2I; csrftoken=UtCMmCiqydgzZBR8KifCdujsgU1dvlsc; ds_user_id=59341379259; rur="NAO\\05459341379259\\0541714268353:01f717d3c4ba2722b9074d71615cbd29c53c35d5e9c81bc3a11e41cae319ac8458a6fb3b"',
#         'origin': 'https://www.instagram.com',
#         'referer': 'https://www.instagram.com/accounts/login/?next=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fonetap%2F%3Fnext%3D%252F%26__coig_login%3D1',
#         'sec-ch-prefers-color-scheme': 'light',
#         'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
#         'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.137", "Google Chrome";v="112.0.5615.137", "Not:A-Brand";v="99.0.0.0"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"macOS"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         # 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
#         'viewport-width': '1792',
#         'x-asbd-id': '198387',
#         'x-csrftoken': 'UtCMmCiqydgzZBR8KifCdujsgU1dvlsc',
#         'x-ig-app-id': '936619743392459',
#         'x-ig-www-claim': 'hmac.AR2YO6VDIeOp7b_M_Yk0IXDnUlUsCYvmoFDnF_KDxACqvTUy',
#         'x-instagram-ajax': '1007398833',
#         'x-requested-with': 'XMLHttpRequest',
#     }

#     data = {
#         # 'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1682733447:AfVQAKlgUR7yjwMZNrPNRKv+9xkH8Y3RMcKng3r81nQx4VcTUHLyRrbOCVXEwlsFbP6NEYs0PM90E6hKlNhaUheYfWeH9FA83hC6tGK0ve2mAhihkjFII20w2JQhpyoSKvBViCaDFmzmuPlMCu2e',
#         'enc_password': encrypt_password("i0Z5W5goo2G"),
#         'username': 'nancyandersonkbxcwktfqv',
#         'queryParams': '{"next":"https://www.instagram.com/accounts/onetap/?next=%2F&__coig_login=1"}',
#         'optIntoOneTap': 'false',
#         'trustedDeviceRecords': '{}',
#     }
    
#     response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)
#     return response

# print(ig_login_request().text)

# print()

# quit()
#
# proxy_nums = [20, 48, 49, 50, 58, 72, 77] #webshare
# # proxy = "http://12c99475-1105182:2krbs5ekyu@89.38.99.29:41612"
# def misc_other_stuff():

#     print(requests.get('https://ipinfo.io', proxies=proxys).text)
#     quit()

#     cookies = {
#         'NID': '511=hqTYurC3n63DLwAk-kmfy6Lg77Bj2NlxaYo8UkSIoFlPz44SPtLUtyG75gWEzTy3I4-4mfICICvT10c_jqgxtAkNyUiXUFyHDmiDvXGm-FcnHzKO9e45oINIJvNt7hsvR7n0Ei2728hYt1FHRwsoT9n6Se9YtnmTBS3-WUGlSQg',
#         '__Host-GAPS': '1:lK8QB_-emL7M_5VBEOPcf0Gn6VE2tg:41q7x8-sx2YRHRrj',
#     }

#     headers = {
#         'authority': 'accounts.google.com',
#         'accept': '*/*',
#         'accept-language': 'en-US,en;q=0.9',
#         'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
#         # 'cookie': 'NID=511=hqTYurC3n63DLwAk-kmfy6Lg77Bi2NlxaYo8UkSIoFlPz44SPtLUtyG75gWEzTy3I4-4mfICICvT10c_jqgxtAkNyUiXUFyHDmiDvXGm-FcnHzKO9e45oINIJvNt7hsvR7n0Ei2728hYt1FHRwsoT9n6Se9YtnmTBS3-WUGlSQg; __Host-GAPS=1:lK8QB_-emL7M_5VBEOPcf0Gn6VE2tg:41q7x8-sx2YRHRrj',
#         'google-accounts-xsrf': '1',
#         'origin': 'https://accounts.google.com',
#         'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp',
#         'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"macOS"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
#         'x-same-domain': '1',
#     }

#     params = {
#         'hl': 'en',
#         '_reqid': '307159',
#         'rt': 'j',
#     }

#     data = 'continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&f.req=%5B%22AEThLlzBaWRYKLiraseveCSgfrDQPV958U8xPZDLZG1SqryG8R0wd_NLdBUcaw00aK3mUFlaFuHzc6bCXkcN2qm_MyUn-eA7gvJkPSio7S3SkHInQ0bKyfKVyA5g-1v8eEJ9WCbcxV6_iKeWoMAsS_VWpZTPeiqGCYL0udMMORfed1p8493YdUW-If3CUo3v_aCOp3i6GAtPZTgVR-Bf-Cj0bhA1DN8Q-A%22%2C%22jacob%22%2C%22doerr%22%2C%22jacob%22%2C%22doerr%22%2C%22jacobdoerr342%22%2C%22Maxx%401234%22%2C%22jacobdoerr342%22%2Ctrue%2C1%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%5D&bgRequest=%5B%22web-glif-signup%22%2C%22%3CSIRqhNkCAAYnP6FbBz-NbXobPfbU0-v0ADkAIwj8RiHv8s2hlx81SdOoERknkC4Bq7GJH3_5-eXQnY-z3VoN8VF5YC_aUYzilsTdb0PFu0ASdQbNAAAB3Z0AAAADpwEHVgxf3_Ul_MHh3srYGAy10CIQkmuolc5n4uPXzG9BGRAgDS39_krqKlUdrYIgTcVM88Qy6GRyk8Rkc3Zo-hDu9ztZI7WsEC3KmE2vf-HsujIif0obU8zdJ1f-JQAqIubNDthUDGtnLv269UF5eMQYWZNTdEe892WsUPhvvpbxUcsZp0OL7OU0nL_MBBf0_xUoHTWEDuj1th84w2t8dm4FRtTSi4Qya8oEcw2QOyDKm7xGL8p73Y7JOIk7boGcIONOcL6vJE9KAl14CHoLAeanwQzNR5NBbW-joHKsgxZDUdGye4Wqj2fiDVsxqAHNdtpDG5PGE-mxOqrfkmKs4bbq4d22nmvMvFxgfEXxJp-AnWdYOIMP_GRJb2q5xWnAj3twewNP7ah_p1l0Ln5K8zG7c2uFgA5NUihC8Rxz7VnaQW8O62Q6CK8IOCD_XjvvYc5aXUY2cFhtu2OK2OMgd4GnhgeurG3RzrTg7kPDuboD3gkEVlZ5LSC5qKCkXzuDGCP3w4IAFgnnECBizq1MbiGnJ1ljb_6edZREOL3HDVfSGvx5Vjh5bxKs4bDXKFnujf28FfI5RuODIt8pBaxZmuHHLoeJAMfdNMLvJ_IVIirxJnbkWQ_eUN-rIn5F1Ls08lABqYVVNoogE9nY4B2ly9WwRJBbD1JTXYTexsqO2YYfTphwVGQ0V0K_jMZtEA4JZEoStyC2q4dzPpV3GW3oS_hE_Z8gea4Jbd3p5UGrGx6u6l0_5XF3NXci42Aez0INLNrF_gFeUhCJMj3XYYuTFWGKEVcplq3r-0vE8q7v6suwrP0_sanKv8jliX0sNE2OPBFPZNMlZmv2uQ-t9FxeTrVitZFdtwcI5X9_uBOns7Xy8ettl23PdHYkbj8HNG4_z8qga1MUSevLUacVvSmJj5HowXVhk7307kf5Ey3m_kbumUkZ-h4MHPbnjnE3cuwfXS5kYTVLTFcs-atH4iUmBjFfU9Seq_Kt6KpqEn3agG2lvIH5K3cCeLoaeBnD7JHeT4On1J1DC-bOj_ytbRUb4jIwQrEHcjv6WgHakA-1O9MFQ_S5Evp1dyMoKtpx3U6zSjeZuBik9f252N2Mr9AB8QaTsi6RqG9qKV3n7faLwILyuvuRXapdzu3Kh5zxbygDT-F-WIn1mBqIbII5O-qWbPtTK7PPgh7MwIUC0sujiP_kxANSaAclKsXR1M7R39wtlTUx27Z-nvhvijY_bbBgrCU3MNG30wl6HryLrVxlA5AI8Fx0YpOqd7bqfMr-lJmoHa960XZEnwiSsIxtOEDDgVaWjioNX7aY557qAH9y0hfJtLSPBw3qmdyYuPtzjpBOPuzm13pFaKqKAUBE5thN251dSX-3kigUwMMZ0bndv49VvflvfvO9cFabZGgrJ0H9c2p1zZtLo8ieai-e7tt3175pZuA6VvC5prpMfzpFYE2kX_5-7--pZwwLhnahGQGu74uLNZrN0Es-aEfxMqn5nYKU1nVgGJpUMPRJGnB2MeaDaXoWAy9bZNf786HVk4v7XG468-Ln2bHbc9S_W5YBDinLc0EHgG3-WN57N2FCBmE1eOSpZlgwE_YuXFhn688i8Rop3U71ExJpZVY_X7Tz4GdsE17vtmRs-op1zGAEj8LGGGDkVXAcwgT1h2hj49zRujTNP720UrYClPTaVe9GzytI2psO7p8V_WgOGgbjHvBX7nFHSRATMMP1-RsCxZBI4BD9C2BU_i_BoJ5BrPaT0mvFwNVUy7ByjkC_gMkml3hV8vWcmKhse_oDkOM9zevKD-asiTCFfr7nu3ETPgU2Uo9BYBT3gZ6B6hMQ6fCs2VpLGvI1wEKXorB-qcG8D9dajTuxkXLaI0ow8cyupV6v4dVVMhol_qX2QGSU2g1ZsM1ikVMcgRke3dA3BIjCi6KVFSN-BVnh9puT1N2nV0qacczHRQkMIHDiKs_oq4HtkVjLW3XNVrCIeAoT3PbfrCTgml2yJDayyZWHZ_01ntwWUXXfD0TVHyjWt9JTf790kJtk7W1PqFLIB_HDtuXvPn99wwcUvPgCXhqf0BlwjvPEy7hn3SGp7QzWKmj8_JBuwB8EfO01PGN-Ipu8NHj9WwBF8JUBDWBXIxUsCIldgtA_lCVBhOW5f0zT4ejAWiiIw8p8gpj2wC-kXXY7mSmRKcbas9aG5KiSlg4wIN5ZzgPRZdloetwg3z-Kic9_34GYf4Ter_K6ET9ME26nDLOeNK7tdMhfKfhbCppfcF0LSTHcOt2XpaTJNHVqrduKAAHoJQVLaqMO5mGpusDQkgAaEpX3rdkIw0SO6HizTQCCLf7pFro9G_bx5tU2TMm2QZ-gPaNVLN9IsXbbHhS7MBWy7Azm12uPRMhqcy3iFqXAjGHR1Pl11brSa-KsqMF3-pak8YSQClSNuoEqEbvy87xalx39N9-ubzLq_aQdY28RMwq93Cy_F_V2stPiiKc6KogP8X02i-NBmm6h58OlOer09yVhELU_SpUFq32l-mQNc_Rx0LFNvueqaFHn5SsUc_FinnuXyGg0xmLLhtlshtscnsF0hpejCIc8LSsfvqEF_Y_k1lnAFkWb8HlZwiRPOktYVKCyoqjIvsuSaIKhLAEavjcCsdix_1aYAu2FkN5K3M4AhAlDLSMbzznSrzhXrvshIffUpzb1n3d_bgXGOnTHLfdEZjD2IJ6CJdbMcaglR1S8TqqkXICa5UNenwweUrq7H2M1-Vr1UQHATzorxjH3pzU_Dz3XBFoKG8aGAteUD7M1m9xhdMuDoPao0ntelPOmnNO6SbbAksyeQlFlgrCIem2LywebSl-50fa0DT_lLyP0OtNv8tPmMn3p0M9cYF36XCAR2bUiAAw5DRAyXLe6QvRsFe2ImP1cOVeOh5AsGMXG0CRdtAbaABDOc6grBlPAyIBlut1YwocobbjOnkUPA9fJ62JiRE8MIQQ_ld_T9l4Rrck1WZPaDu8neTukYU8CSr-pPoFgOG_u7kSyo1G_TRG6IrA_LYs0NufhzBDFwPHw4w7IPIdhBfJ9AL0WZAkND8CV2zb4gj1f2sc2eYIceuio-gtd3rs6nhmdfCP4oO6S50SllT5RFoXCdnyYg04-pFFofR_-lgeHdjUljyqofqHP6z0xK63Ho6Y9m_P2ftitFXudvdORSHB3LGJJDJ_7ekYnMzljo0b1UQwKS6Lx2cJ7BFQp-PdHDqBDcUtmwP1RqmWa_vbGrHGc8xRC6Ygg3YYY5mFpixV-ED_Lam6lQp9YYnCML2u3-5ghOHLPcZ3mDua7J7uAUy8s1mLb7K4AAhyRxZCwIQXA00TMhaBWh5ZyF4phr3Sxn4UeC4sIMsCaD3-uR-grlfewG8T9NmvkORpV12sNjJIMlV5q-vSV8FVa40b_SipydBXbAHx3bn-cQ6TxfB3OJK01nFKTNNYLi6ZpjUdun-hDDCTFmIXGqoxQXvx_u87FOLs8UVK7RptaeKnZ8flENaG0_DxOFnnIIEcn5sByHJf-cGQJzghoFFhNVb1ggnlzLODMwcfvqLj2vXLdhUkrT0BGWwxDwB_kW9lZA07LXae1AHbpK5Bw_RbOulAqBf88sGF06OFK7Nbs99jjrOGsapX2pq6qZqF2NPnOXJ0qFOyrpTHdq9wZEnmtjCJEQJo4ihfAyq-gDL7UmlSL3qRy5n7l7K-_4RTL74_zn9ECPewkHhKcKtCtLrEaawz2T75_B-ndQQ_YFloGwnZbs2gUKBKwOJAkB84il66w3JF8m-Aqdr6touZq8xTJPaMpmUBWYCiXuxXUVlwyc0wcogQZ5wIY83QigLyIoDjof1JIKgVvNnSMjsfZ39AGBvGeek9tff5wV5t4XPFTh4as2IVyUpvMm51a45n4pfBmxFc1QXVJs4ndjpT5iXior28Xyf-YwM9VZobPfV3HQ7MqK6cfXP2uyBz8TFodNiSEvvz5DSHrQCgVLAgxzIVdtMaNAbj9MblI8FM3RluSF8DCZGgytIH4OJ52Ejta4wiGYyvbwk08Eyi4Alc4v5Dy27Z1p560A91rs2uEkBzpHgvkp0JEQFy-JAZ_4EJjdFWTNOHdCP3jC5i4xS3YxM0iiuCtJ3maYaE0cZEvWGq2G-T_TJpoMw_9fyxRTufERlFoIJXDAU4S82IqxtyUZ3NjfuUZvZBoExNag4rWZU37gH-Kqx8XnpOs3t_up_IPwy0PVHExYpimpd4lo8BqDYpDvG_6bv0%22%5D&azt=AFoagUVJTpbttl_q25MGHLa7gy-bO1STow%3A1682661525166&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22US%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cfalse%2C1%2C%22%22%2Cnull%2Cnull%2C1%5D&gmscoreversion=undefined&'

#     response = requests.post(
#         'https://accounts.google.com/_/signup/accountdetails',
#         params=params,
#         cookies=cookies,
#         headers=headers,
#         data=data,
#         # proxies=proxys
#     )

#     print(response.text)
#     quit()


#     # proxy = f"http://{data[2]}:{data[3]}@{data[0]}:{data[1]}"
#     proxy = "http://12c99475-1105182:2krbs5ekyu@89.38.99.29:41612"
#     proxy = {
#         'http': proxy,
#         'https': proxy
#     }

#     # data = {
#     #     "_csrftoken":
#     #     "".join(
#     #         random.choices(string.ascii_lowercase +
#     #                     string.ascii_uppercase + string.digits,
#     #                     k=32)),
#     #     "username":
#     #     'beyonceyy',
#     #     "guid":
#     #     uuid.uuid4(),
#     #     "device_id":
#     #     uuid.uuid4()
#     # }
#     # head = {
#     #     "user-agent":
#     #     f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"
#     # }

#     # print(proxy, requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head, data=data, proxies=proxy).text)
#     # quit()

#     for proxy in proxy_nums:
#         data = {
#             "_csrftoken":
#             "".join(
#                 random.choices(string.ascii_lowercase +
#                             string.ascii_uppercase + string.digits,
#                             k=32)),
#             "username":
#             'joellyy',
#             "guid":
#             uuid.uuid4(),
#             "device_id":
#             uuid.uuid4()
#         }
#         head = {
#             "user-agent":
#             f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"
#         }
#         print(proxy, requests.post("https://i.instagram.com/api/v1/accounts/send_password_reset/", headers=head, data=data, proxies=proxies(proxy)).text)
#     quit()

