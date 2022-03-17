from behavioral.strategy.payment.methods.online import OnlinePaymentMethod
from behavioral.strategy.payment.models.order import Order
from behavioral.strategy.payment.services.payment import PaymentService


def run():
    order = Order(pk=4356, price=100000)
    payment_method = OnlinePaymentMethod()
    payment = PaymentService(method=payment_method)
    payment.pay(order)


if __name__ == '__main__':
    run()