class DiscountConstraint:
    def __init__(self, percentage, min_amount, max_amount, limit, expiry_date):
        self.percentage = percentage
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.limit = limit
        self.expiry_date = expiry_date
