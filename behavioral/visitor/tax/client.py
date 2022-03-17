from behavioral.visitor.tax.employees.developer import Developer
from behavioral.visitor.tax.employees.manager import Manager
from behavioral.visitor.tax.employees.team_lead import TeamLead
from behavioral.visitor.tax.visitors.tax_calculator import TaxCalculator

if __name__ == '__main__':
    tax = TaxCalculator()

    developer = Developer()
    team_lead = TeamLead()
    manager = Manager()

    print(developer.accept(visitor=tax))
    print(team_lead.accept(visitor=tax))
    print(manager.accept(visitor=tax))
