from solid.dependency_inversion_principle.authentication.sloution.contracts.user_interface import UserProviderInterface


class Authentication:

    def __init__(self, user_provider: UserProviderInterface):
        self.user_provider = user_provider

    def check_password(self, username, password):
        user = self.user_provider.find_user(username=username)
        if user.password == password:
            return True
        return False
