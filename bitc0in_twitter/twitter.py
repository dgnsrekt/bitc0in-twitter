# Provides twitter api functionality.

from pathlib import Path
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

    @property
    def user(self):
        """The latests status of the users profile."""
        return self.api.me()

    @staticmethod
    def choose_random_png_from_path(path: Path) -> str:
        """Helper method which chooses a random png file from a given path.

        :param path: The path to search for the png.
        :returns: The location of a randomly choosen png file.
        """
        return str(choice(list(path.glob("*.png"))))

    def set_profile_image(self, *, path: Path) -> None:
        """Replaces the twitter profiles image with a randomly choosen image from the given path.

        :param path: The path to search for the png.
        """
        image = self.choose_random_png_from_path(path)
        self.logger.debug(f"Setting profile image to {image}.")
        self.api.update_profile_image(image)

    def set_profile_banner(self, *, path: Path) -> None:
        """Replaces the twitter profiles banner with a randomly choosen image from the given path.

        :param path: The path to search for the png.
        """
        banner = self.choose_random_png_from_path(path)
        self.logger.debug(f"Setting profile banner to {banner}.")
        self.api.update_profile_banner(banner)

    def set_profile_color(self, *, color: str) -> None:
        """Replaces the twitter profiles color.

        :param color: Hexidecimal rgb value.
        """
        self.logger.debug(f"Setting profile color to {color}.")
        self.api.update_profile(profile_link_color=color)

    def set_profile_description(self, *, description: str) -> None:
        """Replaces the twitter profiles description.

        :param description: The description of the twitter page.
        """
        self.logger.debug(f"Setting profile description to {description}.")
        self.api.update_profile(description=description)
