from ig_defines import getCreds, makeApiCall

def getMessages(params ) :
	""" Publish content

	Args:
		mediaObjectId: id of the media object
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-user-id}/media_publish?creation_id={creation-id}&access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	url = params['endpoint_base'] + (str)(params['instagram_account_id']) + '/page/messages' # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['access_token'] = params['access_token'] # access token

	return makeApiCall( url, endpointParams, 'GET' ) # make the api call

account = 'cute cats'
params = getCreds(account)
print(getMessages(params))

## This doesn't work