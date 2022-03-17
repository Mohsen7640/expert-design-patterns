from typing import List

from structural.composite.menu.contracts.menu import Menu


class MenuCollection(Menu):

    def __init__(self):
        self.collections: List[Menu] = []

    def add(self, item: Menu):
        self.collections.append(item)

    def build(self):
        print('<div>')
        print('<ul>')

        for item in self.collections:
            print('<li>')
            item.build()
            print('</li>')

        print('</ul>')
        print('</div>')
