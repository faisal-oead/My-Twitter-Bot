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

