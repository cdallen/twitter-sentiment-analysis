## Source: https://www.earthdatascience.org/courses/earth-analytics-python/using-apis-natural-language-processing-twitter/get-and-use-twitter-data-in-python/
## Created by Connor Allen and Dr. Curt Rode

import os
import tweepy as tw
import pandas as pd
import json

consumer_key = "2jXxCVgDN426krzkFEtTbsXxG"
consumer_secret = "57rUy8NySrCrgoifLZTSW5IdoUKmmxs0X9yfCpnDWK5juU6NFY"
access_token = "1241885426-hdCjopPeTpxhorvmWzAmFZfRboDTLhkjaXFeV6m"
access_secret = "kbdPlmlyVPhUHPWHnAwjU8V1AcbWGLRYZWFtVAK8YyvWI"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables. Can be a hash tag or phrases
search_words = "#RIPKobe"
date_since = "2020-1-26"

# filter out RT
new_search = search_words + " -filter:retweets"
new_search

# Collect tweets
tweets = tw.Cursor(api.search,
              q=new_search,
              lang="en",
              since=date_since,
              tweet_mode="extended").items(10000)

#test = [tweet.text for tweet in tweets]

#print(test)


# scrape the last 100 tweets for a hashtag from the Twitter API and save to JSON file
fname = search_words + ".json"
with open(fname,"w") as file:
    for tweet in tweets:
        file.write(json.dumps(tweet._json) + "\r\n")


# Iterate and print tweets
#for tweet in tweets:
#    print(tweet.text)

# Collect a list of tweets
#[tweet.text for tweet in tweets]

# Sort by user location and screen name
#users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
#users_locs

#all_tweets = [tweet.text for tweet in tweets]
#all_tweets[:5]


# put tweet information into a dataframe
#tabled_tweets = pd.DataFrame(data=all_tweets, 
 #                   columns=['user', "location", "tweets"])
#tabled_tweets
