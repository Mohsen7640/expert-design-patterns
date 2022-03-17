from solid.liskov_substitution_principle.file.contracts.encode_file_interface import EncodeFileInterface
from solid.liskov_substitution_principle.file.contracts.file_service_interface import FileServiceInterface


class FileService(FileServiceInterface):

    def encode(self, file: EncodeFileInterface):
        pass
