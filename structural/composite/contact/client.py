from structural.composite.contact.composite.group import GroupContact
from structural.composite.contact.leaf.person import PersonContact


def run():
    mom = PersonContact(name='Anna', phone='12-15-3222')
    dad = PersonContact(name='John', phone='22-15-3412')

    amy = PersonContact(name='Amy', phone='22-45-1287')

    parents = GroupContact()
    parents.add(mom)
    parents.add(dad)

    lee = PersonContact(name='lee', phone='12-15-4455')
    alice = PersonContact(name='alice', phone='12-15-4455')

    girls = GroupContact()
    girls.add(lee)
    girls.add(alice)

    jeff = PersonContact(name='jeff', phone='12-15-4455')
    ray = PersonContact(name='ray', phone='12-15-4455')

    collage = GroupContact()
    collage.add(jeff)
    collage.add(ray)
    collage.add(girls)

    parents.send(message="I'm coming home this weekend")

    mom.send(message="I miss you mom")
    amy.send(message="Best friends")

    collage.send(message='Collage')
    girls.send(message='miss you')


if __name__ == "__main__":
    run()
