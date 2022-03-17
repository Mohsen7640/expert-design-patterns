from solid.interface_segregation_principle.sloution.contracts.email import EmailNotifier


class EmailProvider(EmailNotifier):

    def send_email(self):
        pass
