from pathlib import Path

BASE_PATH = Path(__file__).parent

IMAGE_PATH = BASE_PATH.parent / "images"

BANNER_PATH = IMAGE_PATH / "banner"
PROFILE_PATH = IMAGE_PATH / "profile"

BANNER_BULLISH_PATH = BANNER_PATH / "bullish"
BANNER_BEARISH_PATH = BANNER_PATH / "bearish"

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
