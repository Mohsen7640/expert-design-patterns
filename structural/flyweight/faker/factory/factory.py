from structural.flyweight.faker.constraints.constraint import UserConstraint
from structural.flyweight.faker.context.user import User


class UserFactory:

    def __init__(self):
        self.constraints = {}
        self.users = []

    def create_user(self, national_code, first_name, last_name, gender, age, city):
        constraint = self.create_constraint(first_name, last_name, gender, age, city)
        user = User(national_code, constraint)
        self.users.append(user)
        return user

    def create_constraint(self, first_name, last_name, gender, age, city):
        key = tuple(locals().values())

        if not self.constraints.get(key):
            self.constraints[key] = UserConstraint(first_name, last_name, gender, age, city)
        return self.constraints[key]
