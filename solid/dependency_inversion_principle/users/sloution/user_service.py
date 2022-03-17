class UserService:

    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def register(self, username, password):
        # ... insert user in database
        self.dispatcher.dispatch(event="user_register", params={"user_id": 1})