# This module provides functionality dealing with state.

from transitions import Machine, State
from abc import abstractmethod, ABCMeta


class MarketState(metaclass=ABCMeta):

    states = ["bullish", "bearish"]

    def __init__(self):
        self.machine = Machine(model=self, states=MarketState.states, initial="bullish")

        self.machine.add_transition(trigger="positive", source="bullish", dest="bullish")
        self.machine.add_transition(trigger="negative", source="bearish", dest="bearish")
        self.machine.add_transition(
            trigger="positive", source="bearish", dest="bullish", after="transition_bullish"
        )
        self.machine.add_transition(
            trigger="negative", source="bullish", dest="bearish", after="transition_bearish"
        )

    @abstractmethod
    def transition_bullish(self):
        pass

    @abstractmethod
    def transition_bearish(self):
        pass


class BitcoinMarketState(MarketState):
    def transition_bullish(self):
        print("going bullish")

    def transition_bearish(self):
        print("going bearish")
