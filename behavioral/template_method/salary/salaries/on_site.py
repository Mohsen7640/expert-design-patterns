from behavioral.template_method.salary.contracts.salary import Salary


class OnSiteSalary(Salary):

    def get_base_salary(self):
        return 5000000

    def get_extra_work_salary(self):
        pass