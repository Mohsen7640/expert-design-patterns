from abc import ABC, abstractmethod

from structural.adapter.payment.models.invoice import Invoice


class Gateway(ABC):

    @abstractmethod
    def do_payment(self, invoice: Invoice):
        pass
