from structural.adapter.notification.contracts.notifier import Notifier


class SMSProvider(Notifier):

    def send(self, message):
        return f'Send SMS: {message}'
