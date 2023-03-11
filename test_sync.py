from ig_post_functions import test_post
from multiprocessing import Process
from data import account_data_indiv
import time

def run_tests():
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
  runInParallel(*[func(account) for account in account_data_indiv.index])
  end = time.time()
  print(end-start)