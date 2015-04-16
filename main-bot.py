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
y = 0

try:
	api = tweepy.API(auth)
	user = api.me()
	followers_list = api.followers_ids(user)
	friends_list = api.friends_ids(user)

	# الغاء متابعة الغير المتابعين
	try:	
		for friend in friends_list:
			if friend not in followers_list:
				api.destroy_friendship(friend)
				time.sleep(60)
				x = x + 1
				if x == 200:
					break
	except tweepy.error.TweepError as ee:
		print ee
		pass

	#متابعة اشخاص جدد
	try:
		for follower in api.followers_ids("MohamadAlarefe"):
			if follower not in followers_list:
				api.create_friendship(follower)
				time.sleep(60)
				y = y + 1
				if y == 100:
					break
	except tweepy.error.TweepError as eee:
		print eee
		pass

except tweepy.error.TweepError as e:
	print e
	pass
