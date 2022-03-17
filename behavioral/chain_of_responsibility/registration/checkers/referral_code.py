from behavioral.chain_of_responsibility.registration.base.base_checker import BaseChecker


class ReferralCodeChecker(BaseChecker):

    def check(self, registration):
        if not registration.referral_code_validate():
            return False
        return super().check(registration)
