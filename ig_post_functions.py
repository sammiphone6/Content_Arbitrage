import time
from ig_defines import getCreds, makeApiCall
from content_manipulation import tiktok_to_webhosted_link
from tt_update_data import increment_last_posted, increment_last_posted_popular

def createMediaObject( params ) :
	""" Create media object

	Args:
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-user-id}/media?image_url={image-url}&caption={caption}&access_token={access-token}
		https://graph.facebook.com/v5.0/{ig-user-id}/media?video_url={video-url}&caption={caption}&access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	url = params['endpoint_base'] + (str)(params['instagram_account_id']) + '/media' # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['caption'] = params['caption']  # caption for the post
	endpointParams['access_token'] = params['access_token'] # access token

	if 'IMAGE' == params['media_type'] : # posting image
		endpointParams['image_url'] = params['media_url']  # url to the asset
	else : # posting video
		endpointParams['media_type'] = params['media_type']  # specify media type
		endpointParams['video_url'] = params['media_url']  # url to the asset
	
	return makeApiCall( url, endpointParams, 'POST' ) # make the api call

def getMediaObjectStatus( mediaObjectId, params ) :
	""" Check the status of a media object

	Args:
		mediaObjectId: id of the media object
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-container-id}?fields=status_code

	Returns:
		object: data from the endpoint

	"""

	url = params['endpoint_base'] + '/' + mediaObjectId # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'status_code' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return makeApiCall( url, endpointParams, 'GET' ) # make the api call

def publishMedia( mediaObjectId, params ) :
	""" Publish content

	Args:
		mediaObjectId: id of the media object
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-user-id}/media_publish?creation_id={creation-id}&access_token={access-token}

	Returns:
		object: data from the endpoint

	"""

	url = params['endpoint_base'] + (str)(params['instagram_account_id']) + '/media_publish' # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['creation_id'] = mediaObjectId # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return makeApiCall( url, endpointParams, 'POST' ) # make the api call

def getContentPublishingLimit( params ) :
	""" Get the api limit for the user

	Args:
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-user-id}/content_publishing_limit?fields=config,quota_usage

	Returns:
		object: data from the endpoint

	"""

	url = params['endpoint_base'] + (str)(params['instagram_account_id']) + '/content_publishing_limit' # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'config,quota_usage' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return makeApiCall( url, endpointParams, 'GET' ) # make the api call

def postReel(account, media_link, caption, tries = 0):
	params = getCreds(account) # get creds from defines
	params['media_type'] = 'REELS' # type of asset
	params['media_url'] = media_link # url on public server for the post
	params['caption'] = caption

	videoMediaObjectResponse = createMediaObject( params ) # create a media object through the api
	print(videoMediaObjectResponse['json_data'])
	videoMediaObjectId = videoMediaObjectResponse['json_data']['id'] # id of the media object that was created
	videoMediaStatusCode = 'IN_PROGRESS'

	cycles = 0
	cycles_threshold = 20
	while videoMediaStatusCode != 'FINISHED' : # keep checking until the object status is finished
		videoMediaObjectStatusResponse = getMediaObjectStatus( videoMediaObjectId, params ) # check the status on the object
		videoMediaStatusCode = videoMediaObjectStatusResponse['json_data']['status_code'] # update status code
		print("once through")
		cycles+=1
		if(cycles > cycles_threshold):
			break
		time.sleep( 5 ) # wait 5 seconds if the media object is still being processed

	if (cycles > cycles_threshold and tries == 0):
		postReel(account, media_link, caption, tries = 1)
	elif (cycles > cycles_threshold and tries == 1):
		try:
			increment_last_posted(account)
		except:
			increment_last_posted_popular(account)
		return 0
	else:
		publishMedia( videoMediaObjectId, params ) # publish the post to instagram
		print("POST COMPLETE!")
		try:
			increment_last_posted(account)
		except:
			increment_last_posted_popular(account)
		
		contentPublishingApiLimit = getContentPublishingLimit( params ) # get the users api limit

		print( "\n---- CONTENT PUBLISHING USER API LIMIT -----\n" ) # title
		print( "\tResponse:" ) # label
		print( contentPublishingApiLimit['json_data_pretty'] ) # json response from ig api
	return 1

def post_reel(account, tiktok_link, caption):
	print("NOW CREATING POST FOR ", tiktok_link)
	link = tiktok_to_webhosted_link(tiktok_link)
	if(link == 0):
		time.sleep(12)
		return
	if postReel(account, link, caption) == 1:
		print("Post made and transferred from ", account)
	else:
		print("An issue occured when making post from ", account)




## Test Functions
def test_post(account, tiktok_link, caption):
	try:
		media_link = tiktok_to_webhosted_link(tiktok_link)
		params = getCreds(account) # get creds from defines
		params['media_type'] = 'REELS' # type of asset
		params['media_url'] = media_link # url on public server for the post
		params['caption'] = caption

		videoMediaObjectResponse = createMediaObject( params ) # create a media object through the api
		videoMediaObjectId = videoMediaObjectResponse['json_data']['id'] # id of the media object that was created
		videoMediaStatusCode = 'IN_PROGRESS'
		print(f".....Posting for {account} is Working!")
		return True
	except:
		print(f"ERROR {account} broken :(")
		return False