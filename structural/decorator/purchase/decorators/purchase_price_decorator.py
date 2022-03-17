from structural.decorator.purchase.contracts.purchase_price import PurchasePrice


class PurchasePriceDecorator(PurchasePrice):

    def __init__(self, purchase_price: PurchasePrice):
        self.purchase_price = purchase_price

    def total_price(self):
        return self.purchase_price.total_price()
