class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_detail(self):
        return f'Name: {self.name} - Price: {self.price}'
