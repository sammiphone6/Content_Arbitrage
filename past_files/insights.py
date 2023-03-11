from ig_defines import getCreds, makeApiCall
from data import tiktok_data_indiv, tiktok_data_popular, exclude
import pandas as pd
import time
import datetime

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

def getUserInsights( params ) :
	""" Get insights for a users account
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{ig-user-id}/insights?metric={metric}&period={period}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['metric'] = 'follower_count,impressions,profile_views,reach' # fields to get back
	endpointParams['period'] = 'day' # period
	endpointParams['access_token'] = params['access_token'] # access token

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
    accounts = [acc for acc in tiktok_data_indiv] + [acc for acc in tiktok_data_popular]
    for account in accounts:
        if account not in exclude:
            params = getCreds(account) # get creds
            response = getUserInsights( params ) # get insights for a user

            new_row = {'account': account}
            for insight in response['json_data']['data'] : # loop over user account insights
                new_row[insight['title'] + " (" + insight['values'][0]['end_time'][:10] + ")"] = insight['values'][1]['value']
                if edit:
                    col_metric = insight['title'] + " (" + insight['values'][0]['end_time'][:10] + ")"
                    edit = False
            
            response = getUserMedia( params ) # get users media from the api
            num_posts = len(response['json_data']['data'])
            new_row['Total Posts'] = '25+' if num_posts >= 25 else num_posts

            if(df.empty):
                for key in new_row:
                    new_row[key] = [new_row[key]]
                df = pd.DataFrame(new_row)
            else:
                df = df.append(new_row, ignore_index = True)
        
    return df.sort_values(by=[col_metric], ascending = False).reset_index(drop = True)

def time_adjusted_impressions():
    df = pd.DataFrame()
    
    t_start = 0
    t_end = 0
    t_frame = 0
    col_metric = 0
    edit = True

    for account in tiktok_data_indiv:
        params = getCreds(account) # get creds
        response = getUserInsights( params ) # get insights for a user

        new_row = {'account': account}
        for insight in response['json_data']['data'] : # loop over user account insights
            if edit:
                t_start = str(datetime.datetime.fromtimestamp(int(response['json_data']['paging']['next'][-27:-17])))
                t_end = str(datetime.datetime.fromtimestamp(int(response['json_data']['paging']['next'][-10:])))
                t_frame = " (" + t_start + " - " + t_end + ")"
                col_metric = insight['title'] + t_frame
                edit = False
            print(response['json_data']['paging']['next'][-10:])
            new_row[insight['title'] + t_frame] = insight['values'][1]['value']
        
        response = getUserMedia( params ) # get users media from the api
        num_posts = len(response['json_data']['data'])
        new_row['Total Posts'] = '25+' if num_posts >= 25 else num_posts

        if(df.empty):
             for key in new_row:
                  new_row[key] = [new_row[key]]
             df = pd.DataFrame(new_row)
        else:
             df = df.append(new_row, ignore_index = True)
        
    return df.sort_values(by=[col_metric], ascending = False).reset_index(drop = True)


# sample('alixearle')

start = time.time()
stats = impressions()
print(stats, "\n")

print(stats.sum()[1:], "\n")

end = time.time()
print(end-start, "\n")
