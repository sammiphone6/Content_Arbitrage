import requests
from account_posting.ig_defines import getCreds, makeApiCall, proxies
from account_posting.data import account_data_indiv, account_data_popular, exclude, fb_app_data
from multiprocessing import Process, Manager
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import datetime
import random

def getUserMedia( params, proxy ) :
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

	return makeApiCall( url, endpointParams, params['debug'], proxy ) # make the api call

def getMediaInsights( params, proxy ) :
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

	return makeApiCall( url, endpointParams, params['debug'], proxy ) # make the api call

def getUserInsights( params , days=2, metrics = 'impressions,follower_count,profile_views,reach', proxy = None) :
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

	return makeApiCall( url, endpointParams, params['debug'], proxy ) # make the api call

def sample(account):
    params = getCreds(account) # get creds
    proxy = params['proxy']
    response = getUserMedia( params, proxy ) # get users media from the api

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

    response = getMediaInsights( params, proxy ) # get insights for a specific media id
    print ("\n---- LATEST POST INSIGHTS -----\n") # section header

    for insight in response['json_data']['data'] : # loop over post insights
        print ("\t" + insight['title'] + " (" + insight['period'] + "): " + str( insight['values'][0]['value'] )) # display info

    # ### NEW THING TO TEST ###
    # params['since'] = 1678934165-60*60*24*4
    # params['until'] = 1678934165
    # ### NEW THING TO TEST ###
    response = getUserInsights( params, proxy = proxy ) # get insights for a user
    # print('response', response['json_data_pretty'])
    print ("\n---- DAILY USER ACCOUNT INSIGHTS -----\n") # section header

    for insight in response['json_data']['data'] : # loop over user account insights
        print ("\t" + insight['title'] + " (" + insight['period'] + "): " + str( insight['values'][0]['value'] )) # display info

        for value in insight['values'] : # loop over each value
            print ("\t\t" + value['end_time'] + ": " + str( value['value'] )) # print out counts for the date

def impressions(responses, sort = 'impressions'):
    df = pd.DataFrame()
    col_metric = 0
    edit = True

    for account in responses:
        
        response = responses[account]
        new_row = {'account': account}
        for insight in response[0]['json_data']['data']: # loop over user account insights
            if 'Follower' not in insight['title']:
                heading = insight['title'].title() + " (" + insight['values'][0]['end_time'][:10] + ")"
                new_row[heading] = insight['values'][1]['value']
                if edit:
                    title = 'Total Followers' if sort == 'followers' else 'Impressions'
                    col_metric = title + " (" + insight['values'][0]['end_time'][:10] + ")"
                    edit = False
        
        # num_posts = len(response[1]['json_data']['data'])
        # new_row['Posts'] = '25+' if num_posts >= 25 else num_posts
        heading = " (" + insight['values'][0]['end_time'][:10] + ")"
        new_row['Total Followers' + heading] = response[2]
        new_row['Total Posts' + heading] = response[3]
        
        if(df.empty):
            for key in new_row:
                new_row[key] = [new_row[key]]
            df = pd.DataFrame(new_row)
        else:
            df = pd.concat([df, pd.DataFrame.from_records([new_row])], ignore_index=True)
            # df = df.append(new_row, ignore_index = True)
    
    return df.sort_values(by=[col_metric], ascending = False).reset_index(drop = True)

