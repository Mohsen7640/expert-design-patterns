from behavioral.visitor.tax.contracts.employee import Employee


class Manager(Employee):

    def salary(self):
        return 5500

    def accept(self, visitor):
        return visitor.visit_high_range(self)
