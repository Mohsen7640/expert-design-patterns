from abc import ABC, abstractmethod


class SMSNotifier(ABC):

    @abstractmethod
    def send_sms(self):
        pass
