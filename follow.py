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

