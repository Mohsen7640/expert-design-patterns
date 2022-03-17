class DiscountService:

    def is_valid(self, coupon):
        """Coupon is valid if it is not expired, and it is not used"""
        pass

    def apply(self, coupon):
        """Apply discount to order"""
        if self.is_valid(coupon):
            pass
        else:
            raise Exception("Coupon is not valid")
