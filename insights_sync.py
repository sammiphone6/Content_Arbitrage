from ig_defines import getCreds, makeApiCall
from data import account_data_indiv, account_data_popular, exclude
from multiprocessing import Process, Manager
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import datetime
import random

def getUserMedia( params ) :
	""" Get users media
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['instagram_account_id'] + '/media' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def getMediaInsights( params ) :
	""" Get insights for a specific media id
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-media-id}/insights?metric={metric}

	Returns:
		object: data from the endpoint

	"""
	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['metric'] = params['metric'] # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + params['latest_media_id'] + '/insights' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def getUserInsights( params , days=2, metrics = 'follower_count,impressions,profile_views,reach') :
	""" Get insights for a users account
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['metric'] = metrics # fields to get back
	endpointParams['period'] = 'day' # period
	endpointParams['access_token'] = params['access_token'] # access token
    
	# days = 2 #2 is default, max is 30
	t = int(time.time()) #this is default
	endpointParams['since'] = t-60*60*24*days
	endpointParams['until'] = t

	url = params['endpoint_base'] + params['instagram_account_id'] + '/insights' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def sample(account):
    params = getCreds(account) # get creds
    response = getUserMedia( params ) # get users media from the api

    print ("\n---- LATEST POST -----\n") # section header
    print ("\tLink to post:") # link to post
    print ("\t" + response['json_data']['data'][0]['permalink']) # link to post
    print ("\n\tPost caption:") # post caption
    print ("\t" + response['json_data']['data'][0]['caption']) # post caption
    print ("\n\tMedia Type:") # type of media
    print ("\t" + response['json_data']['data'][0]['media_type']) # type of media
    print ("\n\tPosted at:") # when it was posted
    print ("\t" + response['json_data']['data'][0]['timestamp']) # when it was posted

    params['latest_media_id'] = response['json_data']['data'][0]['id'] # store latest post id

    if 'VIDEO' == response['json_data']['data'][0]['media_type'] : # media is a video
        params['metric'] = 'reach,saved' #'engagement,impressions,reach,saved,video_views'
    else : # media is an image
        params['metric'] = 'engagement,impressions,reach,saved'

    response = getMediaInsights( params ) # get insights for a specific media id
    print ("\n---- LATEST POST INSIGHTS -----\n") # section header

    for insight in response['json_data']['data'] : # loop over post insights
        print ("\t" + insight['title'] + " (" + insight['period'] + "): " + str( insight['values'][0]['value'] )) # display info

    # ### NEW THING TO TEST ###
    # params['since'] = 1678934165-60*60*24*4
    # params['until'] = 1678934165
    # ### NEW THING TO TEST ###
    response = getUserInsights( params ) # get insights for a user
    # print('response', response['json_data_pretty'])
    print ("\n---- DAILY USER ACCOUNT INSIGHTS -----\n") # section header

    for insight in response['json_data']['data'] : # loop over user account insights
        print ("\t" + insight['title'] + " (" + insight['period'] + "): " + str( insight['values'][0]['value'] )) # display info

        for value in insight['values'] : # loop over each value
            print ("\t\t" + value['end_time'] + ": " + str( value['value'] )) # print out counts for the date

def impressions():
    df = pd.DataFrame()
    col_metric = 0
    edit = True

    for account in responses:
        
        response = responses[account]
        new_row = {'account': account}
        for insight in response[0]['json_data']['data'] : # loop over user account insights
            heading = insight['title'] + " (" + insight['values'][0]['end_time'][:10] + ")"
            new_row[heading] = insight['values'][1]['value']
            if edit:
                col_metric = insight['title'] + " (" + insight['values'][0]['end_time'][:10] + ")"
                edit = False
        
        num_posts = len(response[1]['json_data']['data'])
        new_row['Total Posts'] = '25+' if num_posts >= 25 else num_posts
        
        if(df.empty):
            for key in new_row:
                new_row[key] = [new_row[key]]
            df = pd.DataFrame(new_row)
        else:
            df = df.append(new_row, ignore_index = True)
    
    return df.sort_values(by=[col_metric], ascending = False).reset_index(drop = True)


# ## This function is shit, probably trash it
# def time_adjusted_impressions():
#     df = pd.DataFrame()
    
#     t_start = 0
#     t_end = 0
#     t_frame = 0
#     col_metric = 0
#     edit = True

#     timerow = {'account': 'timestamp'}
#     timestamp = time.time()
#     for account in account_data_indiv:
#         params = getCreds(account) # get creds
#         response = getUserInsights( params ) # get insights for a user

