import pytest

from decouple import config

from bitc0in_twitter.twitter import TwitterHandler

from pathlib import Path

from random import randint

TEST_BANNER_IMAGE_PATH = Path(__file__).parent / "images" / "test_banner"
TEST_PROFILE_IMAGE_PATH = Path(__file__).parent / "images" / "test_profile"


@pytest.fixture
def TwitterFixture():
    key = config("CONSUMER_KEY")
    secret = config("CONSUMER_SECRET")
    token = config("ACCESS_KEY")
    token_secret = config("ACCESS_SECRET")
    return TwitterHandler(key=key, secret=secret, token=token, token_secret=token_secret)


def test_image_paths_exists():
    assert TEST_BANNER_IMAGE_PATH.exists()
    assert TEST_PROFILE_IMAGE_PATH.exists()


def test_choose_random_png_from_path(TwitterFixture):
    image = TwitterFixture.choose_random_png_from_path(TEST_BANNER_IMAGE_PATH)
    assert image.endswith(".png")
    image = TwitterFixture.choose_random_png_from_path(TEST_PROFILE_IMAGE_PATH)
    assert image.endswith(".png")


@pytest.mark.online
def test_set_profile_image(TwitterFixture):
    t_before = TwitterFixture.user.profile_image_url
    TwitterFixture.set_profile_image(path=TEST_PROFILE_IMAGE_PATH)
    t_after = TwitterFixture.user.profile_image_url
    assert t_before != t_after


@pytest.mark.online
def test_set_banner_image(TwitterFixture):
    t_before = TwitterFixture.user.profile_banner_url
    TwitterFixture.set_profile_banner(path=TEST_BANNER_IMAGE_PATH)
    t_after = TwitterFixture.user.profile_banner_url
    assert t_before != t_after


def create_random_hex_color():
    def random_color():
        return randint(0, 255)

    return f"#{random_color():02x}{random_color():02x}{random_color():02x}".upper()


@pytest.mark.online
def test_profile_color(TwitterFixture):
    test_color = create_random_hex_color()
    t_before = TwitterFixture.user.profile_link_color
    TwitterFixture.set_profile_color(color=test_color)

    t_after = TwitterFixture.user.profile_link_color
    assert t_before != t_after

    TwitterFixture.set_profile_color(color=t_before)
    t_clean_up = TwitterFixture.user.profile_link_color

    assert t_before == t_clean_up


@pytest.mark.online
def test_set_profile_description(TwitterFixture):
    t_before = TwitterFixture.user.description
    TwitterFixture.set_profile_description(description="testing description")
    t_after = TwitterFixture.user.description
    assert t_before != t_after

    TwitterFixture.set_profile_description(description=t_before)
    t_clean = TwitterFixture.user.description
    assert t_before == t_clean
