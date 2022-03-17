from abc import ABC, abstractmethod


class StateInterface(ABC):

    def __init__(self):
        self.post = None

    def set_post(self, post):
        self.post = post

    @abstractmethod
    def draft(self):
        pass

    @abstractmethod
    def moderation(self):
        pass

    @abstractmethod
    def published(self):
        pass
