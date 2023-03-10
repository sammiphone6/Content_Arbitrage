from ig_defines import getCreds, makeApiCall
import datetime
from misc_functions import get_account_data_indiv, get_account_data_popular
from data import exclude

def debugAccessToken( params ) :
	""" Get info on an access token 
	
	API Endpoint:
		https://graph.facebook.com/debug_token?input_token={input-token}&access_token={valid-access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['input_token'] = params['access_token'] # input token is the access token
	endpointParams['access_token'] = params['access_token'] # access token to get debug info on

	url = params['graph_domain'] + '/debug_token' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def debug_access_token(FB_App_Owner):
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
	response = debugAccessToken( params ) # hit the api for some data!

	print ("\nData Access Expires at: ") # label
	print (datetime.datetime.fromtimestamp( response['json_data']['data']['data_access_expires_at'] )) # display out when the token expires

	print ("\nToken Expires at: ") # label
	print (datetime.datetime.fromtimestamp( response['json_data']['data']['expires_at'] )) # display out when the token expires


# FB_App_Owner = 'sam@ercfilings.us' ###### EDIT #######
# debug_access_token(FB_App_Owner)

