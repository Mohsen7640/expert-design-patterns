from structural.adapter.notification.contracts.notifier import Notifier


class EmailProvider(Notifier):

    def send(self, message):
        return f'Send Email: {message}'
