from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def price(self):
        pass
