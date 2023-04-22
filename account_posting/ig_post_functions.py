import time
from account_posting.ig_defines import getCreds, makeApiCall
from account_posting.content_manipulation import tiktok_to_webhosted_link
from account_posting.tt_update_data import increment_last_posted_indiv, increment_last_posted_popular, update_data, update_financial_data
from account_posting.misc_functions import announce_pause
from account_posting.data import account_data_financial, account_data_indiv, account_data_popular, tiktok_data_indiv, tiktok_captions_indiv, tiktok_data_popular, tiktok_data_financial, exclude, save_files
from multiprocessing import Process, Manager
import random
import requests

## General Post Functions
def createMediaObject( params, proxy ) :
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

	return makeApiCall( url, endpointParams, 'POST', proxy ) # make the api call

def getMediaObjectStatus( mediaObjectId, params, proxy ) :
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
	endpointParams['fields'] = 'status_code,status,id' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return makeApiCall( url, endpointParams, 'GET', proxy ) # make the api call

def publishMedia( mediaObjectId, params, proxy ) :
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

	return makeApiCall( url, endpointParams, 'POST', proxy ) # make the api call

def getContentPublishingLimit( params, proxy ) :
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

	return makeApiCall( url, endpointParams, 'GET', proxy) # make the api call

def postReel(account, media_link, caption, tries = 0, increment = True):
	params = getCreds(account) # get creds from defines
	params['media_type'] = 'REELS' # type of asset
	params['media_url'] = media_link # url on public server for the post
	params['caption'] = caption
	proxy = params['proxy']
	# print(account, media_link, caption)

	videoMediaObjectResponse = createMediaObject( params, proxy ) # create a media object through the api
	print(account, videoMediaObjectResponse['json_data'])
	videoMediaObjectId = videoMediaObjectResponse['json_data']['id'] # id of the media object that was created
	
	videoMediaStatusCode = 'IN_PROGRESS'

	cycles = 0
	wait_time = 10
	cycles_threshold = 75//wait_time
	post_failed = False
	while videoMediaStatusCode != 'FINISHED' : # keep checking until the object status is finished
		time.sleep(wait_time) # wait if the media object is still being processed

		videoMediaObjectStatusResponse = getMediaObjectStatus( videoMediaObjectId, params, proxy ) # check the status on the object
		# print(videoMediaObjectStatusResponse['json_data'], account)
		videoMediaStatusCode = videoMediaObjectStatusResponse['json_data']['status_code'] # update status code
		
		cycles+=1
		print(f"media object loading for {account}, cycle {cycles}.")

		if(videoMediaStatusCode == 'ERROR'):
			videoMediaObjectStatusResponse = getMediaObjectStatus( videoMediaObjectId, params, proxy ) # check the status on the object
			print(videoMediaObjectStatusResponse, account)
			post_failed = True
			break
		if(cycles > cycles_threshold):
			post_failed = True
			break

	if (post_failed and tries == 0):
		return postReel(account, media_link, caption, tries = 1)
	elif (post_failed and tries == 1):
		increment_last_posted_and_save(account, increment)
		return 0
	else:
		publishMedia( videoMediaObjectId, params, proxy ) # publish the post to instagram
		print("POST COMPLETE!")
		increment_last_posted_and_save(account, increment)

		contentPublishingApiLimit = getContentPublishingLimit( params, proxy ) # get the users api limit
		print( "\n---- CONTENT PUBLISHING USER API LIMIT -----\n" ) # title
		print( "\tResponse:" ) # label
		print( contentPublishingApiLimit['json_data_pretty'] ) # json response from ig api
		return 1

def create_and_post_reel(account, tiktok_link, caption, increment = True, speed = None):
	caption = ' '.join(['instagram'.join(token.split('tiktok')) for token in caption.split()])
	print("NOW CREATING POST FOR: ", tiktok_link)
	link = tiktok_to_webhosted_link(tiktok_link, speed)
	if(link == 0):
		increment_last_posted_and_save(account, increment)
		print("tiktok link ", tiktok_link, ' not valid for ', account)
		time.sleep(6)
		return 0
	if postReel(account, link, caption, increment=increment) == 1:
		print("Post made and transferred from ", account)
		return 1
	else:
		print("An issue occured when making post from ", account)
		return 0


## Financial Post Functions
def post_round_financial():
	update_financial_data()
	for link_dict in tiktok_data_financial:
		link = list(link_dict.keys())[0]
		caption = tiktok_captions_indiv[link.split("/video/")[-1].strip('/')]
		if len(link_dict[link]) < 2:
			acc1 = random.choice(list(account_data_financial.index))
			if create_and_post_reel(acc1, link, caption, increment = False, speed = None):
				link_dict[link].append(acc1)
				print(link, " posted to ", acc1, " !!")
		save_files()
			


## Individual Post Functions
def post_round_indiv(hashtags = True):
    num_posts = 0
    num_accounts = 0
    double_dip = []#['kevwithin', 'kevwithin', 'jairvill7', 'kevwithin']
    for account in tiktok_data_indiv:
        num_posts+=update_and_post_indiv(account, hashtags)
        num_accounts+=1
        announce_pause(4)
    for account in double_dip:
        update_and_post_indiv(account, hashtags)
        announce_pause(4)
    print(f"POSTING ROUND COMPLETED: {num_posts} POSTS MADE ACROSS {num_accounts} ACCOUNTS.")
    return num_posts

