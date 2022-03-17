from solid.dependency_inversion_principle.authentication.problem.connection import Connection


class Authentication:

    def __init__(self, connection: Connection):
        self.connection = connection

    def check_password(self, username, password):
        try:
            user = self.connection.query(
                query=f"""SELECT * FROM users WHERE username=?""",
                params={"username": username}
            )
        except Exception:
            raise Exception("User DoesNot Exists")

        if user.password == password:
            return True
        return False
