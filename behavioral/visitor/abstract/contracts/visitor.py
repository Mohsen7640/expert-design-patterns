from abc import ABC, abstractmethod


class Visitor(ABC):

    @abstractmethod
    def visit_element_a(self, element_a):
        pass

    @abstractmethod
    def visit_element_b(self, element_b):
        pass

    @abstractmethod
    def visit_element_c(self, element_c):
        pass
