from behavioral.observer.product.contracts.subscriber_interface import SubscriberInterface


class ProductPriceSubscriber(SubscriberInterface):

    def update(self, product):
        print(f'{product.title} changed price to {product.price}')
