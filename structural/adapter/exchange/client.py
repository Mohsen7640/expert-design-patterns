from structural.adapter.exchange.models.product import Product
from structural.adapter.exchange.providers.fixer.rate_adapter import RateAdapter
from structural.adapter.exchange.providers.fixer.rate_api import RateAPI


def run():
    p1 = Product(name='Samsung', price=800)
    p2 = Product(name='Apple', price=1200)
    p3 = Product(name='Persian Rugs', price=500)

    products = [p1, p2, p3]

    rate_api = RateAPI(token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    rate = RateAdapter(rate_api)

    for product in products:
        print(
            f'Detail: {product.get_detail()} - Toman Price: {rate.exchange(product)}'
        )


if __name__ == "__main__":
    run()
