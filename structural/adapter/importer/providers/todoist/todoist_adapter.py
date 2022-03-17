from structural.adapter.importer.contracts.importer import Importer
from structural.adapter.importer.models.task import Task, TaskStatus
from structural.adapter.importer.providers.todoist.todoist_api import TodoistAPI


class TodoistAdapter(Importer):

    def __init__(self, todoist_api: TodoistAPI):
        self.todoist_api = todoist_api

    def importer(self):
        tasks = self.todoist_api.fetch_tasks(category=0, count=20)
        return [Task(title=task.title, description=task.description, status=TaskStatus.DONE) for task in tasks]