def update_and_post_indiv(account, tt_data = False, update = True, tries = 0, hashtags = True):
	if tries >= 5: 
		if tt_data: return 0, tiktok_data_indiv[account], tiktok_captions_indiv
		else: return 0
	if update: update_data(account)
	if(account not in exclude):
		if (tiktok_data_indiv[account]["last_posted"] < len(tiktok_data_indiv[account]["video_ids"]) - 1):
			vid_id = tiktok_data_indiv[account]["video_ids"][tiktok_data_indiv[account]["last_posted"]+1]
			tt_link = f"https://tiktok.com/@{account}/video/{vid_id}/"
			tt_caption = tiktok_captions_indiv[vid_id] + f" #{account_data_indiv['Hashtag'][account]}" #ADD THEIR NAME TO THIS HANDLE
			if hashtags == False: tt_caption = tt_caption.split('#')[0]
			increment = True
			speed = None
		else:
			vid_id = tiktok_data_indiv[account]["video_ids"][random.choice([_ for _ in range(int(tiktok_data_indiv[account]["last_posted"]*0.8))])]
			tt_link = f"https://tiktok.com/@{account}/video/{vid_id}/"
			tt_caption = tiktok_captions_indiv[vid_id] + f" #{account_data_indiv['Hashtag'][account]} #fyp #foryoupage" #ADD THEIR NAME TO THIS HANDLE
			if hashtags == False: tt_caption = tt_caption.split('#')[0]
			increment = False
			speed = random.randrange(104, 130)/100

		if tt_data:
			result = create_and_post_reel(account, tt_link, tt_caption, increment, speed)
			if result == 0: return update_and_post_indiv(account, tt_data, update = False, tries = tries+1)
			else: return result, tiktok_data_indiv[account], tiktok_captions_indiv
		else:
			result = create_and_post_reel(account, tt_link, tt_caption, increment, speed)
			if result == 0: return update_and_post_indiv(account, tt_data, update = False, tries = tries+1)
			else: return result
	if tt_data:
		return 0, 0, 0
	else:
		return 0

## Popular Post Functions
def post_round_popular(hashtags = True):
    for name in tiktok_data_popular:
        post_popular(name, hashtags = hashtags)
    print(f"POST ROUND COMPLETED.")
    
def post_popular(name, tt_data = False, hashtags = True):
	if(name not in exclude):
		if(tiktok_data_popular[name]['last_posted'] < len(tiktok_data_popular[name]['videos']) - 1):
			tt_link, tt_caption = tiktok_data_popular[name]['videos'][random.choice([_ for _ in range(int(tiktok_data_popular[name]["last_posted"]*0.8))])]
			tt_caption += f" #{account_data_popular['Hashtag'][name]}" #ADD THEIR NAME TO THIS HANDLE
			if hashtags == False: tt_caption = tt_caption.split('#')[0]
			increment = True
			speed = None
		else:
			tt_link, tt_caption = tiktok_data_popular[name]['videos'][tiktok_data_popular[name]['last_posted']+1]
			tt_caption += f" #{account_data_popular['Hashtag'][name]} #fyp #foryoupage" #ADD THEIR NAME TO THIS HANDLE
			if hashtags == False: tt_caption = tt_caption.split('#')[0]
			increment = False
			speed = random.randrange(104, 130)/100
		
		if tt_data:
			result = create_and_post_reel(name, tt_link, tt_caption, increment, speed)
			return result, tiktok_data_popular[name]
		else:
			return create_and_post_reel(name, tt_link, tt_caption, increment, speed)
	if tt_data:
		return 0, 0
	else:
		return 0


## Increment and Save (both indiv and popular)
def increment_last_posted_and_save(account, increment = True):
	if not increment: return
	try:
		increment_last_posted_indiv(account)
	except:
		increment_last_posted_popular(account)
	save_files()


## Test Functions
def test_post(account, broken, deep_test = False):
	debug = False
	try:
		media_link = 'https://files.catbox.moe/3pudmc.mp4'
		params = getCreds(account) # get creds from defines
		proxy = params['proxy']
		params['media_type'] = 'REELS' # type of asset
		params['media_url'] = media_link # url on public server for the post
		params['caption'] = 'Here’s a fun spur of moment thing that happened in Spain when I flew in for some business. Loved saying hello to so many of you from across Central and South America. Love you ALL right back and always grateful for every second 🇪🇸🖤🙏🏾'
		params['caption'] += 'Plus, I had to quit while I was ahead before you guys started asking me to speak different languages 😂😂 🇵🇪 🇧🇷 🇪🇸 #Hola #Spain #Peru #Brazil'
		
		if debug: print('1', account)
		videoMediaObjectResponse = createMediaObject( params, proxy ) # create a media object through the api
		if debug: print('2', account)
		if debug: print('object response:', videoMediaObjectResponse)
		videoMediaObjectId = videoMediaObjectResponse['json_data']['id'] # id of the media object that was created
		videoMediaStatusCode = 'IN_PROGRESS'

		if deep_test:
			cycles = 0
			cycles_threshold = 15
			while videoMediaStatusCode != 'FINISHED' : # keep checking until the object status is finished
				videoMediaObjectStatusResponse = getMediaObjectStatus( videoMediaObjectId, params, proxy ) # check the status on the object
				if debug: print('status response:', videoMediaObjectStatusResponse)
				videoMediaStatusCode = videoMediaObjectStatusResponse['json_data']['status_code'] # update status code
				cycles+=1
				if(videoMediaStatusCode == 'ERROR'):
					videoMediaObjectStatusResponse = getMediaObjectStatus( videoMediaObjectId, params, proxy ) # check the status on the object
					print(account, videoMediaObjectStatusResponse)
					raise Exception(f"{account} couldn't get finished status code")
				if(cycles > cycles_threshold):
					raise Exception(f"{account} took too many cycles")
				time.sleep(5) # wait 5 seconds if the media object is still being processed
				
		print(f"...............Posting for {account} is Working!\n")
		return True
	except:
		print(f"ERROR ERROR {account} broken :(\n")
		broken.append(account)
		print(broken)
		return False


#### SYNC FUNCTIONS ####

