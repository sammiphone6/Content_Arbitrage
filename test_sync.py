from ig_post_functions import test_post
from multiprocessing import Process
from data import account_data_indiv, account_data_popular, exclude
import time

def run_tests(deep_test = False):
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
        return test_post(account, deep_test)
    return test


  start = time.time()
  accounts = [acc for acc in account_data_indiv.index if acc not in exclude] + [acc for acc in account_data_popular.index if acc not in exclude]
  runInParallel(*[func(account) for account in accounts])
  end = time.time()
  print(end-start)