def get_followers_and_posts(account, proxy):
    cookies = {
        'mid': 'ZBXtIQAEAAGWpHSR7XGgpHbOs4gD',
        'ig_did': '0CB4A17E-64F5-441F-9167-0E9F4EB88F5C',
        'ig_nrcb': '1',
        'datr': 'IO0VZE0tGLIAMSNFMq-HKUM1',
        'fbm_124024574287414': 'base_domain=.instagram.com',
        'ds_user_id': '58603175168',
        'csrftoken': 'f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0',
        'shbid': '"12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"',
        'shbts': '"1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"',
        'dpr': '2',
        'sessionid': '58603175168%3Asv2ODVlrx539vv%3A27%3AAYd7UnsXFyCst52BOa6fpnchAXo6OW1ya_p0QdwUUA',
        'fbsr_124024574287414': 'crEYG5YAgt_Y9gdsbNfr1lPXb4nLsN7cjfGX9Q14_zA.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ1Voc3RDem1uM2tyQkQwWmM2VHFHUUlNWFROS3ljcGhLVHZSaUQwYWZnR0NWUGVlYk1kVGpYbFVVTHZVVzdINGtwdEo5VDhUNWM3SmhKSEZ2Y21zTUo5eHFFTy1sc3hVaGxsRnVMdDZuaEVPQjlXX2hMbTZGaXZzeE5USDJPVkI5MnRzenY3cmRacThlaUdUVnJXT293SF9MdEROSzJlR0lScHZJODNBMXJnSmVZa3haSU1kZ0tZNmY0cUwzMThBSDc0eGhUMjF5M2tESlJQWnZSQmJ3UjQtaHo3aFhkRS1yM28zVmowSnVYcnlyNXZMVTM5TDUyc0lJUW15VWI4bU93QjdZbVF2Q09ZZnpEU3F6OFFwMFVfUTc5QmpndVZpWnFLaHNMLUFnWFQ0d0pmQU5TRlRTNWtFRV9NcmZLbElfUDFkR0g3eVB2ODh4LUlxZk5MT09LIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU0zWkF2VG9DZnk2SGhScUR2MUZxZFRzV1JjcVZZZEt1TGxaQzQ2ODRlclQ1OFBVM052c1BVUzlEbWp0ZFpDRERuRUZiMUZURTl2VGdDVGhnSnhCa0xRWkJRem1saFM0eURLU0puWkFmNVl1NnVBeHF6cWtKVEhEeGxGaG9TQzJPT2t0RmR1NFNzbVpDRDAxY2tGdFBycWZ4Z2JiNlpDcGwySmttTU5XR2NCMzRpajhJSzJZTW9aRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODIzMjE1fQ',
        'fbsr_124024574287414': '6ZublH1s5pkhChnmCTwv9xqu2fR_z3y78RACM96fcfA.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRG9YMFhHbHpLSmhXLWF2V21QNlMzVm5qb3FiV0tSQlBSekkzb3hEYm9SMy1tV0N6TEJLOHJPY0ZZeE90M296NzFZVEp5SmVOUmljUnF4X2JCZTItTEFNWERlQWRPUUh4WHF0SnZuZDB5cWpqVVhBa1V4WlRLN0hMS21oX0tHemc4ZDBpbFduU3lkWkczYnFYeVhzcXRwelgyMUt6NGFuLU1xSVRTRHhRUW9nREpOSkpmVVhpYXJvcDZvaE4wVGFzanVPYTVzdDhOaFRvUkt6UkY4cjNvQ25QRldfTXZzbGpKczVwQ1d0alhqQmxGUGZwTXJQczdFLU43a21Vbnh3Q0x6MnZxWm52NkRkMzBhMVMyeGhhV1E3NVlPSnFsMm5IcGpUQmFnODV4OEo2Uk11bzFYYTBuSjlpeGY0dnEzTW8xWlBjMlFKdWhWejVDeE9NeS0zU0wzIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUc4S1dCZTVGRGhVQ1pCYVF0blZ2eUlBWEpvcEd6OFpCUTNpOHkxS3o4WFFaQWhmbnByWUFYakN6akd3U1ZGOFJrVHNzRjFVMk9ZYUYwdmlPOEZoN2RGUFF0dllKR1BvdmI1MTBLcHA1TzFXWVVaQWZHTDh5dGVuNHJUUnBoY3FMSkQ2dGk4TlgzVWhmQjdqTXF6UmNNQURYRGV0bElmRUp5cEMzTktxWkNaQm1GWkM1VEFnQkVaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODI0NDUyfQ',
        'rur': '"VLL\\05458603175168\\0541714360453:01f76efb0767a635b4159bbd9fac331b2cdc56cc434ac784de4b05f0ff3e0e4c9cbe22f0"',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'mid=ZBXtIQAEAAGWpHSR7XGgpHbOs4gD; ig_did=0CB4A17E-64F5-441F-9167-0E9F4EB88F5C; ig_nrcb=1; datr=IO0VZE0tGLIAMSNFMq-HKUM1; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=58603175168; csrftoken=f1pHOXaoNlkyDBnWb3Qny7wjfpNIxmR0; shbid="12360\\05458603175168\\0541714351046:01f7506e1801a5fa2a0effcc20b7d3a05ce7a12d21e1b9ab11e35c5e29c492f1280703a1"; shbts="1682815046\\05458603175168\\0541714351046:01f7901ec35e9a41be3096eb73be2785099a7d2517ba0c438923a01b5a966c98623babe2"; dpr=2; sessionid=58603175168%3Asv2ODVlrx539vv%3A27%3AAYd7UnsXFyCst52BOa6fpnchAXo6OW1ya_p0QdwUUA; fbsr_124024574287414=crEYG5YAgt_Y9gdsbNfr1lPXb4nLsN7cjfGX9Q14_zA.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRQ1Voc3RDem1uM2tyQkQwWmM2VHFHUUlNWFROS3ljcGhLVHZSaUQwYWZnR0NWUGVlYk1kVGpYbFVVTHZVVzdINGtwdEo5VDhUNWM3SmhKSEZ2Y21zTUo5eHFFTy1sc3hVaGxsRnVMdDZuaEVPQjlXX2hMbTZGaXZzeE5USDJPVkI5MnRzenY3cmRacThlaUdUVnJXT293SF9MdEROSzJlR0lScHZJODNBMXJnSmVZa3haSU1kZ0tZNmY0cUwzMThBSDc0eGhUMjF5M2tESlJQWnZSQmJ3UjQtaHo3aFhkRS1yM28zVmowSnVYcnlyNXZMVTM5TDUyc0lJUW15VWI4bU93QjdZbVF2Q09ZZnpEU3F6OFFwMFVfUTc5QmpndVZpWnFLaHNMLUFnWFQ0d0pmQU5TRlRTNWtFRV9NcmZLbElfUDFkR0g3eVB2ODh4LUlxZk5MT09LIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQU0zWkF2VG9DZnk2SGhScUR2MUZxZFRzV1JjcVZZZEt1TGxaQzQ2ODRlclQ1OFBVM052c1BVUzlEbWp0ZFpDRERuRUZiMUZURTl2VGdDVGhnSnhCa0xRWkJRem1saFM0eURLU0puWkFmNVl1NnVBeHF6cWtKVEhEeGxGaG9TQzJPT2t0RmR1NFNzbVpDRDAxY2tGdFBycWZ4Z2JiNlpDcGwySmttTU5XR2NCMzRpajhJSzJZTW9aRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODIzMjE1fQ; fbsr_124024574287414=6ZublH1s5pkhChnmCTwv9xqu2fR_z3y78RACM96fcfA.eyJ1c2VyX2lkIjoiMTAwMDkwMDI0ODE4MzYxIiwiY29kZSI6IkFRRG9YMFhHbHpLSmhXLWF2V21QNlMzVm5qb3FiV0tSQlBSekkzb3hEYm9SMy1tV0N6TEJLOHJPY0ZZeE90M296NzFZVEp5SmVOUmljUnF4X2JCZTItTEFNWERlQWRPUUh4WHF0SnZuZDB5cWpqVVhBa1V4WlRLN0hMS21oX0tHemc4ZDBpbFduU3lkWkczYnFYeVhzcXRwelgyMUt6NGFuLU1xSVRTRHhRUW9nREpOSkpmVVhpYXJvcDZvaE4wVGFzanVPYTVzdDhOaFRvUkt6UkY4cjNvQ25QRldfTXZzbGpKczVwQ1d0alhqQmxGUGZwTXJQczdFLU43a21Vbnh3Q0x6MnZxWm52NkRkMzBhMVMyeGhhV1E3NVlPSnFsMm5IcGpUQmFnODV4OEo2Uk11bzFYYTBuSjlpeGY0dnEzTW8xWlBjMlFKdWhWejVDeE9NeS0zU0wzIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUc4S1dCZTVGRGhVQ1pCYVF0blZ2eUlBWEpvcEd6OFpCUTNpOHkxS3o4WFFaQWhmbnByWUFYakN6akd3U1ZGOFJrVHNzRjFVMk9ZYUYwdmlPOEZoN2RGUFF0dllKR1BvdmI1MTBLcHA1TzFXWVVaQWZHTDh5dGVuNHJUUnBoY3FMSkQ2dGk4TlgzVWhmQjdqTXF6UmNNQURYRGV0bElmRUp5cEMzTktxWkNaQm1GWkM1VEFnQkVaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjgyODI0NDUyfQ; rur="VLL\\05458603175168\\0541714360453:01f76efb0767a635b4159bbd9fac331b2cdc56cc434ac784de4b05f0ff3e0e4c9cbe22f0"',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.137", "Google Chrome";v="112.0.5615.137", "Not:A-Brand";v="99.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'viewport-width': '1792',
    }

    if account in account_data_indiv.index:
        instagram = account_data_indiv['Instagram'][account]
    if account in account_data_popular.index:
        instagram = account_data_popular['Instagram'][account]

    response = requests.get(f'https://www.instagram.com/{instagram}/', cookies=cookies, headers=headers, proxies = proxies(proxy))
    text = response.text
    followers = text.split(" Followers")[0].split('content=\"')[-1].replace(',', '')
    posts = text.split(" Posts")[0].split(' ')[-1].replace(',', '')

    for abbrev in [('K', 1000), ('M', 1000000)]:
        if abbrev[0] in followers:
            followers = int(followers[:-1]) * abbrev[1]
        if abbrev[0] in posts:
            followers = int(posts[:-1]) * abbrev[1]

    return int(followers), int(posts)


