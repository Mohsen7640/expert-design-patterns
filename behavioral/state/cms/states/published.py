from behavioral.state.crm.contracts.state_interface import StateInterface


class PublishedState(StateInterface):

    def draft(self):
        from behavioral.state.crm.states.draft import DraftState
        self.post.change_state(DraftState())

    def moderation(self):
        raise ValueError("مطلب منتشر شده نمیتواند وارد صف بررسی شود")

    def published(self):
        raise ValueError("مطلبی که منتشر شده نمیتواند دوباره منتشر شده")
