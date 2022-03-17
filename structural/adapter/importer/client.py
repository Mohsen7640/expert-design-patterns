from structural.adapter.importer.providers.anydo.anydo_adapter import AnyDoAdapter
from structural.adapter.importer.providers.anydo.anydo_api import AnyDoAPI
from structural.adapter.importer.providers.todoist.todoist_adapter import TodoistAdapter
from structural.adapter.importer.providers.todoist.todoist_api import TodoistAPI
from structural.adapter.importer.providers.trello.terllo_api import TrelloAPI
from structural.adapter.importer.providers.trello.trello_adapter import TrelloAdapter


def run():
    anydo_api = AnyDoAPI(username='usr', password='passwd')
    anydo = AnyDoAdapter(anydo_api)
    anydo.importer()

    trello_api = TrelloAPI(api_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    trello = TrelloAdapter(trello_api)
    trello.importer()

    todoist_api = TodoistAPI(token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    todoist = TodoistAdapter(todoist_api)
    todoist.importer()


if __name__ == "__main__":
    run()
