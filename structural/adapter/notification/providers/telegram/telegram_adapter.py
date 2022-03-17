from structural.adapter.notification.contracts.notifier import Notifier
from structural.adapter.notification.providers.telegram.telegram_api import TelegramAPI


class TelegramAdapter(Notifier):

    def __init__(self, telegram_api: TelegramAPI, chat_id):
        self.telegram_api = telegram_api
        self.chat_id = chat_id

    def send(self, message):
        return self.telegram_api.send(self.chat_id, message)
