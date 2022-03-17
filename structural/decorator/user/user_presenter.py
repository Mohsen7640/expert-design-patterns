from structural.decorator.user.user import User


class UserPresenter:

    def __init__(self, user: User):
        self.user = user

    @property
    def get_full_name(self):
        return f"{self.user.get_first_name} {self.user.get_last_name}"

    @property
    def get_persian_join_data(self):
        return self.user.get_join_date
