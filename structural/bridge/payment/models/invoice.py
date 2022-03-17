class Invoice:

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def get_price(self):
        return self.price
