from structural.bridge.payment.handlers.online import ZarinpalHandler
from structural.bridge.payment.methods.online import ZarinpalOnlinePayment
from structural.bridge.payment.models.invoice import Invoice


def run():
    invoice = Invoice(title='sample', price=200000)
    zarinpal_handler = ZarinpalHandler()
    zarinpal = ZarinpalOnlinePayment(zarinpal_handler)
    zarinpal.start_pay(invoice)


if __name__ == "__main__":
    run()