## Helper functions for updating data
def update_saved_insights(stats, new = False):
    file_location = 'account_posting/data/insights.csv'
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

def update_stats(new_data):
    file = 'account_posting/data/stats.csv'

    df = pd.read_csv(file, index_col=0)
    data = df.to_dict()

    for acc in [acc for acc in data] + [acc for acc in new_data]:
        if acc in data and acc not in new_data:
            pass
        elif acc in new_data and acc not in data:
            data[acc] = new_data[acc]
        elif acc in data and acc in new_data:
            data[acc].update(new_data[acc])

    df = pd.DataFrame(data)
    df.to_csv(file)

## Sync here (also some edits in impressions())
def get_insights(sort = 'impressions'):
    def compute(responses, account):
        params = getCreds(account)
        proxy = params['proxy']
        # print(account, requests.get('https://ipinfo.io', proxies=proxies(proxy)).json()['ip'])
        followers, posts = get_followers_and_posts(account, proxy)
        # user_media_params = getUserMedia(params) #Used to count the number of post objects it returned, now we just scrape instagram since this maxed out at 25
        responses[account] = (getUserInsights(params, proxy=proxy), None, followers, posts)
        
    
    accounts = [acc for acc in account_data_indiv.index if acc not in exclude] + [acc for acc in account_data_popular.index if acc not in exclude]
    def runInParallel():
        responses = dict()
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
        return responses

    start = time.time()
    responses = runInParallel()

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', None)
    
    stats = impressions(responses, sort)
    # stats = stats[:13]
    print(stats, "\n")
    print(stats.sum()[1:], "\n")

    stats = add_timestamp_row(stats)
    update_saved_insights(stats, new = False)

    end = time.time()
    print(end-start, "\n")

