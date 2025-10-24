from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def display_profile(self):
        pass
