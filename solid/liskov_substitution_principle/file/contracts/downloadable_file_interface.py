from abc import abstractmethod

from solid.liskov_substitution_principle.file.contracts.file_interface import FileInterface


class DownloadableFileInterface(FileInterface):

    @abstractmethod
    def download(self) -> bool:
        pass
