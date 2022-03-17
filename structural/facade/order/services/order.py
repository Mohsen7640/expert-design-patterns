from structural.facade.order.models.basket import Basket
from structural.facade.order.models.order import Order
from structural.facade.order.services.discount import DiscountService
from structural.facade.order.services.quantity import QuantityService


class OrderService:

    def __init__(self, quantity_service: QuantityService, discount_service: DiscountService):
        self.quantity_service = quantity_service
        self.discount_service = discount_service

    def register(self, basket: Basket):
        # TODO-1: Check quantity of products
        for product in basket.products:
            if not self.quantity_service.exists(product):
                raise Exception('Product {} is out of stock'.format(product.name))

        # TODO-2: Apply discount
        discount = self.discount_service.apply(coupon=basket.coupon)

        # TODO-3: Register order
        order = Order.create(user_id=12, amount=basket.total_price() - discount, order_lines=[], coupon=basket.coupon)
