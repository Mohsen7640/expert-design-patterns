from abc import ABC, abstractmethod


class TranslatorInterface(ABC):

    @abstractmethod
    def translate(self, text):
        pass
