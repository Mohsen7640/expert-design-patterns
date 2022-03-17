from abc import ABC, abstractmethod


class Notifier(ABC):

    @abstractmethod
    def send_sms(self):
        pass

    @abstractmethod
    def send_email(self):
        pass
