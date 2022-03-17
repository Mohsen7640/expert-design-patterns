from structural.adapter.exchange.contracts.exchange import Exchange
from structural.adapter.exchange.providers.fixer.rate_api import RateAPI


class RateAdapter(Exchange):

    def __init__(self, rate_api: RateAPI):
        self.rate_api = rate_api

    def exchange(self, product):
        return product.price * self.rate_api.get_rate()
