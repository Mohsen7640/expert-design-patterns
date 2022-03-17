from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def get(self):
        pass
