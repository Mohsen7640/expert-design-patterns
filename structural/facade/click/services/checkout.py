from structural.facade.click.models.order import Order


class CheckoutService:

    def __init__(self, order: Order):
        self.order = order

    def set_shipping_address(self, address):
        self.order.set_shipping_address(address)

    def set_payment_method(self, payment_method):
        self.order.set_payment_method(payment_method)

    def review_order(self):
        print('Reviewing order...')
        print('Order Contains:', self.order.items)
        print('Shipping address:', self.order.shipping_address)
        print('Payment method:', self.order.payment_method)
        print('Order total:', self.order.total_price())
        print('Order review complete.')

    def place_order(self):
        print('Placing order...')
        print('Order total:', self.order.total_price())
        print('Order placed successfully.')
