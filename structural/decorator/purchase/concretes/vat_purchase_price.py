from structural.decorator.purchase.contracts.purchase_price import PurchasePrice
from structural.decorator.purchase.decorators.purchase_price_decorator import PurchasePriceDecorator
from structural.decorator.purchase.models.vat import Vat


class VatPurchasePrice(PurchasePriceDecorator):

    def __init__(self, purchase_price: PurchasePrice):
        super().__init__(purchase_price)
        self.address = self.purchase_price.address

    def total_price(self):
        vat_percent = Vat.VATS.get(self.address.country)
        total_price = self.purchase_price.total_price()
        vat_plus_total_price = total_price + (total_price * (vat_percent / 100))
        return vat_plus_total_price
