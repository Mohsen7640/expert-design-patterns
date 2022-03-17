from solid.open_close_principle.sloution.contracts.encoder_factory_interface import EncoderFactoryInterface


class GenericEncoder:

    def __init__(self, encoder_factory: EncoderFactoryInterface):
        self.encoder_factory = encoder_factory

    def encode(self, data, format_to):
        encoder = self.encoder_factory.create_encoder(format_to)
        return encoder.encode(data)
