class UserConstraint:

    def __init__(self, first_name, last_name, gender, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.city = city

    def __str__(self):
        return f'User(first_name={self.first_name}, last_name={self.last_name},' \
               f' gender={self.gender}, age={self.age}, city={self.city})'
