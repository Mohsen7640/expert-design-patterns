class TelegramAPI:
    """
        - Adaptee
    """

    def send(self, chat_id, message):
        return f'Send Telegram Message: send "{message}" to {chat_id}'
