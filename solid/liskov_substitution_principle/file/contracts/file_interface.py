from abc import ABC, abstractmethod


class FileInterface(ABC):

    @abstractmethod
    def rename(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def copy(self):
        pass
