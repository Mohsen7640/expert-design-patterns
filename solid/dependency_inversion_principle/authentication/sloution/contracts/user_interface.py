from abc import ABC, abstractmethod


class UserProviderInterface(ABC):

    @abstractmethod
    def find_user(self, username):
        pass
