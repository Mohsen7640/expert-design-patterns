from structural.adapter.notification.providers.email.email import EmailProvider
from structural.adapter.notification.providers.slack.slack_adapter import SlackAdapter
from structural.adapter.notification.providers.slack.slack_api import SlackAPI
from structural.adapter.notification.providers.sms.sms import SMSProvider
from structural.adapter.notification.providers.telegram.telegram_adapter import TelegramAdapter
from structural.adapter.notification.providers.telegram.telegram_api import TelegramAPI


def run():
    sms = SMSProvider()
    print(sms.send(message="Hello World"))

    email = EmailProvider()
    print(email.send(message="Hello World"))

    telegram_api = TelegramAPI()
    telegram = TelegramAdapter(telegram_api, "13an75YT")
    print(telegram.send(message="Hello World"))

    slack_api = SlackAPI()
    slack = SlackAdapter(slack_api, "4455123aa234123tree12", "13an75YT")
    print(slack.send(message="Hello World"))


if __name__ == "__main__":
    run()
