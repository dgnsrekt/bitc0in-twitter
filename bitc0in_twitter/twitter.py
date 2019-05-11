# Provides twitter api functionality.

from random import choice

import logme

import tweepy


@logme.log
class TwitterHandler:
    def __init__(self, *, key, secret, token, token_secret):
        # Preparing OAuth authentication
        self.auth = tweepy.OAuthHandler(key, secret)
        self.auth.set_access_token(token, token_secret)

        # Creating API interface
        self.api = tweepy.API(self.auth)

        # Creates a connection to the users profile
        self.user = self.api.me()

    @staticmethod
    def choose_random_png_from_path(path):
        return str(choice(list(path.glob("*.png"))))

    def set_profile_image(self, *, path):
        image = self.choose_random_png_from_path(path)
        self.logger.debug(f"Setting profile image to {image}.")
        self.api.update_profile_image(image)

    def set_profile_banner(self, *, path):
        banner = self.choose_random_png_from_path(path)
        self.logger.debug(f"Setting profile banner to {banner}.")
        self.api.update_profile_banner(banner)

    def set_profile_color(self, *, color):
        self.logger.debug(f"Setting profile color to {color}.")
        self.api.update_profile(profile_link_color=color)

    def set_profile_description(self, *, description):
        self.logger.debug(f"Setting profile description to {description}.")
        self.api.update_profile(description=description)

    def set_profile_username_suffix(self, *, username, suffix):
        name = f"{username}{suffix}"
        self.logger.debug(f"Setting profile name to {name}.")
        self.api.update_profile(name=name)


# from decouple import config
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
