from abc import ABC, abstractmethod


class FileCommand(ABC):

    @abstractmethod
    def execute(self):
        pass
