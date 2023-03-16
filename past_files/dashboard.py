import pandas as pd
import matplotlib.pyplot as plt
from insights_sync import getUserInsights
from ig_defines import getCreds
from data import account_data_indiv, account_data_popular, exclude
import time

def plot_barchart(days = 30, log_scale = False):
    data = dict()
    accounts = [acc for acc in account_data_indiv.index] + [acc for acc in account_data_popular.index]
    for account in accounts[:14]+accounts[15:]+accounts[14:15]:
        params = getCreds(account) # get creds
        response = getUserInsights(params, days=days, metrics='impressions')
        for insight in response['json_data']['data'] : # loop over user account insights
            acc_data = dict()
            for value in insight['values'] : # loop over each value
                acc_data[value['end_time'][5:-14]] = int(value['value'])
        data[account] = acc_data
    
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    plt.xlabel("Date")
    plt.ylabel("Impressions")
    plt.xticks(fontsize=10, rotation = 90)
    if log_scale:
        ax.set_yscale("log")
    df.plot(kind='bar', stacked=True, legend=True, ax=ax)
    plt.show()    



# start = time.time()
# days = 30
# data = dict()
# accounts = [acc for acc in account_data_indiv.index] + [acc for acc in account_data_popular.index]
# for account in accounts[:14]+accounts[15:]+accounts[14:15]:
#     params = getCreds(account) # get creds
#     response = getUserInsights(params, days=days, metrics='impressions')
#     for insight in response['json_data']['data'] : # loop over user account insights
        
#         acc_data = dict()
#         # print ("\t" + insight['title'] + " (" + insight['period'] + "): " + str( insight['values'][0]['value'] )) # display info
#         for value in insight['values'] : # loop over each value
#             acc_data[value['end_time'][5:-14]] = int(value['value'])
#             # print ("\t\t" + value['end_time'] + ": " + str( value['value'] )) # print out counts for the date
#     data[account] = acc_data

# # x_total = []
# # y_total = [0]*days
# # for account in data:
# #     # create data
# #     x = []
# #     y = []
# #     i=0
# #     for key in data[account]:
# #         x.append(key)
# #         y.append(data[account][key])
# #     x_total = x
# #     y_total = [sum(e) for e in zip(y, y_total)]
    
# #     # plot lines
# #     plt.plot(x, y, label = f"{account}", scaley='log')
# # plt.plot(x_total, y_total, label = f"total", scaley='log')

# print(time.time()-start)
# df = pd.DataFrame(data)



# fig, ax = plt.subplots()
# plt.xlabel("Date")
# plt.ylabel("Impressions")
# plt.xticks(fontsize=10, rotation = 90)
# # ax.set_yscale("log")
# df.plot(kind='bar', stacked=True, legend=True, ax=ax)

# plt.show()    

# print(time.time()-start)