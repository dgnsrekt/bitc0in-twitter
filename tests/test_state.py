import pytest
from bitc0in_twitter.state import MarketState


class MarketStateT(MarketState):
    def __init__(self, state):
        super().__init__(state)

    def transition_bullish(self):
        return "bullish"

    def transition_bearish(self):
        return "bearish"


@pytest.fixture
def bitcoin_state_start_bullish():
    state = MarketStateT("bullish")
    return state


def test_default_starts_bullish(bitcoin_state_start_bullish):
    t_expected_state = "bullish"
    t_current_state = bitcoin_state_start_bullish.state
    assert t_expected_state == t_current_state


def test_bullish_transition_to_bullish(bitcoin_state_start_bullish):
    t_expected_state = "bullish"
    bitcoin_state_start_bullish.pumping()
    t_current_state = bitcoin_state_start_bullish.state
    assert t_expected_state == t_current_state


def test_bullish_transition_to_bearish(bitcoin_state_start_bullish):
    t_inital_state = bitcoin_state_start_bullish.state
    t_expected_state = "bullish"
    assert t_inital_state == t_expected_state

    bitcoin_state_start_bullish.dumping()
    t_changed_state = bitcoin_state_start_bullish.state
    t_expected_state = "bearish"
    assert t_changed_state == t_expected_state


@pytest.fixture
def bitcoin_state_start_bearish():
    state = MarketStateT("bearish")
    return state


def test_starts_bearish(bitcoin_state_start_bearish):
    t_expected_state = "bearish"
    t_current_state = bitcoin_state_start_bearish.state
    assert t_expected_state == t_current_state


def test_bearish_transition_to_bearish(bitcoin_state_start_bearish):
    t_expected_state = "bearish"
    bitcoin_state_start_bearish.dumping()
    t_current_state = bitcoin_state_start_bearish.state
    assert t_expected_state == t_current_state

    bitcoin_state_start_bearish.pumping()
    assert bitcoin_state_start_bearish.state == "bullish"


def test_bearish_transition_to_bullish(bitcoin_state_start_bearish):
    t_inital_state = bitcoin_state_start_bearish.state
    t_expected_state = "bearish"
    assert t_inital_state == t_expected_state

    bitcoin_state_start_bearish.pumping()
    t_changed_state = bitcoin_state_start_bearish.state
    t_expected_state = "bullish"
    assert t_changed_state == t_expected_state
