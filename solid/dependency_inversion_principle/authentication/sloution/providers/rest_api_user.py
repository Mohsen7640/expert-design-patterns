from solid.dependency_inversion_principle.authentication.sloution.contracts.user_interface import UserProviderInterface


class RestAPIUserProvider(UserProviderInterface):

    def find_user(self, username):
        pass
