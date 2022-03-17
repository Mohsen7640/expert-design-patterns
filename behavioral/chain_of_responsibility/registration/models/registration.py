class Registration:

    def __init__(self, email, referral_code, password):
        self.email = email
        self.referral_code = referral_code
        self.password = password

    def email_exists(self):
        """
        Check are exists email(Duplicate)
        :return:
        """
        pass

    def password_validate(self):
        """
        Check are password is validated
        :return:
        """
        pass

    def referral_code_validate(self):
        """
        Check are referral code is validated
        :return:
        """
        pass
