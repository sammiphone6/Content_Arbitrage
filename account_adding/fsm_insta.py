import time
import datetime
from data import instas, infos, tiktok_account_data, instas_start, open_filedata, save_instas, save_filedata, save_updated_counters
from fsm import change_vpn, instagram

####################
# Make sure tempPFPs is the default folder
# Make sure Nord is set up to the right as needed (with France to US in view)
# Make sure no pages to the right of the safari/nord split page
# Make sure to record screen
####################

def insta_creation_script():
    results = dict()
    start = time.time()

    while instas_start < len(instas):
        country = change_vpn()
        print(country)

        insta = (instas['Default username'][instas_start], instas['Default password'][instas_start])
        instas['Country'][instas_start] = country
        save_instas()

        results[instas_start] = instagram(insta)
        print((insta), results[instas_start], country)
        instas['Result'][instas_start] = results[instas_start]
        save_instas()

        instas_start += 1
        save_updated_counters(instas_start=instas_start)
        print(datetime.datetime.fromtimestamp(int(time.time()-start)), '\n\n')
        print("Starting next one... (you could pause here)")

    print(time.time()-start)
    print(results)

insta_creation_script()