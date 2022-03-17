from abc import ABC, abstractmethod


class StateInterface(ABC):

    @abstractmethod
    def send_to_client(self):
        pass

    @abstractmethod
    def send_to_operator(self):
        pass

    @abstractmethod
    def send_to_supervisor(self):
        pass

    @abstractmethod
    def send_to_internal_manager(self):
        pass

    @abstractmethod
    def send_to_managing_director(self):
        pass
