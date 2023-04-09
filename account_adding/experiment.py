import requests
from account_adding.data import open_filedata, instas, infos, save_instas, save_filedata
import pprint
import pyautogui
import time
import pandas.io.clipboard as pic

# prev_data = open_filedata('data/tiktok_accounts_data.txt')
# print([acc for acc in prev_data])
# x = ['hannahstocking', 'hoopsnation', 'bilalahy', 'noahschnapp', 'mattiapolibio', 'enochtrue', 'wewearcute', 'itspierreboo', 'rosssmith', 'pudgywoke', 'itsjojosiwa', 'ondreazlopez', 'coupleontour', 'keniaos', 'jackson_krecioch', 'brefran77', 'joealbanese', 'tanamongeaulol', 'carterpcs', 'lala_sadii', 'dameliofamilyofficial', 'marrkadams', 'swagboyq', 'tommyunold', 'mackenzieziegler', 'sophiat24', 'michellebellexo', 'willywonkatiktok', 'baileyspinn', 'dylanmulvaney', 'charlidamelio', 'irisferrari', 'just_dt', 'hope_schwing', 'solcarlosofficial', 'jacobsartorius', 'brandonspam_', 'miafaithe', 'ironsanctuary', 'lilpapiclowngirl', 'thehypehouse', 'mckenzibrooke', 'dannyphantom.exe', 'itzshauni', 'jamescharles', 'mahoganylox', 'sarati', 'megnutt02', 'lexibrookerivera', 'zeth', 'iamjonathanpeter', 'jadensprinz', '4kidscallmedad', 'katstickler', 'ramizeinn', 'wren.eleanor', 'spicyycam_', 'daquan', 'arii', 'majno', 'rileyhubatka', 'undos', 'markellwashington1', 'quenblackwell', 'thatlittlepuff', 'baderalsafar', 'trippybryce', 'letwins', 'lizzo', 'its.bellido', 'youneszarou', 'sweetyhigh', 'hollyh', 'derkslurp', 'marlucas18', 'jimmydarts', 'dani_itss', 'klrdubs', 'kylethomas', 'krissimalloy', 'donaldducc', 'garett__nolan', 'nadyaokamoto', 'elliezeiler', 'nathantriska', 'itsari.aleise', 'jostasy', 'chris', 'officialsalicerose', 'lourdasprec', 'marcusolin', 'nfl', 'ayesebastien', 'lelepons', 'straw_hat_goofy', 'tooturnttony', 'noeneubanks', 'bellapoarch', 'noahglenncarter', 'jesseunderhill', 'yeahimcaroline', 'willsmith', 'olivermoy', 'duncanyounot', 'shangerdanger', 'wh0.nia', 'therealtati', 'alyssamckayyy', 'iamoliviaponton', 'davidjustinn', 'misocolorful', 'peytoncoffee', 'kurlyheadmarr', 'nickandsienna', 'fyp', 'sherinicolee', 'marionovembre', 'psg', 'wizqueifa_', 'nate_wyatt', 'joerauth_', 'kimandnorth', 'blesiv', 'caintrent', 'baidaugh', 'payton', 'liamsilk', 'siennamae', 'bbygshaii', 'antoniolievano', 'cristiandennis', 'paulinat', 'nmillz1', 'akamztwenty20', 'kessel_nathan_official', 'lgndfrvr', 'mrbeast', 'adamw', 'zoelaverne', 'marta.losito', 'billyvsco', 'wifiloo_m', 'newt', 'the_mannii', 'nabela', 'arianalee99', 'marvinlaqueen', 'hannahrylee', 'juliathekindafunnyperson', 'imgriffinjohnson', 'datrie', 'auditydraws', 'zacklugo', 'yakiemsgreenscreen', 'nickaufmann', 'devvyyy_', 'itsmenicksmithy', 'thebentist', 'calebcoffee', 'brookeashleyhall', 'rhia.official', 'lucianospinelli', 'kingbach', 'justmaiko', 'baby_simba47', 'matt_and_abby', 'mr.prada47', 'andreswilley', 'tania.rodri23', 'annacatify', 'thefurrhafamily', 'samanthayve', 'jordan_the_stallion8', 'haileeandkendra', 'carew_ellington', 'annabananaxdddd', 'luvanthony', 'itsselmo', 'tabithaswatosh', 'austinsprinz', 'charlyjordan', 'beasteater', 'gnb.official', 'erikatitus', 'vhackerr', 'huddy', 'gabby_murrayy', 'aarondoh', 'elongatedmusk', 'vctorperezz', 'maverickbaker', 'los_chicaneros', 'moontellthat', 'lorengray', 'skyandtami', 'laurimfgarciaa', 'primevideo', 'drewafualo', 'addisonre', 'xinnixinnita5', 'pepperonimuffin', 'stokestwins', 'real.ona', 'hotspanishmx', 'everett', 'ideatimes', 'twinmelody', 'abrameng', 'jettsetfarmhouse', 'isseypovs', 'abbieherbert', 'mamalindy', 'emiirbayrak', 'lisaandlena', 'iamjordiofficial', 'dobretwins', 'ayaatanjali_', 'icycol', 'anxietycouple', 'notcoratilley', 'thebrandonrobert', 'ash.e.e', 'itskingchris', 'miantwins', 'mndiaye_97', 'rebeccazamolo', 'snerixx', 'mikaylanogueira', 'charlieputh', 'overtime', 'therealhammytv', 'jaydenbartels', 'joe.bartolozzi', 'leanadeeb', 'lilyxgarcia', 'partyshirt', 'garyvee', 'foodies']
# save_filedata('data/infos.txt', x)
# pp = pprint.PrettyPrinter(depth=6)
# print(len(prev_data))
# pp.pprint(prev_data['charlidamelio'])

