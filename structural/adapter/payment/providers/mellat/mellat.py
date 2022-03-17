from structural.adapter.payment.contracts.gateway import Gateway
from structural.adapter.payment.models.invoice import Invoice


class MellatProvider(Gateway):

    def do_payment(self, invoice: Invoice):
        return f'Do Payment In Mellat Gateway => {invoice}'