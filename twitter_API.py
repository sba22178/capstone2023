# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 16:45:41 2023

@author: danma
"""

import tweepy

consumer_key = "y4RMZFYWrpaEFXYG58X1vikw9"
consumer_secret = "YybZBs78dg0UaLZuCXMRN6YM9CAfUumtiQlMW8sasYiqj2igPp"
access_token = "133191204-mImxZFu2H1grVHv7usgFLdf9d4Rkp1qPb7SOXKo5"
#bear_access_token = "AAAAAAAAAAAAAAAAAAAAADgppwEAAAAAK5ILiuuOIArpPvJMw3EdH%2BRI%2BGI%3DjVOknpjUrt6Nv9PLOz6Zty3vky1Ch41gtHF0SNg78PAyCNjYJt"
access_token_secret = "YCVVrXQHdson9lPdilUvHpDVZcGue1SOUypIWGmH200V5"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Define your search query
search_query = "greyhound racing Ireland"

tweets = api.search(q=400,query=search_query, max_results=10)