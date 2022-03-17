from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def do_payment(self, order):
        pass
