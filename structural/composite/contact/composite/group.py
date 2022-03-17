from typing import List

from structural.composite.contact.contracts.contact import Contact


class GroupContact(Contact):

    def __init__(self):
        self.contacts: List[Contact] = []

    def add(self, contact: Contact):
        self.contacts.append(contact)

    def send(self, message):
        for contact in self.contacts:
            contact.send(message)