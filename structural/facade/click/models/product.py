class Product:

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_price(self):
        return self.amount
