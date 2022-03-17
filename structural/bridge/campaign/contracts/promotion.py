from abc import ABC, abstractmethod


class Promotion(ABC):

    @abstractmethod
    def display(self):
        pass
