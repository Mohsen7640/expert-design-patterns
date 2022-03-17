from structural.flyweight.faker.constraints.constraint import UserConstraint


class User:

    def __init__(self, national_code, constraint: UserConstraint):
        self.national_code = national_code
        self.constraint = constraint

    def __str__(self):
        return f'User(national_code={self.national_code}, constraint={self.constraint})'
