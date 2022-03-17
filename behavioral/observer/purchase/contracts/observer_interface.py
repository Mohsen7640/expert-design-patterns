from abc import ABC, abstractmethod


class ObserverInterface(ABC):

    @abstractmethod
    def send(self, message):
        pass
