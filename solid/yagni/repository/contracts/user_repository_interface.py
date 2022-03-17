from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):

    @abstractmethod
    def create(self, **kwargs):
        pass
