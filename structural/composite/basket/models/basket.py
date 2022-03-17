from typing import List

from structural.composite.basket.contracts.product import Product


class Basket:

    def __init__(self):
        self.items: List[Product] = []

    def add(self, item: Product):
        self.items.append(item)

    def total_price(self):
        return sum([item.price() for item in self.items])
