class Invoice:

    def __init__(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def __str__(self):
        return f'Invoice Price: {self.get_amount()}'
