from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def notify(self, event, emitter, data=None):
        pass
