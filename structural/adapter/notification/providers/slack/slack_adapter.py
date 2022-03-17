from structural.adapter.notification.contracts.notifier import Notifier
from structural.adapter.notification.providers.slack.slack_api import SlackAPI


class SlackAdapter(Notifier):

    def __init__(self, slack_api: SlackAPI, join_code, chat_id):
        self.slack_api = slack_api
        self.join_code = join_code
        self.chat_id = chat_id

    def send(self, message):
        return self.slack_api.send(self.join_code, self.chat_id, message)
