from account_posting.ig_defines import proxies
import requests

i = 64
response = requests.get('https://ipinfo.io', proxies=proxies(i))
print(response, response.text)
response = requests.get('https://instagram.com', proxies=proxies(i))
print(response, len(response.text))


# import instaloader

# # Creating an instance of the Instaloader class
# bot = instaloader.Instaloader()

# # Loading the profile from an Instagram handle
# profile = instaloader.Profile.from_username(bot.context, 'cristiano')
# print(profile)


# import instaloader

# # Creating an instance of the Instaloader class
# bot = instaloader.Instaloader()

# # Provide the search query here
# search_results = instaloader.TopSearchResults(bot.context, 'music')

# # Iterating over the extracted usernames
# for username in search_results.get_profiles():
#     print(username)

# # Iterating over the extracted hashtags
# for hashtag in search_results.get_hashtags():
#     print(hashtag)



# import instaloader
# import pandas as pd
# import time

# start = time.time()
# # Creating an instance of the Instaloader class
# bot = instaloader.Instaloader()
# bot.login(user="barbaragreentrkyazltqn", passwd="Qhml3gHn")

# # Loading a profile from an Instagram handle
# profile = instaloader.Profile.from_username(bot.context, 'chriscrpyto')

# # Retrieving the usernames of all followers
# followers = [follower.username for follower in profile.get_followers()]

# # Converting the data to a DataFrame
# followers_df = pd.DataFrame(followers)

# # Storing the results in a CSV file
# followers_df.to_csv('followers.csv', index=False)

# # Retrieving the usernames of all followings
# followings = [followee.username for followee in profile.get_followees()]

# # Converting the data to a DataFrame
# followings_df = pd.DataFrame(followings)

# # Storing the results in a CSV file
# followings_df.to_csv('followings.csv', index=False)

# end = time.time()
# print(end-start)