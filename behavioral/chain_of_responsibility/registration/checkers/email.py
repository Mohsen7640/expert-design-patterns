from behavioral.chain_of_responsibility.registration.base.base_checker import BaseChecker


class EmailChecker(BaseChecker):

    def check(self, registration):
        if registration.email_exists():
            return False
        return super().check(registration)
