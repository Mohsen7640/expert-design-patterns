from structural.proxy.lazy.contracts.handler import Handler


class MongoHandler(Handler):

    def get(self):
        print('Mongo')
