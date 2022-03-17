from behavioral.observer.purchase.models.product import Product
from behavioral.observer.purchase.observers.email import EmailObserver
from behavioral.observer.purchase.observers.push import PushObserver
from behavioral.observer.purchase.observers.sms import SMSObserver
from behavioral.observer.purchase.publishers.payment import Payment
from behavioral.observer.purchase.publishers.purchase import Purchase


def run():
    p1 = Product(pk=1, title="Product#1", price=120000)
    p2 = Product(pk=2, title="Product#2", price=110000)
    p3 = Product(pk=3, title="Product#3", price=100000)

    email_observer = EmailObserver()
    sms_observer = SMSObserver()
    push_observer = PushObserver()

    payment = Payment()
    payment.attach(observer=email_observer)
    payment.attach(observer=push_observer)

    purchase = Purchase([p1, p2, p3], payment)
    purchase.attach(observer=email_observer)
    purchase.attach(observer=sms_observer)
    purchase.attach(observer=push_observer)

    purchase.checkout()
    purchase.cancel()


if __name__ == '__main__':
    run()
