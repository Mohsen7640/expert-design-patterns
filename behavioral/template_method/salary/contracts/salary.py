from abc import ABC, abstractmethod


class Salary(ABC):

    def calculate(self):
        return self.get_base_salary() + self.get_extra_work_salary()

    @abstractmethod
    def get_base_salary(self):
        pass

    @abstractmethod
    def get_extra_work_salary(self):
        pass
