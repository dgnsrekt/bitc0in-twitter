# Provides twitter api functionality.

import tweepy
from random import choice
from decouple import config


class TwitterHandler:
    def __init__(self, *, key, secret, token, token_secret):
        # Preparing OAuth authentication
        self.auth = tweepy.OAuthHandler(key, secret)
        self.auth.set_access_token(token, token_secret)

        # Creating API interface
        self.api = tweepy.API(self.auth)

        # Creates a connection to the users profile
        self.user = self.api.me()

    def set_profile_image(self, *, path):
        image = str(choice(list(path.glob("*.png"))))
        self.api.update_profile_image(image)

    def set_profile_banner(self, *, path):
        banner = str(choice(list(path.glob("*.png"))))
        self.api.update_profile_banner(banner)

    def set_profile_color(self, *, color):
        self.api.update_profile(profile_link_color=color)

    def set_profile_description(self, *, description):
        self.api.update_profile(description=description)

    def set_profile_username_suffix(self, *, username, suffix):
        name = f"{username}{suffix}"
        self.api.update_profile(name=name)


# from config import Configuration
#
# config = Configuration()
# tp = TwitterHandler(
#     key=config.key, secret=config.secret, token=config.token, token_secret=config.token_secret
# )
# from paths import PROFILE_BEARISH_PATH, BANNER_BEARISH_PATH
#
# tp.set_profile_image(path=PROFILE_BEARISH_PATH)
# tp.set_profile_banner(path=BANNER_BEARISH_PATH)
# # image, banner, username, desc, color
# print(tp.user.name)
# print(tp.user.screen_name)
# print(tp.user.description)
# print(tp.user.profile_banner_url)
# print(tp.user.profile_image_url)
# print(tp.user.profile_link_color)
