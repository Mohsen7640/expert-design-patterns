from behavioral.visitor.abstract.contracts.element import Element


class ElementC(Element):

    def accept(self, visitor):
        visitor.visit_element_c(self)
