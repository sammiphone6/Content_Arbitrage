from ig_defines import getCreds, makeApiCall
import pprint
from data import fb_app_data
def getUserPages( params ) :
	""" Get facebook pages for a user
	
	API Endpoint:
		https://graph.facebook.com/{graph-api-version}/me/accounts?access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['access_token'] = params['access_token'] # access token

	url = params['endpoint_base'] + 'me/accounts' # endpoint url

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def get_page_data(fb_email):
	params = getCreds('alixearle') # get creds - can be anything, just using it for params['endpoint_base']
	params['access_token'] = fb_app_data['Access Token'][fb_email]
	params['debug'] = 'no' # set debug
	response = getUserPages( params ) # get debug info

	for page in response['json_data']['data']:
		if page['name'] == 'Once upon a page':
			print(page)

	page_data = [(page['name'], page['id']) for page in response['json_data']['data']]
	return page_data

def getInstagramAccount( params ) :
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

	return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

def get_instagram_id(access_token, fb_page_id):
	params = getCreds('alixearle') # can be anyone, only using it for params['endpoint_base']
	params['access_token'] = access_token #'EAARmBm67OlgBAN3BPKziNyYdEoHPZCEgN8URGbtZCn1zSu9GYM1Sj2sD97jOKdOfrkJxOeK9cBwZCiZCfWzTAJAXRhFqk88Q8e8Iw970ZA4FuO5LDMopY1nKQZBjSU5kbGkcoXxxjINKAjq2JgYwAgJ1W0fuvUpNGq6zjMOYc7EZCIJ80FC9JYt'#'EAARmBm67OlgBANhgFPIPCNn98zaSZAf2Fu8vhkjWonbvFidMwdFZCZA1ZCxC4fcmmfbTkpsTunAtbZBNPaiQQOSpjTxeHxGU2PpHJN8aDogxsgNJxP8ojCSTNjEBniT1jZCHTQxiybVVZABrfnWe8mdZAkpZBZBX639Ei899LqZClph1DK6R3ufsuwg3jokIqLBUrAZD'
	params['page_id'] = fb_page_id #'109736578719076'

	response = getInstagramAccount(params) # get debug info
	return response['json_data']['instagram_business_account']['id']

pp = pprint.PrettyPrinter(depth=6)
fb = 'shimaxc2566@simaenaga.com'
page_data = get_page_data(fb)
pp.pprint(page_data)

for page in page_data:
	print(get_instagram_id(fb_app_data['Access Token'][fb], page[1]))

# print(get_instagram_id(fb_app_data['Access Token'][fb], '109930088698992'))
# https://www.facebook.com/profile.php?id=