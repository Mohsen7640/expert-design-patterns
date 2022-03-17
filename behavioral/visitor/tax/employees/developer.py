from behavioral.visitor.tax.contracts.employee import Employee


class Developer(Employee):

    def salary(self):
        return 2500

    def accept(self, visitor):
        return visitor.visit_low_range(self)
