from abc import ABC, abstractmethod


class EmailNotifier(ABC):

    @abstractmethod
    def send_email(self):
        pass
