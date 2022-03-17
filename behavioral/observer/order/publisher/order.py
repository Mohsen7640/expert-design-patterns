from typing import Set

from behavioral.observer.order.contracts.observer_interface import ObserverInterface
from behavioral.observer.order.observers.price import OrderPriceObserver


class OrderStatus:
    PENDING = 1
    PROCESSING = 2
    READY = 3
    SENT = 4
    DELIVERED = 5


class Order:

    def __init__(self, pk, amount, status=OrderStatus.PENDING):
        self.pk = pk
        self.amount = amount
        self.status = status

        self.observers: Set[ObserverInterface] = set()

    def process(self):
        self.status = OrderStatus.PROCESSING
        self.register_processing_observers()

    def ready(self):
        self.status = OrderStatus.READY

    def sent(self):
        self.status = OrderStatus.SENT

    def delivered(self):
        self.status = OrderStatus.DELIVERED

    def register_processing_observers(self):
        order_price_observer = OrderPriceObserver()
        self.attach(observer=order_price_observer)

    def clean_processing_observers(self):
        self.observers.clear()

    def attach(self, observer):
        self.observers.add(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)
