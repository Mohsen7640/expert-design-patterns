from abc import ABC, abstractmethod


class Presentation(ABC):

    @abstractmethod
    def present(self):
        pass
