from behavioral.chain_of_responsibility.registration.base.base_checker import BaseChecker


class PasswordChecker(BaseChecker):

    def check(self, registration):
        if not registration.password_validate():
            return False
        return super().check(registration)
