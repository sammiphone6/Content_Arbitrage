import asyncio
import time
import pickle
from ig_post_functions import test_post
from misc_functions import open_filedata, get_account_data_indiv
from multiprocessing import Process

accounts = get_account_data_indiv()

async def request(code):

    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://www.hyatt.com/shop/rates/{hotel}', params=params, cookies=cookies, headers=headers) as resp:
            return await resp.text()

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

def func(account):
   def test():
      return test_post(account)
   return test

start = time.time()

runInParallel(*[func(account) for account in accounts.index])

end = time.time()
print(end-start)