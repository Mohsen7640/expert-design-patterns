from behavioral.visitor.abstract.contracts.visitor import Visitor


class Algorithm(Visitor):

    def visit_element_a(self, element_a):
        print(f"Element A: {element_a}")

    def visit_element_b(self, element_b):
        print(f"Element A: {element_b}")

    def visit_element_c(self, element_c):
        print(f"Element A: {element_c}")
