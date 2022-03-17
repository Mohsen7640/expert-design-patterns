from abc import ABC, abstractmethod


class DispatcherInterface(ABC):

    @abstractmethod
    def dispatch(self, event, params):
        pass
