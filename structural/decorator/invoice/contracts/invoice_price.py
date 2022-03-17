from abc import ABC, abstractmethod


class InvoicePrice(ABC):

    @abstractmethod
    def price(self):
        pass
