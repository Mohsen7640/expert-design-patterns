from behavioral.state.order.contracts.order_interface import OrderInterface


class PendingStatus(OrderInterface):

    def pending(self):
        pass

    def paid(self):
        pass

    def prepare(self):
        pass

    def ready(self):
        pass

    def sent(self):
        pass

    def delivered(self):
        pass