import requests
from data import open_filedata, instas, save_instas, save_filedata
import pprint

# prev_data = open_filedata('data/tiktok_accounts_data.txt')

# pp = pprint.PrettyPrinter(depth=6)
# print(len(prev_data))
# pp.pprint(prev_data['charlidamelio'])

counters = open_filedata('data/insta_creation_counters.txt')
print(counters)
# instas.drop(columns = ['Unnamed: 0','Unnamed: 0.1'], inplace=True)
print(instas)
save_instas()