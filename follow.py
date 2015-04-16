# -*- coding: utf-8 -*-

#بوت تويتر 
#فيصل الجعيد
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

try:
	api = tweepy.API(auth)
	user = api.me()
	followers_list = api.followers_ids(user)
	friends_list = api.friends_ids(user)
	
	for follower in followers_list:
		try:
			if follower not in friends_list:
				api.create_friendship(follower)
				api.send_direct_message(screen_name = str(api.get_user(follower).screen_name),text= '')
				x = x + 1
				if x == 20:
					break
				time.sleep(2500)
		except tweepy.error.TweepError as e:
			pass

except tweepy.error.TweepError as ee:
	print ee
	pass

