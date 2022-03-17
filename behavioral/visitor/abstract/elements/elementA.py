from behavioral.visitor.abstract.contracts.element import Element


class ElementA(Element):

    def accept(self, visitor):
        visitor.visit_element_a(self)
