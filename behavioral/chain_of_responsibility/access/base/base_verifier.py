from behavioral.chain_of_responsibility.access.contracts.verifier_interface import VerifierInterface


class BaseVerifier(VerifierInterface):

    def __init__(self, next_verifier: VerifierInterface = None):
        self.next_verifier = next_verifier

    def verify(self, user, product):
        if self.next_verifier is None:
            return True
        return self.next_verifier.verify(user, product)
