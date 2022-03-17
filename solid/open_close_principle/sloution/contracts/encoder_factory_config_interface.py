from abc import ABC, abstractmethod


class EncoderFactoryConfigInterface(ABC):

    @classmethod
    @abstractmethod
    def add_encoder_factory(cls, format_to, factory):
        pass