## Tests Sync
def run_tests(deep_test = False):

	def runInParallel(accounts):
		with Manager() as manager:
			broken_manager = manager.list()
			proc = []
			for account in accounts:
				p = Process(target=test_post, args=(account, broken_manager, deep_test))
				p.start()
				proc.append(p)
			for p in proc:
				p.join()

			return set(broken_manager)

	start = time.time()
	accounts = [acc for acc in account_data_indiv.index if acc not in exclude] + [acc for acc in account_data_popular.index if acc not in exclude]
	broken = runInParallel(accounts)
	print(f"Broken of {len(accounts)} accounts: ", broken if len(broken) > 0 else None)
	end = time.time()
	print(end-start)


## Posts Sync
def posts_sync(accounts, hashtags = True):
	def post(account, indiv_data, indiv_captions, popular_data, posted_manager):
		if account in account_data_indiv.index:
			print('Posting ', account)
			result = update_and_post_indiv(account, tt_data = True, hashtags = hashtags)
			print('FINISHED', account)
			if result[1] != 0: indiv_data[account] = result[1]
			if result[2] != 0: indiv_captions = indiv_captions.update(result[2])
			if result[0] == 1: posted_manager.append(account)
		elif account in account_data_popular.index:
			result = post_popular(account, tt_data = True, hashtags = hashtags)
			if result[1] != 0: popular_data[account] = result[1] 
			if result[0] == 1: posted_manager.append(account)

	def runInParallel():
		with Manager() as manager:
			tt_indiv_data = manager.dict()
			tt_indiv_captions = manager.dict()
			tt_popular_data = manager.dict()
			posted_manager = manager.list()

			proc = []
			for account in accounts:
				p = Process(target=post, args=(account, tt_indiv_data, tt_indiv_captions, tt_popular_data, posted_manager))
				proc.append(p)
				p.start()
				# time.sleep(4)
			for p in proc:
				p.join()
			tiktok_data_indiv.update(tt_indiv_data)
			tiktok_captions_indiv.update(tt_indiv_captions)
			tiktok_data_popular.update(tt_popular_data)
			save_files()

			return set(accounts).difference(set(posted_manager))
	
	start = time.time()
	print(f"Accounts that failed to post out of the {len(accounts)} accounts attempted: ", runInParallel())
	end = time.time()
	print("Posting Complete")
	print(end-start, "\n")


# spcyysamm = [
#     'https://www.tiktok.com/@spcyysamm/video/7224914904942251310',
#     'https://www.tiktok.com/@spcyysamm/video/7224571889782443310',
#     'https://www.tiktok.com/@spcyysamm/video/7224236393202027818',
#     'https://www.tiktok.com/@spcyysamm/video/7222735840106007850',
#     'https://www.tiktok.com/@spcyysamm/video/7222377541586160942',
#     'https://www.tiktok.com/@spcyysamm/video/7222735840106007850',
#     'https://www.tiktok.com/@spcyysamm/video/7222377541586160942',
#     'https://www.tiktok.com/@spcyysamm/video/7222377010629217582',
#     'https://www.tiktok.com/@spcyysamm/video/7222366674740137259',
#     'https://www.tiktok.com/@spcyysamm/video/7221549642931293486',
#     'https://www.tiktok.com/@spcyysamm/video/7221519962978962730',
#     'https://www.tiktok.com/@spcyysamm/video/7220575554221706542',
#     'https://www.tiktok.com/@spcyysamm/video/7220509951049993514',
#     'https://www.tiktok.com/@spcyysamm/video/7219746718332554542',
#     'https://www.tiktok.com/@spcyysamm/video/7219334206755720491',
#     'https://www.tiktok.com/@spcyysamm/video/7219017261900746026',
#     'https://www.tiktok.com/@spcyysamm/video/7218246032218524970',
#     'https://www.tiktok.com/@spcyysamm/video/7217911569378856238',
#     'https://www.tiktok.com/@spcyysamm/video/7217531885369576747',
#     'https://www.tiktok.com/@spcyysamm/video/7215994429943860523',
#     'https://www.tiktok.com/@spcyysamm/video/7215242994713251118',
#     'https://www.tiktok.com/@spcyysamm/video/7215242397444328747',
#     'https://www.tiktok.com/@spcyysamm/video/7215240420387786027',
#     'https://www.tiktok.com/@spcyysamm/video/7214114027331423534',
#     'https://www.tiktok.com/@spcyysamm/video/7213766716625554731',
#     'https://www.tiktok.com/@spcyysamm/video/7213766265121344811',
#     'https://www.tiktok.com/@spcyysamm/video/7212751681162087726',
#     'https://www.tiktok.com/@spcyysamm/video/7212706289158278442',
#     'https://www.tiktok.com/@spcyysamm/video/7212705951411948843',
#     'https://www.tiktok.com/@spcyysamm/video/7212705793970375979',
#     'https://www.tiktok.com/@spcyysamm/video/7212321202243800366',
#     'https://www.tiktok.com/@spcyysamm/video/7212321143007579438',
#     'https://www.tiktok.com/@spcyysamm/video/7208974843100843306',
#     'https://www.tiktok.com/@spcyysamm/video/7208974571394059566',
#     'https://www.tiktok.com/@spcyysamm/video/7208974464631999786',
#     'https://www.tiktok.com/@spcyysamm/video/7208267098190236974',
#     'https://www.tiktok.com/@spcyysamm/video/7208266999326149930',
#     'https://www.tiktok.com/@spcyysamm/video/7208216127145545003',
#     'https://www.tiktok.com/@spcyysamm/video/7207940104021675307',
#     'https://www.tiktok.com/@spcyysamm/video/7207932922588957994',
#     'https://www.tiktok.com/@spcyysamm/video/7207932688311897390',
#     'https://www.tiktok.com/@spcyysamm/video/7204516651788766507',
#     'https://www.tiktok.com/@spcyysamm/video/7204516334061866286',
#     'https://www.tiktok.com/@spcyysamm/video/7203825321118829867',
#     'https://www.tiktok.com/@spcyysamm/video/7203825321118829867',
#     'https://www.tiktok.com/@spcyysamm/video/7202337677956402475',
#     'https://www.tiktok.com/@spcyysamm/video/7202336574430907691',
# ]