#         new_row = {'account': account}
#         for insight in response['json_data']['data'] : # loop over user account insights
#             if edit:
#                 t_start = str(datetime.datetime.fromtimestamp(int(response['json_data']['paging']['next'][-27:-17])))
#                 t_end = str(datetime.datetime.fromtimestamp(int(response['json_data']['paging']['next'][-10:])))
#                 t_frame = " (" + t_start + " - " + t_end + ")"
#                 col_metric = insight['title'] + t_frame
#                 timerow[col_metric] = timestamp
#                 edit = False
#             print(response['json_data']['paging']['next'][-10:])
#             new_row[col_metric] = insight['values'][1]['value']
        
#         response = getUserMedia( params ) # get users media from the api
#         num_posts = len(response['json_data']['data'])
#         new_row['Total Posts'] = '25+' if num_posts >= 25 else num_posts

#         if(df.empty):
#              for key in new_row:
#                   new_row[key] = [new_row[key]]
#              df = pd.DataFrame(new_row)
#         else:
#              df = df.append(new_row, ignore_index = True)
    
#     timerow['Total Posts'] = timestamp
#     df = df.append(timerow, ignore_index = True)
#     return df.sort_values(by=[col_metric], ascending = False).reset_index(drop = True)


## Helper functions for updating data
def update_saved_insights(stats, new = False):
    file_location = 'data/insights.csv'
    if new:
         stats.to_csv(file_location)
    else:
        saved_insights = pd.read_csv(file_location)
        updated_insights = pd.concat([saved_insights.set_index('account'), stats.set_index('account')], axis=1)
        updated_insights.to_csv(file_location)

def add_timestamp_row(stats):
    timestamp = int(time.time())
    stats.loc[len(stats.index)] = ['timestamp'] + [timestamp]*(stats.shape[1]-1) 
    return stats


## Sync here (also some edits in impressions())
responses = dict()
def get_insights():
    def compute(responses, account):
        params = getCreds(account)
        responses[account] = (getUserInsights(params), getUserMedia(params))
    
    accounts = [acc for acc in account_data_indiv.index if acc not in exclude] + [acc for acc in account_data_popular.index if acc not in exclude]
    def runInParallel():
        with Manager() as manager:
            m_resps = manager.dict()
            proc = []
            for account in accounts:
                p = Process(target=compute, args=(m_resps, account))
                proc.append(p)
                p.start()
            for p in proc:
                p.join()
            responses.update(m_resps)

    start = time.time()
    runInParallel()

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    
    stats = impressions()
    print(stats, "\n")
    print(stats.sum()[1:], "\n")

    stats = add_timestamp_row(stats)
    update_saved_insights(stats, new = False)

    end = time.time()
    print(end-start, "\n")

data_responses = dict()
def plot_barchart(days = 30, log_scale = False, cumulative = False):
    def compute(data_responses, account):
        params = getCreds(account) # get creds
        response = getUserInsights(params, days=days, metrics='impressions')
        acc_data = dict()
        for insight in response['json_data']['data'] : # loop over user account insights 
            for value in insight['values'] : # loop over each value
                acc_data[value['end_time'][5:-14]] = int(value['value'])
        data_responses[account] = acc_data
    
    accounts = [acc for acc in account_data_indiv.index if acc not in exclude] + [acc for acc in account_data_popular.index if acc not in exclude]
    accounts = accounts[:14] + accounts[15:] + accounts[14:15]
    random.shuffle(accounts)
    def runInParallel():
        with Manager() as manager:
            m_resps = manager.dict()
            proc = []
            for account in accounts:
                p = Process(target=compute, args=(m_resps, account))
                proc.append(p)
                p.start()
            for p in proc:
                p.join()
            data_responses.update(m_resps)

    start = time.time()
    runInParallel()
    
    df = pd.DataFrame(data_responses)
    print(df.sum().sort_values())
    print('Total: ', df.sum().sum())
    fig, ax = plt.subplots()

    if log_scale:
        ax.set_yscale("log")

    end = time.time()
    print(end-start, "\n")

    if cumulative:
        df.sum().sort_values().plot(kind='bar', ax=ax)
        plt.xticks(fontsize=7, rotation = 90)
        plt.xlabel("Accounts", fontsize = 20)
        plt.ylabel(f"Impressions over last {days} days", fontsize = 17)
    else:
        df.plot(kind='bar', stacked=True, legend=True, ax=ax)
        plt.xlabel("Date", fontsize = 20)
        plt.ylabel("Daily Impressions", fontsize = 20)

    plt.savefig(f'dashboards/rrob gone {days}days, log {log_scale}, cumu {cumulative}.png')



# get_insights()
# plot_barchart()

# sample('cute cats')



# import pprint
# def print_inventory(dct):
#     print("Items held:")
#     for item, amount in dct.items():  # dct.iteritems() in Python 2
#         pp = pprint.PrettyPrinter(depth=6)
#         pp.pprint("{} ({})".format(item, amount))

# print_inventory(getUserInsights(getCreds('faithordway7')))

# print(f'{account} insight: ', insight)