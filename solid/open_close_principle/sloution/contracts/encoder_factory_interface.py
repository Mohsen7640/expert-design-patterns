from abc import ABC, abstractmethod


class EncoderFactoryInterface(ABC):

    @classmethod
    @abstractmethod
    def create_encoder(cls, format_to):
        pass
