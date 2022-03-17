from typing import Callable

from solid.open_close_principle.sloution.contracts.encoder_factory_config_interface import EncoderFactoryConfigInterface
from solid.open_close_principle.sloution.contracts.encoder_factory_interface import EncoderFactoryInterface


class EncoderFactory(EncoderFactoryInterface, EncoderFactoryConfigInterface):
    """
    Factories ==> {"XML": XMLEncoder(), "JSON": JSONEncoder(), "YAML": YAMLEncoder()}
    """
    factories = dict()

    @classmethod
    def add_encoder_factory(cls, format_to, factory: Callable):
        cls.factories.setdefault(format_to.lower(), factory)

    @classmethod
    def create_encoder(cls, format_to):
        if cls.factories.get(format_to, None) is None:
            raise Exception("Invalid format")

        factory = cls.factories.get(format_to)
        return factory()
