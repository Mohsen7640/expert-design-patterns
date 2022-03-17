from behavioral.state.order.status.pending import PendingStatus


class Order:

    def __init__(self):
        self.status = self.change_status(status=PendingStatus())

    def change_status(self, status):
        self.status.set_order(status)
        return status

    def pending(self):
        self.status.pending()

    def paid(self):
        self.status.paid()

    def prepare(self):
        self.status.prepare()

    def ready(self):
        self.status.ready()

    def sent(self):
        self.status.sent()

    def delivered(self):
        self.status.delivered()
