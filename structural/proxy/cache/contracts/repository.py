from abc import ABC, abstractmethod


class RepositoryInterface(ABC):

    @abstractmethod
    def all(self):
        pass
