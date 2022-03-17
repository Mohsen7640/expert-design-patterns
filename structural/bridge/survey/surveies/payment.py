from structural.bridge.survey.contracts.survey import Survey


class PaymentSurvey(Survey):

    def __init__(self, user, title, price, presentation):
        self.user = user
        self.title = title
        self.price = price
        super().__init__(presentation)

    def display(self):
        return self.presentation.present()
