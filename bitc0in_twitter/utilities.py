from PIL import Image


class ImageError(Exception):
    pass


def check_image_dimensions(image: str, *, expected_width: int, expected_height: int, **kwargs):
    """Checks an images is within a certian specification.

    :param image: The path to the location of the image.
    :param expected_width: The width the image should be in pixels.
    :param expected_height: The height the image should be in pixels.
    :raises ImagesError: When the width or height is wrong.
    """
    with Image.open(image) as img:
        width, height = img.size

    if width != expected_width:
        raise ImageError(f"{image} width is {width} and should be {expected_width}.")
    if height != expected_height:
        raise ImageError(f"{image} height is {height} and should be {expected_height}.")


def check_image_file_size(image: str, *, max_bytes: int, **kwargs):
    """Checks the size of the file in bytes.

    :param image: The path to the location of the image.
    :param max_bytes: The max allowed size of the image in bytes.
    :raises ImageError: When the size of the file is greater than the max_bytes.
    """
    image_bytes = image.stat().st_size
    if image_bytes > max_bytes:
        raise ImageError(f"{image} size is {image_bytes} bytes and should be {max_bytes} bytes.")


def check_hex_color_format(color: str):
    """Checks the hex color is a properly formatted RGB hex string.

    :param color: The color to check.
    :raises ValueError: When the color is not in the following format #000000.
    """
    if not color.startswith("#"):
        raise ValueError(f"{color} should start with a #.")
    try:
        int(color[1:], 16)
    except ValueError:
        raise ValueError(f"{color} should be in rgb hex format. Example: #00FF11.")

    if len(color) != 7:
        raise ValueError(f"{color} should be in rgb hex format. Example: #00FF11.")


# from paths import PROFILE_BEARISH_PATH, PROFILE_BULLISH_PATH
# photo = list(PROFILE_BEARISH_PATH.glob("*.png"))[0]
# check_image_dimensions(photo, expected_width=400, expected_height=400)
# check_image_file_size(photo, max_bytes=2048)
# check_hex_color_format("#00FFb1")
