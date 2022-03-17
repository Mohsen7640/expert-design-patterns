from behavioral.chain_of_responsibility.coupon.contracts.coupon_interface import CouponInterface
from behavioral.chain_of_responsibility.coupon.models.coupon import Coupon


class BaseCoupon(CouponInterface):

    def __init__(self, next_validator: CouponInterface = None):
        self.next_validator = next_validator
        self.coupon = Coupon

    def validate(self, code):
        if self.next_validator is None:
            return True

        return self.next_validator.validate(code)
