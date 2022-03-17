class Coupon:

    def __init__(self, pk, code):
        self.pk = pk
        self.code = code

    @classmethod
    def find(cls, code):
        """
        Check are exists code in database
        :param code:
        :return:
        """
        pass

    @classmethod
    def is_active(cls, code):
        """
        Check are is active code
        :param code:
        :return:
        """
        pass

    @classmethod
    def is_expired(cls, code):
        """
        Check are is expired code
        :param code:
        :return:
        """
        pass
