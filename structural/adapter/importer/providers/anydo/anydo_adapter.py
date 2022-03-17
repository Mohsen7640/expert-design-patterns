from structural.adapter.importer.contracts.importer import Importer
from structural.adapter.importer.models.task import TaskStatus, Task
from structural.adapter.importer.providers.anydo.anydo_api import AnyDoAPI


class AnyDoAdapter(Importer):

    def __init__(self, anydo_api: AnyDoAPI):
        self.anydo_api = anydo_api

    def importer(self):
        tasks = self.anydo_api.fetch(count=10, status=TaskStatus.INIT)
        return [Task(title=task.name, description='', status=TaskStatus.INIT) for task in tasks]
