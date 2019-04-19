from pathlib import Path
from appdirs import user_config_dir

BASE_PATH = Path(__file__).parent

CONFIG_PATH = Path(user_config_dir(appname=BASE_PATH.name, appauthor="dgnsrekt"))

IMAGE_PATH = BASE_PATH.parent / "images"

HEADER_PATH = IMAGE_PATH / "header"
PROFILE_PATH = IMAGE_PATH / "profile"

HEADER_BULLISH_PATH = HEADER_PATH / "bullish"
HEADER_BEARISH_PATH = HEADER_PATH / "bearish"

PROFILE_BULLISH_PATH = PROFILE_PATH / "bullish"
PROFILE_BEARISH_PATH = PROFILE_PATH / "bearish"

if __name__ == "__main__":
    print("BASE_PATH:", BASE_PATH, BASE_PATH.exists())
    print("CONFIG_PATH:", CONFIG_PATH, CONFIG_PATH.exists())
    print("IMAGE_PATH:", IMAGE_PATH, IMAGE_PATH.exists())
    print("HEADER_BULLISH:", HEADER_BULLISH_PATH, HEADER_BULLISH_PATH.exists())
    print("HEADER_BEARISH:", HEADER_BEARISH_PATH, HEADER_BEARISH_PATH.exists())
    print("PROFILE_BULLISH_PATH:", PROFILE_BULLISH_PATH, PROFILE_BULLISH_PATH.exists())
    print("PROFILE_BEARISH_PATH:", PROFILE_BEARISH_PATH, PROFILE_BEARISH_PATH.exists())
