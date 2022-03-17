class Order:

    def __init__(self):
        self.items = []
        self.shipping_address = None
        self.payment_method = None

    def add_products(self, products):
        if not isinstance(products, list):
            products = [products]
        self.items.extend(products)

    def set_shipping_address(self, address):
        self.shipping_address = address

    def set_payment_method(self, method):
        self.payment_method = method

    def total_price(self):
        return sum([item.price for item in self.items])