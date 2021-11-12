import logging
import os

import sentry_sdk
import tweepy

# for logging errors
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

SENTRY_LINK = os.getenv("SENTRY_LINK")
sentry_sdk.init(SENTRY_LINK, traces_sample_rate=1.0)

# Authentication
CONSUMER_KEY = os.getenv("ConsumerKey")
CONSUMER_SECRET_KEY = os.getenv("ConsumerSecretKey")
ACCESS_TOKEN = os.getenv("AccessToken")
ACCESS_TOKEN_SECRET = os.getenv("AccessTokenSecret")

HASHTAGS = [
    "#optometry",
    "#ophthalmology",
    # "#glaucoma",
    "#optometrist",
    # "#maculadegeneration",
    # "#diabeticretinopathy",
    # "#keratoconnus",
    # "#cataract",
    # "#myopia",
    # "#dryeye",
    # "#retina",
]


def create_api(
    CONSUMER_KEY=CONSUMER_KEY,
    CONSUMER_SECRET_KEY=CONSUMER_SECRET_KEY,
    ACCESS_TOKEN=ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET=ACCESS_TOKEN_SECRET,
):
    """
    Authentication for the Twitter API
    Credentials are based on @optombot account
    Instructions on how to set up API authentication keys here:
        - https://developer.twitter.com/
    """

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # checking if API is verfied
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error in authenticating API")
        logger.error(f"Message: {e}", exc_info=True)
        raise e
    logger.info("API created and verfied")
    return api


class FavRetweetListener(tweepy.Stream):
    """This initiaises the class for the bot, including custom functions

    Inherits from the tweepy's Stream class
        - https://docs.tweepy.org/en/stable/stream.html

    Args:
        api (tweepy.API): This is the authenticated user object (aka bot)
        consumer_key (str): inherited, the consumer key
        consumer_secret (str): inherited, the consumer secret
        access_token (str): inherited, the access token
        access_token_secret (str): inherited, the access token secret
    """

    def __init__(self, api: tweepy.API, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api = api
        self.me = api.verify_credentials().id

    def on_connect(self):
        logger.info("Connected")

    def on_status(self, tweet):
        logger.info(f"Processing tweet id: {tweet.id}")
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me:
            # ignores replies or author posts
            return
        if not tweet.favorited:
            try:
                self.api.create_favorite(tweet.id)
            except Exception:
                logger.error("Error on fav", exc_info=True)
        if not tweet.retweeted:
            try:
                self.api.retweet(tweet.id)
            except Exception:
                logger.error("Error on fav and retweeted", exc_info=True)

    def on_error(self, status):
        logger.error(status)


def create_bot():
    """
    Creates the bot
    """
    bot = FavRetweetListener(
        api=create_api(),
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET_KEY,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
    )
    bot.filter(track=HASHTAGS, languages=["en"])
