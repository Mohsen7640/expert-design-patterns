from structural.decorator.invoice.concretes.service_invoice_price import ServiceInvoicePrice
from structural.decorator.invoice.concretes.vat_invoice_price import VatInvoicePrice
from structural.decorator.invoice.services.invoice import Invoice


def run():
    invoice = Invoice()

    vat = VatInvoicePrice(invoice)
    service = ServiceInvoicePrice(vat)

    print(service.price())


if __name__ == '__main__':
    run()
