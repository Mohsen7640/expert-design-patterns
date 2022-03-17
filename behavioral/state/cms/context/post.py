from behavioral.state.crm.states.draft import DraftState


class Post:

    def __init__(self, pk, title, content):
        self.pk = pk
        self.title = title
        self.content = content
        self.state = self.change_state(state=DraftState())

    def change_state(self, state):
        self.state = state
        self.state.set_post(self)
        return state

    def draft(self):
        self.state.draft()

    def moderation(self):
        self.state.moderation()

    def published(self):
        self.state.published()