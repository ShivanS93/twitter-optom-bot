# TheOptomBot/bots/config.py
# this script is used to authenticate the python bot with @OptomBot
# credentials are saved to a .env file and used by the script as environment variables


import tweepy
import os
import logging
from dotenv import load_dotenv

logger = logging.getLogger()

def create_api():
    load_dotenv()
    API_KEY = os.getenv('APIKey')
    API_SECRET_KEY = os.getenv('APISecretKey')
    ACCESS_TOKEN = os.getenv('AccessToken')
    ACCESS_TOKEN_SECRET = os.getenv('AccessTokenSecret')

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
            wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Error creating API', exc_info=True)
        raise e
    logger.info('API created')
    return api
