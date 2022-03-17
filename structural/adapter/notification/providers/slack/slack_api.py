class SlackAPI:

    def send(self, join_code, chat_id, message):
        return f'Send Slack Message: ({join_code}) send "{message}" to {chat_id}'
