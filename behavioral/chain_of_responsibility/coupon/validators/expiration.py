from behavioral.chain_of_responsibility.coupon.base.base_coupon import BaseCoupon


class ExpirationValidator(BaseCoupon):

    def validate(self, code):
        if self.coupon.is_expired(code):
            raise ValueError("Code Is Expired")
        return super().validate(code)
