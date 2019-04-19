from bitc0in_twitter.btc import get_percent_change


def test_get_percent_change():
    btc = get_percent_change()
    assert isinstance(btc, float)
