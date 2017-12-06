# -*- encoding: utf-8 -*-
"""
dumper.py

This module uses Twitter's Tweepy library to create aCSV of a user's tweets.
"""

import os
import csv
import tweepy

class Dumper(object):

    def __init__(self, handle):
        self.handle = handle
        self.get_keys()
        self.api = self.authorize()

    def get_keys(self):
        """ Get Twitter credentials on server start """
        key = input("ENTER CONSUMER KEY: ")
        secret = input("ENTER CONSUMER SECRET: ")

        os.environ["CONSUMER_KEY"] = key
        os.environ["CONSUMER_SECRET"] = secret

    def authorize(self): 
        consumer_key = os.environ.get("CONSUMER_KEY")
        consumer_secret = os.environ.get("CONSUMER_SECRET")

        # authorize Twitter
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        # intalize Tweepy
        return tweepy.API(auth)

    def get_all_tweets(self):
        tweets = []

        # can request 200 tweets at a time
        new_tweets = self.api.user_timeline(screen_name = self.handle, count = 200)
        tweets.extend(new_tweets)

        # oldest tweet, subtract one
        oldest_tweet = tweets[-1].id - 1

        # get tweets until maxed out
        while len(new_tweets) > 0:
            print("Getting tweets before %s" % oldest)
            
            # use oldest tweet
            new_tweets = self.api.user_timeline(screen_name = self.handle, 
                                                count = 200, max_id = oldest)

            tweets.extend(new_tweets)

            # update id
            oldest = tweets[-1].id - 1

            print("... %s tweets downloaded so far" % (len(tweets)))

