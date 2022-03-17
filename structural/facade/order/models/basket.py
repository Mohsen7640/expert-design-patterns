class Basket:

    def __init__(self):
        self.products = []

    def add_products(self, products):
        if not isinstance(products, list):
            products = [products]
        self.products.extend(products)

    @property
    def coupon(self):
        return 'COUPON'

    def total_price(self):
        return sum([product.get_price for product in self.products])
