from abc import ABC, abstractmethod


class DeliveryMethod(ABC):

    @abstractmethod
    def deliver(self, order):
        pass

    @abstractmethod
    def price(self, order):
        pass
