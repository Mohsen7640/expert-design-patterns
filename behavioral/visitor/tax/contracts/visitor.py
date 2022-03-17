from abc import ABC, abstractmethod


class Visitor(ABC):

    @abstractmethod
    def visit_high_range(self, manager):
        pass

    @abstractmethod
    def visit_mid_range(self, team_lead):
        pass

    @abstractmethod
    def visit_low_range(self, developer):
        pass
