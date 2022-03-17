from solid.single_responsibility_principle.sloution.contracts.template_engine import TemplateEngineInterface
from solid.single_responsibility_principle.sloution.contracts.translator import TranslatorInterface
from solid.single_responsibility_principle.sloution.models.message import Message


class ConfirmationMailFactory:

    def __init__(self, template_engine: TemplateEngineInterface, translator: TranslatorInterface):
        self.template_engine = template_engine
        self.translator = translator

    def create_message_for(self, user):
        subject = self.translator.translate(text=f'Please confirm your email address')
        body = self.template_engine.render(
            template="email.confirm.html",
            params={
                "confirm_code": user.get_confirm_code(),
            }
        )
        return Message(subject=subject, body=body, email_address=user.get_email_address())
