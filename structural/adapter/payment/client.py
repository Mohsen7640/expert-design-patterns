from structural.adapter.payment.models.invoice import Invoice
from structural.adapter.payment.providers.mellat.mellat import MellatProvider
from structural.adapter.payment.providers.saman.saman_adapter import SamanAdapter
from structural.adapter.payment.providers.saman.saman_api import SamanAPI
from structural.adapter.payment.providers.zarinpal.zarinpal import ZarinpalProvider


def run():
    invoice = Invoice(amount=100)

    zarinpal = ZarinpalProvider()
    print(zarinpal.do_payment(invoice))

    mellat = MellatProvider()
    print(mellat.do_payment(invoice))

    saman_api = SamanAPI("5562-412r-rtq23-ij231j")
    saman = SamanAdapter(saman_api)
    print(saman.do_payment(invoice))


if __name__ == "__main__":
    run()
