class Order:

    def __init__(self, user_id, amount, order_lines, coupon):
        self.user_id = user_id
        self.amount = amount
        self.order_lines = order_lines
        self.coupon = coupon

    @classmethod
    def create(cls, user_id, amount, order_lines, coupon):
        return cls(user_id, amount, order_lines, coupon)
