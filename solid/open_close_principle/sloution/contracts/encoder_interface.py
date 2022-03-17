from abc import ABC, abstractmethod


class EncoderInterface(ABC):

    @abstractmethod
    def encode(self, data):
        pass