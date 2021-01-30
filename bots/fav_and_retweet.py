#!/usr/bin/env python3
# TheOptomBot/bots/fav_and_retweet.py
# the aim of this script is to fav and retweet
# posts with the hashtag contained in the the config.py file

import tweepy
import logging
from config import create_api
from config import hashtags
import database_connector as dc
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

class FavRetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
      
    def on_status(self, tweet):
        logger.info('Processing tweet id %s' % tweet.id)
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            # ignores replies or author posts
            return
        if dc.check_tweet(tweet):
            logger.info('Tweet has already been tweeted')
            # prevents 'tweet spam'
        if not tweet.favorited:
            # mark it as liked, as not been done
            try:
                tweet.favorite()
            except Exception as e:
                logger.error('Error on fav', exc_info=True)
        if not tweet.retweeted:
            # retweet, since we have not retweeted it yet
            try:
                tweet.retweet()
                dc.store_tweet(tweet)
                #print('Tweet to retweet: %s' % tweet.text)
            except Exception as e:
                logger.error('Error on fav and retweeted', exc_info=True)

    def on_error(self, status):
        logger.error(status)
 
def main(keywords):
    dc.create_db()
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=['en'])

if __name__ == '__main__':
    main(hashtags())
