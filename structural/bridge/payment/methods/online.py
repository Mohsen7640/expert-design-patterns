from structural.bridge.payment.contracts.method import PaymentMethod


class ZarinpalOnlinePayment(PaymentMethod):

    def __init__(self, handler):
        super().__init__(handler)

    def start_pay(self, invoice):
        self.handler.pay(invoice)


class MellatOnlinePayment(PaymentMethod):

    def __init__(self, handler):
        super().__init__(handler)

    def start_pay(self, invoice):
        self.handler.pay(invoice)
