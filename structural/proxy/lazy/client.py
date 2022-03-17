from structural.proxy.lazy.proxy.proxy import LazyLoaderProxy
from structural.proxy.lazy.services.mongo import MongoHandler
from structural.proxy.lazy.services.mysql import MySQLHandler


def run():
    mysql = LazyLoaderProxy(MySQLHandler)
    mongo = LazyLoaderProxy(MongoHandler)

    mysql.get()
    mongo.get()


if __name__ == '__main__':
    run()
