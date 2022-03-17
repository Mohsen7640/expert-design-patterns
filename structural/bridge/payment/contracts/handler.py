from abc import ABC, abstractmethod


class PaymentHandler(ABC):

    @abstractmethod
    def pay(self, invoice):
        pass
