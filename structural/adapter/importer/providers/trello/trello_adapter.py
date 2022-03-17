from structural.adapter.importer.contracts.importer import Importer
from structural.adapter.importer.models.task import Task, TaskStatus
from structural.adapter.importer.providers.trello.terllo_api import TrelloAPI


class TrelloAdapter(Importer):

    def __init__(self, trello_api: TrelloAPI):
        self.trello_api = trello_api

    def importer(self):
        tasks = self.trello_api.fetch(count=10)
        return [Task(title=task.name, description='', status=TaskStatus.DOING) for task in tasks]
