from abc import ABC, abstractmethod
import random


class State(ABC):
    """Class to define a state object."""

    def __init__(self):
        print("Processing current state:", str(self))
        # TODO: change this to logging, f-string

    @abstractmethod
    def on_event(self, event):
        """Handle events that are delegated to this State."""
        pass

    def __repr__(self):
        """Leverages the __str__ method to describe the State."""
        return self.__str__()

    def __str__(self):
        """Returns the name of the State."""
        return self.__class__.__name__
