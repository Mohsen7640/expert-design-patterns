from behavioral.chain_of_responsibility.coupon.base.base_coupon import BaseCoupon


class ExistsValidator(BaseCoupon):

    def validate(self, code):
        if not self.coupon.find(code):
            raise ValueError("Code Not Exists")
        return super().validate(code)
