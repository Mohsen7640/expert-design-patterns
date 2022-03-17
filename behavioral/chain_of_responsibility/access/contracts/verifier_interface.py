from abc import ABC, abstractmethod


class VerifierInterface(ABC):

    @abstractmethod
    def verify(self, user, product):
        pass