# spcysam = [
#     'https://www.tiktok.com/@spcysam/video/7146710235565067522',
#     'https://www.tiktok.com/@spcysam/video/7143012019871042818',
#     'https://www.tiktok.com/@spcysam/video/7142969730721271042',
#     'https://www.tiktok.com/@spcysam/video/7142601104956591362',
#     'https://www.tiktok.com/@spcysam/video/7141798371764817153',
#     'https://www.tiktok.com/@spcysam/video/7141482085465820417',
#     'https://www.tiktok.com/@spcysam/video/7140781375057136897',
#     'https://www.tiktok.com/@spcysam/video/7140417077524925697',
#     'https://www.tiktok.com/@spcysam/video/7140335963057704193',
#     'https://www.tiktok.com/@spcysam/video/7139638219905207554',
#     'https://www.tiktok.com/@spcysam/video/7138944603750698241',
#     'https://www.tiktok.com/@spcysam/video/7138913511425494274',
#     'https://www.tiktok.com/@spcysam/video/7138190271648484610',
#     'https://www.tiktok.com/@spcysam/video/7136133253810982146',
#     'https://www.tiktok.com/@spcysam/video/7134780864541510914',
#     'https://www.tiktok.com/@spcysam/video/7134499701663010049',
#     'https://www.tiktok.com/@spcysam/video/7134130362384403713',
#     'https://www.tiktok.com/@spcysam/video/7133644675075935489',
#     'https://www.tiktok.com/@spcysam/video/7133635791456128257',
# ]

# simp_for_samfrank = [
#     'https://www.tiktok.com/@simp_for_samfrank/video/7223701513200323883',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7216857137404808494',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7216293937143811374',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7213605477735796014',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7211122374337367338',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7210747622510939435',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7209339883599564075',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7206689234160209195',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7204827121376726318',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7203829287059770666',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7200140809553874219',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7198245652999064878',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7195527048339770666',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7194822793954102574',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7190359161518181678',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7188982804271631659',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7185087359237557546',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7179390122876521771',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7179339709796191531',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7171542549692173610',
#     'https://www.tiktok.com/@simp_for_samfrank/video/7171409630751591726',
# ]

# all_links = spcysam+spcysam+simp_for_samfrank

# def get_caption(tt_link):

