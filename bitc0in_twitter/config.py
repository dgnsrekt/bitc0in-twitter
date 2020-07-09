from collections import namedtuple

from decouple import UndefinedValueError, config

import logme

from paths import BANNER_BEARISH_PATH, BANNER_BULLISH_PATH
from paths import PROFILE_BEARISH_PATH, PROFILE_BULLISH_PATH

from utilities import check_hex_color_format, check_image_dimensions, check_image_file_size


config_logger = logme.log(scope="module", name="config")


class ConfigurationError(Exception):
    pass


class Configuration:
    ConfigurationOptions = namedtuple(
        "ConfigurationOptions", ["image", "banner", "color", "description"]
    )
    ConfigurationOptions.__new__.__defaults__ = (False, False, False, False)

    def __init__(self):
        self.key = config("CONSUMER_KEY")
        self.secret = config("CONSUMER_SECRET")
        self.token = config("ACCESS_KEY")
        self.token_secret = config("ACCESS_SECRET")

        image = config("CONTROL_PROFILE_IMAGE", cast=bool)
        banner = config("CONTROL_BANNER_IMAGE", cast=bool)
        color = config("CONTROL_PROFILE_COLOR", cast=bool)
        description = config("CONTROL_PROFILE_DESCRIPTION", cast=bool)

        self.options = Configuration.ConfigurationOptions(image, banner, color, description)

        if self.options.image:
            config_logger.debug("Checking profile picture images are configured.")
            self.check_path_images(
                PROFILE_BULLISH_PATH, expected_width=400, expected_height=400, max_bytes=2024
            )
            self.check_path_images(
                PROFILE_BEARISH_PATH, expected_width=400, expected_height=400, max_bytes=2024
            )
            config_logger.info("Profile pictures are properly configured.")

        if self.options.banner:
            # TODO: Find the max byte size of a banner.
            config_logger.debug("Checking profile banner images are configured.")
            self.check_path_images(
                BANNER_BULLISH_PATH, expected_width=1500, expected_height=500, max_bytes=4048
            )
            self.check_path_images(
                BANNER_BEARISH_PATH, expected_width=1500, expected_height=500, max_bytes=4048
            )
            config_logger.info("Profile banners are properly configured.")

        if self.options.color:
            config_logger.debug("Checking profile colors are configured.")
            self.check_required_setting_exists("BULLISH_PROFILE_LINK_COLOR")
            self.check_required_setting_exists("BEARISH_PROFILE_LINK_COLOR")

            check_hex_color_format(config("BULLISH_PROFILE_LINK_COLOR"))
            check_hex_color_format(config("BEARISH_PROFILE_LINK_COLOR"))
            config_logger.info("Profile color configuration has been set.")

        if self.options.description:
            # TODO: CHECK LESS THAN MAX CHARS LEN
            config_logger.debug("Checking profile descriptions are configured.")
            self.check_required_setting_exists("BULLISH_PROFILE_DESCRIPTION")
            self.check_required_setting_exists("BEARISH_PROFILE_DESCRIPTION")
            config_logger.info("Profile description has been set.")

    def get_twitter_keys(self):
        return self.key, self.secret, self.token, self.token_secret

    @staticmethod
    def check_path_images(image_path, **kwargs):
        config_logger.debug(f"Checking '{image_path}' has png image files.")
        images = list(image_path.glob("*.png"))
        if len(images) < 0:
            raise ConfigurationError(f"Please add a png image to {image_path}.")
        for image in images:
            check_image_dimensions(image, **kwargs)
            check_image_file_size(image, **kwargs)

    @staticmethod
    def check_required_setting_exists(setting):
        config_logger.debug(f"Checking {setting} exists.")
        try:
            if len(config(setting).strip()) < 1:
                raise ConfigurationError(f"Please add a {setting} setting to the .env file.")
        except UndefinedValueError:
            raise ConfigurationError(f"Please add a {setting} setting to the .env file.")
