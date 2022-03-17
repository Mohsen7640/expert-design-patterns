from structural.bridge.payment.contracts.method import PaymentMethod


class CashPayment(PaymentMethod):

    def __init__(self, handler):
        super().__init__(handler)

    def start_pay(self, invoice):
        self.handler.pay(invoice)
