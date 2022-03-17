from structural.flyweight.discount.constraints.constraint import DiscountConstraint
from structural.flyweight.discount.context.discount import Discount


class DiscountFactory:

    def __init__(self):
        self.constraints = {}
        self.discounts = []

    def create_discount(self, user_id, code, percent, min_amount, max_amount, limit, expire_data):
        constraint = DiscountConstraint(percent, min_amount, max_amount, limit, expire_data)
        discount = Discount(user_id, code, constraint)
        self.discounts.append(discount)
        return discount

    def create_constraint(self, percent, min_amount, max_amount, limit, expire_data):
        key = tuple(locals().values())

        if not self.constraints.get(key):
            self.constraints[key] = DiscountConstraint(percent, min_amount, max_amount, limit, expire_data)
        return self.constraints.get(key)
