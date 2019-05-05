# This module provides functionality dealing with state.

from transitions import Machine
from abc import abstractmethod, ABCMeta


class MarketState(metaclass=ABCMeta):

    states = ["bullish", "bearish"]

    def __init__(self, initial_state):
        self.machine = Machine(model=self, states=MarketState.states, initial=initial_state)

        self.machine.add_transition(trigger="pumping", source="bullish", dest="bullish")
        self.machine.add_transition(trigger="dumping", source="bearish", dest="bearish")
        self.machine.add_transition(
            trigger="pumping", source="bearish", dest="bullish", after="transition_bullish"
        )
        self.machine.add_transition(
            trigger="dumping", source="bullish", dest="bearish", after="transition_bearish"
        )

    @abstractmethod
    def transition_bullish(self):
        pass

    @abstractmethod
    def transition_bearish(self):
        pass
