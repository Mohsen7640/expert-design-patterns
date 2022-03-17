from random import choices, choice, randint
from string import digits

from structural.flyweight.faker.factory.factory import UserFactory


def run():
    factory = UserFactory()
    for _ in range(1000000):
        factory.create_user(
            national_code=choices(digits, k=11),
            first_name=choice(['John', 'Anna', 'Mark', 'Sherlock', 'Watson']),
            last_name=choice(['John', 'Anna', 'Mark', 'Sherlock', 'Watson']),
            gender=choice(['male', 'female', 'other']),
            age=randint(18, 40),
            city=choice(['Tehran', 'Isfahan', 'London', 'Paris'])
        )

    print(len(factory.users))

    for key in factory.constraints:
        print(key, factory.constraints[key])


if __name__ == '__main__':
    run()
