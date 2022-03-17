from abc import ABC, abstractmethod


class Exchange(ABC):

    @abstractmethod
    def exchange(self, product):
        pass
