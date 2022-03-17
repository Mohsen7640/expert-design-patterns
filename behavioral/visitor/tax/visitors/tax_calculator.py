from behavioral.visitor.tax.contracts.visitor import Visitor


class TaxCalculator(Visitor):

    def visit_high_range(self, manager):
        return manager.salary() * 0.5

    def visit_mid_range(self, team_lead):
        return team_lead.salary() * 0.35

    def visit_low_range(self, developer):
        if developer.salary() <= 2500:
            return 0
        return developer.salary() * 0.20