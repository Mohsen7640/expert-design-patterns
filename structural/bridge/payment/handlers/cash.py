from structural.bridge.payment.contracts.handler import PaymentHandler


class CashHandler(PaymentHandler):

    def pay(self, invoice):
        print('Cash Handler')