import requests
from data import open_filedata, instas, save_instas, save_filedata
import pprint

prev_data = open_filedata('data/tiktok_accounts_data.txt')

pp = pprint.PrettyPrinter(depth=6)
print(len(prev_data))
# pp.pprint(prev_data['charlidamelio'])