from behavioral.state.crm.contracts.state_interface import StateInterface


class DraftState(StateInterface):

    def draft(self):
        self.post.change_state(DraftState())

    def moderation(self):
        from behavioral.state.crm.states.moderation import ModerationState
        self.post.change_state(ModerationState())

    def published(self):
        raise ValueError("مطلبی که در حالت پیش نویس باشد نمیتواند منتشر شود")