# counters = open_filedata('data/insta_creation_counters.txt')
# print(counters)
# # instas.drop(columns = ['Unnamed: 0','Unnamed: 0.1'], inplace=True)
# print(instas)
# # instas.loc[lambda df: df['Default username'] == 'susan8hernandezlsk', 'Country']
# save_instas()

# print(pause_for('button_icons/Nord/Sweden.png'),3)
# file = 'button_icons/incognito/incognito3.png'
# # print(pause_for(file, 3))
# time.sleep(4)
# print(pyautogui.locateCenterOnScreen(image = file, confidence = 0.60))

# pic.clipboard_set('gerer')
# print(pic.clipboard_get())

# print(len(infos))

def speed_up(web_hosted_tt_link, speed):
    # 0.5 < speed < 2

    response1 = requests.get('https://ezgif.com/video-speed?url='+web_hosted_tt_link)
    text1 = response1.text

    link1 = text1.split('.mp4')[0].split("\"")[-1]+'.mp4'

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

    link2 = "im" + text2.split('.mp4')[0].split("src=\"//im")[-1]+'.mp4'
    return link2

# this link is missing though
tt_link = "https://v19.tiktokcdn-us.com/739320ac7d3f2046c90592277527dbc1/642a4a46/video/tos/useast5/tos-useast5-ve-0068c003-tx/2a448767afc042d584af3bd35e017ff3/?a=1233&ch=0&cr=0&dr=0&cd=0%7C0%7C0%7C0&cv=1&br=3590&bt=1795&cs=0&ds=6&ft=kJrRfy7oZ-10PD1Kf05Xg9wdbNJ5vEeC~&mime_type=video_mp4&qs=0&rc=NjxoOGRpZDs7O2g2ZWc3NUBpajNtczM6ZnNvaTMzZzczNEBjMC4uXmItNS8xMV8uY15gYSNrazJhcjQwLmNgLS1kMS9zcw%3D%3D&l=2023040221384107E48AB50AF470FE7DDE"
speed = 1.16
# print(speed_up(tt_link, speed))

account_data = open_filedata('data/tiktok_accounts_data.txt')
print(sorted([account_data[tt]['tt_posting_rate'] for tt in account_data]))

threshold = 100
print(len([account_data[tt]['tt_posting_rate'] for tt in account_data if account_data[tt]['tt_posting_rate'] < threshold]))
print(len(account_data))