# 	cookies = {
# 		# 'MONITOR_WEB_ID': '309c8090-6469-4377-b9ad-745bbddc8f72',
# 		# 'MONITOR_DEVICE_ID': '8d32196f-b4a7-48c7-b517-0012f20b842c',
# 		# '_ttp': '289J0zFF3tfkEFKeyLDCZKFwDMC',
# 		# 'tiktok_webapp_theme': 'light',
# 		# 'tt_csrf_token': 'r16ny1BX-ESae4IUXYwaSlnIqU3bSLqKJGvQ',
# 		# 's_v_web_id': 'verify_ldgr2ah9_xz7m8a1G_7Lit_4xlj_985M_JMIPWGVpbMZN',
# 		# 'd_ticket': '156ce90a06b2b94cae934a6bcdac0274024ea',
# 		# 'uid_tt': 'ca756457013b4db955360f56b19678518583b7e30c2753eecd5e9d6afc8d650b',
# 		# 'uid_tt_ss': 'ca756457013b4db955360f56b19678518583b7e30c2753eecd5e9d6afc8d650b',
# 		# 'sid_tt': 'a76d4ca06ba5c894586138c7d158fe98',
# 		# 'sessionid': 'a76d4ca06ba5c894586138c7d158fe98',
# 		# 'sessionid_ss': 'a76d4ca06ba5c894586138c7d158fe98',
# 		# 'store-idc': 'useast5',
# 		# 'store-country-code': 'us',
# 		# 'store-country-code-src': 'uid',
# 		# 'tt-target-idc': 'useast5',
# 		# 'tt-target-idc-sign': 'J2zC8abDjFPdDukSUlAP9z669_pAxKquT9QkKSvHByOXmSl7e-NPfVfyeZdnnQFQSMwCErEYDMuV032IZMH5Py0Fjv-xioY4iEXxB1L4tXc93xMceauR1FpTj3FIfD9LEKTpE3u8Yry-S9xaA4K0I2Ee-FamDwL-8gjMRArr8Sdb2GzlDdcysInt9DMG_W2fcDNA2vAIc6Ndt6wzVq9p6trVpW6BfYJpo4LQtm5es02KQVdLjvM99tlS41ojW84RQHERJyQMzJRTmMOyeU4VmvmWE49bZougUPmA2MVRcNEPW8BtdxQfCuhBpm5lAuGq5a4JpiMBnsKTuft0SaX1wqZLLKmyBzc98q7Y6ZbZHtDEnXfFUuchAjQCwiQ63RYN4F0Bm6CxrWE97T8Ew_J0pU6j8LnWOUc_7iXSedv-tYWyyhOtQvmvM0RAvDx0AYcGG0Uh9hul_sGapwedBqezMt4OG92aXp0i8DX1TvNat-WmXFSe2PsCaN1RwxmMy5Xa',
# 		# 'csrf_session_id': '0fd659681307d0f9d9cf261c8d0e0b99',
# 		# 'passport_fe_beating_status': 'true',
# 		# '__tea_cache_tokens_1988': '{%22user_unique_id%22:%227166372563806291502%22%2C%22timestamp%22:1674958582630%2C%22_type_%22:%22default%22}',
# 		# '_abck': 'E372DE3F8F68C9482D8CA6BD492A5E99~0~YAAQRDoZuAwYFNqGAQAAy0di7AmVJZZL4daDsgacXCs1/3TFdiUMjCe0e/odl1HkPMsmOy5N8RKVXaTh55HZO34Fi6lRSlgFlkJQMxwW4OMRzjohTS2KJMbThhXxkjM+WHZHknPv12I0qOkRMdK8F8hYOELVwx046WqDYDjWgBdytjtsl3pLtj8TbgKiS0fgiYcuZOXgD2RJwDCrR46YLgzHgEvDLyB8QRY5df7UWEyVusRnP1UC9QPq3ok9swSLu1wujMJgxfAvkBEt5yFkxzpDvv1SBgSTG3xCqnrUaZIIYANcGxTclOpg5qLEM16dHE5Ds3JZ4J9MnXOdMNOwAj/tvwq0O3OI09p8RUv5lDcgER0zjzlOvlWZJ0gC80aGrJpkRJXHoBmRieqYLsd+lcmfR1G5ov5n~-1~-1~-1',
# 		# 'cookie-consent': '{%22ga%22:false%2C%22af%22:false%2C%22fbp%22:false%2C%22lip%22:false%2C%22bing%22:false%2C%22ttads%22:false%2C%22reddit%22:false%2C%22criteo%22:false%2C%22version%22:%22v9%22}',
# 		# 'sid_guard': 'a76d4ca06ba5c894586138c7d158fe98%7C1681584522%7C15552000%7CThu%2C+12-Oct-2023+18%3A48%3A42+GMT',
# 		# 'sid_ucp_v1': '1.0.0-KGZjMmU2NzhmZDBlYTIyNjI3YWEzMzVjMDI0MzZjMjQ1OThlYmNlOTAKIAiriNPyhK3z6mMQiuProQYYswsgDDDbm9eeBjgCQPEHEAQaB3VzZWFzdDUiIGE3NmQ0Y2EwNmJhNWM4OTQ1ODYxMzhjN2QxNThmZTk4',
# 		# 'ssid_ucp_v1': '1.0.0-KGZjMmU2NzhmZDBlYTIyNjI3YWEzMzVjMDI0MzZjMjQ1OThlYmNlOTAKIAiriNPyhK3z6mMQiuProQYYswsgDDDbm9eeBjgCQPEHEAQaB3VzZWFzdDUiIGE3NmQ0Y2EwNmJhNWM4OTQ1ODYxMzhjN2QxNThmZTk4',
# 		# 'tt_chain_token': '+7hqfC9Fp2bQ45CHIVx3EQ==',
# 		# '_tea_utm_cache_1988': '{%22utm_source%22:%22hoobe%22%2C%22utm_medium%22:%22social%22}',
# 		# '_tea_utm_cache_345918': '{%22utm_source%22:%22hoobe%22%2C%22utm_medium%22:%22social%22}',
# 		# 'odin_tt': 'b2e784cdc3db1f34a2f643df3d20c4d03b741a6b01e7c2821bb5bacbb40d6747d5724adc63f65bc3a9b3ef2233da4e78c810be7529fba213a35ac34550c64a19183093ea1f6097622416a0b6b2f6d11c',
# 		# 'ttwid': '1%7CT_5sZDUaUw2lnkHwrKmEqusBeEqkapMM7ie9gQ5aWgY%7C1682202919%7C5a3063910dfe7f4dc621f146078cf557de88167dc93a94bf8e1564074c03ec43',
# 		# 'msToken': 'Wq-pB_1n9Wi6a5Tufa8PWGJGIhCa9LQVvO6-v-f74vj0lEORzBIuN8M4lu3wFND_rglG_gIKhWtvIdsjVG2o6YFDTtx9ApIaUTzcEAb47rHZiTHoryWsU-62C45PE25rYUtAI6VH4w9kggv8c1Y=',
# 		# 'msToken': 'Wq-pB_1n9Wi6a5Tufa8PWGJGIhCa9LQVvO6-v-f74vj0lEORzBIuN8M4lu3wFND_rglG_gIKhWtvIdsjVG2o6YFDTtx9ApIaUTzcEAb47rHZiTHoryWsU-62C45PE25rYUtAI6VH4w9kggv8c1Y=',
# 	}

