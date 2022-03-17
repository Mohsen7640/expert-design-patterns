from behavioral.chain_of_responsibility.coupon.base.base_coupon import BaseCoupon


class ActivationValidator(BaseCoupon):

    def validate(self, code):
        if not self.coupon.is_active(code):
            raise ValueError("Code Not Active")
        return super().validate(code)
