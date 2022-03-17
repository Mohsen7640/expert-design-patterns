from behavioral.state.automation.contracts.state_interface import StateInterface


class OperatorState(StateInterface):

    def __init__(self):
        self.message = None

    def set_message(self, message):
        self.message = message

    def send_to_client(self):
        from behavioral.state.automation.states.client import ClientState

        self.message.transition_to(state=ClientState())
        print("پیغام برای کاربر ارسال شد.")

    def send_to_operator(self):
        raise ValueError("پیغام نمیتواند به اوپراور ارسال شود")

    def send_to_supervisor(self):
        from behavioral.state.automation.states.supervisor import SupervisorState

        self.message.transition_to(state=SupervisorState())
        print("پیغام برای سرپرست ارسال شد.")

    def send_to_internal_manager(self):
        raise ValueError("پیغام نمیتواند به مدیر داخلی ارسال شود")

    def send_to_managing_director(self):
        raise ValueError("پیغام نمیتواند به مدیر عامل ارسال شود")
