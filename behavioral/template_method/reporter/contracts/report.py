from abc import ABC, abstractmethod


class UserReport(ABC):

    def __init__(self, users):
        self.users = users
        self.data_to_export = None

    def generate(self):
        self.data_to_export = self.prepare_process()
        self.export()

    def prepare_process(self):
        return self.users.objects.filter(age__gt=18)

    @abstractmethod
    def export(self):
        pass
