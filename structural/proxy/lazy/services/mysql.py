from structural.proxy.lazy.contracts.handler import Handler


class MySQLHandler(Handler):

    def get(self):
        print('MySQL')
