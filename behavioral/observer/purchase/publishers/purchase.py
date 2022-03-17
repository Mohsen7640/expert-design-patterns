class Purchase:

    def __init__(self, product_list, payment):
        self.product_list = product_list
        self.payment = payment

        self.observers = set()

    def attach(self, observer):
        self.observers.add(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def checkout(self):
        self.payment.checkout()

    def cancel(self):
        for observer in self.observers:
            observer.send(message="Purchased Canceled")
