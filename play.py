from bitc0in_twitter.twitter import TwitterHandler
from bitc0in_twitter.paths import HEADER_BULLISH_PATH, HEADER_BEARISH_PATH
from bitc0in_twitter.paths import PROFILE_BULLISH_PATH, PROFILE_BEARISH_PATH
import os
from random import choice, randint
from pathlib import Path
from decouple import config


KEY = config("CONSUMER_KEY")
SECRET = config("CONSUMER_SECRET")
TOKEN = config("ACCESS_KEY")
TOKEN_SECRET = config("ACCESS_SECRET")

profile = TwitterHandler(key=KEY, secret=SECRET, token=TOKEN, token_secret=TOKEN_SECRET)


def bullish():
    header = str(choice(list(HEADER_BULLISH_PATH.glob("*.png"))))
    profile_pic = str(choice(list(PROFILE_BULLISH_PATH.glob("*.png"))))
    username = "run2dev"
    username_suffix = "[PUMPIT]"
    description = "TOO THE MOON!!!!!"
    username = f"{username}{username_suffix}"
    profile.api.update_profile(profile_link_color="#00AA00")
    profile.api.update_profile(description=description)
    profile.api.update_profile(name=username)
    profile.api.update_profile_image(profile_pic)
    profile.api.update_profile_banner(header, width=1500, height=500)
    profile.api.update_status(status=f"testing bullish {randint(0, 1000)}")


def bearish():
    header = str(choice(list(HEADER_BEARISH_PATH.glob("*.png"))))
    profile_pic = str(choice(list(PROFILE_BEARISH_PATH.glob("*.png"))))
    username = "run2dev"
    username_suffix = "[DUMPIT]"
    description = "BITCOIN IS A SCAM!!!!!"
    username = f"{username}{username_suffix}"
    profile.api.update_profile(profile_link_color="#FF001F")
    profile.api.update_profile(description=description)
    profile.api.update_profile(name=username)
    profile.api.update_profile_image(profile_pic)
    profile.api.update_profile_banner(header, width=1500, height=500)
    profile.api.update_status(status=f"testing bearish {randint(0, 1000)}")


print(config("CONTROL_PROFILE_IMAGE", cast=bool))
print(config("CONTROL_HEADER_IMAGE", cast=bool))
print(config("CONTROL_PROFILE_COLOR", cast=bool))
print(config("CONTROL_PROFILE_DESCRIPTION", cast=bool))
print(config("ADD_USERNAME_SUFFIX", cast=bool))

print(config("PROFILE_USERNAME", cast=str))
