from structural.facade.click.services.checkout import CheckoutService


class OneClickCheckoutService:

    def __init__(self, order, default_address, default_payment_method):
        self.checkout_service = CheckoutService(order)
        self.default_address = default_address
        self.default_payment_method = default_payment_method

    def click(self):
        self.checkout_service.set_shipping_address(self.default_address)
        self.checkout_service.set_payment_method(self.default_payment_method)
        self.checkout_service.place_order()
