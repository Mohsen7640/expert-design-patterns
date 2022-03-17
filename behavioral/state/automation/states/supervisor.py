from behavioral.state.automation.contracts.state_interface import StateInterface


class SupervisorState(StateInterface):

    def __init__(self):
        self.message = None

    def set_message(self, message):
        self.message = message

    def send_to_client(self):
        raise ValueError("پیغام نمیتواند به کاربر ارسال شود")

    def send_to_operator(self):
        from behavioral.state.automation.states.operator import OperatorState

        self.message.transition_to(state=OperatorState())
        print("پیغام برای اوپراتور ارسال شد.")

    def send_to_supervisor(self):
        raise ValueError("پیغام نمیتواند به سرپرست ارسال شود")

    def send_to_internal_manager(self):
        from behavioral.state.automation.states.internal_manager import InternalMangerState

        self.message.transition_to(state=InternalMangerState())
        print("پیغام برای مدیر داخلی ارسال شد.")

    def send_to_managing_director(self):
        raise ValueError("پیغام نمیتواند به مدیر عامل ارسال شود")
