from solid.dependency_inversion_principle.authentication.problem.connection import Connection
from solid.dependency_inversion_principle.authentication.sloution.contracts.user_interface import UserProviderInterface


class UserProvider(UserProviderInterface):

    def __init__(self, connection: Connection):
        self.connection = connection

    def find_user(self, username):
        try:
            return self.connection.query(
                query=f"""SELECT * FROM users WHERE username=?""",
                params={"username": username}
            )
        except Exception:
            raise Exception("User DoesNot Exists")