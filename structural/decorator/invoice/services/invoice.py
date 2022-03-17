from structural.decorator.invoice.contracts.invoice_price import InvoicePrice


class Invoice(InvoicePrice):

    def price(self):
        return 1000000
