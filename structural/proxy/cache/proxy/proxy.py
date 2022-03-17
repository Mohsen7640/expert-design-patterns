from structural.proxy.cache.contracts.cache import CacheInterface
from structural.proxy.cache.contracts.repository import RepositoryInterface


class CachedRepositoryProxy(RepositoryInterface):

    def __init__(self, repository_service: RepositoryInterface, cache_service: CacheInterface):
        self.repository_service = repository_service
        self.cache_service = cache_service

    def all(self):
        cached = self.cache_service.get(key='products')

        if cached is None:
            products = self.repository_service.all()
            self.cache_service.set(key='products', value=products)
        return self.cache_service.get(key='products')
