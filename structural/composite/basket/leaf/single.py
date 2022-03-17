from structural.composite.basket.contracts.product import Product


class SingleProduct(Product):

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def price(self):
        return self.amount