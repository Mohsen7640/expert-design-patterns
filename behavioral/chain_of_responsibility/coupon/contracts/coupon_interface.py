from abc import ABC, abstractmethod

from behavioral.chain_of_responsibility.coupon.models.coupon import Coupon


class CouponInterface(ABC):

    @abstractmethod
    def validate(self, code: Coupon):
        pass
