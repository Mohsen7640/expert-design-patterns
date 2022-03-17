from typing import List

from structural.composite.basket.contracts.product import Product


class PackageProduct(Product):

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def price(self):
        return sum([product.price() for product in self.products])