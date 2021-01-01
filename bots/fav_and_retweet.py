#!/usr/bin/env python3
# TheOptomBot/bots/fav_and_retweet.py
# the aim of this script is to fav and retweet
# posts with the hashtag #Optometry and #Opthalmology

import tweepy
import logging
from config import create_api
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
                #print('Tweet to retweet: %s' % tweet.text)
            except Exception as e:
                logger.error('Error on fav and retweeted', exc_info=True)

    def on_error(self, status):
        logger.error(status)
 
def main(keywords):
    api = create_api()
    tweets_listener = FavRetweetListener(api)
    stream = tweepy.Stream(api.auth, tweets_listener)
    stream.filter(track=keywords, languages=['en'])

    #for tweet in api.search(q=keywords, lang='en', rpp=10):
    #    print(f'{tweet.user.name}: {tweet.text}')

if __name__ == '__main__':
    main(['#Optometry', '#Opthalmology'])
