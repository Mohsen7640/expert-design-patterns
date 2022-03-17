from abc import ABC, abstractmethod


class Notifier(ABC):
    """
        Interface
    """
    @abstractmethod
    def send(self, message):
        pass
