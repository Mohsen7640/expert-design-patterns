from solid.single_responsibility_principle.problem.models.message import Message

from solid.single_responsibility_principle.problem.contracts.template_engine import TemplateEngineInterface
from solid.single_responsibility_principle.problem.contracts.mailer import MailerInterface
from solid.single_responsibility_principle.problem.contracts.translator import TranslatorInterface


class ConfirmMailMailer:

    def __init__(self, template_engine: TemplateEngineInterface, translator: TranslatorInterface,
                 mailer: MailerInterface):
        self.template_engine = template_engine
        self.translator = translator
        self.mailer = mailer

    def send_to(self, user):
        message = self.__create_message_for(user)
        self.__send_message(message)

    def __create_message_for(self, user):
        subject = self.translator.translate(text=f'Please confirm your email address')
        body = self.template_engine.render(
            template="email.confirm.html",
            params={
                "confirm_code": user.get_confirm_code(),
            }
        )

        return Message(subject=subject, body=body, email_address=user.get_email_address())

    def __send_message(self, message):
        self.mailer.send(message)
