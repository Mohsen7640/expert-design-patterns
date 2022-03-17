from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def accept(self, visitor):
        pass
