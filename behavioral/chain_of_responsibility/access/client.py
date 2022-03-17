from behavioral.chain_of_responsibility.access.models.product import Product
from behavioral.chain_of_responsibility.access.models.user import User
from behavioral.chain_of_responsibility.access.verifiers.subscription import SubscriptionVerifier
from behavioral.chain_of_responsibility.access.verifiers.expiration import ExpirationVerifier
from behavioral.chain_of_responsibility.access.verifiers.activation import ActivationVerifier


def run(user, product):
    return SubscriptionVerifier(
        next_verifier=ExpirationVerifier(
            next_verifier=ActivationVerifier()
        )
    ).verify(user, product)


if __name__ == '__main__':
    user = User(pk=1, username="john", password="passwd-123")
    product = Product(pk=45, name="Product#1", price=12000)
    run(user, product)
