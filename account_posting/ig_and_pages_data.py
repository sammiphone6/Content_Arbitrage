from account_posting.ig_defines import getCreds, makeApiCall
import pprint
from account_posting.data import fb_app_data
def getUserPages( params, proxy ) :
	""" Get facebook pages for a user
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + 'me/accounts' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'], proxy ) # make the api call

def get_page_data(fb_email):
	params = getCreds('alixearle') # get creds - can be anything, just using it for params['endpoint_base']
	params['access_token'] = fb_app_data['Access Token'][fb_email]
	params['debug'] = 'no' # set debug
	proxy = fb_app_data['Proxy'][fb_email]
	response = getUserPages( params, proxy ) # get debug info
	# print(response)

	page_data = [(page['name'], page['id']) for page in response['json_data']['data']]
	return page_data

def getInstagramAccount( params, proxy ) :
	""" Get instagram account
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/{page-id}?access_token={your-access-token}&fields=instagram_business_account

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['access_token'] = params['access_token'] # tell facebook we want to exchange token
	endpointParams['fields'] = 'instagram_business_account' # access token

	url = params['endpoint_base'] + params['page_id'] # endpoint url

	return makeApiCall( url, endpointParams, params['debug'], proxy ) # make the api call

def get_instagram_id(email, access_token, fb_page_name):
	
	params = getCreds('alixearle') # can be anyone, only using it for params['endpoint_base']
	params['access_token'] = access_token #'EAARmBm67OlgBAN3BPKziNyYdEoHPZCEgN8URGbtZCn1zSu9GYM1Sj2sD97jOKdOfrkJxOeK9cBwZCiZCfWzTAJAXRhFqk88Q8e8Iw970ZA4FuO5LDMopY1nKQZBjSU5kbGkcoXxxjINKAjq2JgYwAgJ1W0fuvUpNGq6zjMOYc7EZCIJ80FC9JYt'#'EAARmBm67OlgBANhgFPIPCNn98zaSZAf2Fu8vhkjWonbvFidMwdFZCZA1ZCxC4fcmmfbTkpsTunAtbZBNPaiQQOSpjTxeHxGU2PpHJN8aDogxsgNJxP8ojCSTNjEBniT1jZCHTQxiybVVZABrfnWe8mdZAkpZBZBX639Ei899LqZClph1DK6R3ufsuwg3jokIqLBUrAZD'
	fb_page_id = [pair[1] for pair in get_page_data(email) if pair[0] == fb_page_name][0]
	params['page_id'] = fb_page_id
	proxy = fb_app_data['Proxy'][email]

	response = getInstagramAccount(params, proxy) # get debug info
	return response['json_data']['instagram_business_account']['id']


# print(get_instagram_id('arlindloshi503@yahoo.com', 
# 		 'EAALN9H7yu5gBAEopdCGkouwazdtfSDgHcN9z2Pf4rdzyVIZBGe8TiMnicM7UqspFLd9ZCuIeConDqH7L20CtsvqNSodMTGc7oiHYAVB9WgIoHsxWdSC1vQSXlxZADk2OlfCGJT9lW0uSogD32UtZBP1BoOpNdWh1UXxxkSQMdPVpgtcx8xbQ',
# 		 'Noellevyaa'))