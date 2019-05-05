from PIL import Image


class ImageError(Exception):
    pass


def check_image_dimensions(image, *, expected_width, expected_height, **kwargs):
    with Image.open(image) as img:
        width, height = img.size

    if width != expected_width:
        raise ImageError(f"{image} width is {width} and should be {expected_width}.")
    if height != expected_height:
        raise ImageError(f"{image} height is {height} and should be {expected_height}.")


def check_image_file_size(image, *, max_bytes, **kwargs):
    image_bytes = image.stat().st_size
    if image_bytes > max_bytes:
        raise ImageError(f"{image} size is {image_bytes} bytes and should be {max_bytes} bytes.")


def check_rgb_format(rbg_string):
    if not rbg_string.startswith("#"):
        raise ValueError(f"{rbg_string} should start with a #.")

    try:
        int(rbg_string[1:], 16)
    except ValueError:
        raise ValueError(f"{rbg_string} should be in rgb hex format. Example: #00FF11.")


# from paths import PROFILE_BEARISH_PATH, PROFILE_BULLISH_PATH
# photo = list(PROFILE_BEARISH_PATH.glob("*.png"))[0]
# check_image_dimensions(photo, expected_width=400, expected_height=400)
# check_image_file_size(photo, max_bytes=2048)
# check_rgb_format("#00FF11")
