class ChatRoom:

    def __init__(self, emitter):
        self.emitter = emitter
        self.users = {}

    def connect(self, user):
        self.users[user.pk] = user

    def disconnect(self, user):
        self.users.pop(user.pk)

    def send(self, message):
        receiver = self.users[message.receiver]
        self.emitter.emit(receiver, message)
