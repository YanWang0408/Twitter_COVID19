#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Import packages
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import re

# Enter Twitter API Keys
consumer_key = ""
consumer_secret = ""
access_token = "-"
access_token_secret = ""

# Create tracklist with the words that will be searched for
tracklist = ['#coronavirus', '#covid19']
# Initialize Global variable
tweet_count = 0
# Input number of tweets to be downloaded
n_tweets = 500000

# Create the class that will handle the tweet stream
class StdOutListener(StreamListener):
      
    def on_data(self, data):
        global tweet_count
        global n_tweets
        global stream
        if tweet_count < n_tweets:
            print(data)
            tweet_count += 1
            return True
        else:
            stream.disconnect()

    def on_error(self, status):
        print(status)



# Handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=tracklist)


# In[ ]:




