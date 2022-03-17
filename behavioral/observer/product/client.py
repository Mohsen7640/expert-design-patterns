from behavioral.observer.product.publisher.product import Product
from behavioral.observer.product.subscribers.offer import ProductPriceSubscriber


def run():
    product_offer_subscriber = ProductPriceSubscriber()

    product = Product(pk=5, title="Product#1", price=120000)

    product.attach(subscriber=product_offer_subscriber)

    product.change_price(new_price=100000)


if __name__ == '__main__':
    run()
