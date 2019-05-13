from pathlib import Path
import pytest
from bitc0in_twitter.utilities import (
    check_image_dimensions,
    check_image_file_size,
    check_hex_color_format,
    ImageError,
)


@pytest.fixture
def image_fixture():
    TEST_IMAGE_FOLDER = Path(__file__).parent / "images"
    bad, good = list(TEST_IMAGE_FOLDER.glob("*"))
    yield bad, good


def test_good_check_image_dimensions(image_fixture):
    _, good = image_fixture
    try:
        check_image_dimensions(good, expected_width=400, expected_height=400)
    except ImageError:
        pytest.fail("An Images Error was raised.")


def test_bad_check_image_dimensions(image_fixture):
    bad, _ = image_fixture
    with pytest.raises(ImageError):
        check_image_dimensions(bad, expected_width=400, expected_height=400)


def test_good_check_image_file_size(image_fixture):
    _, good = image_fixture
    try:
        check_image_file_size(good, max_bytes=2024)
    except ImageError:
        pytest.fail("An Images Error was raised.")


def test_bad_check_image_file_size(image_fixture):
    bad, _ = image_fixture
    with pytest.raises(ImageError):
        check_image_file_size(bad, max_bytes=2024)
