from solid.open_close_principle.problem.encoders.json_encoder import JSONEncoder
from solid.open_close_principle.problem.encoders.xml_encoder import XMLEncoder


class GenericEncoder:

    def encode(self, data, format_to):
        """
        Variation Single Responsibility and Open / Close Principle
        :param data:
        :param format_to:
        :return:
        """
        if format_to == "JSON":
            encoder = JSONEncoder()
        elif format_to == "XML":
            encoder = XMLEncoder()
        else:
            raise Exception("Invalid format.")

        return encoder.encode(data)
