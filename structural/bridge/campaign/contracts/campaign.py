from abc import ABC, abstractmethod


class Campaign(ABC):

    def __init__(self, promotion):
        self.promotion = promotion

    @abstractmethod
    def run(self):
        pass
