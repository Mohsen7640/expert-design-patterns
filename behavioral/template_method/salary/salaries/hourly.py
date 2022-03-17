from behavioral.template_method.salary.contracts.salary import Salary


class HourlySalary(Salary):

    def get_base_salary(self):
        return 0

    def get_extra_work_salary(self):
        pass