class Payment:

    def __init__(self):
        self.observers = set()

    def attach(self, observer):
        self.observers.add(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def checkout(self):
        for observer in self.observers:
            observer.send(message="Purchase Paid")
