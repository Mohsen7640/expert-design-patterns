from behavioral.chain_of_responsibility.registration.checkers.email import EmailChecker
from behavioral.chain_of_responsibility.registration.checkers.password import PasswordChecker
from behavioral.chain_of_responsibility.registration.checkers.referral_code import ReferralCodeChecker
from behavioral.chain_of_responsibility.registration.models.registration import Registration


def run(registration):
    return EmailChecker(
        next_checker=PasswordChecker(
            next_checker=ReferralCodeChecker()
        )
    ).check(registration)


if __name__ == '__main__':
    registration = Registration(email="sample@gmail.com", referral_code="fffe344hb", password="passwd-123")
    run(registration)
