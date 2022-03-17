from structural.adapter.payment.contracts.gateway import Gateway
from structural.adapter.payment.models.invoice import Invoice


class ZarinpalProvider(Gateway):

    def do_payment(self, invoice: Invoice):
        return f'Do Payment In Zarinpal Gateway => {invoice}'
