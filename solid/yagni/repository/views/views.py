class UserView:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create(self, **kwargs):
        user = self.user_repository.create(**kwargs)
        return user