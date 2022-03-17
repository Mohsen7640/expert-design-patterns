from structural.decorator.purchase.contracts.purchase_price import PurchasePrice
from structural.decorator.purchase.decorators.purchase_price_decorator import PurchasePriceDecorator
from structural.decorator.purchase.models.service import Service


class ServicePurchasePrice(PurchasePriceDecorator):

    def __init__(self, purchase_price: PurchasePrice):
        super().__init__(purchase_price)
        self.address = self.purchase_price.address

    def total_price(self):
        service_price = Service.SERVICES.get(self.address.country)
        total_price = self.purchase_price.total_price()
        service_plus_total_price = total_price + service_price
        return service_plus_total_price
