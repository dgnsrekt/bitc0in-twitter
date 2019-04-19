import pytest
from bitc0in_twitter.state import BitcoinMarketState


@pytest.fixture
def bitcoin_state_start_bullish():
    state = BitcoinMarketState()
    return state


def test_default_starts_bullish(bitcoin_state_start_bullish):
    assert bitcoin_state_start_bullish.state == "bullish"


def test_bullish_transition_to_bullish(bitcoin_state_start_bullish):
    bitcoin_state_start_bullish.positive()
    assert bitcoin_state_start_bullish.state == "bullish"


def test_bullish_transition_to_bearish(bitcoin_state_start_bullish):
    assert bitcoin_state_start_bullish.state == "bullish"
    bitcoin_state_start_bullish.negative()
    assert bitcoin_state_start_bullish.state == "bearish"


@pytest.fixture
def bitcoin_state_start_bearish():
    state = BitcoinMarketState(initial_state="bearish")
    return state


def test_starts_bearish(bitcoin_state_start_bearish):
    assert bitcoin_state_start_bearish.state == "bearish"


def test_bearish_transition_to_bearish(bitcoin_state_start_bearish):
    bitcoin_state_start_bearish.negative()
    assert bitcoin_state_start_bearish.state == "bearish"


def test_bearish_transition_to_bullish(bitcoin_state_start_bearish):
    assert bitcoin_state_start_bearish.state == "bearish"
    bitcoin_state_start_bearish.positive()
    assert bitcoin_state_start_bearish.state == "bullish"
