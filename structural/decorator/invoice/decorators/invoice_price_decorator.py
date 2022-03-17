from structural.decorator.invoice.contracts.invoice_price import InvoicePrice


class InvoicePriceDecorator(InvoicePrice):

    def __init__(self, invoice_price: InvoicePrice):
        self.invoice_price = invoice_price

    def price(self):
        return self.invoice_price.price()
