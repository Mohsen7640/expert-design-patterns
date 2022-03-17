from solid.yagni.repository.contracts.user_repository_interface import UserRepositoryInterface


class ORMUserRepository(UserRepositoryInterface):

    def create(self, **kwargs):
        """
        Create and save user
        :param kwargs:
        :return:
        """
        user = User.objects.create_user(**kwargs)
        return user
