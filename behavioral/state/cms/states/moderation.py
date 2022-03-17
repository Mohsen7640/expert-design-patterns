from behavioral.state.crm.contracts.state_interface import StateInterface


class ModerationState(StateInterface):

    def draft(self):
        from behavioral.state.crm.states.draft import DraftState
        self.post.change_state(DraftState())

    def moderation(self):
        self.post.change_state(ModerationState())

    def published(self):
        from behavioral.state.crm.states.published import PublishedState
        self.post.change_state(PublishedState())
