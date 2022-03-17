from structural.composite.menu.contracts.menu import Menu


class MenuItem(Menu):

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def build(self):
        print(f'<a href={self.url}>{self.title}</a>')
