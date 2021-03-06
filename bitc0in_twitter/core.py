from config import Configuration

from decouple import config

import logme

from paths import BANNER_BEARISH_PATH, BANNER_BULLISH_PATH
from paths import PROFILE_BEARISH_PATH, PROFILE_BULLISH_PATH

from state import MarketState

from twitter import TwitterHandler


profile_logger = logme.log(scope="module", name="profile")


class BitcoinTwitterProfile(MarketState):
    def __init__(self, *, bitcoin_percent_change):
        initial_state = self.get_market_state(bitcoin_percent_change)
        super().__init__(initial_state=initial_state)

        self.config = Configuration()
        key, secret, token, token_secret = self.config.get_twitter_keys()

        self.twitter_profile = TwitterHandler(
            key=key, secret=secret, token=token, token_secret=token_secret
        )

        if self.state == "bearish":
            self.transition_bearish()
        else:
            self.transition_bullish()

    @staticmethod
    def get_market_state(bitcoin_percent_change):
        if bitcoin_percent_change < 0:
            return "bearish"
        else:
            return "bullish"

    def transition_bullish(self):
        profile_logger.info("transitioning to bullish state.")
        image, banner, color, description = self.config.options
        if image:
            self.twitter_profile.set_profile_image(path=PROFILE_BULLISH_PATH)

        if banner:
            self.twitter_profile.set_profile_banner(path=BANNER_BULLISH_PATH)

        if color:
            self.twitter_profile.set_profile_color(color=config("BULLISH_PROFILE_LINK_COLOR"))

        if description:
            self.twitter_profile.set_profile_description(
                description=config("BULLISH_PROFILE_DESCRIPTION")
            )

    def transition_bearish(self):
        profile_logger.info("transitioning to bearish state.")
        image, banner, color, description = self.config.options
        if image:
            self.twitter_profile.set_profile_image(path=PROFILE_BEARISH_PATH)

        if banner:
            self.twitter_profile.set_profile_banner(path=BANNER_BEARISH_PATH)

        if color:
            self.twitter_profile.set_profile_color(color=config("BEARISH_PROFILE_LINK_COLOR"))

        if description:
            self.twitter_profile.set_profile_description(
                description=config("BEARISH_PROFILE_DESCRIPTION")
            )
