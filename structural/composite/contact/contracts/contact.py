from abc import ABC, abstractmethod


class Contact(ABC):

    @abstractmethod
    def send(self, message):
        pass
