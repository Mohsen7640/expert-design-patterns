from abc import ABC, abstractmethod


class OrderInterface(ABC):

    def __init__(self):
        self.order = None

    def set_order(self, order):
        self.order = order

    @abstractmethod
    def pending(self):
        pass

    @abstractmethod
    def paid(self):
        pass

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def ready(self):
        pass

    @abstractmethod
    def sent(self):
        pass

    @abstractmethod
    def delivered(self):
        pass
