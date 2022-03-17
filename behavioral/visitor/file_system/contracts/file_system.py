from abc import ABC, abstractmethod


class FileSystem(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass
