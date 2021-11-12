import pytest
import tweepy

from bots.fav_and_retweet import FavRetweetListener, create_api


@pytest.fixture
def api():
    return create_api()


class TestFavRetweetListener:
    """
    Testing Bot
    """

    def test_bot_connects(self, api):
        """
        Checks if the bot
        """
        assert isinstance(api.verify_credentials(), tweepy.models.User)
        assert api.verify_credentials().name == "TheOptomBot"
