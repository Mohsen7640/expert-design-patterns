from behavioral.strategy.payment.contracts.method import PaymentMethod


class PaymentService:

    def __init__(self, method: PaymentMethod):
        self.method = method

    def pay(self, order):
        self.method.do_payment(order)