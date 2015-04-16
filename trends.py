# -*- coding: utf-8 -*-

#بوت تويتر 
#12:49 الجمعة 24 يناير

import tweepy
import time

# == معلومات الامان ==

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
x = 0
a=""
try:
	api = tweepy.API(auth)
	user = api.me()
	trends_list = api.trends_place(23424938)
	data = trends_list[0]
	trends = data['trends']

	for trend in trends:
		try:
			a= trend['name'].encode('utf-8','ignore')
			if '#' in a:
				api.update_with_media('','') + a)
				x = x + 1
			else:
				pass

			if x == 10:
				break
			time.sleep(120)
		except tweepy.error.TweepError as e:
			pass

except tweepy.error.TweepError as ee:
	print ee
	pass

