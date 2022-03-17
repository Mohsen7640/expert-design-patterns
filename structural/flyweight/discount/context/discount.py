from structural.flyweight.discount.constraints.constraint import DiscountConstraint


class Discount:

    def __init__(self, user_id, code, constraint: DiscountConstraint):
        self.user_id = user_id
        self.code = code
        self.constraint = constraint
