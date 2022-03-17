from structural.composite.menu.composite.collection import MenuCollection
from structural.composite.menu.leaf.item import MenuItem


def run():
    google = MenuItem(title='Google', url=' ')
    apple = MenuItem(title='Apple', url=' ')

    col1 = MenuCollection()
    col1.add(google)
    col1.add(apple)

    microsoft = MenuItem(title='Microsoft', url=' ')
    hp = MenuItem(title='Hp', url=' ')

    col2 = MenuCollection()
    col2.add(microsoft)
    col2.add(hp)

    col = MenuCollection()
    col.add(col1)
    col.add(col2)

    col2.build()


if __name__ == "__main__":
    run()
