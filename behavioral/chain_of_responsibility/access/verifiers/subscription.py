from behavioral.chain_of_responsibility.access.base.base_verifier import BaseVerifier
from behavioral.chain_of_responsibility.access.models.subscription import Subscription


class SubscriptionVerifier(BaseVerifier):

    def verify(self, user, product):
        subscription = Subscription.find_by_user_and_product(user, product)
        if not subscription:
            return False

        return super().verify(user, product)
