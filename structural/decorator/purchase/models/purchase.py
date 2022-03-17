from structural.decorator.purchase.contracts.purchase_price import PurchasePrice


class Purchase(PurchasePrice):

    def __init__(self, customer, address):
        self.customer = customer
        self.address = address
        self.product_list = []

    def add_products(self, product_list):
        if not isinstance(product_list, list):
            product_list = [product_list]
        self.product_list.extend(product_list)

    def total_price(self):
        total_price_products = 0

        for product in self.product_list:
            total_price_products += product.price
        return total_price_products
