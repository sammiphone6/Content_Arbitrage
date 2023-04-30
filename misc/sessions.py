import requests
import time
from os import system
print('\033[1;36m THIS TOOL IS MADE BY Shanu INSTAGRAM @1x.ios')
username = 'arendateteiwl' #input('\033[1;34m[+] - Enter Your Username : ')
passowrd = 'W9UPw1Xt' #input('\033[1;35m[+] - Enter Your Password : ')
c ='https://www.instagram.com/accounts/login/ajax/'## The login link works only in tools and applications, it does not work in Web
head1 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-length': '319',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YrX_FwABAAFVRYLepbLqUSO9nyBK; ig_did=B86D9D0C-8059-4D38-AB32-62F66F91EB8A; ig_nrcb=1; shbid="6887\054479320179\0541687630562:01f72f17d27d1bf82c5011a7e21c360468f4e96ffc8c8d9bc8f3389196b275ab0b6d598c"; shbts="1656094562\054479320179\0541687630562:01f75b9e3dad31375f7599a21ee1e6b0b33b430c850ee605a7591dd83682126848a683cd"; dpr=3; datr=av-1Yj1HLbt2sRgtjJ2hIyTk; rur="ASH\054479320179\0541687707865:01f7969a9a044b6e5a39c124177ea698ce171408d797be83e4e94e6efc69642ea3b90ed9"; csrftoken=QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',#Very important cookies
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; JSN-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
        'viewport-width': '360',
        'x-asbd-id': '437806',
        'x-csrftoken': 'QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',
        'x-ig-app-id': '1217981644879628',
        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
        'x-instagram-ajax': '57ac339ce6f4',
        'x-requested-with': 'XMLHttpRequest'
    }
print(time.time())
tim = str(time.time()).split('.')[0]##Time today but in decimal places
print(tim)
# quit()
data1 = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{passowrd}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
    }
rq = requests.post(c,headers=head1,data=data1)
    
    
if ('"userId"') in rq.text:
	co = rq.cookies
	coo =co.get_dict()
	tok = coo['sessionid']#To extract tokens print(tok)
	system('clear')
	print(tok)
	exit()
	cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"
	system('clear')
	print(cookiee)
elif ('"checkpoint_required"') in rq.text:
	print('plz aprove login')#secure 
else:
	print('wrong password')#Wrong password or account