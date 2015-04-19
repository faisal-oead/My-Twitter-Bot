#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#  
#  Copyright 2014 faisal oead <fafagold@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

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
