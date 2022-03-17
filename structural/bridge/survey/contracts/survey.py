from abc import ABC, abstractmethod


class Survey(ABC):

    def __init__(self, presentation):
        self.presentation = presentation

    @abstractmethod
    def display(self):
        pass