# 	headers = {
# 		'authority': 'www.tiktok.com',
# 		# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
# 		'accept-language': 'en-US,en;q=0.9',
# 		# 'cookie': 'MONITOR_WEB_ID=309c8090-6469-4377-b9ad-745bbddc8f72; MONITOR_DEVICE_ID=8d32196f-b4a7-48c7-b517-0012f20b842c; _ttp=289J0zFF3tfkEFKeyLDCZKFwDMC; tiktok_webapp_theme=light; tt_csrf_token=r16ny1BX-ESae4IUXYwaSlnIqU3bSLqKJGvQ; s_v_web_id=verify_ldgr2ah9_xz7m8a1G_7Lit_4xlj_985M_JMIPWGVpbMZN; d_ticket=156ce90a06b2b94cae934a6bcdac0274024ea; uid_tt=ca756457013b4db955360f56b19678518583b7e30c2753eecd5e9d6afc8d650b; uid_tt_ss=ca756457013b4db955360f56b19678518583b7e30c2753eecd5e9d6afc8d650b; sid_tt=a76d4ca06ba5c894586138c7d158fe98; sessionid=a76d4ca06ba5c894586138c7d158fe98; sessionid_ss=a76d4ca06ba5c894586138c7d158fe98; store-idc=useast5; store-country-code=us; store-country-code-src=uid; tt-target-idc=useast5; tt-target-idc-sign=J2zC8abDjFPdDukSUlAP9z669_pAxKquT9QkKSvHByOXmSl7e-NPfVfyeZdnnQFQSMwCErEYDMuV032IZMH5Py0Fjv-xioY4iEXxB1L4tXc93xMceauR1FpTj3FIfD9LEKTpE3u8Yry-S9xaA4K0I2Ee-FamDwL-8gjMRArr8Sdb2GzlDdcysInt9DMG_W2fcDNA2vAIc6Ndt6wzVq9p6trVpW6BfYJpo4LQtm5es02KQVdLjvM99tlS41ojW84RQHERJyQMzJRTmMOyeU4VmvmWE49bZougUPmA2MVRcNEPW8BtdxQfCuhBpm5lAuGq5a4JpiMBnsKTuft0SaX1wqZLLKmyBzc98q7Y6ZbZHtDEnXfFUuchAjQCwiQ63RYN4F0Bm6CxrWE97T8Ew_J0pU6j8LnWOUc_7iXSedv-tYWyyhOtQvmvM0RAvDx0AYcGG0Uh9hul_sGapwedBqezMt4OG92aXp0i8DX1TvNat-WmXFSe2PsCaN1RwxmMy5Xa; csrf_session_id=0fd659681307d0f9d9cf261c8d0e0b99; passport_fe_beating_status=true; __tea_cache_tokens_1988={%22user_unique_id%22:%227166372563806291502%22%2C%22timestamp%22:1674958582630%2C%22_type_%22:%22default%22}; _abck=E372DE3F8F68C9482D8CA6BD492A5E99~0~YAAQRDoZuAwYFNqGAQAAy0di7AmVJZZL4daDsgacXCs1/3TFdiUMjCe0e/odl1HkPMsmOy5N8RKVXaTh55HZO34Fi6lRSlgFlkJQMxwW4OMRzjohTS2KJMbThhXxkjM+WHZHknPv12I0qOkRMdK8F8hYOELVwx046WqDYDjWgBdytjtsl3pLtj8TbgKiS0fgiYcuZOXgD2RJwDCrR46YLgzHgEvDLyB8QRY5df7UWEyVusRnP1UC9QPq3ok9swSLu1wujMJgxfAvkBEt5yFkxzpDvv1SBgSTG3xCqnrUaZIIYANcGxTclOpg5qLEM16dHE5Ds3JZ4J9MnXOdMNOwAj/tvwq0O3OI09p8RUv5lDcgER0zjzlOvlWZJ0gC80aGrJpkRJXHoBmRieqYLsd+lcmfR1G5ov5n~-1~-1~-1; cookie-consent={%22ga%22:false%2C%22af%22:false%2C%22fbp%22:false%2C%22lip%22:false%2C%22bing%22:false%2C%22ttads%22:false%2C%22reddit%22:false%2C%22criteo%22:false%2C%22version%22:%22v9%22}; sid_guard=a76d4ca06ba5c894586138c7d158fe98%7C1681584522%7C15552000%7CThu%2C+12-Oct-2023+18%3A48%3A42+GMT; sid_ucp_v1=1.0.0-KGZjMmU2NzhmZDBlYTIyNjI3YWEzMzVjMDI0MzZjMjQ1OThlYmNlOTAKIAiriNPyhK3z6mMQiuProQYYswsgDDDbm9eeBjgCQPEHEAQaB3VzZWFzdDUiIGE3NmQ0Y2EwNmJhNWM4OTQ1ODYxMzhjN2QxNThmZTk4; ssid_ucp_v1=1.0.0-KGZjMmU2NzhmZDBlYTIyNjI3YWEzMzVjMDI0MzZjMjQ1OThlYmNlOTAKIAiriNPyhK3z6mMQiuProQYYswsgDDDbm9eeBjgCQPEHEAQaB3VzZWFzdDUiIGE3NmQ0Y2EwNmJhNWM4OTQ1ODYxMzhjN2QxNThmZTk4; tt_chain_token=+7hqfC9Fp2bQ45CHIVx3EQ==; _tea_utm_cache_1988={%22utm_source%22:%22hoobe%22%2C%22utm_medium%22:%22social%22}; _tea_utm_cache_345918={%22utm_source%22:%22hoobe%22%2C%22utm_medium%22:%22social%22}; odin_tt=b2e784cdc3db1f34a2f643df3d20c4d03b741a6b01e7c2821bb5bacbb40d6747d5724adc63f65bc3a9b3ef2233da4e78c810be7529fba213a35ac34550c64a19183093ea1f6097622416a0b6b2f6d11c; ttwid=1%7CT_5sZDUaUw2lnkHwrKmEqusBeEqkapMM7ie9gQ5aWgY%7C1682202919%7C5a3063910dfe7f4dc621f146078cf557de88167dc93a94bf8e1564074c03ec43; msToken=Wq-pB_1n9Wi6a5Tufa8PWGJGIhCa9LQVvO6-v-f74vj0lEORzBIuN8M4lu3wFND_rglG_gIKhWtvIdsjVG2o6YFDTtx9ApIaUTzcEAb47rHZiTHoryWsU-62C45PE25rYUtAI6VH4w9kggv8c1Y=; msToken=Wq-pB_1n9Wi6a5Tufa8PWGJGIhCa9LQVvO6-v-f74vj0lEORzBIuN8M4lu3wFND_rglG_gIKhWtvIdsjVG2o6YFDTtx9ApIaUTzcEAb47rHZiTHoryWsU-62C45PE25rYUtAI6VH4w9kggv8c1Y=',
# 		'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
# 		'sec-ch-ua-mobile': '?0',
# 		'sec-ch-ua-platform': '"macOS"',
# 		'sec-fetch-dest': 'document',
# 		'sec-fetch-mode': 'navigate',
# 		'sec-fetch-site': 'none',
# 		'sec-fetch-user': '?1',
# 		'upgrade-insecure-requests': '1',
# 		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
# 	}

# 	response = requests.get(tt_link, cookies=cookies, headers=headers)

