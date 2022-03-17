from abc import ABC, abstractmethod

from behavioral.chain_of_responsibility.registration.models.registration import Registration


class CheckerInterface(ABC):

    @abstractmethod
    def check(self, registration: Registration):
        pass
