class UserService:

    def __init__(self, event_dispatcher):
        self.event_dispatcher = event_dispatcher

    def delete_user(self, user_id):
        self.event_dispatcher.fire(
            event="user:deleted",
            emitter=self,
            data={
                "user_id": user_id,
            }
        )
