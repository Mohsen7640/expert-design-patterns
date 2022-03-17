from structural.decorator.purchase.concretes.service_purchase_price import ServicePurchasePrice
from structural.decorator.purchase.concretes.vat_purchase_price import VatPurchasePrice
from structural.decorator.purchase.models.address import Address
from structural.decorator.purchase.models.customer import Customer
from structural.decorator.purchase.models.product import Product
from structural.decorator.purchase.models.purchase import Purchase


def run():
    customer = Customer()
    address = Address(country='Iran')
    purchase = Purchase(customer, address)

    p1 = Product(name='Product 1', price=50000)
    p2 = Product(name='Product 2', price=30000)
    p3 = Product(name='Product 3', price=20000)

    products = [p1, p2, p3]

    purchase.add_products(products)

    vat = VatPurchasePrice(purchase)
    service = ServicePurchasePrice(vat)

    print(purchase.total_price())
    print(service.total_price())


if __name__ == '__main__':
    run()
