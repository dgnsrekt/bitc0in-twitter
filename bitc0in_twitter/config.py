from decouple import config, UndefinedValueError
from utilities import check_image_dimensions, check_image_file_size, check_rgb_format

from paths import PROFILE_BEARISH_PATH, PROFILE_BULLISH_PATH
from paths import HEADER_BEARISH_PATH, HEADER_BULLISH_PATH


class ConfigurationError(Exception):
    pass


class Configuration:
    def __init__(self):
        self.key = config("CONSUMER_KEY")
        self.secret = config("CONSUMER_SECRET")
        self.token = config("ACCESS_KEY")
        self.token_secret = config("ACCESS_SECRET")

        # TODO: add a twitter cred check, might get the username from here
        # or maybe keep this decoupled from the twitter handler

        self.control_profile_image = config("CONTROL_PROFILE_IMAGE", cast=bool)
        self.control_header_image = config("CONTROL_HEADER_IMAGE", cast=bool)
        self.control_profile_color = config("CONTROL_PROFILE_COLOR", cast=bool)
        self.control_profile_description = config("CONTROL_PROFILE_DESCRIPTION", cast=bool)
        self.add_username_suffix = config("ADD_USERNAME_SUFFIX", cast=bool)

        if self.control_profile_image:
            self.check_path_images(
                PROFILE_BULLISH_PATH, expected_width=400, expected_height=400, max_bytes=2024
            )
            self.check_path_images(
                PROFILE_BEARISH_PATH, expected_width=400, expected_height=400, max_bytes=2024
            )

        if self.control_header_image:
            # FIND MAX SIZE
            self.check_path_images(
                HEADER_BULLISH_PATH, expected_width=1500, expected_height=500, max_bytes=4048
            )
            self.check_path_images(
                HEADER_BEARISH_PATH, expected_width=1500, expected_height=500, max_bytes=4048
            )

        if self.control_profile_color:
            print("Checking for bullish and bearish profile colors.")
            self.check_required_setting_exists("BULLISH_PROFILE_LINK_COLOR")
            self.check_required_setting_exists("BEARISH_PROFILE_LINK_COLOR")

            check_rgb_format(config("BULLISH_PROFILE_LINK_COLOR"))
            check_rgb_format(config("BEARISH_PROFILE_LINK_COLOR"))

        if self.control_profile_description:
            # TODO: CHECK LESS THAN MAX CHARS LEN
            print("Checking profile description.")
            self.check_required_setting_exists("BULLISH_PROFILE_DESCRIPTION")
            self.check_required_setting_exists("BEARISH_PROFILE_DESCRIPTION")

        if self.add_username_suffix:
            # TODO CHECK that username + space + suffix < max char len
            print("username_suffix check")
            self.check_required_setting_exists("PROFILE_USERNAME")
            self.check_required_setting_exists("BULLISH_PROFILE_USERNAME_SUFFIX")
            self.check_required_setting_exists("BEARISH_PROFILE_USERNAME_SUFFIX")

    @staticmethod
    def check_path_images(image_path, **kwargs):
        print(f"Checking '{image_path}' has png image files.")  # TODO: LOGGING
        images = list(image_path.glob("*.png"))
        if len(images) < 0:
            raise ConfigurationError(f"Please add a png image to {image_path}.")
        print(kwargs)
        for image in images:
            check_image_dimensions(image, **kwargs)
            check_image_file_size(image, **kwargs)

    @staticmethod
    def check_required_setting_exists(setting):
        print(f"Checking {setting} exists.")
        try:
            if len(config(setting).strip()) < 1:
                raise ConfigurationError(f"Please add a {setting} setting to the .env file.")
        except UndefinedValueError:
            raise ConfigurationError(f"Please add a {setting} setting to the .env file.")


conf = Configuration()
