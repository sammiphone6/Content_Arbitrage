import time
from ig_defines import getCreds, makeApiCall
from content_manipulation import tiktok_to_webhosted_link
from tt_update_data import increment_last_posted_indiv, increment_last_posted_popular, update_data
from misc_functions import announce_pause
from data import account_data_indiv, account_data_popular, tiktok_data_indiv, tiktok_captions_indiv, tiktok_data_popular, exclude, save_files

## General Post Functions
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
	cycles_threshold = 15
	post_failed = False
	while videoMediaStatusCode != 'FINISHED' : # keep checking until the object status is finished
		videoMediaObjectStatusResponse = getMediaObjectStatus( videoMediaObjectId, params ) # check the status on the object
		videoMediaStatusCode = videoMediaObjectStatusResponse['json_data']['status_code'] # update status code
		print("once through")
		cycles+=1
		if(videoMediaStatusCode == 'ERROR'):
			videoMediaObjectStatusResponse = getMediaObjectStatus( videoMediaObjectId, params ) # check the status on the object
			print(videoMediaObjectStatusResponse)
			post_failed = True
			break
		if(cycles > cycles_threshold):
			post_failed = True
			break
		time.sleep(5) # wait 5 seconds if the media object is still being processed

	if (post_failed and tries == 0):
		return postReel(account, media_link, caption, tries = 1)
	elif (post_failed and tries == 1):
		increment_last_posted_and_save(account)
		return 0
	else:
		publishMedia( videoMediaObjectId, params ) # publish the post to instagram
		print("POST COMPLETE!")
		increment_last_posted_and_save(account)

		contentPublishingApiLimit = getContentPublishingLimit( params ) # get the users api limit

		print( "\n---- CONTENT PUBLISHING USER API LIMIT -----\n" ) # title
		print( "\tResponse:" ) # label
		print( contentPublishingApiLimit['json_data_pretty'] ) # json response from ig api
		return 1

def create_and_post_reel(account, tiktok_link, caption):
	caption = ' '.join(['instagram'.join(token.split('tiktok')) for token in caption.split()])
	print("NOW CREATING POST FOR ", tiktok_link)
	link = tiktok_to_webhosted_link(tiktok_link)
	if(link == 0):
		increment_last_posted_and_save(account)
		print("tiktok link ", tiktok_link, ' not valid for ', account)
		time.sleep(6)
		return 0
	if postReel(account, link, caption) == 1:
		print("Post made and transferred from ", account)
		return 1
	else:
		print("An issue occured when making post from ", account)
		return 0


## Individual Post Functions
def post_round_indiv():
    num_posts = 0
    num_accounts = 0
    double_dip = ['kevwithin', 'kevwithin', 'jairvill7', 'kevwithin']
    for account in tiktok_data_indiv:
        num_posts+=update_and_post_indiv(account)
        num_accounts+=1
        announce_pause(4)
    for account in double_dip:
        update_and_post_indiv(account)
        announce_pause(4)
    print(f"POSTING ROUND COMPLETED: {num_posts} POSTS MADE ACROSS {num_accounts} ACCOUNTS.")
    return num_posts

def update_and_post_indiv(account):
    update_data(account)
    if(account not in exclude and tiktok_data_indiv[account]["last_posted"] < len(tiktok_data_indiv[account]["video_ids"]) - 1):
        vid_id = tiktok_data_indiv[account]["video_ids"][tiktok_data_indiv[account]["last_posted"]+1]
        tt_link = f"https://tiktok.com/@{account}/video/{vid_id}/"
        tt_caption = tiktok_captions_indiv[vid_id] + f" #{account_data_indiv['Hashtag'][account]}" #ADD THEIR NAME TO THIS HANDLE

        return create_and_post_reel(account, tt_link, tt_caption) 
    else:
        return 0


## Popular Post Functions
def post_round_popular():
    for name in tiktok_data_popular:
        post_popular(name)
    print(f"POST ROUND COMPLETED.")
    
def post_popular(name):
	if(name not in exclude):
		if(tiktok_data_popular[name]['last_posted'] < len(tiktok_data_popular[name]['videos']) - 1):
			announce_pause(4)
			tt_link, tt_caption = tiktok_data_popular[name]['videos'][tiktok_data_popular[name]['last_posted']+1]
			tt_caption += f" #{account_data_popular['Hashtag'][name]}" #ADD THEIR NAME TO THIS HANDLE
			
			return create_and_post_reel(name, tt_link, tt_caption)
	return 0


## Increment and Save (both indiv and popular)
def increment_last_posted_and_save(account):
	try:
		increment_last_posted_indiv(account)
	except:
		increment_last_posted_popular(account)
	save_files()


## Test Functions
def test_post(account, deep_test = False):
	try:
		media_link = 'https://files.catbox.moe/3pudmc.mp4'
		params = getCreds(account) # get creds from defines
		params['media_type'] = 'REELS' # type of asset
		params['media_url'] = media_link # url on public server for the post
		params['caption'] = 'Here’s a fun spur of moment thing that happened in Spain when I flew in for some business. Loved saying hello to so many of you from across Central and South America. Love you ALL right back and always grateful for every second 🇪🇸🖤🙏🏾'
		params['caption'] += 'Plus, I had to quit while I was ahead before you guys started asking me to speak different languages 😂😂 🇵🇪 🇧🇷 🇪🇸 #Hola #Spain #Peru #Brazil'
		
		videoMediaObjectResponse = createMediaObject( params ) # create a media object through the api
		videoMediaObjectId = videoMediaObjectResponse['json_data']['id'] # id of the media object that was created
		videoMediaStatusCode = 'IN_PROGRESS'

		if deep_test:
			cycles = 0
			cycles_threshold = 15
			while videoMediaStatusCode != 'FINISHED' : # keep checking until the object status is finished
				videoMediaObjectStatusResponse = getMediaObjectStatus( videoMediaObjectId, params ) # check the status on the object
				videoMediaStatusCode = videoMediaObjectStatusResponse['json_data']['status_code'] # update status code
				cycles+=1
				if(videoMediaStatusCode == 'ERROR'):
					videoMediaObjectStatusResponse = getMediaObjectStatus( videoMediaObjectId, params ) # check the status on the object
					print(videoMediaObjectStatusResponse)
					raise Exception(f"{account} couldn't get finished status code")
				if(cycles > cycles_threshold):
					raise Exception(f"{account} took too many cycles")
				time.sleep(5) # wait 5 seconds if the media object is still being processed
				
		print(f".....Posting for {account} is Working!\n")
		return True
	except:
		print(f"ERROR {account} broken :(\n")
		return False