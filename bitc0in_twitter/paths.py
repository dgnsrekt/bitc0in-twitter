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


def check_paths_status():
    """Shows the status of all the above paths."""
    global_variables = globals().copy()

    for key, value in global_variables.items():
        if "_PATH" in key:
            print(key, value, value.exists())


if __name__ == "__main__":
    check_paths_status()
