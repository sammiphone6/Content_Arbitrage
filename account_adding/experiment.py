import requests
# from data import open_filedata, instas, save_instas, save_filedata
import pprint
import pyautogui
import time

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
file = 'button_icons/incognito/incognito3.png'
# print(pause_for(file, 3))
time.sleep(4)
print(pyautogui.locateCenterOnScreen(image = file, confidence = 0.60))
