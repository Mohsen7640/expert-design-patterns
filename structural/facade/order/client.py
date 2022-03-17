from structural.facade.order.models.basket import Basket
from structural.facade.order.services.discount import DiscountService
from structural.facade.order.services.order import OrderService
from structural.facade.order.services.quantity import QuantityService


def run():
    quantity = QuantityService()
    discount = DiscountService()

    order = OrderService(quantity_service=quantity, discount_service=discount)
    basket = Basket()

    order.register(basket)


if __name__ == '__main__':
    run()
