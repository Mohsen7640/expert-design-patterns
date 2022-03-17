class User:

    def __init__(self, first_name, last_name, email, join_date):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__join_date = join_date

    @property
    def get_first_name(self):
        return self.__first_name

    @property
    def get_last_name(self):
        return self.__last_name

    @property
    def get_email(self):
        return self.__email

    @property
    def get_join_date(self):
        return self.__join_date
