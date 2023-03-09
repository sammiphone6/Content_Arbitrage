from ig_defines import getCreds, makeApiCall
import datetime
from misc_functions import get_account_data_indiv, get_account_data_popular
from exclude import exclude

def getLongLivedAccessToken( params ) :
	""" Get long lived access token
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/oauth/access_token?grant_type=fb_exchange_token&client_id={app-id}&client_secret={app-secret}&fb_exchange_token={your-access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['grant_type'] = 'fb_exchange_token' # tell facebook we want to exchange token
	endpointParams['client_id'] = params['client_id'] # client id from facebook app
	endpointParams['client_secret'] = params['client_secret'] # client secret from facebook app
	endpointParams['fb_exchange_token'] = params['access_token'] # access token to get exchange for a long lived token

	url = params['endpoint_base'] + 'oauth/access_token' # endpoint url

	print(endpointParams['client_id'])

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def get_long_lived_access_token(FB_App_Owner):
	account = None 
	account_data_indiv = get_account_data_indiv()
	for acc in account_data_indiv.index:
		if account_data_indiv['FB App Owner'][acc] == FB_App_Owner:
			account = acc
			break

	if not account:
		account_data_popular = get_account_data_popular()
		for acc in account_data_popular.index:
			if account_data_popular['FB App Owner'][acc] == FB_App_Owner:
				account = acc
				break

	params = getCreds(account) # get creds
	params['debug'] = 'yes' # set debug
	response = getLongLivedAccessToken( params ) # hit the api for some data!

	print ("\n ---- ACCESS TOKEN INFO ----\n") # section header
	print ("Access Token:")  # label
	print (response['json_data']) # display access token
	print (response['json_data']['access_token']) # display access token


# FB_App_Owner = 'sam@ercfilings.us' ###### EDIT #######
# get_long_lived_access_token(FB_App_Owner)

