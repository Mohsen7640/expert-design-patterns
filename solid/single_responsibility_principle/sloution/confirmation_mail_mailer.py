from solid.single_responsibility_principle.problem.contracts.mailer import MailerInterface
from solid.single_responsibility_principle.sloution.factory.confirmation_mail_factory import ConfirmationMailFactory


class ConfirmationMailMailer:

    def __init__(self, mailer: MailerInterface, confirmation_mail_factory: ConfirmationMailFactory):
        self.mailer = mailer
        self.confirmation_mail_factory = confirmation_mail_factory

    def send_to(self, user):
        message = self.__create_message_for(user)
        self.__send_message(message)

    def __create_message_for(self, user):
        return self.confirmation_mail_factory.create_message_for(user)

    def __send_message(self, message):
        self.mailer.send(message)
