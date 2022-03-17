from behavioral.strategy.delivery.contracts.method import DeliveryMethod


class DeliveryService:

    def __init__(self, method: DeliveryMethod):
        self.method = method

    def start_delivery(self, order):
        delivery_price = self.method.price(order)
        self.method.deliver(order)