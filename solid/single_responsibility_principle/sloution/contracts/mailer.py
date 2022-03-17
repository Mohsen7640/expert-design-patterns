from abc import ABC, abstractmethod


class MailerInterface(ABC):

    @abstractmethod
    def send(self, message):
        pass