data_responses = dict()
def plot_barchart(days = 30, log_scale = False, cumulative = False, color = 0, show = False):
    def compute(data_responses, account):
        params = getCreds(account) # get creds
        response = getUserInsights(params, days=days, metrics='impressions', proxy = params['proxy'])
        acc_data = dict()
        for insight in response['json_data']['data'] : # loop over user account insights 
            for value in insight['values'] : # loop over each value
                acc_data[value['end_time'][2:-14]] = int(value['value'])
        data_responses[account] = acc_data
    
    accounts = [acc for acc in account_data_indiv.index if acc not in exclude] + [acc for acc in account_data_popular.index if acc not in exclude]
    # accounts = accounts[:14] + accounts[15:] + accounts[14:15]
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
    # runInParallel()
    # df = pd.DataFrame(data_responses)
    # update_stats(data_responses)

    df = pd.read_csv('account_posting/data/stats.csv', index_col=0)

    # df2 = pd.read_csv('account_posting/data/stats.csv', index_col=0)
    # sum = 0
    # for acc in df2.columns:
    #     if acc in data_responses:
    #         sum += df2[acc].sum()
    #         print(acc, df2[acc].sum())
    # print(sum)

    print(df.sum().sort_values().astype(int).tail(20))
    total = str(int(df.sum().sum()))
    print(f"Total: {total[:-6]},{total[-6:-3]},{total[-3:]}")
    fig, ax = plt.subplots()

    if log_scale:
        ax.set_yscale("log")

    end = time.time()
    print(end-start, "\n")

    if cumulative:
        df.sum().sort_values().plot(kind='bar', ax=ax)
        plt.xticks(fontsize=7, rotation = 90)
        plt.xlabel("Accounts", fontsize = 20)
        plt.ylabel(f"Total Impressions", fontsize = 17)
    else:
        # ax.yaxis.tick_right()
        df.plot(kind='bar', stacked=True, legend=True, ax=ax, colormap='tab20') #change legend to true
        # plt.color(plt.cm.rainbow(np.linspace(0, 1, df.shape[0])))
        plt.legend(ncol = 2, loc ="upper left", fontsize = 5)
        plt.xlabel("Date", fontsize = 20)
        plt.ylabel("Daily Impressions", fontsize = 20)

    if show: plt.show()
    plt.savefig(f'account_posting/dashboards/rrob gone {days}days, log {log_scale}, cumu {cumulative}.png')

