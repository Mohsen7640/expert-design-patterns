from abc import ABC, abstractmethod

from solid.liskov_substitution_principle.file.contracts.encode_file_interface import EncodeFileInterface


class FileServiceInterface(ABC):

    @abstractmethod
    def encode(self, file: EncodeFileInterface):
        pass
