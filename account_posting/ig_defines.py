import requests
import json
from account_posting.data import account_data_indiv, account_data_popular, fb_app_data

def proxies(i):
	return None
	try:
		i = int(i)
		if i not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
			return None
	except:
		return None
	
	username = 'user-rzt5e8cfbe12a-country-us'
	password = 'AuU1T6n20w'

	proxy = f"http://{username}:{password}@dc.razorproxy.com:800{i}"
	print(proxy)
	proxies = {
		'http': proxy,
		'https': proxy
	}
	return proxies

def getCreds(account) :
	""" Get creds required for use in the applications
	
	Returns:
		dictonary: credentials needed globally

	"""
	if account in account_data_indiv.index:
		account_data = account_data_indiv
	elif account in account_data_popular.index:
		account_data = account_data_popular

	email = account_data['FB App Owner'][account]
	creds = dict() # dictionary to hold everything
	creds['access_token'] = str(fb_app_data["Access Token"][email]) #'EAARByfZAa4rcBAMcApDzyHvI4Ct45ACFvEZCzfw6TFHPnQkT5LJfzzZAMllrwZBwTV68L1AcbOdY74LlEWGG1YUvTcmVumvR1iTwVOkUC2DDHWI7spsxiyTxvpXAQ7ptMTtzhuz3ys6YQwN7XEe0QlgXDTghnMmC1BkXaZCQLLhBr2ZC7f2zYEGNIlxK1LQ563mrIZAd54a8buZAVZBn3kvl2kH1QYnSVlEUZD' #'EAARmBm67OlgBAN3BPKziNyYdEoHPZCEgN8URGbtZCn1zSu9GYM1Sj2sD97jOKdOfrkJxOeK9cBwZCiZCfWzTAJAXRhFqk88Q8e8Iw970ZA4FuO5LDMopY1nKQZBjSU5kbGkcoXxxjINKAjq2JgYwAgJ1W0fuvUpNGq6zjMOYc7EZCIJ80FC9JYt' #'EAARmBm67OlgBAON5jmZAjNUSXotZBLPZB9zKQVrRJXqkD8eJojEWF178mz5OZCPM81Wuj4CWKlZBZCNTOchURZApMCsbvZCk4Pw4qG0nHZCRupa6HZBZCxqjiFKKhP68c3jlhRmCiJCZBRSp5kmfqEeENZCPt1z4DZCdGoDsHeMpD7NFWqefwK0ArZAFo71' # access token for use with all api calls
	creds['client_id'] = str(int(fb_app_data["App ID"][email])) #"1198235584225975" #'1238077720443480' # client id from facebook app IG Graph API Test
	creds['client_secret'] = str(fb_app_data["App Secret"][email]) #"f271ca1f37c38574004cc24256345ec6" #'cfca2bd25f40ec77c546d508fab33d17' # client secret from facebook app
	creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
	creds['graph_version'] = 'v16.0' # version of the api we are hitting
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['debug'] = 'no' # debug mode for api call
	creds['proxy'] = fb_app_data['Proxy'][email]

	creds['instagram_account_id'] = str(account_data["IG ID"][account]) #'INSTAGRAM-BUSINESS-ACCOUNT-ID' # users instagram account id

	return creds

# data = requests.post('http://ipinfo.io', proxies=proxies(1))
# print(data)
# print(data.text)

def makeApiCall( url, endpointParams, type, proxy = None) :
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters


	Returns:
		object: data from the endpoint

	"""
	# print(url, endpointParams, proxies(proxy))
	if type == 'POST' : # post request
		data = requests.post( url, endpointParams, proxies = proxies(proxy))
	else : # get request
		data = requests.get( url, endpointParams, proxies = proxies(proxy))

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	return response # get and return content

