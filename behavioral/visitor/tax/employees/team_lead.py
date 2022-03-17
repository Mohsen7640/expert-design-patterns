from behavioral.visitor.tax.contracts.employee import Employee


class TeamLead(Employee):

    def salary(self):
        return 3500

    def accept(self, visitor):
        return visitor.visit_mid_range(self)
