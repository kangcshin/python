import tweepy
from textblob import TextBlob

consumer_key = 	'cbk0LjZM1THbmPVTIeZ9bKnRc'
consumer_secret = '8a3mp9wETyY9qVACKSBgt0Y0YLUHCQmb0MYoBdEAVdHsBAndwT'

access_token = '772054924054192128-H3gbyfiR0SKZXT2f2Y9xJiC9ecKgemo'
access_token_secret = 'oNyV04df2lUTseBGt6q7uNeAXGlOiCgSU6zfZbPbfsqn8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)