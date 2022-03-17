from behavioral.visitor.abstract.contracts.element import Element


class ElementB(Element):

    def accept(self, visitor):
        visitor.visit_element_b(self)
