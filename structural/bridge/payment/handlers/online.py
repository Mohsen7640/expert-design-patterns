from structural.bridge.payment.contracts.handler import PaymentHandler


class ZarinpalHandler(PaymentHandler):

    def pay(self, invoice):
        print('Zarinpal Handler')


class MellatHandler(PaymentHandler):

    def pay(self, invoice):
        print('Mellat Handler')
