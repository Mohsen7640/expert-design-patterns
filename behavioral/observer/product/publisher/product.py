from typing import Set

from behavioral.observer.product.contracts.subscriber_interface import SubscriberInterface


class Product:

    def __init__(self, pk, title, price):
        self.pk = pk
        self.title = title
        self.price = price

        self.subscribers: Set[SubscriberInterface] = set()

    def change_price(self, new_price):
        if self.price == new_price:
            return
        if new_price < 0:
            raise ValueError("مبلغ یک محصول نمیتواند کمتر از صفر باشد")

        self.price = new_price
        self.notify()

    def attach(self, subscriber):
        self.subscribers.add(subscriber)

    def detach(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(product=self)