# 	text = response.text
# 	caption = text.split("property=\"og:description\" content=\"")[1].split("\"/><meta data-rh=\"tru")[0]
# 	return '' if '&' in caption or 'x2' in caption else caption
# 	# x = property="og:description" content="😅oh well #fyp "/><meta data-rh="tru


samfrank_link_and_captions = [('https://www.tiktok.com/@spcysam/video/7146710235565067522',
  '😅oh well #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7143012019871042818', '🍿🎬 #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7142969730721271042',
  'uh huh honey #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7142601104956591362', 'that’s all'),
 ('https://www.tiktok.com/@spcysam/video/7141798371764817153', ''),
 ('https://www.tiktok.com/@spcysam/video/7141482085465820417', ''),
 ('https://www.tiktok.com/@spcysam/video/7140781375057136897', ''),
 ('https://www.tiktok.com/@spcysam/video/7140417077524925697', '🙈🙈 #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7140335963057704193', ''),
 ('https://www.tiktok.com/@spcysam/video/7139638219905207554', '@spcysam hi '),
 ('https://www.tiktok.com/@spcysam/video/7138944603750698241',
  'you know what i’m saying ?!?! #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7138913511425494274', '@spcysam '),
 ('https://www.tiktok.com/@spcysam/video/7138190271648484610', ''),
 ('https://www.tiktok.com/@spcysam/video/7136133253810982146',
  '#FreezeFramePhoto '),
 ('https://www.tiktok.com/@spcysam/video/7134780864541510914',
  'have you tho🥵 #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7134499701663010049', ''),
 ('https://www.tiktok.com/@spcysam/video/7134130362384403713', ''),
 ('https://www.tiktok.com/@spcysam/video/7133644675075935489', '#fyp '),
 ('https://www.tiktok.com/@spcysam/video/7133635791456128257',
  'WHAT POV IS NEXTTT?! #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7146710235565067522',
  '😅oh well #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7143012019871042818', '🍿🎬 #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7142969730721271042',
  'uh huh honey #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7142601104956591362', 'that’s all'),
 ('https://www.tiktok.com/@spcysam/video/7141798371764817153', ''),
 ('https://www.tiktok.com/@spcysam/video/7141482085465820417', ''),
 ('https://www.tiktok.com/@spcysam/video/7140781375057136897', ''),
 ('https://www.tiktok.com/@spcysam/video/7140417077524925697', '🙈🙈 #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7140335963057704193', ''),
 ('https://www.tiktok.com/@spcysam/video/7139638219905207554', '@spcysam hi '),
 ('https://www.tiktok.com/@spcysam/video/7138944603750698241',
  'you know what i’m saying ?!?! #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7138913511425494274', '@spcysam '),
 ('https://www.tiktok.com/@spcysam/video/7138190271648484610', ''),
 ('https://www.tiktok.com/@spcysam/video/7136133253810982146',
  '#FreezeFramePhoto '),
 ('https://www.tiktok.com/@spcysam/video/7134780864541510914',
  'have you tho🥵 #fyp '),
 ('https://www.tiktok.com/@spcysam/video/7134499701663010049', ''),
 ('https://www.tiktok.com/@spcysam/video/7134130362384403713', ''),
 ('https://www.tiktok.com/@spcysam/video/7133644675075935489', '#fyp '),
 ('https://www.tiktok.com/@spcysam/video/7133635791456128257',
  'WHAT POV IS NEXTTT?! #fyp '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7223701513200323883',
  '#foryoupage #fypシ #samfrank '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7216857137404808494',
  '#for#youpage #foryou #samfrank @spcysam '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7216293937143811374',
  '#samfrank #foryou #foryoupage '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7213605477735796014',
  '#foryoupage #foryou #samfrank  I love u with all my heart '
  '❤️ '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7211122374337367338',
  '#CapCut #foryou #foryoupage #samfrank ❤️'),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7210747622510939435',
  '#CapCut #foryoupage #foryou #samfrank '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7209339883599564075',
  '#foryoupage #foryou #samfrank '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7206689234160209195',
  '#18 #foryou #foryoupage '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7204827121376726318',
  '#foryoupage #foryou #18 '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7203829287059770666',
  'Clip made for spam #foryoupage #foryou #18 '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7200140809553874219',
  '#18 #samfrank #foryoupage #foryou @spcysam '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7198245652999064878',
  '#fyp #foryoupage #samfrank #18 '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7195527048339770666',
  '#foryou #samfrank '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7194822793954102574',
  '#samfrank #foryoupage #18 #foryou '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7190359161518181678',
  '#foryoupage #18 #samfrank '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7188982804271631659',
  '#foryou #samfrank #foryoupage Old sam tic toks'),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7185087359237557546',
  '#foryoupage #samfrank #foryou '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7179390122876521771',
  '2019 SAM #foryou #fyp #samfrank #foryoupage @spcysam '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7179339709796191531',
  'The best Christmas gift 🎁 #samfrank #fyp #foryou @spcysam '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7171542549692173610',
  'My top 10 photos of Sam frank #samfrank #fyp #foryou #foryoupage @spcysam '),
 ('https://www.tiktok.com/@simp_for_samfrank/video/7171409630751591726',
  '💞Sam💞#foryoupage #foryou #fyp #samfrank @spcysam '),
 ('https://www.tiktok.com/@spcyysamm/video/7224914904942251310',
  'this could be you😄'),
 ('https://www.tiktok.com/@spcyysamm/video/7224571889782443310',
  'follow me for more🥰'),
 ('https://www.tiktok.com/@spcyysamm/video/7224236393202027818',
  'this could be you follow me😊'),
 ('https://www.tiktok.com/@spcyysamm/video/7222735840106007850', '🤣👍'),
 ('https://www.tiktok.com/@spcyysamm/video/7222377541586160942', '😳'),
 ('https://www.tiktok.com/@spcyysamm/video/7222735840106007850', '🤣👍'),
 ('https://www.tiktok.com/@spcyysamm/video/7222377541586160942', '😳'),
 ('https://www.tiktok.com/@spcyysamm/video/7222377010629217582', '😭😭'),
 ('https://www.tiktok.com/@spcyysamm/video/7222366674740137259', '🤣'),
 ('https://www.tiktok.com/@spcyysamm/video/7221549642931293486', '😂😂'),
 ('https://www.tiktok.com/@spcyysamm/video/7221519962978962730', '😁😁'),
 ('https://www.tiktok.com/@spcyysamm/video/7220575554221706542',
  'what would you say😂'),
 ('https://www.tiktok.com/@spcyysamm/video/7220509951049993514',
  'what mall should we go to next to? '),
 ('https://www.tiktok.com/@spcyysamm/video/7219746718332554542',
  'where should i go next😁'),
 ('https://www.tiktok.com/@spcyysamm/video/7219334206755720491',
  'did he win or lose? follow for more😂'),
 ('https://www.tiktok.com/@spcyysamm/video/7219017261900746026',
  'lets hope she doesnt see this…😭'),
 ('https://www.tiktok.com/@spcyysamm/video/7218246032218524970',
  'this could be you follow me😁'),
 ('https://www.tiktok.com/@spcyysamm/video/7217911569378856238', 'W '),
 ('https://www.tiktok.com/@spcyysamm/video/7217531885369576747',
  'thid could be you just follow me🥰'),
 ('https://www.tiktok.com/@spcyysamm/video/7215994429943860523', '🤣🤣'),
 ('https://www.tiktok.com/@spcyysamm/video/7215242994713251118', '😂😂'),
 ('https://www.tiktok.com/@spcyysamm/video/7215242397444328747', '😅'),
 ('https://www.tiktok.com/@spcyysamm/video/7215240420387786027', '😳'),
 ('https://www.tiktok.com/@spcyysamm/video/7214114027331423534',
  'dont be boring😝'),
 ('https://www.tiktok.com/@spcyysamm/video/7213766716625554731',
  'i did not expect that🤣'),
 ('https://www.tiktok.com/@spcyysamm/video/7213766265121344811', 'wow😭😂'),
 ('https://www.tiktok.com/@spcyysamm/video/7212751681162087726', '😳😳'),
 ('https://www.tiktok.com/@spcyysamm/video/7212706289158278442',
  'he wanted both😳'),
 ('https://www.tiktok.com/@spcyysamm/video/7212705951411948843',
  'might have to😂 '),
 ('https://www.tiktok.com/@spcyysamm/video/7212705793970375979', '😂💗'),
 ('https://www.tiktok.com/@spcyysamm/video/7212321202243800366',
  'wowww\U0001fae3'),
 ('https://www.tiktok.com/@spcyysamm/video/7212321143007579438',
  'she said it 😳'),
 ('https://www.tiktok.com/@spcyysamm/video/7208974843100843306', '#fyp '),
 ('https://www.tiktok.com/@spcyysamm/video/7208974571394059566', '#fyp '),
 ('https://www.tiktok.com/@spcyysamm/video/7208974464631999786', 'W 👍 #fyp '),
 ('https://www.tiktok.com/@spcyysamm/video/7208267098190236974',
  '😳 @montyjlopez '),
 ('https://www.tiktok.com/@spcyysamm/video/7208266999326149930', '😂😂'),
 ('https://www.tiktok.com/@spcyysamm/video/7208216127145545003',
  'valid 😂 tag him in the comments #fyp '),
 ('https://www.tiktok.com/@spcyysamm/video/7207940104021675307', '#fyp '),
 ('https://www.tiktok.com/@spcyysamm/video/7207932922588957994', '😆 #fyp '),
 ('https://www.tiktok.com/@spcyysamm/video/7207932688311897390',
  'would you🤭 #fyp '),
 ('https://www.tiktok.com/@spcyysamm/video/7204516651788766507', ''),
 ('https://www.tiktok.com/@spcyysamm/video/7204516334061866286',
  'who is it😂😂 #fy '),
 ('https://www.tiktok.com/@spcyysamm/video/7203825321118829867',
  'honestly, didn’t hesitate 👍 #fyp '),
 ('https://www.tiktok.com/@spcyysamm/video/7203825321118829867',
  'honestly, didn’t hesitate 👍 #fyp '),
 ('https://www.tiktok.com/@spcyysamm/video/7202337677956402475',
  'he can’t see the 🌶️ contnent ##fyp'),
 ('https://www.tiktok.com/@spcyysamm/video/7202336574430907691',
  'guess my occupation😂 ##fyp')]

