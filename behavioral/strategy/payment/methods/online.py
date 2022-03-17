from behavioral.strategy.payment.contracts.method import PaymentMethod


class OnlinePaymentMethod(PaymentMethod):

    def do_payment(self, order):
        pass
