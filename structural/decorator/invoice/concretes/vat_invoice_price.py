from structural.decorator.invoice.contracts.invoice_price import InvoicePrice
from structural.decorator.invoice.decorators.invoice_price_decorator import InvoicePriceDecorator


class VatInvoicePrice(InvoicePriceDecorator):

    def __init__(self, invoice_price: InvoicePrice):
        super().__init__(invoice_price)

    def price(self):
        return self.invoice_price.price() + (self.invoice_price.price() * 0.09)