# for link in spcyysamm:
# 	caption = get_caption(link)
# 	print(link, get_caption(link))
# 	samfrank_link_and_captions.append((link, caption))


# import pprint
# pp = pprint.PrettyPrinter(depth=6)
# pp.pprint(samfrank_link_and_captions)

# print(len(samfrank_link_and_captions))

def post_sam_frank(p = 0.4):
	def post(account, posted_manager):
		link, caption = random.choice(samfrank_link_and_captions)
		caption += ' @samxfrank'
		res = create_and_post_reel(account, link, caption, increment=False, speed = random.randrange(95, 130)/100)
		if res == 1: posted_manager.append(account)

	def runInParallel(accounts):
		with Manager() as manager:
			posted_manager = manager.list()

			proc = []
			for account in accounts:
				p = Process(target=post, args=(account, posted_manager))
				proc.append(p)
				p.start()
				# time.sleep(4)
			for p in proc:
				p.join()

			return set(accounts).difference(set(posted_manager))
	
	start = time.time()
	accounts = [acc for acc in account_data_indiv.index if acc not in exclude and random.random() < p]
	print(accounts)
	print(f"Accounts that failed to post out of the {len(accounts)} accounts attempted: ", runInParallel(accounts))
	end = time.time()
	print("Posting Complete")
	print(end-start, "\n")