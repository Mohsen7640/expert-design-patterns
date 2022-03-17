from structural.decorator.user.user import User
from structural.decorator.user.user_presenter import UserPresenter


def run():
    user = User(first_name='John', last_name='Doe', email='john_doe@gmail.com', join_date='2019-01-01')
    present = UserPresenter(user)

    print(user.get_first_name)
    print(user.get_last_name)
    print(user.get_email)
    print(user.get_join_date)

    print(present.get_full_name)
    print(present.get_persian_join_data)


if __name__ == '__main__':
    run()
