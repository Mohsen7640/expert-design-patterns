from abc import ABC, abstractmethod


class PurchasePrice(ABC):

    @abstractmethod
    def total_price(self):
        pass
