from account_adding.fsm_functions import facebook_pairing_script, insta_creation_script
from multiprocessing import Process

def runInParallel(*fns):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()

def update():
    ##TODO
    pass

####################
# FOR INSTAS: Make sure tempPFPs is the default folder
# FOR BOTH: Make sure Nord is set up to the right as needed (with France to US in view)
# FOR BOTH: Make sure no pages to the right of the safari/nord split page
# FOR BOTH: Make sure to record screen
####################


types = [
    # 'insta',
    # 'facebook',
]

if 'insta' in types:
    insta_creation_script()


if 'facebook' in types: 
    runInParallel(facebook_pairing_script(), update())