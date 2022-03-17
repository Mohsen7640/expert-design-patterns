from structural.bridge.payment.contracts.handler import PaymentHandler


class ChequeHandler(PaymentHandler):

    def pay(self, invoice):
        print('Cheque Handler')

