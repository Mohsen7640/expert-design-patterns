from structural.adapter.payment.contracts.gateway import Gateway
from structural.adapter.payment.models.invoice import Invoice
from structural.adapter.payment.providers.saman.saman_api import SamanAPI


class SamanAdapter(Gateway):

    def __init__(self, saman_api: SamanAPI):
        self.saman_api = saman_api

    def do_payment(self, invoice: Invoice):
        return self.saman_api.pay(invoice.get_amount())