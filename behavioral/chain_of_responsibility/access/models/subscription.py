class Subscription:

    @classmethod
    def find_by_user_and_product(cls, user, product):
        """
        Check are exists product for user
        :param user:
        :param product:
        :return:
        """
        pass

    def check_expire_subscription(self):
        """
        Check are subscription expired
        :return:
        """
        pass

    def check_activation_subscription(self):
        """
        Check are subscription is active
        :return:
        """
        pass
