from behavioral.chain_of_responsibility.registration.contracts.checker_interface import CheckerInterface


class BaseChecker(CheckerInterface):

    def __init__(self, next_checker: CheckerInterface = None):
        self.next_checker = next_checker

    def check(self, registration):
        if self.next_checker is None:
            return True
        return self.next_checker.check(registration)
