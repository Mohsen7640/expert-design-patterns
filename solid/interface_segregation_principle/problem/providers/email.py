from solid.interface_segregation_principle.problem.contracts.notifier import Notifier


class EmailProvider(Notifier):

    def send_sms(self):
        pass

    def send_email(self):
        pass