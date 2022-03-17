from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    def __init__(self, handler):
        self.handler = handler

    @abstractmethod
    def start_pay(self, invoice):
        pass
