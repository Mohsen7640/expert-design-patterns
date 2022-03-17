from behavioral.state.automation.states.client import ClientState


class Message:

    def __init__(self, subject, body):
        self.subject = subject
        self.body = body
        self.state = None
        self.transition_to(state=ClientState())

    def transition_to(self, state):
        self.state = state
        self.state.set_message(self)

    def send_to_client(self):
        self.state.send_to_client()

    def send_to_operator(self):
        self.state.send_to_operator()

    def send_to_supervisor(self):
        self.state.send_to_supervisor()

    def send_to_internal_manager(self):
        self.state.send_to_internal_manager()

    def send_to_managing_director(self):
        self.state.send_to_managing_director()
