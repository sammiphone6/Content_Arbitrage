from ig_post_functions import update_and_post_indiv, post_popular
from misc_functions import announce_pause
from multiprocessing import Process
from data import account_data_indiv, account_data_popular
import time

def sync_posts(time_spacing):
  def runInParallel(*fns):
    proc = []
    for fn in fns:
      p = Process(target=fn)
      p.start()
      announce_pause(time_spacing)
      proc.append(p)
    for p in proc:
      p.join()

  def func(account):
    def post():
        if account in account_data_indiv.index:
            return update_and_post_indiv(account)
        if account in account_data_popular.index:
            return post_popular(account)
    return post


  start = time.time()
  accounts = [acc for acc in account_data_indiv.index] + [acc for acc in account_data_popular.index]
  runInParallel(*[func(account) for account in accounts])
  end = time.time()
  print(end-start)

sync_posts(4)
### FOR SOME REASON LAST_POSTED ISN"T SAVING AFTER INCREMENTING DUE TO THE MULTIPROCESSING ###