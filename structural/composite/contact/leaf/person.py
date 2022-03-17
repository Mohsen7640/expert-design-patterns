from structural.composite.contact.contracts.contact import Contact


class PersonContact(Contact):

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def send(self, message):
        print(f'Message {self.name}({self.phone})')
        print(f'----> {message}')
